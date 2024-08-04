from tkinter import *

from PIL import Image, ImageTk

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 1060

IMAGE_NAMES = [
    "key_green_left",
    "key_green_mid",
    "key_green_right",
    "key_green_top",
    "key_red_left",
    "key_red_mid",
    "key_red_right",
    "key_red_top",
]
NOTES_TO_IMAGE_MAP = {
    0: "left",
    1: "top",
    2: "mid",
    3: "top",
    4: "right",
    5: "left",
    6: "top",
    7: "mid",
    8: "top",
    9: "mid",
    10: "top",
    11: "right",
    12: "left",
}
NOTES_Y = 401
NOTES_X = {36: 2, 37: 26.0, 38: 35, 39: 60.0, 40: 69, 41: 103.5, 42: 128.0, 43: 137.5, 44: 162.0, 45: 171.5, 46: 196.5, 47: 206.0, 48: 240.0, 49: 264.5, 50: 274.0, 51: 298.5, 52: 308.0, 53: 342.5, 54: 366.5, 55: 376.5, 56: 401.0, 57: 410.5, 58: 435.0, 59: 444.5, 60: 479.0, 61: 503.5, 62: 513.0, 63: 537.5, 64: 547.0, 65: 581.5, 66: 605.5, 67: 615.5, 68: 640.0, 69: 649.5, 70: 674.0, 71: 683.5, 72: 718.0, 73: 742.5, 74: 752.0, 75: 776.5, 76: 786.0, 77: 820.0, 78: 844.5, 79: 854.5, 80: 878.5, 81: 888.0, 82: 912.5, 83: 922.5, 84 : 957,85: 980.5, 86:990.5, 87: 1015.5,88:1025
}





class NoteDisplay:
    """
    A main class for UI display
    """

    def __init__(self, button_callback, button_replay_callback) -> None:
        self.window = Tk()
        self.window.title("Jazz Piano Trainer")
        self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.window.resizable(False,False)

        self.frame = Frame(self.window)
        self.frame.pack(side=RIGHT)

        self.canvas = Canvas(
            self.frame, bg="white", width=WINDOW_WIDTH, height=WINDOW_HEIGHT
        )
        self.canvas.pack()

        self.keys_img = ImageTk.PhotoImage(Image.open("images/keys.png"))
        self.canvas.create_image(0, 400, image=self.keys_img, anchor="w")

        self.images = {}
        for i in IMAGE_NAMES:
            image = ImageTk.PhotoImage(Image.open(f"images/{i}.png"))
            self.images[i] = image

        self.notes_widgets = {}
        self.button = Button(
            self.canvas, text="NEXT", command=button_callback, height=2, width=20
        )
        self.button_replay = Button(
            self.canvas, text="REPLAY", command=button_replay_callback, height=2, width=20
        )

        self.q_label = Label(self.canvas, text="Choose a Mode and press Next", font=("Arial", 25))
        self.theory_type_name = Label(self.canvas, text="abc", font=("Arial", 25))

        self.a_img = ImageTk.PhotoImage(Image.open("images/placeholder.png"))
        self.a_label = Label(self.canvas, text="")

        self.option_var = StringVar(self.canvas)
        self.option_var.set("MODES")
        self.selected_option = "MODES"
        self.option_widget = OptionMenu(
            self.canvas, self.option_var, "MODES", "CHORDS", "SCALES" , command=self.option_update
        )

        self.canvas.create_window(150, 58, window=self.option_widget)
        self.canvas.create_window(150, 100, window=self.button)
        self.canvas.create_window(150, 150, window=self.button_replay)
        self.canvas.create_window(500, 100, window=self.q_label)
        self.canvas.create_window(500, 200, window=self.theory_type_name)
        self.canvas.create_window(800, 100, window=self.a_label)

    def option_update(self, selected_option) -> None:
        """
        Update a selected option
        """
        self.selected_option = selected_option

    def get_note_image(self, note_id: int) -> str:
        """
        Get a note`s image
        """
        real_note = None
        for n in [84,72, 60, 48, 36]:
            if note_id >= n:
                real_note = note_id - n
                break
        return NOTES_TO_IMAGE_MAP[real_note] if real_note is not None else None

    def add_note(self, note_id: int, is_green: bool = True) -> None:
        """
        Add a note widget to the UI
        """
        note_name = self.get_note_image(note_id)
        note_image_name = f"key_green_{note_name}" if is_green else f"key_red_{note_name}"
        new_img = self.canvas.create_image(
            NOTES_X[note_id], NOTES_Y, image=self.images[note_image_name], anchor="w"
        )
        self.notes_widgets[note_id] = new_img

    def remove_note(self, note_id: int) -> None:
        """
        Remove a note widget from the UI
        """
        if note_id in self.notes_widgets:
            self.canvas.delete(self.notes_widgets[note_id])
            del self.notes_widgets[note_id]

    def update_question(self, txt: str) -> None:
        """
        Update a question text (UI)
        """
        self.q_label.config(text=txt)
        self.q_label.text = txt

    def update_answer(self, image_path: str, txt: str) -> None:
        """
        Update an answer image (UI)
        """
        new_img = ImageTk.PhotoImage(Image.open(image_path))
        self.a_label.config(image=new_img)
        self.a_label.image = new_img
        self.theory_type_name.config(text=txt)
        self.theory_type_name.text = txt
