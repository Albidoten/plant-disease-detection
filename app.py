from flask import Flask, request, render_template, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import base64
import io

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
RESULTS_FOLDER = 'results'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}

# Create directories if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)
os.makedirs('static', exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULTS_FOLDER'] = RESULTS_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Load YOLO model
print("Loading YOLO model...")
try:
    model = YOLO('yolov8n.pt')  # This will download the model if not present
    print("YOLO model loaded successfully!")
except Exception as e:
    print(f"Error loading YOLO model: {e}")
    model = None

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_image_with_yolo(image_path):
    """Process image with YOLO model and return results"""
    if model is None:
        return None, "YOLO model not loaded"
    
    try:
        # Run inference
        results = model(image_path)
        
        # Get the first result (assuming single image)
        result = results[0]
        
        # Draw bounding boxes on the image
        annotated_image = result.plot()
        
        # Convert BGR to RGB for web display
        annotated_image_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
        
        # Convert to PIL Image
        pil_image = Image.fromarray(annotated_image_rgb)
        
        # Save the result image
        result_filename = f"result_{os.path.basename(image_path)}"
        result_path = os.path.join(app.config['RESULTS_FOLDER'], result_filename)
        pil_image.save(result_path)
        
        # Get detection details
        detections = []
        if result.boxes is not None:
            for box in result.boxes:
                detection = {
                    'class_name': model.names[int(box.cls)],
                    'confidence': float(box.conf),
                    'bbox': box.xyxy[0].tolist()  # [x1, y1, x2, y2]
                }
                detections.append(detection)
        
        return result_filename, detections
        
    except Exception as e:
        return None, f"Error processing image: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file selected'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Add timestamp to avoid conflicts
        import time
        timestamp = str(int(time.time()))
        filename = f"{timestamp}_{filename}"
        
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Process with YOLO
        result_filename, detections = process_image_with_yolo(filepath)
        
        if result_filename:
            return jsonify({
                'success': True,
                'original_image': filename,
                'result_image': result_filename,
                'detections': detections
            })
        else:
            return jsonify({'error': detections}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/results/<filename>')
def result_file(filename):
    return send_from_directory(app.config['RESULTS_FOLDER'], filename)

if __name__ == '__main__':
    print("Starting YOLO Web Application...")
    print("Make sure to install requirements: pip install -r requirements.txt")
    
    # Get port from environment variable for deployment platforms
    import os
    port = int(os.environ.get('PORT', 5000))
    
    # Use debug=False in production
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
