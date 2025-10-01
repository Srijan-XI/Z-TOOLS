import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
import hardware_tests as ht

class DiagnosticTool(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hardware Diagnostic Tool")
        self.setGeometry(100, 100, 600, 400)
        self.layout = QVBoxLayout()

        # Buttons for each test
        tests = {
            "Test Bluetooth": ht.check_bluetooth,
            "Test Wi-Fi": ht.check_wifi,
            "Test Camera": ht.check_camera,
            "Test Microphone": ht.check_microphone,
            "Test Speaker": ht.check_speaker,
            "Test mouse": ht.check_mouse,
        }

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        
        for label, func in tests.items():
            button = QPushButton(label)
            button.clicked.connect(lambda checked, f=func: self.run_test(f))
            self.layout.addWidget(button)

        self.layout.addWidget(self.output)
        self.setLayout(self.layout)

    def run_test(self, func):
        result = func()
        self.output.append(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DiagnosticTool()
    window.show()
    sys.exit(app.exec_())
