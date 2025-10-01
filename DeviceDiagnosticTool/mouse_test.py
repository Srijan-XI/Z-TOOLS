from pynput import mouse

def check_mouse():
    print("\nTesting Mouse/Trackpad (Click to detect, stops after 10 clicks)...")
    click_count = [0]  # Mutable type to allow modification in nested function

    def on_click(x, y, button, pressed):
        if pressed:
            click_count[0] += 1
            print(f"Click {click_count[0]}: Mouse clicked at ({x}, {y}) with {button}")
            if click_count[0] >= 10:
                # Stop listener after 10 clicks
                return False

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

if __name__ == "__main__":
    check_mouse()
# This code tests mouse or trackpad functionality by counting clicks and printing their coordinates.
# It uses the `pynput` library to listen for mouse events and stops after 10 clicks.
# Make sure to install the `pynput` library if you haven't already:
# pip install pynput
# Ensure you have the necessary permissions to access mouse events on your system.
# This code is designed to be run in a Python environment where the `pynput`
# library is installed and the script has permission to listen to mouse events.