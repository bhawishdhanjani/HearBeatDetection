from fastapi import FastAPI, File, UploadFile
import shutil
from pathlib import Path
from PyQt5.QtWidgets import QApplication
from rppg import RPPG
import uuid
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this list to specify which origins are allowed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the path where you want to store uploaded videos
UPLOAD_DIR = Path("./uploaded_videos")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.post("/heartbeat/")
async def heartbeat(file: UploadFile = File(...)):
    # Define file path for saving
    file_name = str(uuid.uuid4())+"."+str.split(file.filename,".")[1]
    file_path = UPLOAD_DIR / file_name
    
    # Save the file
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    


    rppg = RPPG()

    # Specify the path to your recorded video file
    
    average_heartbeat = rppg.process_video(file_path)

    # return
    
    return {"filename": file.filename, "status": "Uploaded successfully","average_heartbeat" : average_heartbeat}

