import io
import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import requests


app = Flask(__name__, static_folder="tempDir")


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        file_name = secure_filename(f.filename)
        dirName = 'tempDir'
        if not os.path.exists(dirName):
            os.mkdir(dirName)
        f.save(os.path.join(dirName, file_name))

        # code here

        return render_template()


if __name__ == '__main__':
    if "PORT" in os.environ:
        app.run(host='0.0.0.0', port=os.environ["PORT"])
    else:
        app.run(host='0.0.0.0')
