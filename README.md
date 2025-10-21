🎥 AutoFaceBlur

AutoFaceBlur is a simple, easy-to-run Python project that detects faces in videos (using OpenCV Haar Cascade) and blurs only the face regions. It includes a Streamlit web UI so anyone can upload a video, process it, preview the result, and download the blurred output — no frontend coding required.

🔹 Features

Face detection using OpenCV Haar Cascade (haarcascade_frontalface_default.xml)

Face-only blurring (tight crop around detected face)

Adjustable blur strength via Streamlit slider

Streamlit web UI with upload → process (spinner) → preview → download

Single-threaded (simple and portable)

⚙️ Prerequisites

Python 3.8+

FFmpeg is not required for this OpenCV-based version (we process with OpenCV).

(Optional) A modern web browser to open the Streamlit app.

🛠 Installation

Clone the repository (or create the folder and add files):

git clone https://github.com/samarthgalhe89/AutoFaceBlur.git

(Optional but recommended) Create and activate a virtual environment:
python -m venv venv

# macOS / Linux
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Windows (cmd)
venv\Scripts\activate.bat


#Install dependencies
pip install -r requirements.txt


Example requirements.txt:

opencv-python>=4.6.0
streamlit>=1.20.0
tqdm>=4.60.0

=> Run the App (Streamlit UI)
Start the app:
streamlit run app.py


Once started, open the link shown in the terminal — usually:
👉 http://localhost:8501

#App Workflow

Upload a Video: Supported formats → .mp4, .avi, .mov

Adjust Blur Strength: Use the slider to control the blur intensity.

Processing: App displays a spinner while detecting and blurring faces.

View Results: The processed video will appear once complete.