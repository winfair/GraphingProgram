from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QComboBox

class ColumnSelector(QDialog):
    """Dialog for selecting Time and Temperature columns from a dataset."""
    
    def __init__(self, columns):
        super().__init__()
        self.setWindowTitle("Select Data Columns")
        self.setGeometry(200, 200, 300, 150)

        # Layout
        layout = QVBoxLayout()

        # Time Column Selector
        self.time_label = QLabel("Select Time Column:")
        self.time_combo = QComboBox()
        self.time_combo.addItems(columns)

        # Temperature Column Selector
        self.temp_label = QLabel("Select Temperature Column:")
        self.temp_combo = QComboBox()
        self.temp_combo.addItems(columns)

        # Confirm Button
        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)

        # Add widgets to layout
        layout.addWidget(self.time_label)
        layout.addWidget(self.time_combo)
        layout.addWidget(self.temp_label)
        layout.addWidget(self.temp_combo)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def get_selected_columns(self):
        """Returns the user-selected columns."""
        return self.time_combo.currentText(), self.temp_combo.currentText()
