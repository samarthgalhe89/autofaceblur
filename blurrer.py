import cv2
import json
from tqdm import tqdm

def blur_faces_cv2(input_video, faces_json, output_video="output_videos/blurred.mp4", blur_strength=35):
    with open(faces_json, "r") as f:
        frames_data = json.load(f)

    cap = cv2.VideoCapture(input_video)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in tqdm(range(total_frames), desc="Applying blur"):
        ret, frame = cap.read()
        if not ret:
            break

        faces = frames_data[i] if i < len(frames_data) else []
        for (x, y, w, h) in faces:
            # Crop tighter around face (10% margin inside bounding box)
            x1 = x + int(w * 0.1)
            y1 = y + int(h * 0.1)
            w1 = int(w * 0.8)
            h1 = int(h * 0.8)

            face_region = frame[y1:y1+h1, x1:x1+w1]
            if face_region.size > 0:
                face_region = cv2.GaussianBlur(face_region, (blur_strength, blur_strength), 30)
                frame[y1:y1+h1, x1:x1+w1] = face_region

        out.write(frame)

    cap.release()
    out.release()
    print(f"🎉 Blurred faces saved to {output_video}")
