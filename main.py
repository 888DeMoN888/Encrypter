import os
import pyAesCrypt
import sys
from PyQt5 import QtWidgets, QtGui
import form
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QListWidgetItem

wb_patch = ''
passw = ''
filename = ''
typeFile = ''

class App(QtWidgets.QMainWindow, form.Ui_MainWindow):

	def __init__(self):
		super().__init__()
		self.setupUi(self)  # Это нужно для инициализации нашего дизайна
		self.Browse.clicked.connect(self.browse_folder)  # Выполнить функцию browse_folder
		self.Go.clicked.connect(self.showDialog) # Выполнить функцию go_button
		self.initUI()
		self.setWindowIcon(QtGui.QIcon('icon.ico'))

	def initUI(self):
		self.setGeometry(300, 300, 290, 150)
		self.show()

	def showDialog(self):

		global mode, passw, typeFile, wb_patch

		if self.Encrypt.isChecked():
			mode = 0
		elif self.Decrypt.isChecked():
			mode = 1
		if wb_patch != '':

			if self.Encrypt.isChecked() and wb_patch != '':
				crypter(0, wb_patch)
				self.path_to_file.clear()
				wb_patch = ''
			elif self.Decrypt.isChecked() and wb_patch != '' and passw == passw:
				typeFile, ok = QInputDialog.getText(self, 'Type', 'Enter the file type without a dot')
				if ok and typeFile != '':
					crypter(1, wb_patch)
					self.path_to_file.clear()
					wb_patch = ''
		else:
			pass

	def browse_folder(self):

		global wb_patch, filename

		self.path_to_file.clear()  # На случай, если в списке уже есть элементы
		# directory, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Single File', '')
		wb_patch = QtWidgets.QFileDialog.getOpenFileName()[0]
		# открыть диалог выбора директории и установить значение переменной
		# равной пути к выбранной директории
		if wb_patch:  # не продолжать выполнение, если пользователь не выбрал директорию
			self.path_to_file.addItem(QListWidgetItem(wb_patch))   # добавить файл в listWidget
			filename = wb_patch
	
class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
	
def main():
	app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
	window = App()  # Создаём объект класса App
	window.show()  # Показываем окно
	app.exec_()  # и запускаем приложение

def crypter(_mode, _file):
	password = passw
	buffer = 512 * 1024
	ext = _file.split('.')

	if(int(_mode) == 0):
		pyAesCrypt.encryptFile(_file, ext[0] + '.den', password, buffer)

	elif(int(_mode) == 1):
		_type = typeFile
		pyAesCrypt.decryptFile(_file, ext[0] + '.' + _type, password, buffer)

	os.remove(_file)

def function():	
	global wb_patch
	try:
		if __name__ == '__main__':
			main()
	except:
		function()
		wb_patch = ''
function()