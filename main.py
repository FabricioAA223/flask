from flask import Flask, render_template, jsonify
import cv2
import time
import base64
from datetime import datetime

app = Flask(__name__)
camera = cv2.VideoCapture(0)  # Utiliza el índice 0 para la cámara integrada de la lapto

def capture_images(interval, duration):
    start_time = time.time()
    images = []
    while time.time() - start_time < duration:
        success, frame = camera.read()
        if success:
            _, buffer = cv2.imencode('.jpg', frame)
            image_base64 = base64.b64encode(buffer).decode('utf-8')
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            images.append({'image': image_base64, 'timestamp': timestamp})
            time.sleep(interval)

    return images

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_images/<int:interval>/<int:duration>', methods=['GET'])
def get_images(interval, duration):
    images = capture_images(interval, duration)
    return jsonify({'images': images})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
