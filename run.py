import io
import os
import numpy as np
import imgaug as ia
from PIL import Image
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from Segmenter import Segmenter, display_image

app = Flask(__name__, static_folder="static")
segmenter = Segmenter()


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        img_name = secure_filename(f.filename)
        dirName = 'static'
        results_folder = os.path.join(dirName, 'results')
        img_path = os.path.join(dirName, img_name)
        if not os.path.exists(dirName):
            os.mkdir(dirName)
        if not os.path.exists(results_folder):
            os.mkdir(results_folder)
        f.save(img_path)

        img = Image.open(img_path)
        segmap, id_to_class = segmenter.predict_on_image(img)
        img = display_image(img, segmap)
        result_img_path = os.path.join(results_folder, img_name)
        img.save(result_img_path)

        return render_template('results.html', file_name=img_name, file_path=result_img_path, clothing_detected=id_to_class)


if __name__ == '__main__':
    if "PORT" in os.environ:
        app.run(host='0.0.0.0', port=os.environ["PORT"])
    else:
        app.run(host='0.0.0.0')
