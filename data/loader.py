from PyQt5.QtWidgets import QFileDialog, QMessageBox

def load_dataset(multiple=False):
    """
    Opens a file dialog to allow the user to select one or multiple datasets.
    Returns a list of selected file paths.
    """
    options = QFileDialog.Options()
    file_filter = "CSV Files (*.csv);;Text Files (*.txt)"
    
    if multiple:
        file_paths, _ = QFileDialog.getOpenFileNames(None, "Select Datasets", "", file_filter, options=options)
    else:
        file_path, _ = QFileDialog.getOpenFileName(None, "Select Dataset", "", file_filter, options=options)
        file_paths = [file_path] if file_path else []
    
    if not file_paths:
        QMessageBox.warning(None, "No File Selected", "Please select a valid dataset file.")
    
    return file_paths
