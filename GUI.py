import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon

class Window(QMainWindow):
	"""docstring for Window"""
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50,50,800,500)
		self.setWindowTitle("Casino Card Game")
		#self.setWindowIcon(Qt.Gui.Qicon(""))
		self.show()

app = QApplication(sys.argv)

GUI = Window()

sys.exit(app.exec_())