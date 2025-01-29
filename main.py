from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from ui.main_window import MainWindow


def main():
    """
    Entry point of the program. Initializes the PyQt Application and Main Window.
    """
    app = QApplication([])  # Create the application
    window = MainWindow()  # Create the main window
    window.show()  # Show the window
    app.exec_()  # Run the application event loop


if __name__ == "__main__":
    main()
