from PyQt4 import QtGui, QtCore


class Query_Window(QtGui.QWidget):
    def __init__(self, parent=None, fields=None, desc=None):
        super(Query_Window, self).__init__(parent)
        self.fields = fields
        self.desc = desc
        self.text_fields = []
        self.resize(500, 300)

        self.group = QtGui.QGroupBox('Description: %s' % self.desc)

        self.form = QtGui.QFormLayout()
        self.save_form = QtGui.QFormLayout()
        self.horizontal = QtGui.QHBoxLayout()
        self.save_horizontal = QtGui.QHBoxLayout()
        self.horizontal_run = QtGui.QHBoxLayout()

        self.upload = QtGui.QPushButton("Upload Codes", self)
        self.upload.move(250, 150)
        self.upload.setFixedWidth(100)

        for index, value in self.fields.iterrows():
            self.label = QtGui.QLabel(index)
            if any(value == 'date'):
                exec ('self.textEdit' + index + ' = QtGui.QDateEdit(QtCore.QDate.currentDate().addDays(-1))')
                exec ('self.textEdit' + index + '.setCalendarPopup(True)')
                exec ('self.textEdit' + index + '.setFixedWidth(100)')

            elif any(value == 'csv'):
                exec ('self.textEdit' + index + ' = QtGui.QHBoxLayout()')
                exec ('self.csv_upload = QtGui.QLineEdit()')
                exec ('self.csv_upload.setReadOnly(True)')
                exec ('self.textEdit' + index + '.addWidget(self.csv_upload)')
                exec ('self.textEdit' + index + '.addWidget(self.upload)')

            else:
                exec ('self.textEdit' + index + ' = QtGui.QLineEdit()')

            exec ('self.form.addRow(self.label, self.textEdit' + index + ')')

        self.save_to_label = QtGui.QLabel('Save to: ')
        self.save_to_text = QtGui.QLineEdit()
        self.save_to_text.setReadOnly(True)
        self.save_to = QtGui.QPushButton("Browse", self)
        self.save_to.move(250, 150)
        self.save_to.setFixedWidth(100)
        self.save_to.clicked.connect(self.download)

        self.save_horizontal.addWidget(self.save_to_text)
        self.save_horizontal.addWidget(self.save_to)

        self.save_form.addRow(self.save_to_label, self.save_horizontal)

        self.run_button = QtGui.QPushButton("Run")
        self.run_button.setFixedWidth(200)
        self.run_button.setGeometry(50, 100, 100, 0)
        self.horizontal_run.addWidget(self.run_button)
        self.horizontal_run.setAlignment(QtCore.Qt.AlignJustify)
        self.vbox = QtGui.QVBoxLayout()
        self.vertical1 = QtGui.QVBoxLayout()
        self.vertical = QtGui.QVBoxLayout()
        self.upload.clicked.connect(self.upload_codes)
        self.run_button.clicked.connect(self.display)
        self.vbox.addLayout(self.form)
        self.vertical1.addLayout(self.save_form)
        self.vertical1.addLayout(self.horizontal_run)
        self.group.setLayout(self.vbox)
        self.vertical.addWidget(self.group)
        self.vertical.addLayout(self.vertical1)
        self.setLayout(self.vertical)

    def display(self):
        lst = []
        for index, value in self.fields.iterrows():
            if any(value == 'date'):
                exec ('self.date' + index + ' = self.textEdit' + index + '.date()')
                lst.append(eval('self.date' + index + '.toPyDate()'))

            elif any(value == 'csv'):
                print eval('self.csv_upload.text()')

            elif any(value == 'int'):
                if value.Id == '2':
                    try:
                        number = int(eval('self.textEdit' + index + '.text()'))
                        if type(number) == int:
                            print number

                    except ValueError:
                        QtGui.QMessageBox.about(self, 'Error',
                                                'Insert only numbers for "{0}"'.format(str(index).upper()))

                if value.Id == '3':
                    try:
                        number = int(eval('self.textEdit' + index + '.text()'))
                        if type(number) == int:
                            print number

                    except ValueError:
                        QtGui.QMessageBox.about(self, 'Error',
                                                'Insert only numbers for "{0}"'.format(str(index).upper()))

            else:
                x = eval('self.textEdit' + index + '.text()')

                print "id is ", x

        for d in lst:
            if not type(d):
                raise
            else:
                print d

    def upload_codes(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        self.csv_upload.setText(filename)

        content = open(filename, 'r')
        print content.read()

    def download(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        self.save_to_text.setText(filename)

        print 'Path file :', filename


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    widget = Query_Window()
    widget.show()
    sys.exit(app.exec_())
