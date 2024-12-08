from PyQt6.QtCore import QTimer

def note_handler(message, window):
    print (window.requirednotes)
    if message.type == "note_on":
        if message.note == window.requirednotes[0]:
            QTimer.singleShot(0, window.add_image)
            window.get_theory()

    if message.type == "note_off":

        if message.note == window.requirednotes[0]:
            QTimer.singleShot(0, window.remove_image)
