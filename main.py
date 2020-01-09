"""
main.py
Python Version: 3.8.1

Created by Mauro S. Mendoza Elguera at 08-01-20
Pontifical Catholic University of Chile

"""

import sys

from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from datetime import datetime
from functions import vacantes

form, base = uic.loadUiType(uifile='UI files/mainwindow.ui')


class MainWindow(form, base):
    def __init__(self, _ramos, _url):
        super(base, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(
            ""
            "background-color: rgb(50, 50, 50);"
            ""
        )
        self.statusBar.setStyleSheet(
            ""
            "background-color: rgb(40, 40, 40);"
            "color: white"
            ""
        )
        self.pushButton.setStyleSheet(
            ""
            "background-color: rgb(90, 90, 90);"
            "color: white"
            ""
        )

        self.ramos = _ramos
        self.url = _url

        # Conectando botones
        self.pushButton.clicked.connect(self.reload)

        # Linkeando los gráficos
        self.gvs = [
            self.graphicsView_1, self.graphicsView_2,
            self.graphicsView_3, self.graphicsView_4,
            self.graphicsView_5, self.graphicsView_6,
            self.graphicsView_7
        ]
        self.chvs = [
            QChartView(self.graphicsView_1), QChartView(self.graphicsView_2),
            QChartView(self.graphicsView_3), QChartView(self.graphicsView_4),
            QChartView(self.graphicsView_5), QChartView(self.graphicsView_6),
            QChartView(self.graphicsView_7)
        ]

        self.reload()

    def reload(self):
        """

        :return:
        """

        for i in range(7):
            sigla, sec = self.ramos[i]
            ocupadas, libres = vacantes(sigla, sec, self.url).values()

            chv = QChartView(self.gvs[i])

            chv.setMinimumSize(465, 262)
            chv.setRenderHint(QPainter.Antialiasing)
            chv.chart().setTheme(QChart.ChartThemeLight)
            chv.chart().layout().setContentsMargins(0, 0, 0, 0)
            chv.chart().setBackgroundRoundness(0)

            scene = chv.scene()
            text = scene.addText(f"{sigla}-{sec}", QFont('Helvetica', 20, 75))
            text.setDefaultTextColor(Qt.white)
            text.setPos(111, 119)

            slice_l = QPieSlice(f'V. Libres:   {libres}', libres)
            slice_l.setColor(QColor('#595959'))
            # slice_l.setColor(QColor('white'))
            slice_l.setBorderWidth(4)
            slice_l.setBorderColor(QColor('black'))
            slice_o = QPieSlice(f'V. Ocupadas: {ocupadas}', ocupadas)
            slice_o.setColor(QColor('#990000'))
            slice_o.setBorderWidth(4)
            slice_o.setBorderColor(QColor('black'))

            donut = QPieSeries()
            donut.append([slice_l, slice_o])
            donut.setHoleSize(0.65)
            donut.setPieSize(0.9)

            chv.chart().addSeries(donut)
            chart = chv.chart()
            chart.setBackgroundBrush(QBrush(QColor('black')))
            legend = chart.legend()
            legend.setLabelColor(QColor('white'))
            legend.setAlignment(Qt.AlignRight)

            self.chvs[i] = chv

        # Actualiza el msj en la statusbar
        self.statusBar.showMessage(
            f"Done! {datetime.now().strftime('%d/%m/%Y - %H:%M:%S')}"
        )
        self.show()

        for i in range(7):
            self.gvs[i] = QGraphicsView()


if __name__ == '__main__':
    ramos = {0: ('DPT6900', 1), 1: ('IIC2613', 1), 2: ('IIC2764', 1),
             3: ('ICS3153', 1), 4: ('ICS3151', 1), 5: ('ICS2613', 2),
             6: ('IIC2733', 1)}
    url = 'http://buscacursos.uc.cl/?cxml_semestre=2020-1&' \
          'cxml_sigla={}#resultados'

    app = QApplication(sys.argv)
    mw = MainWindow(ramos, url)

    sys.exit(app.exec_())
