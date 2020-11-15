"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""
import os
from datetime import datetime
from flask import request, send_file, jsonify, make_response
from flask_restx import Resource
from werkzeug.utils import secure_filename

from .vision_script import best_match_uploaded_img
from .vision_script import best_match_uri
from .security import require_auth
from . import api_rest
from google.protobuf.json_format import MessageToJson
import proto
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

        # filename = secure_filename(file.filename)
        # if not os.path.isdir('app/upload'):
        #     os.mkdir('app/upload')
        # file_path = os.path.join('app/upload', filename)
        # file.save(file_path)
        # send_file(os.path.join('upload', filename), mimetype='image')

        # ReverseImage.get(self,file.stream.read())
        
        # files={"file": request.files["file"]}



        return Segment.get(self, file.read())

@api_rest.route('/reverse-image/<string:img>')
class ReverseImage(SecureResource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, img):
        results = best_match_uploaded_img(img)

        print(results)

        annotations = results.web_detection

        best_web_entity = annotations.web_entities[0]
        best_matching_pages = annotations.pages_with_matching_images[0]

        result = {}
        result['best_web_entity'] = best_web_entity
        result['best_matching_pages'] = annotations.pages_with_matching_images

        # print(result)


        # result['best_web_entity'] = best_web_entity
        # result['best_matching_pages'] = annotations.pages_with_matching_images

        json_string = proto.Message.to_json(results)

        print(json_string)

        return make_response(jsonify(json_string))

@api_rest.route('/reverse-uri/<string:url>')
class ReverseUri(SecureResource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, url):
        result = best_match_uri(url)
        return make_response(jsonify(result))

@api_rest.route('/segment/<string:image>')
class Segment(SecureResource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, image):
        result = get_cropped_segments(image)

        print(result)

        return make_response(jsonify(result))