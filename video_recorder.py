import cv2


class VideoRecorder:
    def __init__(self, output_file='output.mp4', duration=10, fps=20, resolution=(640, 480)):
        self.output_file = output_file
        self.duration = duration
        self.fps = fps
        self.resolution = resolution

    def record(self):
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
        out = cv2.VideoWriter(self.output_file, fourcc,
                              self.fps, self.resolution)

        # Open the default camera (usually the front camera)
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error: Could not open camera.")
            return

        # Record for specified duration
        start_time = cv2.getTickCount()
        while (cv2.getTickCount() - start_time) / cv2.getTickFrequency() < self.duration:
            # Capture frame-by-frame
            ret, frame = cap.read()

            if not ret:
                print("Error: Unable to capture frame.")
                break

            # Write the frame to the output video file
            out.write(frame)

            # Display the resulting frame
            cv2.imshow('Front Camera Feed', frame)
            cv2.waitKey(1)

        # Release resources
        cap.release()
        out.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    # Create an instance of VideoRecorder with default settings
    recorder = VideoRecorder()

    # Start recording
    recorder.record()
