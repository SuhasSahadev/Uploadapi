from flask import Flask, render_template, request, jsonify
import os
import logging
from pathlib import Path

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Determine the uploads directory on the desktop
desktop = Path.home() / 'Desktop'
UPLOADS_DIR = desktop / 'uploads'

def create_uploads_directory():
    """Ensure the uploads directory exists."""
    try:
        if not UPLOADS_DIR.exists():
            UPLOADS_DIR.mkdir(parents=True)
            app.logger.info(f"Created uploads directory: {UPLOADS_DIR}")
        else:
            app.logger.info(f"Uploads directory already exists: {UPLOADS_DIR}")
    except Exception as e:
        app.logger.error(f"Failed to create uploads directory: {str(e)}")
        raise

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/uploadFile', methods=["POST"])
def uploadFile():
    try:
        if "file" not in request.files:
            return jsonify(error="Please select a file"), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify(error="File not selected"), 400

        file_size = request.content_length
        if file_size > 1048576:  # 1 MB limit
            return jsonify(error="File size is too big. Upload file smaller in size"), 400

        # Ensure 'uploads' directory exists
        create_uploads_directory()

        # Save file
        file_path = UPLOADS_DIR / file.filename
        file.save(file_path)
        
        # Verify file save operation
        if file_path.exists():
            app.logger.info(f"File saved successfully at {file_path}")
            return jsonify(message="File uploaded successfully"), 200
        else:
            app.logger.error(f"Failed to save file at {file_path}")
            return jsonify(error="Failed to save file"), 500

    except Exception as e:
        app.logger.error(f"Error uploading file: {str(e)}")
        return jsonify(error="Internal Server Error"), 500

if __name__ == '__main__':
    app.run()  # Set to False in production
