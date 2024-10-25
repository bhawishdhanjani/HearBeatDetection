# main.py
from rppg import RPPG

if __name__ == "__main__":
    rppg = RPPG()
    # Specify the path to your recorded video file
    video_path = "./video3.mp4"
    average_heartbeat = rppg.process_video(video_path)
    print(f"Average Heartbeat: {average_heartbeat}")