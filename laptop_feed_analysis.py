import cv2


def main():
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
    # 20 fps, resolution (640, 480)
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

    # Open the default camera (usually the front camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Record for 10 seconds
    duration = 10  # seconds
    start_time = cv2.getTickCount()
    while (cv2.getTickCount() - start_time) / cv2.getTickFrequency() < duration:
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
    main()
