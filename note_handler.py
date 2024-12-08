from PyQt6.QtCore import QTimer
def note_handler(message, window):

    if message.type == "note_on":
        if message.note == window.requirednotes[0]:
            QTimer.singleShot(0, window.add_note(message))
    if message.type == "note_off":
        if message.note == window.requirednotes[0]:

            QTimer.singleShot(0, window.remove_note(message))

