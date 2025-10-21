🎥 AutoFaceBlur

AutoFaceBlur is a simple, easy-to-run Python project that detects faces in videos (using OpenCV Haar Cascade) and blurs only the face regions. It includes a Streamlit web UI so anyone can upload a video, process it, preview the result, and download the blurred output — no frontend coding required.

🔹 Features

Face detection using OpenCV Haar Cascade (haarcascade_frontalface_default.xml)

Face-only blurring (tight crop around detected face)

Adjustable blur strength via Streamlit slider

Streamlit web UI with upload → process (spinner) → preview → download

Single-threaded (simple and portable)

🗂 Repo structure
AutoFaceBlur/
├─ input_videos/           # Uploaded videos (create this folder)
├─ output_videos/          # Blurred videos output (create this folder)
├─ models/                 # Optional (you can store models or files here)
├─ detector.py             # Face detection (Haar cascade)
├─ blurrer.py              # Face blur function
├─ app.py                  # Streamlit web UI
├─ requirements.txt        # Python dependencies
└─ README.md               # This file

⚙️ Prerequisites

Python 3.8+

FFmpeg is not required for this OpenCV-based version (we process with OpenCV).

(Optional) A modern web browser to open the Streamlit app.

🛠 Installation

Clone the repository (or create the folder and add files):

git clone https://github.com/your-username/AutoFaceBlur.git
cd AutoFaceBlur


(Optional but recommended) Create and activate a virtual environment:

python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Windows (cmd)
venv\Scripts\activate.bat


Install dependencies:

pip install -r requirements.txt


Example requirements.txt:

opencv-python>=4.6.0
streamlit>=1.20.0
tqdm>=4.60.0


Create required folders if they don’t exist:

mkdir input_videos output_videos models

🚀 Run (Streamlit web UI)

Start the app:

streamlit run app.py


Open the URL printed in the terminal (usually http://localhost:8501) in your browser.

Workflow in the app:

Upload a video (mp4, avi, mov)

Choose the blur strength using the slider

The app shows the original video, runs detection & blur (spinner displayed while processing)