
import cv2
import face_recognition
import numpy as np
import os

known_face_path = "python-face-api/known_faces/user1_face.npy"
if not os.path.exists(known_face_path):
    print("No registered face found. Please register first.")
    exit()

known_encoding = np.load(known_face_path)
cap = cv2.VideoCapture(0)
print("Looking for face. Press 'q' to stop.")

match_found = False
while True:
    ret, frame = cap.read()
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for encoding in face_encodings:
        results = face_recognition.compare_faces([known_encoding], encoding)
        if results[0]:
            print("✅ Face Matched! Login Successful.")
            match_found = True
            break
    cv2.imshow("Login - Press q to stop", frame)
    if cv2.waitKey(1) & 0xFF == ord('q') or match_found:
        break

cap.release()
cv2.destroyAllWindows()

if not match_found:
    print("❌ Face not recognized.")
