from flask import Flask, render_template, request, jsonify
import os
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

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
        if file_size > 1048576:
            return jsonify(error="File size is too big. Upload file smaller in size"), 400

        # Ensure 'uploads' directory exists
        uploads_dir = os.path.join(os.getcwd(), 'fileUploadAPI', 'uploads')
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir, exist_ok=True)
        # Save file
        file.save(os.path.join(uploads_dir, file.filename))
        
        return jsonify(message="File uploaded successfully"), 200

    except Exception as e:
        app.logger.error(f"Error uploading file: {str(e)}")
        return jsonify(error="Internal Server Error"), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production