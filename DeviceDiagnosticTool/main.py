import platform

from bluetooth_test import check_bluetooth
from wifi_test import check_wifi
from camera_test import check_camera
from mic_test import check_microphone
from speaker_test import check_speaker
from keyboard_test import check_keyboard
from mouse_test import check_mouse

def main():
    print("===== Device Diagnostic Tool =====")
    print(f"Detected OS: {platform.system()}\n")

    check_bluetooth()
    check_wifi()
    check_camera()
    check_microphone()
    check_speaker()
    check_keyboard()
    check_mouse()

if __name__ == "__main__":
    main()
