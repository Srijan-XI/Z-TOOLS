import subprocess

def get_cpu_temperature():
    try:
        output = subprocess.check_output("sensors", encoding='utf-8')
        lines = output.split('\n')
        temps = [line.strip() for line in lines if 'Core' in line or 'temp1' in line]
        return '\n'.join(temps) if temps else "Temperature data not found."
    except Exception as e:
        return f"Error fetching temperature: {e}"

def get_fan_speed():
    try:
        output = subprocess.check_output("sensors", encoding='utf-8')
        lines = output.split('\n')
        fans = [line.strip() for line in lines if 'fan' in line]
        return '\n'.join(fans) if fans else "Fan speed data not found."
    except Exception as e:
        return f"Error fetching fan speed: {e}"

if __name__ == "__main__":
    print("=== Linux System Monitor ===\n")
    print(">> CPU Temperature:")
    print(get_cpu_temperature())
    print("\n>> Fan Speed:")
    print(get_fan_speed())
