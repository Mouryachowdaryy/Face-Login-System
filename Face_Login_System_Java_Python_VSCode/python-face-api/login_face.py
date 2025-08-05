import cv2
import face_recognition
import numpy as np
import os

# Load the registered face encoding
known_face_path = "python-face-api/known_faces/user1_face.npy"
if not os.path.exists(known_face_path):
    print("No registered face found.")
    exit()

known_face_encoding = np.load(known_face_path)

# Start webcam
video_capture = cv2.VideoCapture(0)

print("Starting face login. Press 'q' to quit.")

while True:
    ret, frame = video_capture.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        results = face_recognition.compare_faces([known_face_encoding], face_encoding)
        if results[0]:
            print("✅ Login successful!")
            video_capture.release()
            cv2.destroyAllWindows()
            exit()

    cv2.imshow('Face Login', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
print("❌ Login failed.")
