import sys
from PyQt6.QtWidgets import QApplication
from spectrum_app import SpectrumApp



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpectrumApp()
    window.show()
    sys.exit(app.exec())
