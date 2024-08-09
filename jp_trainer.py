import mido
from note_display import NoteDisplay
from theory import SCALES, Theory

notes_on: list = []
good_notes: list = []

theory_item: dict
note_ui: NoteDisplay

th = Theory()

def button_handler() -> None:

    global good_notes, theory_item

    match note_ui.selected_option:
        case "CHORDS":
            theory_item = th.get_chord()
            good_notes = theory_item["notes"]
        case "MODES":
            theory_item = th.get_mode()
            good_notes = theory_item["notes"]
        case "SCALES":
            print ("Scales")


note_ui = NoteDisplay(button_handler)

def note_handler(note: mido.Message) -> None:

    if note.type in ["note_on", "note_off"]:
        note_id = int(note.note) if note.note is not None else -1
        if note.type == "note_on":
            is_green = False
            if note_id in good_notes:
                is_green = True
            note_ui.add_note(note_id, is_green)
            if note.note not in notes_on:
                notes_on.append(note.note)
        elif note.type == "note_off":
            note_ui.remove_note(note_id)
            if note_id in notes_on:
                notes_on.remove(note_id)

portname = (mido.get_input_names()[0])
with mido.open_input(portname, callback=note_handler) as port:
    print("Using {}".format(port))
    note_ui.window.mainloop()

