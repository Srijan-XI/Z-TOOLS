# 🔧 System Monitor Tool (Cross-Platform)

A simple and efficient **system monitoring tool** designed to display the **CPU temperature** and **Fan speed** for both **Linux** and **Windows** platforms.

---

## 📂 Project Structure
```
SystemMonitorTool/
│
├── linux_monitor.py # Linux system monitor script
├── windows_monitor.py # Windows system monitor script
├── requirements.txt # Python dependencies list
└── README.md # Documentation and setup guide
```

---

## 🚀 Features

✅ Display **CPU Temperature**  
✅ Display **Fan Speed**  
✅ Platform-specific implementation for Linux and Windows  
✅ Lightweight and Easy-to-Use  
✅ CLI Based (option to extend to GUI or Web in the future)

---

## ⚙️ Platform-specific Details

### 1️⃣ **Linux Setup & Usage**

#### 📌 **Dependencies**

- Python 3.x
- `psutil`
- `lm-sensors`

#### 🛠️ **Installation & Execution**

1. **Install Required Linux Packages**:
   ```bash
   sudo apt update
   sudo apt install lm-sensors
   sudo sensors-detect

2. Install Python Dependencies:
```
pip install -r requirements-for-linux.txt
```

3. Run the Tool:

```
python linux_monitor.py
```
### Output Sample:
```
=== Linux System Monitor ===

>> CPU Temperature:
Core 0:        +45.0°C  
Core 1:        +46.0°C  

>> Fan Speed:
fan1:         1200 RPM
```

### 2️⃣ Windows Setup & Usage

📌 Dependencies

```
Python 3.x
wmi
OpenHardwareMonitor (must be running in background)
```

### 🛠️ Installation & Execution

1. Download & Run OpenHardwareMonitor:

Install and open ```OpenHardwareMonitor.exe.```

Leave it running in the background.

2. Install Python Dependencies:
```
pip install -r requirements-for-win.txt
```
3. Run the Tool:
```
python windows_monitor.py
```
### Output Sample:
```
=== Windows System Monitor ===

Temperature - CPU Package: 47.0 °C
Fan Speed - CPU Fan: 1500 RPM
```
