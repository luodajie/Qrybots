from PyQt4 import QtGui, QtCore
from functools import partial

from read_xml import XmlFileParser


class Window(QtGui.QMainWindow):
    def __init__(self, filename=None, parent=None):
        super(Window, self).__init__(parent)
        self.filename_list = filename
        self.setGeometry(300, 150, 800, 500)
        self.setWindowIcon(QtGui.QIcon("querybots.png"))
        self.setWindowTitle("QryBots")

        self.widget = QtGui.QWidget()

        self.label = QtGui.QLabel("Please click the button below to run the Query:", self)
        self.hbox = QtGui.QHBoxLayout()
        self.hbox.addWidget(self.label)

        self.blank = QtGui.QVBoxLayout()
        self.label1 = QtGui.QLabel("")
        self.label1.setFixedHeight(50)
        self.blank.addWidget(self.label1)
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.setSpacing(10)
        self.label.setFixedWidth(500)
        self.font = QtGui.QFont()
        self.font.setPointSize(14)
        self.font.setBold(True)
        self.font.setWeight(100)
        self.font.setFamily("Helvetica")
        self.palette = QtGui.QPalette()

        self.font1 = QtGui.QFont()
        self.font1.setPointSize(13)
        self.font1.setBold(True)
        self.font1.setWeight(50)
        self.font1.setFamily("Helvetica")
        self.palette1 = QtGui.QPalette()

        self.label.setPalette(self.palette)
        self.label.setFont(self.font)
        self.label.setPalette(self.palette)
        self.label.setFont(self.font)
        self.grid = QtGui.QGridLayout()
        self.grid.setHorizontalSpacing(100)
        self.grid.setVerticalSpacing(20)
        self.dynamically_generated_buttons()
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.blank)
        self.vbox.addLayout(self.grid)
        self.vbox.setAlignment(QtCore.Qt.AlignTop)
        self.widget.setLayout(self.vbox)
        self.setCentralWidget(self.widget)
        self.show()

    def dynamically_generated_buttons(self):

        positions = [(i, j) for i in range(len(self.filename_list)) for j in range(2)]
        for position, name in zip(positions, self.filename_list):
            if name == '':
                continue
            self.button = QtGui.QPushButton(name)
            self.button.setIcon(QtGui.QIcon("database.png"))
            self.connect(self.button, QtCore.SIGNAL("clicked()"), partial(get_attrib_values, self.button.text()))
            self.button.setFixedHeight(40)
            self.button.setPalette(self.palette1)
            self.button.setFont(self.font1)
            self.grid.addWidget(self.button, *position)


def get_attrib_values(text):

    xml_file = str(text) + '.xml'
    xml_instance.fetch_file_data(xml_file)


if __name__ == "__main__":
    import os
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(BASE_DIR, "config")
    xml_instance = XmlFileParser(path)
    filename = xml_instance.get_filename()
    window = Window(filename=filename)
    sys.exit(app.exec_())
