import sys
from PyQt6.QtWidgets import QApplication
from spectrum_app import SpectrumApp

# class SpectrumApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Spectrum Analyzer")
#         self.setGeometry(100, 100, 1200, 600)
#
#         # Main layout
#         main_layout = QHBoxLayout()
#
#         # Left panel with buttons and table
#         left_panel = QVBoxLayout()
#         self.load_button = QPushButton("Загрузить спектр")
#         self.analyze_button = QPushButton("Анализ спектра")
#         self.back_to_list_button = QPushButton("К списку спектров")
#         self.analyze_button.setEnabled(False)  # Пока отключаем кнопку "Анализ спектра"
#
#         left_panel.addWidget(self.load_button)
#         left_panel.addWidget(self.analyze_button)
#         left_panel.addWidget(self.back_to_list_button)
#
#         # Table for displaying data
#         self.table = QTableWidget()
#         self.table.setColumnCount(2)
#         self.table.setHorizontalHeaderLabels(["Волновое число (см⁻¹)", "Пропускание (%)"])
#         left_panel.addWidget(self.table)
#
#         # Right panel with matplotlib canvas and navigation toolbar
#         canvas_layout = QVBoxLayout()
#         self.canvas = SpectrumCanvas()
#         self.toolbar = NavigationToolbar(self.canvas, self)
#         canvas_layout.addWidget(self.toolbar)
#         canvas_layout.addWidget(self.canvas)
#
#         main_layout.addLayout(left_panel, stretch=1)
#         main_layout.addLayout(canvas_layout, stretch=2)
#
#         # Set central widget
#         central_widget = QWidget()
#         central_widget.setLayout(main_layout)
#         self.setCentralWidget(central_widget)
#
#         # Connect button signals
#         self.load_button.clicked.connect(self.load_spectrum)
#
#     def load_spectrum(self):
#         """Load a spectrum from a .txt file and display it."""
#         file_path, _ = QFileDialog.getOpenFileName(self, "Загрузить спектр", "", "Text Files (*.txt)")
#
#         if file_path:
#             try:
#                 # Load data from file
#                 data = np.loadtxt(file_path)
#
#                 # Validate data shape
#                 if data.shape[1] != 2:
#                     raise ValueError("Файл должен содержать две колонки: волновое число и пропускание.")
#
#                 wave_numbers, transmittance = data[:, 0], data[:, 1]
#
#                 # Update the table
#                 self.table.setRowCount(len(wave_numbers))
#                 for i in range(len(wave_numbers)):
#                     self.table.setItem(i, 0, QTableWidgetItem(str(wave_numbers[i])))
#                     self.table.setItem(i, 1, QTableWidgetItem(str(transmittance[i])))
#
#                 # Plot the spectrum
#                 self.canvas.plot_spectrum(wave_numbers, transmittance, self.table)
#
#             except Exception as e:
#                 error_label = QLabel(f"Ошибка: {str(e)}")
#                 error_label.setStyleSheet("color: red;")
#                 self.table.setCellWidget(0, 0, error_label)
#
#
# class SpectrumCanvas(FigureCanvas):
#     def __init__(self, parent=None):
#         self.fig = Figure()
#         self.ax = self.fig.add_subplot(111)
#         super().__init__(self.fig)
#
#         # Enable interaction with the plot
#         self.fig.canvas.mpl_connect("button_press_event", self.on_click)
#         self.table = None
#
#     def plot_spectrum(self, wave_numbers, transmittance, table):
#         """Plot the spectrum on the canvas."""
#         self.ax.clear()
#         self.ax.plot(wave_numbers, transmittance, label="Спектр")
#         self.ax.set_xlabel("Волновое число (см⁻¹)")
#         self.ax.set_ylabel("Пропускание (%)")
#         self.ax.legend()
#         self.ax.grid(True)
#         self.table = table
#         self.wave_numbers = wave_numbers
#         self.transmittance = transmittance
#         self.draw()
#
#     def on_click(self, event):
#         """Handle mouse click on the plot."""
#         if event.inaxes == self.ax:
#             x_click = event.xdata
#             y_click = event.ydata
#
#             # Find the closest point
#             distances = np.sqrt((self.wave_numbers - x_click) ** 2 + (self.transmittance - y_click) ** 2)
#             closest_index = np.argmin(distances)
#
#             # Highlight the point in the table
#             if self.table:
#                 self.table.selectRow(closest_index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpectrumApp()
    window.show()
    sys.exit(app.exec())
