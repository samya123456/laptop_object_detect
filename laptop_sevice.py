from video_recorder import VideoRecorder
from laptop_feed_analysis import generate
import time

recorder = VideoRecorder(duration=5)
recorder.record()
time.sleep(6)
generate()
