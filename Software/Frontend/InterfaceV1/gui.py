import time
from typing import Union

from PyQt5 import QtWidgets, QtCore, uic
from pyqtgraph.widgets import PlotWidget
from pyqtgraph import ViewBox, AxisItem, mkPen, BarGraphItem
from calculate import Calculator


class Interface(QtWidgets.QMainWindow):
    def __init__(self):
        super(Interface, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui.ui', self)  # Load the .ui file
        self.setFixedSize(self.size())  # Disables window resizing
        self.setWindowTitle("Real-Time Portable Polarimeter")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # Used to hide window frame
        self.move(0, 0)  # Move frame to top left of screen

        self.polarisation_ellipse_widget.disableAutoRange(ViewBox.XYAxes)
        self.polarisation_ellipse_widget.setRange(yRange=(-1, 1), xRange=(-1, 1))
        # self.set_widget_titles(
        #     self.polarisation_ellipse_widget,
        #     left_text="Ey",
        #     left_units=None,
        #     bottom_text="Ex",
        #     bottom_units=None
        # )
        self.polarisation_ellipse_plot = self.polarisation_ellipse_widget.plot(**{'pen': 'r'})
        self.polarisation_ellipse_widget.getPlotItem().layout.setContentsMargins(0, 0, 0, 15)
        self.polarisation_ellipse_widget.showGrid(x=True, y=True, alpha=0.4)
        self.polarisation_ellipse_widget.setBackground('w')
        black_pen = mkPen(color='black', width=4)
        self.polarisation_ellipse_widget.getAxis('bottom').setTextPen(black_pen)
        self.polarisation_ellipse_widget.getAxis('left').setTextPen(black_pen)
        self.polarisation_ellipse_widget.setMouseEnabled(x=False, y=False)

        calc = Calculator()
        x = calc.get_polarisation_ellipse_x_data()
        y = calc.get_polarisation_ellipse_y_data()
        self.polarisation_ellipse_plot.setData(x, y)  # Used to update plot in realtime

        self.stokes_parameters_plot = self.stokes_parameters_widget.plot()
        self.stokes_parameters_widget.setMouseEnabled(x=False, y=False)
        self.stokes_parameters_widget.setRange(yRange=(-1, 1))
        self.stokes_parameters_widget.showGrid(x=True, y=True, alpha=0.4)
        self.stokes_parameters_widget.setBackground('w')
        self.stokes_parameters_widget.getAxis('bottom').setTextPen(black_pen)
        self.stokes_parameters_widget.getAxis('left').setTextPen(black_pen)
        self.stokes_parameters_widget.setMouseEnabled(x=False, y=False)
        self.stokes_parameters_widget.getAxis('bottom').setTicks([[(1, "S0"), (2, "S1"), (3, "S2"), (4, "S3")]])

        stokes_x = [1, 2, 3, 4]
        stokes_y = [0, 0, 0, 0]
        bar_graph = BarGraphItem(x=stokes_x, height=stokes_y, width=0.8, brush='r')
        self.stokes_parameters_widget.addItem(bar_graph)

        stokes_y = calc.get_stokes_params()
        bar_graph.setOpts(height=stokes_y)  # Used to update bar graph in realtime


    @staticmethod
    def set_widget_titles(
            widget: PlotWidget,
            left_text: str = "",
            left_units: Union[str, None] = None,
            bottom_text: str = "",
            bottom_units: Union[str, None] = None
    ) -> None:
        """
        Method to set the titles, axis, and format of pyqtgraph plots (i.e. frequency/spectrum plot)
        :param widget: pyqtgraph PlotWidget to modify
        :param left_text: String on left vertical axis
        :param left_units: String for left vertical axis units
        :param bottom_text: String for bottom horizontal axis
        :param bottom_units: String for bottom horizontal units
        :return: None
        """
        label_style = {'color': '#999', 'font-size': '10pt'}
        left_axis = AxisItem('left')
        left_axis.setLabel(text=left_text, units=left_units, **label_style)
        bottom_axis = AxisItem('bottom')
        bottom_axis.setLabel(text=bottom_text, units=bottom_units, **label_style)
        bottom_axis.enableAutoSIPrefix(False)
        widget.setAxisItems(axisItems={'left': left_axis, 'bottom': bottom_axis})
