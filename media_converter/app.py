from flask import Flask, request, render_template, send_file, redirect
import os
import subprocess
import uuid

app = Flask(__name__)

# Create directories for storing uploaded and converted files
UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONVERTED_FOLDER'] = CONVERTED_FOLDER

# Supported audio and video formats for conversion
AUDIO_FORMATS = {'mp3', 'wav', 'aac', 'flac', 'ogg', 'wma'}
VIDEO_FORMATS = {'mp4', 'avi', 'mov', 'mkv', 'flv', 'wmv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in AUDIO_FORMATS.union(VIDEO_FORMATS)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_media():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        # Save the uploaded file
        original_filename = file.filename
        original_filepath = os.path.join(app.config['UPLOAD_FOLDER'], original_filename)
        file.save(original_filepath)

        # Get the target format from the form
        target_format = request.form.get('format')
        if not target_format or target_format.lower() not in AUDIO_FORMATS.union(VIDEO_FORMATS):
            return "Unsupported format", 400

        # Create a unique filename for the converted file
        converted_filename = f"{uuid.uuid4()}.{target_format.lower()}"
        converted_filepath = os.path.join(app.config['CONVERTED_FOLDER'], converted_filename)

        # Convert the media file using FFmpeg
        subprocess.run([
            'ffmpeg', '-i', original_filepath, converted_filepath
        ])

        # Send the converted file to the user
        return send_file(converted_filepath, as_attachment=True)

    return "File not allowed", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
