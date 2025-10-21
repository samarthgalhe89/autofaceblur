import cv2
import json
from tqdm import tqdm

def detect_faces(video_path, output_json="faces.json"):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(video_path)
    frames_data = []

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in tqdm(range(total_frames), desc="Detecting faces"):
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        frames_data.append([list(map(int, f)) for f in faces])

    cap.release()
    with open(output_json, "w") as f:
        json.dump(frames_data, f)

    print("✅ Face detection complete! Saved:", output_json)
