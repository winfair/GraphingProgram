import pandas as pd
from PyQt5.QtCore import QThread, pyqtSignal

class DataProcessor(QThread):
    """ Runs dataset processing in a separate thread to avoid UI freezing. """
    processing_complete = pyqtSignal(list)  # Signal emitted when processing is done

    def __init__(self, file_paths, multiple):
        super().__init__()
        self.file_paths = file_paths
        self.multiple = multiple
        self.dataset_memory = {}

    def run(self):
        """ Processes CSV datasets and emits signal with the processed data. """
        datasets = []
        for file_path in self.file_paths:
            try:
                df = pd.read_csv(file_path)
                if 'Time (s)' in df.columns and 'Temperature (°C)' in df.columns:
                    datasets.append((df, file_path))
                    self.dataset_memory[file_path] = df
                else:
                    print(f"Invalid file format in {file_path}. Ensure columns: Time (s), Temperature (°C)")
            except Exception as e:
                print(f"Error loading file {file_path}: {e}")

        self.processing_complete.emit(datasets)  # Emit results back to UI thread
