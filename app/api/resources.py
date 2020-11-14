"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""
import os
from datetime import datetime
from flask import request, send_file
from flask_restplus import Resource
from werkzeug.utils import secure_filename

from .security import require_auth
from . import api_rest


class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]


@api_rest.route('/upload')
class UploadFile(Resource):
    def post(self):
        if 'file' not in request.files:
            return 'Please upload file', 400

        file = request.files['file']
        if file.filename == '':
            return 'No selected file', 400

        filename = secure_filename(file.filename)
        if not os.path.isdir('app/upload'):
            os.mkdir('app/upload')
        file_path = os.path.join('app/upload', filename)
        file.save(file_path)

        return send_file(os.path.join('upload', filename), mimetype='image')


@api_rest.route('/secure-resource/<string:resource_id>')
class SecureResourceOne(SecureResource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}
