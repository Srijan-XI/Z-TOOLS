import platform
import asyncio
import subprocess
import cv2
import sounddevice as sd
import pygame
from pynput import mouse
from bleak import BleakScanner

# Bluetooth using BLEAK
async def check_bluetooth():
    try:
        devices = await BleakScanner.discover(timeout=4.0)
        if devices:
            result = "Bluetooth Devices Found:\n"
            for d in devices:
                result += f"{d.name} - {d.address}\n"
            return result
        else:
            return "No Bluetooth devices found."
    except Exception as e:
        return f"Bluetooth Error: {e}"

# Wi-Fi Check (Linux-based, 'nmcli' command)
def check_wifi():
    try:
        result = subprocess.check_output(["nmcli", "dev", "wifi"], text=True)
        return result
    except Exception as e:
        return f"Wi-Fi Error: {e}"

# Camera Test
def check_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return "Camera not accessible"
    ret, frame = cap.read()
    cap.release()
    return "Camera working" if ret else "Camera capture failed"

# Microphone Test
def check_microphone():
    try:
        sd.rec(int(3 * 44100), samplerate=44100, channels=2)
        sd.wait()
        return "Microphone recording successful"
    except Exception as e:
        return f"Microphone Error: {e}"

# Speaker Test
def check_speaker():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("test_01.wav")  # Ensure this file exists in the working directory
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        return "Speaker test sound played"
    except Exception as e:
        return f"Speaker Error: {e}"

# Mouse/Trackpad Test - stops after 10 clicks
def check_mouse():
    print("\nTesting Mouse/Trackpad (Click to detect, stops after 10 clicks)...")
    click_count = [0]  # List for mutability in nested function

    def on_click(x, y, button, pressed):
        if pressed:
            click_count[0] += 1
            print(f"Click {click_count[0]}: Mouse clicked at ({x}, {y}) with {button}")
            if click_count[0] >= 10:
                return False  # Stop listener after 10 clicks

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    return "Mouse/Trackpad test completed (10 clicks)."

# Main Testing Function
def run_all_tests():
    print(check_wifi())
    print(check_camera())
    print(check_microphone())
    print(check_speaker())
    print(check_mouse())
    # Run async bluetooth check
    bluetooth_result = asyncio.run(check_bluetooth())
    print(bluetooth_result)

if __name__ == "__main__":
    run_all_tests()
