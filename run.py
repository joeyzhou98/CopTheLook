import io
import os

from PIL import Image
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from Segmenter import Segmenter

app = Flask(__name__, static_folder="tempDir")
segmenter = Segmenter()


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        img_name = secure_filename(f.filename)
        dirName = 'tempDir'
        img_path = os.path.join(dirName, img_name)
        if not os.path.exists(dirName):
            os.mkdir(dirName)
        f.save(img_path)

        img = Image.open(img_path)
        segmap, id_to_class = segmenter.predict_on_image(img)

        return render_template('results.html', file_name=img_name, file_path=img_path)


if __name__ == '__main__':
    if "PORT" in os.environ:
        app.run(host='0.0.0.0', port=os.environ["PORT"])
    else:
        app.run(host='0.0.0.0')
