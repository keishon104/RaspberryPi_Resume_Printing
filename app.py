import os
from printer import printDocument
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/pi/Documents/flask-server/docs'
# raspberrypi upload Folder = '/home/pi/Documents/flask-server'
# Macbook Upload folder = '/Users/darpa/Documents/Development/raspberrypi-flask-server/docs'
ALLOWED_EXTENSIONS = set(['pdf','docx'])

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return 'Hello this will be the document upload system'

@app.route('/fileUpload',  methods=['GET', 'POST'])
def upload_file():
    print('code working')
    print(os.path.dirname(os.path.abspath(__file__)))
    if request.method == 'POST':
        print(request.form)
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        print(file.filename)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            PRINTER_NAME = 'Brother_HL-L3270CDW_series'
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            printDocument(PRINTER_NAME,filePath,1)
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return 'The file has been submitted'


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='2000')
