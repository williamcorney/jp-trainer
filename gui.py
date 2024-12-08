from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QMainWindow, QGraphicsRectItem, QVBoxLayout, QWidget, \
    QGraphicsPixmapItem, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QBrush, QPixmap
from theory import Theory
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        central_widget = QWidget()
        self.layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        self.scene = QGraphicsScene()
        self.pixmap2 = None
        self.button1 = QPushButton("SET")
        self.button1.clicked.connect(self.get_theory)
        self.theory = Theory()

        self.layout.addWidget(self.button1)
    def add_note(self,message):
        print (f"Adding image: {message.note}")
    def remove_note(self,message):
        print (f"Removing image: {message.note}")
    def get_theory (self,message):
        self.requirednotes = self.theory.set_notes()