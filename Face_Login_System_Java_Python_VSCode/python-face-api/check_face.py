import numpy as np
import os

file_path = "python-face-api/known_faces/user1_face.npy"

if os.path.exists(file_path):
    data = np.load(file_path)
    print("✅ Face encoding data found:")
    print(data)
else:
    print("❌ Face not registered. File not found.")
