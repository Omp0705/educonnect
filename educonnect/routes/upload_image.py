from flask import Flask, request, jsonify,Blueprint
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
upload_bp = Blueprint('upload',__name__)

UPLOAD_FOLDER = 'uploads/'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@upload_bp.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image = request.files['image']
    
    if image.filename == '':
        return jsonify({'error': 'No image selected'}), 400
    
    # Secure the filename to avoid file path issues
    filename = secure_filename(image.filename)
    
    # Save the image to the upload folder
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(image_path)
    
    # Create the URL to access the image (assuming the app runs at http://localhost:5000)
    image_url = f"{UPLOAD_FOLDER+filename}"
    
    # Return the image URL
    return jsonify({'image_url': image_url}), 200

app.register_blueprint(upload_bp, url_prefix='/upload')