from PyQt6.QtWidgets import (
    QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QWidget, QTableWidget, QTableWidgetItem, QLabel
)
from spectrum_canvas import SpectrumCanvas
from spectrum_logic import load_spectrum_data

class SpectrumApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spectrum Analyzer")
        self.setGeometry(100, 100, 1200, 600)

        # Main layout
        main_layout = QHBoxLayout()

        # Left panel with buttons and table
        left_panel = QVBoxLayout()
        self.load_button = QPushButton("Загрузить спектр")
        self.analyze_button = QPushButton("Анализ спектра")
        self.back_to_list_button = QPushButton("К списку спектров")
        self.analyze_button.setEnabled(False)

        left_panel.addWidget(self.load_button)
        left_panel.addWidget(self.analyze_button)
        left_panel.addWidget(self.back_to_list_button)

        # Table for displaying data
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Волновое число (см⁻¹)", "Пропускание (%)"])
        self.table.setColumnWidth(0, 150)  # Первая колонка: "Волновое число"
        self.table.setColumnWidth(1, 120)
        left_panel.addWidget(self.table)

        # Right panel with matplotlib canvas and navigation toolbar


        canvas_layout = QVBoxLayout()
        self.canvas = SpectrumCanvas(self)  # Создаем Canvas
        canvas_layout.addWidget(self.canvas.toolbar)  # Подключаем панель инструментов
        canvas_layout.addWidget(self.canvas)

        main_layout.addLayout(left_panel, stretch=1)
        main_layout.addLayout(canvas_layout, stretch=2)

        # Set central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Connect button signals
        self.load_button.clicked.connect(self.load_spectrum)

    def load_spectrum(self):
        """Handle the spectrum loading logic."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Загрузить спектр", "", "Text Files (*.txt)")
        if file_path:
            try:
                wave_numbers, transmittance = load_spectrum_data(file_path)
                self.update_table(wave_numbers, transmittance)
                self.canvas.plot_spectrum(wave_numbers, transmittance, self.table)
            except Exception as e:
                error_label = QLabel(f"Ошибка: {str(e)}")
                error_label.setStyleSheet("color: red;")
                self.table.setCellWidget(0, 0, error_label)

    def update_table(self, wave_numbers, transmittance):
        """Update the table with spectrum data."""
        self.table.setRowCount(len(wave_numbers))
        for i in range(len(wave_numbers)):
            self.table.setItem(i, 0, QTableWidgetItem(str(wave_numbers[i])))
            self.table.setItem(i, 1, QTableWidgetItem(str(transmittance[i])))
