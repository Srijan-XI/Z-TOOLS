import psutil
import tkinter as tk
from tkinter import ttk, messagebox

def get_battery_info(input_watt, capacity_mWh):
    battery = psutil.sensors_battery()
    if battery is None:
        battery_label.config(text="No battery information available.")
        return

    percent = battery.percent
    charging = battery.power_plugged

    battery_label.config(text=f"Battery Percentage: {percent}%")
    charging_label.config(text=f"Charging Status: {'Plugged In' if charging else 'Not Charging'}")

    if charging:
        try:
            charging_rate = (input_watt * 1000) / capacity_mWh  # % per hour
            rate_label.config(text=f"Estimated Charging Rate: {charging_rate:.2f}% per hour")

            if percent < 100:
                remaining_percent = 100 - percent
                est_time_hours = remaining_percent / charging_rate
                est_time_minutes = est_time_hours * 60
                time_label.config(text=f"Est. Time to Full Charge: {est_time_minutes:.0f} minutes")
            else:
                time_label.config(text="Battery Full.")
        except ZeroDivisionError:
            rate_label.config(text="Error: Battery capacity cannot be zero.")
            time_label.config(text="Cannot estimate time.")
    else:
        rate_label.config(text="Estimated Charging Rate: Not Charging")
        time_label.config(text="Est. Time to Full Charge: N/A")

def start_monitoring():
    try:
        input_watt = float(wattage_entry.get())
        capacity_mWh = float(capacity_entry.get())

        if input_watt <= 0 or capacity_mWh <= 0:
            raise ValueError

        # Start periodic battery info updates
        def update():
            get_battery_info(input_watt, capacity_mWh)
            root.after(5000, update)  # Refresh every 5 seconds

        update()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid positive numbers for wattage and capacity.")

# Create GUI window
root = tk.Tk()
root.title("BattTrack Pro - Battery Monitor")
root.geometry("400x350")
root.resizable(False, False)  # Disable resizing

# Input section
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

ttk.Label(input_frame, text="Charger Wattage (W):", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5, sticky='e')
wattage_entry = ttk.Entry(input_frame)
wattage_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Battery Capacity (mWh):", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5, sticky='e')
capacity_entry = ttk.Entry(input_frame)
capacity_entry.grid(row=1, column=1, padx=5, pady=5)

# Start Button
start_button = ttk.Button(root, text="Start Monitoring", command=start_monitoring)
start_button.pack(pady=10)

# Info Labels
battery_label = ttk.Label(root, text="Battery Percentage: ", font=("Arial", 12))
battery_label.pack(pady=5)

charging_label = ttk.Label(root, text="Charging Status: ", font=("Arial", 12))
charging_label.pack(pady=5)

rate_label = ttk.Label(root, text="Estimated Charging Rate: ", font=("Arial", 12))
rate_label.pack(pady=5)

time_label = ttk.Label(root, text="Est. Time to Full Charge: ", font=("Arial", 12))
time_label.pack(pady=5)

# Run GUI
root.mainloop()
