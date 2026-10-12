import sys

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)

def main():

    #Qt Application
    app = QApplication(sys.argv)

    #Main window
    window = QMainWindow()
    window.setWindowTitle("DriveSenseH7 V4.0")
    window.resize(1280, 720)

    #Central Container and Layouts
    central_widget = QWidget()
    main_layout = QVBoxLayout()
    dashboard_layout = QHBoxLayout()

    #Create Labels
    title_label = QLabel("DriveSenseH7 V4 - Live Telemetry")
    speed_label = QLabel("Speed: 0 km/h")
    rpm_label = QLabel("RPM: 0")
    gear_label = QLabel("Gear: N")

    #Title Label Styling
    title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    title_label.setStyleSheet("""
        color: white;
        font-size: 28px;
        font-weight: bold;
        padding: 20px;
    """)

    #Vehicle Inforamation Labels Styling
    indicator_style = """
        color: cyan;
        background-color: #202833;
        font-size: 26px;
        font-weight: bold;
        padding: 25px;
        border-radius: 12px;
    """
    speed_label.setStyleSheet(indicator_style)
    rpm_label.setStyleSheet(indicator_style)
    gear_label.setStyleSheet(indicator_style)

    #Center Indicator Text
    for label in (speed_label, rpm_label, gear_label):
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    #Dashboard layout
    dashboard_layout.addWidget(speed_label)
    dashboard_layout.addWidget(rpm_label)
    dashboard_layout.addWidget(gear_label)

    dashboard_layout.setSpacing(15)

    main_layout.addWidget(title_label)
    main_layout.addLayout(dashboard_layout)

    main_layout.addStretch()

    central_widget.setLayout(main_layout)

    #Dark Background
    central_widget.setStyleSheet("background-color: #111820;")

    window.setCentralWidget(central_widget)

    #Simulated vehicle Speed
    current_speed = 0

    def update_speed():
        nonlocal current_speed
        current_speed += 1
        if current_speed > 200:
            current_speed = 0
        speed_label.setText(f"Speed: {current_speed} km/h")

    #Create a timer
    timer = QTimer()

    #Connect timer signal to our function
    timer.timeout.connect(update_speed)
    timer.start(100)  # Update every 100 ms

    #Show the window
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()