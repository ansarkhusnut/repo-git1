from PyQt5 import uic
import sys, random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.setWindowTitle("Git и желтые окружности")
        self.should_paint_circle = False
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.should_paint_circle:
            k = random.randint(5, 100)
            p = QtGui.QPainter(self)
            p.setRenderHint(QPainter.Antialiasing)
            p.setPen(QPen(Qt.yellow, k, Qt.SolidLine))
            p.drawEllipse(640 // 2, 480 // 2, k, k)

    def run(self):
        self.should_paint_circle = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
