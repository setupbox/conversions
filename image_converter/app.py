from flask import Flask, request, render_template, send_file, redirect, url_for
import os
import subprocess
import uuid

app = Flask(__name__)

# Create a directory for storing uploaded and converted files
UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONVERTED_FOLDER'] = CONVERTED_FOLDER

# Allowed image formats for conversion
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_image():
    # Check if a file is provided
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        # Save the file
        original_filename = file.filename
        original_filepath = os.path.join(app.config['UPLOAD_FOLDER'], original_filename)
        file.save(original_filepath)

        # Get the desired format from the form
        target_format = request.form.get('format')
        if not target_format or target_format.lower() not in ALLOWED_EXTENSIONS:
            return "Unsupported format", 400

        # Create a unique filename for the converted file
        converted_filename = f"{uuid.uuid4()}.{target_format.lower()}"
        converted_filepath = os.path.join(app.config['CONVERTED_FOLDER'], converted_filename)

        # Convert the image using ImageMagick's `convert` command
        subprocess.run(['convert', original_filepath, converted_filepath])

        # Send the converted file to the user
        return send_file(converted_filepath, as_attachment=True)

    return "File not allowed", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
