from PyQt4 import QtGui, QtCore


class Query_Window(QtGui.QWidget):
	def __init__(self, parent=None, fields=None, desc = None):
		super(Query_Window, self).__init__(parent)
		self.fields = fields
		self.desc = desc
		self.text_fields = []
		self.resize(500, 300)
		# print self.fields['Type'].values=='str'

		self.form = QtGui.QFormLayout()

		self.hbox = QtGui.QHBoxLayout()
		self.title = QtGui.QLabel("Description :")
		self.desc_label = QtGui.QLabel(self.desc)
		self.hbox.addWidget(self.title)
		self.hbox.addWidget(self.desc_label)

		self.horizontal = QtGui.QHBoxLayout()
		self.horizontal_run = QtGui.QHBoxLayout()

		# self.dirText = QtGui.QLineEdit()
		# self.dirText.setReadOnly(True)
		# self.uploadButton = QtGui.QPushButton("UPLOAD", self)
		# self.uploadButton.clicked.connect(self.open)
		for index, value in self.fields.iterrows():

			print value
			self.label = QtGui.QLabel(index)
			if any(value == 'date') and True:
				exec('self.textEdit'+index+' = QtGui.QDateEdit(QtCore.QDate.currentDate().addDays(-1))')
				exec('self.textEdit'+index+'.setCalendarPopup(True)')
				exec('self.date'+index+' = self.textEdit'+index+'.date()')
			elif any(value == 'csv')and True:
				exec ('self.textEdit'+index+' = QtGui.QLineEdit()')
				exec('self.textEdit'+index+'.setReadOnly(True)')

			else:
				exec('self.textEdit'+index+' = QtGui.QLineEdit()')

			exec('self.form.addRow(self.label, self.textEdit'+index+')')

		self.download_check = QtGui.QCheckBox("Download File")
		self.download_check.setChecked(False)
		# self.download_check.toggled.connect(lambda:self.btnstate(self.b2))
		self.upload = QtGui.QPushButton("Upload Codes", self)
		self.upload.move(250, 150)
		self.upload.setFixedWidth(100)
		self.horizontal.setAlignment(QtCore.Qt.AlignJustify)
		self.horizontal.addWidget(self.upload)
		self.horizontal.addWidget(self.download_check)
		self.button = QtGui.QPushButton("Run")
		self.button.setFixedWidth(200)
		self.button.setGeometry(50, 100, 100, 0)
		self.horizontal_run.addWidget(self.button)
		self.horizontal_run.setAlignment(QtCore.Qt.AlignJustify)
		self.hbox.setAlignment(QtCore.Qt.AlignJustify)
		self.vbox = QtGui.QVBoxLayout()
		self.upload.clicked.connect(self.open)
		self.button.clicked.connect(self.display)
		self.vbox.addLayout(self.hbox)
		self.vbox.addLayout(self.form)
		self.vbox.addLayout(self.horizontal)
		self.vbox.addLayout(self.horizontal_run)
		self.setLayout(self.vbox)

	def display(self):
		for index, value in self.fields.iterrows():
			if any(value == 'date') and True:
				print eval('self.date'+index+'.toPyDate()')
			# elif not any(value== 'csv') and True:
			else:
				print eval('self.textEdit'+index+'.text()')

	def open (self):
		filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
		for index, value in self.fields.iterrows():
			if any(value == 'csv')and True:
				exec ('self.textEdit'+index+'.setText(filename)')

		print 'Path file :', filename

if __name__ == "__main__":
	import sys

	app = QtGui.QApplication(sys.argv)
	widget = Query_Window()
	widget.show()
	sys.exit(app.exec_())
