import json
import requests
import io
import base64
import numpy as np
import pandas as pd
from PIL import Image
import imgaug as ia


# Mapping of class ids with class names
ID_TO_CLASS = {
    1: 'shirt, blouse',
    2: 'top, t-shirt, sweatshirt',
    3: 'sweater',
    4: 'cardigan',
    5: 'jacket',
    6: 'vest',
    7: 'pants',
    8: 'shorts',
    9: 'skirt',
    10: 'coat',
    11: 'dress',
    12: 'jumpsuit',
    13: 'cape',
    14: 'glasses',
    15: 'hat',
    16: 'headband, head covering, hair accessory',
    17: 'tie',
    18: 'glove',
    19: 'watch',
    20: 'belt',
    21: 'leg warmer',
    22: 'tights, stockings',
    23: 'sock',
    24: 'shoe',
    25: 'bag, wallet',
    26: 'scarf',
    27: 'umbrella',
    28: 'hood',
    29: 'collar',
    30: 'lapel',
    31: 'epaulette',
    32: 'sleeve',
    33: 'pocket',
    34: 'neckline',
    35: 'buckle',
    36: 'zipper',
    37: 'applique',
    38: 'bead',
    39: 'bow',
    40: 'flower',
    41: 'fringe',
    42: 'ribbon',
    43: 'rivet',
    44: 'ruffle',
    45: 'sequin',
    46: 'tassel'
}


class ImageByteEncoder:
    """Class that provides functionalities to encode an image to bytes and
    decode back to image
    """

    def encode(self, img):
        """Encode

        Arguments:
            img {Image} -- PIL Image to be encode

        Returns:
            str -- image encoded as a string
        """
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()
        img_bytes = base64.b64encode(img_bytes).decode('utf8')
        return img_bytes

    def decode(self, img_str):
        """Decode

        Arguments:
            img_str {str} -- Image str as encoded by self.encode

        Returns:
            Image -- PIL Image
        """
        img_bytes = bytes(img_str, encoding='utf8')
        img_bytes = base64.b64decode(img_bytes)
        img = Image.open(io.BytesIO(img_bytes))
        return img


class Segmenter:
    def __init__(self):
        self.inference_url = 'https://models.samasource.com/fashion-seg/invocations'
        self.encoder = ImageByteEncoder()

    def _predict(self, req_json):
        # Request
        response = requests.post(
            url=self.inference_url,
            data=req_json,
            headers={"Content-Type": "application/json"})
        response = json.loads(response.text)[0]

        # Decode the seg info
        seg_str = response['Mask']
        id_to_class = json.loads(response['Mapping'])
        seg = self.encoder.decode(seg_str)
        return seg, id_to_class

    def predict_on_image(self, img):
        # Encode image as Byte String
        img_str = self.encoder.encode(img)

        # Create json request for the service according to pandas schema
        req_df = pd.DataFrame({'Image': [img_str]})
        req_json = req_df.to_json(orient='split')
        return self._predict(req_json)

    def predict_on_url(self, url):
        # Create json request for the service according to pandas schema
        req_df = pd.DataFrame({'Image_url': [url]})
        req_json = req_df.to_json(orient='split')
        return self._predict(req_json)


def get_image_from_url(img_url):
    response = requests.get(img_url)
    img = Image.open(io.BytesIO(response.content))
    return img


def display_image(img, segmap):
    img = np.array(img)
    segmap = np.array(segmap)
    ia_seg_map = ia.SegmentationMapOnImage(segmap, shape=img.shape, nb_classes=47)
    colors = ia_seg_map.DEFAULT_SEGMENT_COLORS + ia_seg_map.DEFAULT_SEGMENT_COLORS[1:6]
    return Image.fromarray(ia_seg_map.draw_on_image(img, colors=colors))


'''
Usage:

segmenter = Segmenter()
img_url = 'www.url.com/to/some/image.png'
img = get_image_from_url(img_url)

segmap, id_to_class = segmenter.predict_on_url(img_url)

display_image(img, segmap)
'''