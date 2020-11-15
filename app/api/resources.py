"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""
import os
import uuid
from datetime import datetime

from PIL import Image
from flask import request, jsonify, send_from_directory, url_for
from flask_restx import Resource
from werkzeug.utils import secure_filename

from .security import require_auth
from . import api_rest
from .segmenter import get_cropped_segments


class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]


@api_rest.route('/secure-resource/<string:resource_id>')
class SecureResourceOne(SecureResource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}


@api_rest.route('/upload')
class UploadFile(Resource):
    def post(self):
        if 'file' not in request.files:
            return 'Please upload file', 400

        file = request.files['file']
        if file.filename == '':
            return 'No selected file', 400

        root_dir = os.getcwd()
        img = Image.open(file)
        filename = secure_filename(file.filename)
        extension = filename.split('.')[1]
        temp_folder_path = os.path.join(root_dir, 'temp')
        if not os.path.isdir(temp_folder_path):
            os.makedirs(temp_folder_path)
        main_img_name = f'{str(uuid.uuid4())}.{extension}'
        main_img_path = os.path.join(temp_folder_path, main_img_name)
        img.save(main_img_path)
        segments = get_cropped_segments(img)

        segments_response = []
        for segment in segments:
            img_name = f'{str(uuid.uuid4())}.{extension}'
            img_path = os.path.join(temp_folder_path, img_name)
            segment['image_object'].save(img_path)
            segments_response.append({
                'img_name': img_name,
                'class': segment['class'],
                'urls': segment['urls']
            })

        return jsonify({
            'main_img_name': main_img_name,
            'segments': segments_response
        })


@api_rest.route('/<string:filename>')
class GetImage(Resource):
    def get(self, filename):
        root_dir = os.getcwd()
        return send_from_directory(os.path.join(root_dir, 'temp'), filename)

# @api_rest.route('/reverse-image/<string:img>')
# class ReverseImage(SecureResource):
#     """ Unsecure Resource Class: Inherit from Resource """
#
#     def get(self, img):
#         results = best_match_uploaded_img(img)
#
#         print(results)
#
#         annotations = results.web_detection
#
#         best_web_entity = annotations.web_entities[0]
#         best_matching_pages = annotations.pages_with_matching_images[0]
#
#         result = {}
#         result['best_web_entity'] = best_web_entity
#         result['best_matching_pages'] = annotations.pages_with_matching_images
#
#         # print(result)
#
#
#         # result['best_web_entity'] = best_web_entity
#         # result['best_matching_pages'] = annotations.pages_with_matching_images
#
#         json_string = proto.Message.to_json(results)
#
#         print(json_string)
#
#         return make_response(jsonify(json_string))
#
#
# @api_rest.route('/reverse-uri/<string:url>')
# class ReverseUri(SecureResource):
#     """ Unsecure Resource Class: Inherit from Resource """
#
#     def get(self, url):
#         result = best_match_uri(url)
#         return make_response(jsonify(result))
#
#
# @api_rest.route('/segment/<string:image>')
# class Segment(SecureResource):
#     """ Unsecure Resource Class: Inherit from Resource """
#
#     def get(self, image):
#         result = get_cropped_segments(image)
#
#         print(result)
#
#         return make_response(jsonify(result))