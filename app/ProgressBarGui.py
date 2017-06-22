from PyQt4 import QtGui, QtCore


class ProgressDialog(QtGui.QDialog):
    def __init__(self, parent=None, mainWindow=None, file_location=None):
        super(ProgressDialog, self).__init__(parent)

        self.setWindowTitle("Please wait...")
        self.file_location = file_location
        self._want_to_close = False

        layout = QtGui.QVBoxLayout(self)
        self.progressBar = QtGui.QProgressBar(self)
        self.progressBar.setRange(0, 0)
        layout.addWidget(self.progressBar)
        self.setLayout(layout)

        self.myLongTask = TaskThread(mainWindow)
        self.myLongTask.start()
        self.myLongTask.taskFinishedSignal.connect(self.onFinished)
        self.myLongTask.taskErrorSignal.connect(self.onError)

    def onFinished(self):
        self.progressBar.setRange(0, 1)
        self.progressBar.setValue(1)
        self._want_to_close = True
        self.close()
        QtGui.QMessageBox.information(self, 'Success', 'Your files are saved at : ' + str(self.file_location))

    def onError(self, argument):
        self._want_to_close = True
        self.close()
        QtGui.QMessageBox.critical(self, 'Error', argument)

    def closeEvent(self, evnt):
        if self._want_to_close:
            super(ProgressDialog, self).closeEvent(evnt)
        else:
            evnt.ignore()


class TaskThread(QtCore.QThread):
    taskFinishedSignal = QtCore.pyqtSignal(int)
    taskErrorSignal = QtCore.pyqtSignal(str)

    def __init__(self, mainWindow=None):
        super(TaskThread, self).__init__()
        self.mainWindow = mainWindow

    def run(self):
        # try:
            msg = self.mainWindow.display()
            self.taskFinishedSignal.emit(msg)
        # except Exception as e:
        #     self.taskErrorSignal.emit(str(e))
