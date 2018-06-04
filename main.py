import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QHBoxLayout,QVBoxLayout,QFileDialog
from PyQt5.QtWidgets import QAction,qApp,QMainWindow

class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi_alani = QTextEdit()
        self.temizle = QPushButton("Temizle")
        self.ac = QPushButton("Ac")
        self.kaydet = QPushButton("Kaydet")
        
        h_box = QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        
        v_box.addLayout(h_box)
        
        self.setLayout(v_box)
        
        self.temizle.clicked.connect(self.yazi_temizle)
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)

    
    def yazi_temizle(self):
        self.yazi_alani.clear()
    def dosya_ac(self):
        dosya_ismi = QFileDialog.getOpenFileName(self,"Dosya Ac",os.getenv("Home"))
        with open(dosya_ismi[0],"r") as file:
            self.yazi_alani.setText(file.read())
    def dosya_kaydet(self):
        dosya_ismi = QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))
        with open(dosya_ismi[0],"w") as file:
            file.write(self.yazi_alani.toPlainText())
        
class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere = Notepad()
        self.setCentralWidget(self.pencere)
        self.menu_olustur()

    def menu_olustur(self):
        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")
        dosya_ac = QAction("Dosya Ac",self)
        dosya_ac.setShortcut("Ctrl+O")
        dosya_kaydet = QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")
        temizle = QAction("Dosyayi Temizle",self)
        temizle.setShortcut("Ctrl+R")
        cikis = QAction("Cikis",self)
        cikis.setShortcut("Ctrl+Q")
        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)

        dosya.triggered.connect(self.yonlendir)

        self.setWindowTitle("Text Editor")
        self.show()

    def yonlendir(self,action):
        if action.text() == "Dosya Ac":
            self.pencere.dosya_ac()
        elif action.text() == "Dosya Kaydet":
            self.pencere.dosya_kaydet()
        elif action.text() == "Dosya Temizle":
            self.pencere.yazi_temizle()
        elif action.text() == "Cikis":
            qApp.quit()


app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())