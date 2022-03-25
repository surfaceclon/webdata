from turtle import color
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import requests
from requests.exceptions import HTTPError

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('WEBDATA v.1')
        self.setGeometry(300, 300, 850, 450)
        self.setStyleSheet(
            'background-color: #000000;\n'
        )

        self.line = QtWidgets.QLineEdit(self)
        self.line.setGeometry(10,10,200,30)
        self.line.setStyleSheet(
            'background-color: #F0F8FF;\n'
            'border-radius: 10px;\n'
            "font-size: 15px;\n"
            "font-weight: bold;"
        )
        self.line.setText('https://')
        

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText('GET')
        self.btn.setStyleSheet(
            'background-color: #A9A9A9;\n'
            'border-radius: 10px;\n'
            "font-size: 12px;\n"
            "font-weight: bold;"
        )
        self.btn.move(215,10)
        self.btn.clicked.connect(self.status)

        self.lab = QtWidgets.QLabel(self)
        self.lab.setGeometry(10, 50, 100, 30)
        self.lab.setStyleSheet(
            'background-color: #D2691E;\n'
            'border-radius: 10px;\n'
            "font-size: 12px;\n"
            "font-weight: bold;"
        )
        self.lab.setText('  Status: ')

        self.indicator = QtWidgets.QLabel(self)
        self.indicator.setGeometry(130, 50, 685, 30)
        self.indicator.setStyleSheet(
            'background-color: #0000CD;\n'
            'border-radius: 10px;\n'
            "font-size: 12px;\n"
            "font-weight: bold;"
        )
        self.indicator.setText('\tINDICATOR SITUATION')

        self.lab_head = QtWidgets.QLabel(self)
        self.lab_head.setStyleSheet(
            'color: #000000;\n'
            'background-color: #F0FFFF;\n'
            'border-radius: 10px;\n'
            'font-weight: bold;\n'
        )
        self.lab_head.setGeometry(10,90,250,300)
        
        self.line_getval = QtWidgets.QLineEdit(self)
        self.line_getval.setGeometry(270,90,200,30)
        self.line_getval.setStyleSheet(
            'background-color: #F0F8FF;\n'
            'border-radius: 5px;\n'
            "font-size: 15px;\n"
            "font-weight: bold;"
        )

        self.but_show = QtWidgets.QPushButton(self)
        self.but_show.setText('Show')
        self.but_show.setStyleSheet(
            'background-color: #A9A9A9;\n'
            'border-radius: 10px;\n'
            "font-size: 12px;\n"
            "font-weight: bold;"
        )
        self.but_show.move(475, 90)
        self.but_show.clicked.connect(self.showheaders)

        self.tex_show = QtWidgets.QTextEdit(self)
        self.tex_show.setStyleSheet(
            'color: #000000;\n'
            'background-color: #F0FFFF;\n'
            'border-radius: 10px;\n'
            'font-weight: bold;\n'
        )
        self.tex_show.setGeometry(270,140,550,250)

        self.btn_clear = QtWidgets.QPushButton(self)
        self.btn_clear.setText('Clear')
        self.btn_clear.setStyleSheet(
            'background-color: #A9A9A9;\n'
            'border-radius: 10px;\n'
            "font-size: 12px;\n"
            "font-weight: bold;"
        )
        self.btn_clear.move(580, 90)
        self.btn_clear.clicked.connect(self.clearfields)
    
    def clearfields(self):
        self.line.clear()
        self.lab_head.clear()
        self.tex_show.clear()
        self.line_getval.clear()

    def showheaders(self):
        self.cont_show = self.line_getval.text()
        lensi = len(self.cont_show)
        if lensi == 0:
            print('Error')
        else:
            responses = requests.get(self.line.text())
            self.tex_show.clear()
            self.tex_show.setText(responses.headers[self.cont_show])

    def status(self):
        self.error = 'Error'
        self.cont = self.line.text()
        try:
            responses = requests.get(self.cont)
            self.lab.clear()
            self.lab.setText('  Status: ' + str(responses.status_code))
        except requests.ConnectionError:
            self.lab.clear()
            self.lab.setText('  Status: ' + self.error)
        try:
            self.lab_head.clear()
            for values in responses.headers:
                self.lab_head.setText(self.lab_head.text() + '\n' + '\t' + values)
        except:
            self.lab_head.setText(self.error)
        if responses.status_code == 200:
            self.indicator.setStyleSheet(
            'background-color: #00FA9A;\n'
            'border-radius: 10px;\n'
            "font-size: 12px;\n"
            "font-weight: bold;"
        )
        elif responses.status_code == 404:
            self.indicator.setStyleSheet(
            'background-color: #FFFF00;\n'
            'border-radius: 10px;\n'
            "font-size: 12px;\n"
            "font-weight: bold;"
        )
        else:
            self.indicator.setStyleSheet(
            'background-color: #FF0000;\n'
            'border-radius: 10px;\n'
            "font-size: 12px;\n"
            "font-weight: bold;"
        )


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    application()
