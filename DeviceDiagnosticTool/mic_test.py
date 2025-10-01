import sounddevice as sd

def check_microphone():
    print("\nTesting Microphone (Recording 3 seconds)...")
    duration = 3
    try:
        recording = sd.rec(int(duration * 44100), samplerate=44100, channels=2)
        sd.wait()
        print("Microphone recording successful.")
    except Exception as e:
        print("Microphone test failed:", e)
