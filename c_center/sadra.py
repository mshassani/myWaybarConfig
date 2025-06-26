from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

import subprocess

import monitor

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("c_center.ui", self)

        #Refresh rate connections
        self.button144.toggled.connect(self.change_rate_144)
        self.button60.toggled.connect(self.change_rate_60)

        #power option connections
        self.shutdown.clicked.connect(self.shutdown_clicked)
        self.reboot.clicked.connect(self.reboot_clicked)
        self.logout.clicked.connect(self.logout_clicked)

    #Refresh rate changer
    def change_rate_144(self):
        monitor.change_fps(144)

    def change_rate_60(self):
        monitor.change_fps(60)

    #Power Options menu
    def shutdown_clicked(self):
        subprocess.run(["shutdown", "now"])
        
    def reboot_clicked(self):
        subprocess.run(["reboot"])

    def logout_clicked(self):
        subprocess.run(["hyprctl", "dispatch", "exit"])

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()