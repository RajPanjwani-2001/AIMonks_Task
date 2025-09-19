import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import uuid
from detector import detect_objects

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        original_filename = secure_filename(file.filename)
        unique_filename = str(uuid.uuid4()) + '_' + original_filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)

        output_image_path, detection_results = detect_objects(filepath, app.config['OUTPUT_FOLDER'])

        # Extract just the filename for URL
        output_image_url = os.path.basename(output_image_path)
        
        # Prepare JSON for download
        json_filename = os.path.splitext(original_filename)[0] + '.json'
        json_output_path = os.path.join(app.config['OUTPUT_FOLDER'], json_filename)
        
        import json
        with open(json_output_path, 'w') as f:
            json.dump(detection_results, f, indent=4)

        return jsonify({
            'output_image_url': output_image_url,
            'detection_results': detection_results,
            'json_filename': json_filename
        })
    else:
        return jsonify({'error': 'Invalid file type'}), 400

@app.route('/static/outputs/<filename>')
def serve_output_image(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)

@app.route('/static/uploads/<filename>')
def serve_uploaded_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/download_json/<filename>')
def download_json(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
