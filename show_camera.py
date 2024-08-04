import cv2

# Initialize the camera capture object with the USB camera.
# Often, the first connected camera is at index 0.
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Continuously capture frames from the camera and display them.
try:
    while True:
        # Capture frame-by-frame.
        ret, frame = cap.read()

        # If frame is read correctly, ret is True.
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Resize the frame.
        width = 640  # Set desired width.
        height = 480  # Set desired height.
        frame_resized = cv2.resize(frame, (width, height))

        # Display the resulting frame.
        cv2.imshow('USB Camera', frame_resized)


        # Press 'q' to exit the loop.
        if cv2.waitKey(1) == ord('q'):
            break
finally:
    # When everything done, release the capture.
    cap.release()
    cv2.destroyAllWindows()
