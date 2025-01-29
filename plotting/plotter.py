from PyQt5.QtWidgets import QWidget, QVBoxLayout, QToolBar
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from plotting.mpl_canvas import MplCanvas

class Plotter(QWidget):
    """Widget for displaying plots with built-in zoom & pan functionality."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Layout
        layout = QVBoxLayout()
        
        # Create Matplotlib canvas
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        
        # Add navigation toolbar for zooming & panning
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        # Add widgets to layout
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot_dataset(self, dataset, label):
        """Plots a single dataset on the graph."""
        self.canvas.axes.clear()
        self.canvas.axes.plot(dataset['Time (s)'], dataset['Temperature (°C)'], label=label)
        self.canvas.axes.set_xlabel("Time (s)")
        self.canvas.axes.set_ylabel("Temperature (°C)")
        self.canvas.axes.legend()
        self.canvas.draw()

    def plot_multiple_datasets(self, datasets):
        """Plots multiple datasets on the same graph."""
        self.canvas.axes.clear()
        for dataset, label in datasets:
            self.canvas.axes.plot(dataset['Time (s)'], dataset['Temperature (°C)'], label=label)
        
        self.canvas.axes.set_xlabel("Time (s)")
        self.canvas.axes.set_ylabel("Temperature (°C)")
        self.canvas.axes.legend()
        self.canvas.draw()
