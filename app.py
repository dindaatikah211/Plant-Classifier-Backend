from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import numpy as np
import tensorflow as tf
import json, io, os

app = Flask(__name__)
CORS(app)

MODEL_PATH = 'model/plant_model.h5'
CLASS_PATH = 'model/class_names.json'

model, class_names = None, []

def load_model():
    global model, class_names
    if os.path.exists(MODEL_PATH) and os.path.exists(CLASS_PATH):
        print("Loading model...")
        model = tf.keras.models.load_model(MODEL_PATH)
        with open(CLASS_PATH) as f:
            class_names = json.load(f)
        print(f"✅ Model loaded! {len(class_names)} kelas")
    else:
        print("⚠️ Belum ada model di folder model/")

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'model_loaded': model is not None})

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model belum di-load'}), 500
    if 'image' not in request.files:
        return jsonify({'error': 'Tidak ada gambar'}), 400

    file  = request.files['image']
    img   = Image.open(io.BytesIO(file.read())).convert('RGB')
    img   = img.resize((224, 224))
    arr   = np.expand_dims(np.array(img) / 255.0, axis=0)

    preds       = model.predict(arr)
    top3_idx    = np.argsort(preds[0])[-3:][::-1]
    top3        = [{'class': class_names[i],
                    'confidence': round(float(preds[0][i]) * 100, 2)}
                   for i in top3_idx]

    return jsonify({
        'predicted_class': top3[0]['class'],
        'confidence'     : top3[0]['confidence'],
        'top3'           : top3
    })

if __name__ == '__main__':
    load_model()
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)