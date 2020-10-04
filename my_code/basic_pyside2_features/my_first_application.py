import sys

from PySide2.QtCore import QSize
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(400, 300))

        button = QPushButton("Press Me!")
        self.setCentralWidget(button)


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # windows are hidden by default

    app.exec_()  # event loop


if __name__ == '__main__':
    main()
