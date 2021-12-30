import sys
import random
import traceback
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Git и желтые окружности')
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()

    # Метод срабатывает, когда виджету надо
    # перерисовать свое содержимое,
    # например, при создании формы
    def paintEvent(self, event):
        if self.do_paint:
            # Создаем объект QPainter для рисования
            self.qp = QPainter()
            # Начинаем процесс рисования
            self.qp.begin(self)
            self.draw_ellipse()
            # Завершаем рисование
            self.qp.end()

    def draw_ellipse(self):
        d = random.randint(1, 500)
        # Задаем кисть
        self.qp.setBrush(QColor(255, 255, 0))
        # Рисуем прямоугольник заданной кистью
        self.qp.drawEllipse(0, 0, d, d)

    def excepthook(exc_type, exc_value, exc_tb):
        tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
        print("Oбнаружена ошибка !:", tb)

        #    QtWidgets.QApplication.quit()             # !!! если вы хотите, чтобы событие завершилось

    sys.excepthook = excepthook


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
