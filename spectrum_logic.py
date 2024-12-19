import numpy as np

def load_spectrum_data(file_path):
    """Load spectrum data from a file."""
    data = np.loadtxt(file_path)
    if data.shape[1] != 2:
        raise ValueError("Файл должен содержать две колонки: волновое число и пропускание.")
    return data[:, 0], data[:, 1]
