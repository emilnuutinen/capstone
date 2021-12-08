import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtWidgets import QGraphicsView
from PyQt6.QtWidgets import QTimeEdit


class Window(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('BP Measurement Dashboard')
        self.resize(1600, 1000)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._createControls()
        self._createGraphs()

    def _createControls(self):
        controlsLayout = QHBoxLayout()

        controlsLayout.addWidget(QPushButton('Start'))
        controlsLayout.addWidget(QTimeEdit())
        controlsLayout.addStretch()

        self.generalLayout.addLayout(controlsLayout)

    def _createGraphs(self):
        graphsLayout = QGridLayout()

        graphsLayout.addWidget(QGraphicsView(), 0, 0, 1, 2)
        graphsLayout.addWidget(QGraphicsView(), 1, 0)
        graphsLayout.addWidget(QGraphicsView(), 2, 0)
        graphsLayout.addWidget(QGraphicsView(), 3, 0)
        graphsLayout.addWidget(QGraphicsView(), 1, 1)
        graphsLayout.addWidget(QGraphicsView(), 2, 1)
        graphsLayout.addWidget(QGraphicsView(), 3, 1)

        self.generalLayout.addLayout(graphsLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
