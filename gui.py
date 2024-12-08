from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QMainWindow, QGraphicsRectItem, QVBoxLayout, QWidget, \
    QGraphicsPixmapItem, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QBrush, QPixmap
from theory import Theory
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Step 1: Create a QGraphicsScene
        self.scene = QGraphicsScene()
        self.requirednotes =[60 ]
        # Add some items to the scene
        pixmap = QGraphicsPixmapItem(QPixmap("./images/keys.png"))
        self.scene.addItem(pixmap)
        # Step 2: Create a QGraphicsView to display the scene
        self.view = QGraphicsView(self.scene)
        button = QPushButton("")
        # Step 3: Set up a layout
        layout = QVBoxLayout()  # You can use other layouts like QHBoxLayout
        layout.addWidget(self.view)
        layout.addWidget(button)
        # Step 4: Create a QWidget for the central area
        central_widget = QWidget()
        central_widget.setLayout(layout)  # Set the layout for the QWidget
        # Step 5: Set the QWidget (with the layout) as the central widget
        self.setCentralWidget(central_widget)
        # Configure the window
        self.setWindowTitle("PyQt6 Scene Example")
        self.resize(1200, 400)
        button.clicked.connect (self.get_theory)
        self.theory = Theory()

    def add_image(self):

        self.pixmap2 = QGraphicsPixmapItem(QPixmap("./images/key_red_mid1.png"))
        self.scene.addItem(self.pixmap2)
    def remove_image(self):

        if not self.pixmap2:
            return

        if self.pixmap2 is not None:
            self.scene.removeItem(self.pixmap2)
            self.pixmap2 = None  # Clear the reference after removal
    def get_theory (self):
        self.requirednotes = self.theory.set_notes()