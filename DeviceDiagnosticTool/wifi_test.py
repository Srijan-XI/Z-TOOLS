import subprocess

def check_wifi():
    print("\nTesting Wi-Fi...")
    try:
        result = subprocess.check_output(["nmcli", "dev", "wifi"], text=True)
        print(result)
    except Exception as e:
        print("Wi-Fi scan failed:", e)
