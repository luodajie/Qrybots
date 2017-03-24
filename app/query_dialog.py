from PyQt4 import QtGui, QtCore


class Query_Window(QtGui.QWidget):
	def __init__(self, parent=None, fields=None):
		super(Query_Window, self).__init__(parent)
		self.fields = fields
		self.text_fields = []
		self.resize(500, 300)
		# print self.fields['Type'].values=='str'

		self.form = QtGui.QFormLayout()

		for index, value in self.fields.iterrows():

			print value
			# print index, value
			self.label = QtGui.QLabel(index)
			if any(value == 'date') and True:
			# self.dateEdit.setDate(QtCore.QDate(2006, 12, 22))
				exec('self.textEdit'+index+' = QtGui.QDateEdit(QtCore.QDate.currentDate().addDays(-1))')
				exec('self.textEdit'+index+'.setCalendarPopup(True)')
				exec('self.date'+index+' = self.textEdit'+index+'.date()')
			else:
				exec('self.textEdit'+index+' = QtGui.QLineEdit()')
			exec('self.form.addRow(self.label, self.textEdit'+index+')')
			# self.text_fields.append(str(self.textEdit.text()))
		self.button = QtGui.QPushButton("Run")
		self.vbox = QtGui.QVBoxLayout()
		self.button.clicked.connect(self.display)
		self.vbox.addLayout(self.form)
		self.vbox.addWidget(self.button)
		# print text_fields
		self.setLayout(self.vbox)

	def display(self):
		for index, value in self.fields.iterrows():
			if any(value == 'date') and True:
				print eval('self.date'+index+'.toPyDate()')
			else:
				print eval('self.textEdit'+index+'.text()')

if __name__ == "__main__":
	import sys

	app = QtGui.QApplication(sys.argv)
	widget = Query_Window()
	widget.show()
	sys.exit(app.exec_())
