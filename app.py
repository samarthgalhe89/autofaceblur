import streamlit as st
import os
import cv2
import json
from detector import detect_faces

st.set_page_config(page_title="AutoFaceBlur", page_icon="🎥", layout="centered")
st.title("🎥 AutoFaceBlur – Face Blur using OpenCV Haar Cascade")
st.markdown("Upload a video, choose blur strength, and blur faces automatically!")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])
blur_strength = st.slider("Blur Strength", min_value=5, max_value=99, value=35, step=2)

if uploaded_file is not None:
    input_path = os.path.join("input_videos", uploaded_file.name)
    output_path = os.path.join("output_videos", "blurred_" + uploaded_file.name)

    # Save uploaded video
    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    st.video(input_path, format="video/mp4")

    # Show spinner while processing
    with st.spinner("Processing… please wait ⏳"):
        # Step 1: Detect faces
        detect_faces(input_path, "faces.json")

        # Step 2: Apply blur frame by frame
        with open("faces.json", "r") as f:
            frames_data = json.load(f)

        cap = cv2.VideoCapture(input_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        for i in range(total_frames):
            ret, frame = cap.read()
            if not ret:
                break

            faces = frames_data[i] if i < len(frames_data) else []

            for (x, y, w, h) in faces:
                # Tighter crop around face
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

    st.success("✅ Done! Faces blurred successfully.")
    st.video(output_path, format="video/mp4")

    with open(output_path, "rb") as f:
        st.download_button("⬇️ Download Blurred Video", f, file_name="blurred_output.mp4")
