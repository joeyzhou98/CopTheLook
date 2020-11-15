
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from google.cloud import vision
import io
import os
import pandas
from os import path


# set path to api key here
""" INPUT PATH TO JSON API KEY"""
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="g_credentials.json"

uri = "https://media.endclothing.com/media/catalog/product/0/6/06-12-2017_adidas_ultraboost_coreblack_bb6166_mg_1.jpg"
uri2 = "https://static.nike.com/a/images/t_PDP_864_v1/f_auto,b_rgb:f5f5f5/gsuin11ptg5qgktmzoat/air-force-1-07-shoe-KyTDGepj.jpg"
# detect_web_uri(uri)

def best_match_uri(uri):
    """ find best matching product from the given uri and returns best match and additional searches """

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.web_detection(image=image)
    annotations = response.web_detection

    best_web_entity = annotations.web_entities[0]
    best_matching_pages = annotations.pages_with_matching_images[0]

    result = {}
    result['best_web_entity'] = best_web_entity
    result['best_matching_pages'] = annotations.pages_with_matching_images

    return result

def best_match_uploaded_img(path):
    """Detects web annotations given an image."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.web_detection(image=image)

    # print(response)

    annotations = response.web_detection

    best_web_entity = annotations.web_entities[0]
    best_matching_pages = annotations.pages_with_matching_images[0]

    result = {}
    result['best_web_entity'] = best_web_entity
    result['best_matching_pages'] = annotations.pages_with_matching_images

    return response


# best_web_entity = best_match_uri(uri)['best_web_entity']
# best_matching_pages = best_match_uri(uri)['best_matching_pages']

# print("The product is " , best_web_entity.description , " with a score of " , best_web_entity.score)

# print("You can find it here ", best_matching_pages[0].url)

# print("\nIf that was not the exact product, here are" , str(len(best_matching_pages)) ," additional searches:\n")
# for item in best_matching_pages:
#     print('\n' , item.page_title, ':' , item.url, '\n')



# detect_web('images/woman_fashion.jpg')