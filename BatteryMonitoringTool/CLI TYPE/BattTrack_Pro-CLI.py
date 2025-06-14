import psutil
import time
import sys

def get_battery_info(input_watt, capacity_mWh):
    battery = psutil.sensors_battery()
    if battery is None:
        print("No battery information available on this device.")
        return

    percent = battery.percent
    charging = battery.power_plugged

    print("="*50)
    print(f"Battery Percentage : {percent}%")
    print("Charging Status    : " + ("Plugged In (Charging)" if charging else "Not Charging"))

    if charging:
        try:
            charging_rate = (input_watt * 1000) / capacity_mWh  # % per hour
            print(f"Estimated Charging Rate : {charging_rate:.2f}% per hour")
            
            if percent < 100:
                remaining_percent = 100 - percent
                est_time_hours = remaining_percent / charging_rate
                est_time_minutes = est_time_hours * 60
                print(f"Estimated Time to Full : {est_time_minutes:.0f} minutes")
        except ZeroDivisionError:
            print("Error: Battery capacity cannot be zero.")
    else:
        print("Note: Estimation only works when charging.")
    print("="*50)

def main():
    try:
        # User input section
        input_watt = float(input("Enter your charger wattage (e.g., 65, 90, 150 , 180): "))
        capacity_mWh = float(input("Enter your battery capacity in mWh (e.g., 50000 for 50Wh): "))
        interval = int(input("Enter refresh interval in seconds (e.g., 10): "))

        if capacity_mWh <= 0 or input_watt <= 0 or interval <= 0:
            print("Error: All input values must be greater than zero.")
            sys.exit(1)

        print("\nBattery Monitor CLI Tool - Started (Press Ctrl+C to stop)\n")

        while True:
            get_battery_info(input_watt, capacity_mWh)
            time.sleep(interval)

    except ValueError:
        print("Invalid input! Please enter numeric values only.")
    except KeyboardInterrupt:
        print("\nExiting Battery Monitor CLI Tool. Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main()
