
import cv2
import face_recognition
import numpy as np
import os

cap = cv2.VideoCapture(0)
print("Registering face. Press 'q' when ready.")
while True:
    ret, frame = cap.read()
    cv2.imshow("Register - Press q to capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

face_locations = face_recognition.face_locations(frame)
face_encodings = face_recognition.face_encodings(frame, face_locations)

if face_encodings:
    encoding = face_encodings[0]
    np.save("python-face-api/known_faces/user1_face.npy", encoding)
    print("Face registered successfully!")
else:
    print("No face found! Try again.")
