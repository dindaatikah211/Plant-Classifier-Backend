# 🌿 Plant Classifier — Backend

REST API berbasis Flask untuk klasifikasi jenis tumbuhan menggunakan model deep learning (MobileNetV2 + Transfer Learning).

> Bagian dari project **Tubes Pengolahan Citra** — sistem klasifikasi tumbuhan berbasis gambar.

---

## Struktur Folder

```
backend/
├── app.py               # Flask API utama
├── requirements.txt     # Daftar dependency
├── venv/                # Virtual environment (tidak di-push)
└── model/
    ├── plant_model.h5       # Model hasil training (tidak di-push, >100MB)
    └── class_names.json     # Daftar nama kelas
```

---

## Instalasi & Menjalankan

### 1. Clone repo

```bash
git clone https://github.com/username/plant-classifier-backend.git
cd plant-classifier-backend
```

### 2. Buat & aktifkan virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install dependency

```bash
pip install -r requirements.txt
```

### 4. Letakkan file model

Taruh `plant_model.h5` dan `class_names.json` di dalam folder `model/`.  
File model bisa di-download dari [Google Drive / Release](#) *(link menyusul)*.

### 5. Jalankan server

```bash
python app.py
```

Server berjalan di `http://localhost:5000`

---

## Endpoints

### `GET /health`
Cek status server dan apakah model sudah ter-load.

**Response:**
```json
{
  "status": "ok",
  "model_loaded": true
}
```

---

### `POST /predict`
Kirim gambar daun untuk diprediksi.

**Request:** `multipart/form-data`
| Field   | Tipe   | Keterangan          |
|---------|--------|---------------------|
| `image` | `file` | File gambar (JPG/PNG/WEBP) |

**Response:**
```json
{
  "predicted_class": "Tomato___Early_blight",
  "confidence": 97.43,
  "top3": [
    { "class": "Tomato___Early_blight", "confidence": 97.43 },
    { "class": "Tomato___Late_blight",  "confidence": 1.82  },
    { "class": "Tomato___healthy",      "confidence": 0.51  }
  ]
}
```

---

## Model

- **Arsitektur:** MobileNetV2 + Transfer Learning
- **Dataset:** [New Plant Diseases Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset) (87.000+ gambar, 38 kelas)
- **Training:** Google Colab (GPU T4)
- **Akurasi validasi:** ~95%+

---

## 🛠️ Tech Stack

- Python 3.x
- Flask
- TensorFlow / Keras
- Pillow
- NumPy

---

## 🔗 Repo Terkait

- **Frontend (Next.js):** [plant-classifier-frontend](https://github.com/dindaatikah211/plant-classifier-frontend)
