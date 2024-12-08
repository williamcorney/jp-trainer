from gui import MainWindow
from PyQt6.QtWidgets import QApplication
import mido
import sys
from note_handler import note_handler

# Main application logic
if __name__ == "__main__":
    # Initialize the application and main window
    app = QApplication([])
    window = MainWindow()
    window.show()

    # Open MIDI input and use note_handler directly as the callback
    with mido.open_input(callback=lambda message: note_handler(message, window)) as inport:
        sys.exit(app.exec())

