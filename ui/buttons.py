from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtCore import Qt
from data.loader import load_dataset
from data.processor import DataProcessor
from plotting.plotter import Plotter
import pandas as pd

class ButtonsPanel(QWidget):
    """PyQt Widget containing buttons for data import, processing, and visualization."""
    
    def __init__(self, plotter):
        super().__init__()
        self.plotter = plotter
        self.temp_unit = "Celsius"
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Buttons
        self.btn_single = QPushButton("Import Single Dataset")
        self.btn_single.clicked.connect(self.handle_single_dataset)
        layout.addWidget(self.btn_single)

        self.btn_multiple = QPushButton("Import Multiple Datasets")
        self.btn_multiple.clicked.connect(self.handle_multiple_datasets)
        layout.addWidget(self.btn_multiple)

        self.btn_toggle_temp = QPushButton("Toggle Temperature Unit")
        self.btn_toggle_temp.clicked.connect(self.toggle_temperature_unit)
        layout.addWidget(self.btn_toggle_temp)

        # Label for displaying temperature unit
        self.temp_label = QLabel(f"Temperature Unit: {self.temp_unit}")
        self.temp_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.temp_label)

        self.setLayout(layout)

    def handle_single_dataset(self):
        """Loads and processes a single dataset."""
        file_paths = load_dataset(multiple=False)
        if file_paths:
            self.process_data(file_paths, multiple=False)

    def handle_multiple_datasets(self):
        """Loads and processes multiple datasets."""
        file_paths = load_dataset(multiple=True)
        if file_paths:
            self.process_data(file_paths, multiple=True)

    def process_data(self, file_paths, multiple):
        """Runs dataset processing in a separate thread."""
        self.processor = DataProcessor(file_paths, multiple, self.temp_unit, "Time (s)", "Temperature (°C)")
        self.processor.processing_complete.connect(self.plot_data)
        self.processor.start()

    def plot_data(self, datasets):
        """Displays processed datasets using the Plotter widget."""
        if not datasets:
            QMessageBox.warning(self, "No Data", "No valid datasets were loaded.")
            return

        if len(datasets) == 1:
            self.plotter.plot_dataset(datasets[0][0], datasets[0][1])
        else:
            self.plotter.plot_multiple_datasets(datasets)

    def toggle_temperature_unit(self):
        """Toggles temperature unit and updates the label + dataset."""
        self.temp_unit = "Fahrenheit" if self.temp_unit == "Celsius" else "Celsius"
        self.temp_label.setText(f"Temperature Unit: {self.temp_unit}")
        print(f"Temperature unit changed to {self.temp_unit}")

        # Reconvert existing data and replot
        if hasattr(self, "processor") and self.processor.dataset_memory:
            datasets = [(self.processor.convert_temperature(df.copy(), self.temp_unit), label) 
                        for label, df in self.processor.dataset_memory.items()]
            self.plot_data(datasets)
