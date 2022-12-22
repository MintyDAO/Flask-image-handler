from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

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
        filename = secure_filename(file.filename)
        file.save(f'uploads/{filename}')
        return render_template('upload.html', message='File uploaded successfully', file=filename)

if __name__ == '__main__':
    app.run(debug=True)