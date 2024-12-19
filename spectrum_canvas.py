import numpy as np
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)
from matplotlib.figure import Figure


class SpectrumCanvas(FigureCanvas):
    def __init__(self, parent=None):
        # Создаем фигуру и оси
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)

        # Создаем панель инструментов
        self.toolbar = NavigationToolbar(self, parent)

        # Включаем обработку кликов
        self.fig.canvas.mpl_connect("button_press_event", self.on_click)

        # Данные графика
        self.wave_numbers = None
        self.transmittance = None
        self.table = None

    def plot_spectrum(self, wave_numbers, transmittance, table):
        """Построение спектра на графике."""
        self.ax.clear()
        self.ax.plot(wave_numbers, transmittance, label="Спектр")
        self.ax.set_xlabel("Волновое число (см⁻¹)")
        self.ax.set_ylabel("Пропускание (%)")
        self.ax.legend()
        self.ax.grid(True)

        # Сохраняем данные для взаимодействия
        self.wave_numbers = wave_numbers
        self.transmittance = transmittance
        self.table = table

        self.draw()

    def on_click(self, event):
        """Обработка клика мыши на графике."""
        if event.inaxes == self.ax and self.wave_numbers is not None:
            x_click = event.xdata
            y_click = event.ydata

            # Найти ближайшую точку
            distances = np.sqrt((self.wave_numbers - x_click) ** 2 + (self.transmittance - y_click) ** 2)
            closest_index = np.argmin(distances)

            # Выделить строку в таблице
            if self.table:
                self.table.selectRow(closest_index)
