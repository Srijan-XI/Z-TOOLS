import wmi

def get_hardware_info():
    try:
        w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        result = []

        for sensor in temperature_infos:
            if sensor.SensorType == 'Temperature':
                result.append(f"Temperature - {sensor.Name}: {sensor.Value} °C")
            elif sensor.SensorType == 'Fan':
                result.append(f"Fan Speed - {sensor.Name}: {sensor.Value} RPM")

        return "\n".join(result) if result else "No sensor data found."

    except Exception as e:
        return f"Error: {e}\nMake sure OpenHardwareMonitor is running as administrator."

if __name__ == "__main__":
    print("=== Windows System Monitor ===\n")
    print(get_hardware_info())
