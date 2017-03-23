from PyQt4 import QtGui, QtCore


class Query_Window(QtGui.QWidget):
	def __init__(self, parent=None, fields=None):
		super(Query_Window, self).__init__(parent)
		self.fields = fields
		self.text_fields = []
		self.resize(500, 300)

		self.form = QtGui.QFormLayout()

		for index, value in self.fields.iterrows():
			# print index, value
			self.label = QtGui.QLabel(index)
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
			print eval('self.textEdit'+index+'.text()')

if __name__ == "__main__":
	import sys

	app = QtGui.QApplication(sys.argv)
	widget = Query_Window()
	widget.show()
	sys.exit(app.exec_())
