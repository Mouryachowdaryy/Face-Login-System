
# 🔐 Face Login System — Java + Python

A hybrid project that allows secure **face login** using a **Java GUI** and **Python OpenCV face recognition**.

---

## 📂 Project Structure

```
Face_Login_System_Java_Python/
│
├── java-app/
│   └── FaceLoginUI.java            # Java UI with face login buttons
│
├── python-face-api/
│   ├── register_face.py           # Capture and save face
│   ├── recognize_face.py          # Face recognition for login
│   └── known_faces/               # Saved encodings (as .npy)
│
├── shared/logs/                   # (Optional) logging folder
├── .vscode/                       # VS Code config
└── README.md                      # This file
```

---

## ✅ Prerequisites

- Java 8+ and VS Code Java Extension Pack
- Python 3.7+ with `opencv-python`, `face_recognition`, `numpy`
```bash
pip install opencv-python face_recognition numpy
```

---

## 🚀 Run Instructions

### 🟡 Step 1: Launch Java UI

```bash
cd java-app
javac FaceLoginUI.java
java FaceLoginUI
```

### 🟢 Step 2: Register Face

- Click “Register Face”
- Your webcam opens → Press `q` to capture your face

### 🔵 Step 3: Login with Face

- Click “Login with Face”
- It compares your face with saved encoding
- Displays success or fail message

---

## 💡 Tip

You can add logging or extend it to include multiple users.

---

Built with ❤️ by integrating Java Swing, Python OpenCV, and Face Recognition.
