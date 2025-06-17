import asyncio
from bleak import BleakScanner

async def check_bluetooth():
    print("Testing Bluetooth (BLEAK)...")
    devices = await BleakScanner.discover(timeout=4.0)
    if devices:
        print("Bluetooth Devices Found:")
        for d in devices:
            print(f"  {d.name} - {d.address}")
    else:
        print("No Bluetooth devices found.")

# Run the async function
if __name__ == "__main__":
    asyncio.run(check_bluetooth())
# Note: This code requires the bleak library to be installed.
# You can install it using pip:
# pip install bleak
# Ensure you have the necessary permissions to access Bluetooth on your system.
# This code is designed to be run in a Python environment where the `bleak` library 