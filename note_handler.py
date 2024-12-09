#note_handler.py

def note_handler(message, window):
    if message.type == "note_on":
        window.note_on_signal.emit(message.note)
        if message.note == window.requirednotes[0]:
            pass
            # Emit signal for note_on
            # window.note_on_signal.emit(message.note)
            #window.get_theory()

    if message.type == "note_off":
        window.note_off_signal.emit(message.note)
        if message.note == window.requirednotes[0]:
            pass
            # Emit signal for note_off

