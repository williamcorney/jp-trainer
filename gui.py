# gui.py

from PyQt6.QtCore import pyqtSignal,Qt
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QMainWindow, QGraphicsPixmapItem, QVBoxLayout, QWidget, \
    QPushButton
from PyQt6.QtGui import QPixmap
from theory import Theory


class MainWindow(QMainWindow):
    # Define signals for note_on and note_off, passing note as an integer
    note_on_signal = pyqtSignal(int)
    note_off_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        # Initialization steps (scene, requirednotes, pixmap2, etc.)
        self.scene = QGraphicsScene()
        self.requirednotes = []
        self.pixmap2 = {}
        self.BackgroundPixmap = QPixmap("./images/keys.png")
        self.BackgroundItem = QGraphicsPixmapItem(self.BackgroundPixmap)
        self.scene.addItem(self.BackgroundItem)
        self.view = QGraphicsView(self.scene)
        self.view.setFixedSize(self.BackgroundPixmap.size())
        self.view.setSceneRect(0, 0, self.BackgroundPixmap.width(), self.BackgroundPixmap.height())
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)



        button = QPushButton("Theory")
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connect theory button and signals to slots
        button.clicked.connect(self.get_theory)
        self.note_on_signal.connect(self.add_image)  # Connect note_on_signal to add_image
        self.note_off_signal.connect(self.remove_image)  # Connect note_off_signal to remove_image

        self.theory = Theory()

    def get_theory(self):

        self.requirednotes = self.theory.set_notes()


    def add_image(self, note):


        self.xcord = self.theory.Theory["NoteCoordinates"][note % 12] + ((note // 12) - 4) * 239

        if note in self.pixmap2:
            return
        color = "green"
        # Create new QGraphicsPixmapItem and add it to the scene
        note_filename = "./images/key_" + color + self.theory.Theory["NoteFilenames"][note % 12]
        print (note_filename)
        pixmap_item = QGraphicsPixmapItem(QPixmap(note_filename))

        self.pixmap2[note] = pixmap_item
        self.scene.addItem(self.pixmap2[note])
        self.pixmap2[note].setPos(self.xcord, 0)


    def remove_image(self, note):

        if note in self.pixmap2:
            self.scene.removeItem(self.pixmap2[note])
            del self.pixmap2[note]

