import pandas as pd
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox

class DataProcessor(QThread):
    """Runs dataset processing in a separate thread to avoid UI freezing."""
    
    processing_complete = pyqtSignal(list)  # Signal emitted when processing is done

    def __init__(self, file_paths, multiple, temp_unit, time_column, temp_column):
        super().__init__()
        self.file_paths = file_paths
        self.multiple = multiple
        self.dataset_memory = {}
        self.temp_unit = temp_unit
        self.time_column = time_column
        self.temp_column = temp_column

    def run(self):
        """Processes CSV datasets and emits signal with the processed data."""
        datasets = []
        
        for file_path in self.file_paths:
            try:
                df = pd.read_csv(file_path)

                # Validate selected columns
                if self.time_column not in df.columns or self.temp_column not in df.columns:
                    self.show_error(f"Invalid file format in {file_path}.\nSelected columns are missing.")
                    continue

                # Rename columns for consistency
                df = df.rename(columns={self.time_column: "Time (s)", self.temp_column: "Temperature (°C)"})

                # Convert temperature if needed
                df = self.convert_temperature(df, self.temp_unit)

                datasets.append((df, file_path))
                self.dataset_memory[file_path] = df  # Store original data in memory

            except Exception as e:
                self.show_error(f"Error loading file {file_path}:\n{str(e)}")

        self.processing_complete.emit(datasets)

    def convert_temperature(self, df, target_unit):
        """Converts temperature between Celsius and Fahrenheit dynamically."""
        if target_unit == "Fahrenheit":
            df["Temperature"] = df["Temperature (°C)"] * 9/5 + 32  # Convert to °F
        else:
            df["Temperature"] = (df["Temperature (°C)"] - 32) * 5/9  # Convert back to °C
        
        return df

    def show_error(self, message):
        """Displays an error message dialog."""
        QMessageBox.critical(None, "Dataset Error", message)
