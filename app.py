from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import converter
from PIL import Image

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return render_template('upload.html', message='No file part')
    file = request.files['file']
    if file.filename == '':
        return render_template('upload.html', message='No file selected')
    if file:
        # load image
        filename = secure_filename(file.filename)
        file.save(f'uploads/{filename}')

        # convert
        image = Image.open(f'uploads/{filename}')
        converter.convert(image)

        # return
        return render_template('upload.html', message='File uploaded and converted successfully, check output', file=filename)

if __name__ == '__main__':
    app.run(debug=True)