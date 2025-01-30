from PyQt5.QtWidgets import QWidget, QVBoxLayout, QToolBar, QPushButton
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from plotting.mpl_canvas import MplCanvas

class Plotter(QWidget):
    """Widget for displaying plots with built-in zoom & pan functionality and grid toggle."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Layout
        layout = QVBoxLayout()
        
        # Create Matplotlib canvas
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        
        # Add navigation toolbar for zooming & panning
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        # Grid toggle button
        self.grid_button = QPushButton("Toggle Grid")
        self.grid_button.clicked.connect(self.toggle_grid)
        
        # Add widgets to layout
        layout.addWidget(self.toolbar)
        layout.addWidget(self.grid_button)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # Grid state
        self.grid_enabled = True  # Default: Grid ON

    def plot_dataset(self, dataset, label):
        """Plots a single dataset on the graph."""
        self.canvas.axes.clear()
        
        try:
            self.canvas.axes.plot(dataset['Time (s)'], dataset["Temperature"], label=label)
        except KeyError as e:
            print(f"Error: Missing column in dataset - {e}")
            return

        self.canvas.axes.set_xlabel("Time (s)")
        self.canvas.axes.set_ylabel("Temperature")
        self.canvas.axes.legend()
        self.canvas.axes.grid(self.grid_enabled)  # Apply grid setting
        self.canvas.draw()

    def plot_multiple_datasets(self, datasets):
        """Plots multiple datasets on the same graph."""
        self.canvas.axes.clear()

        for dataset, label in datasets:
            try:
                self.canvas.axes.plot(dataset['Time (s)'], dataset["Temperature"], label=label)
            except KeyError as e:
                print(f"Error: Missing column in dataset - {e}")
                continue

        self.canvas.axes.set_xlabel("Time (s)")
        self.canvas.axes.set_ylabel("Temperature")
        self.canvas.axes.legend()
        self.canvas.axes.grid(self.grid_enabled)  # Apply grid setting
        self.canvas.draw()

    def toggle_grid(self):
        """Toggles grid visibility on the graph."""
        self.grid_enabled = not self.grid_enabled
        self.canvas.axes.grid(self.grid_enabled)
        self.canvas.draw()
