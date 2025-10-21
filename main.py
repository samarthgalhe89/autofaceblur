from detector import detect_faces
from blurrer import blur_faces_cv2

video = "input_videos/test.mp4"

detect_faces(video, "faces.json")
blur_faces_cv2(video, "faces.json", "output_videos/blurred.mp4")
