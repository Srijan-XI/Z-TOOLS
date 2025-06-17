import cv2

def check_camera():
    print("\nTesting Camera...")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot access camera.")
        return
    ret, frame = cap.read()
    if ret:
        print("Camera working. Displaying preview...")
        cv2.imshow('Camera Test', frame)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
    else:
        print("Failed to capture image.")
    cap.release()
    # Ensure you have the necessary permissions to access the camera on your system.
    # This code is designed to be run in a Python environment where OpenCV is installed.    