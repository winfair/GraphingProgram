from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from ui.buttons import ButtonsPanel
from plotting.plotter import Plotter

class MainWindow(QMainWindow):
    """Main PyQt window for the Cooling Data Analyzer."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cooling Data Analyzer")
        self.setGeometry(100, 100, 800, 600)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Plotter widget
        self.plotter = Plotter()
        layout.addWidget(self.plotter)
        
        # Buttons panel
        self.buttons = ButtonsPanel(self.plotter)
        layout.addWidget(self.buttons)

def main():
    """Entry point of the program."""
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
