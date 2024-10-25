# main.py
from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow
from rppg import RPPG

if __name__ == "__main__":
    app = QApplication([])

    rppg = RPPG(parent=app)

    # Specify the path to your recorded video file
    video_path = "./video3.mp4"
    average_heartbeat = rppg.process_video(video_path)

    print(f"Average Heartbeat: {average_heartbeat}")