from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
import gui
import FileProcessor

# PyQt6'dan gerekli modülleri ve kendi oluşturduğunuz modülleri içe aktarın.

class Pencere(QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # GUI'nin oluşturulması ve tasarımının yüklenmesi
        
        # "File" adında bir menü oluştur
        self.file_menu = self.menuBar().addMenu('File')

        # "Options" adında bir alt menü oluştur
        self.Options_menu = QMenu('Options', self)

        # "Options" menüsünün altına başka bir alt menü ekleyin ("Languages")
        self.sub_menu = QMenu('Languages', self)
        self.Options_menu.addMenu(self.sub_menu)

        # "Languages" alt menüsüne iki dil seçeneği ekleyin (English ve Türkçe)
        self.sub_action = QAction('English', self)
        self.sub_menu.addAction(self.sub_action)
        self.sub_action1 = QAction('Türkçe', self)
        self.sub_menu.addAction(self.sub_action1)

        # "Options" menüsünü "File" menüsüne ekleyin
        self.file_menu.addMenu(self.Options_menu)

        # "Exit" adında bir QAction (eylem) ekleyin
        self.exit_action = QAction('Exit', self)
        
        # Butonlara tıklama olaylarını bağlayın
        self.connect_buttons()

        # Kişileri görüntüleme işlevini çağırın
        self.call_people()

    def connect_buttons(self):
        # Dil seçeneklerinin tıklanma olaylarını bağlayın
        self.sub_action.triggered.connect(self.retranslateUi_en)
        self.sub_action1.triggered.connect(self.retranslateUi_tr)

        # "Kişi Ekle" butonunun tıklanma olayını bağlayın
        self.ekle_butonu.clicked.connect(self.add_people)

        # "Kişi Sil" butonunun tıklanma olayını bağlayın
        self.silme_butonu.clicked.connect(self.delete_people)

        # "Exit" eyleminin tıklanma olayını bağlayın
        self.exit_action.triggered.connect(self.close)

        # "Exit" eylemini "File" menüsüne ekleyin
        self.file_menu.addAction(self.exit_action)

    def call_people(self):
        # Kişileri bir dosyadan alıp, listview'e görüntülemek için işlevi çağırın
        people = FileProcessor.get_people_list()
        model = QStringListModel(people)
        self.listView.setModel(model)

    def add_people(self):
        # Kişi eklemek için işlevi çağırın
        FileProcessor.add_people_list(self.lineEdit.text())
        self.call_people()

    def delete_people(self):
        # Kişi silmek için işlevi çağırın
        need_delete = self.lineEdit_2.text()
        FileProcessor.delete_people_list(need_delete)
        self.call_people()

# Uygulamayı başlatın
app = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
sys.exit(app.exec())
