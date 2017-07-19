from PyQt5 import QtWidgets
from PyQt5 import QtCore
import os
import sys

project_dir = '/Users/pavelpavlov/PycharmProject/Antelope Test Tool/session_folder'
audio_in_dir ='/Users/pavelpavlov/PycharmProject/Antelope Test Tool/audio_in_folder'
audio_out_dir ='/Users/pavelpavlov/PycharmProject/Antelope Test Tool/audio_out_folder'


class TestCase(QtWidgets.QWidget):

    def __init__(self,
                 name: str = "Default", session_folder: str = '',
                 audio_in_folder: str = '', audio_out_folder: str = '',
                 *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

        self._session_folder = session_folder

        self.hbox = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel(name)
        self.button = QtWidgets.QPushButton(name)
        self.button.setCheckable(True)

        self.session_combo = QtWidgets.QComboBox()
        r = self.Access_Dir(session_folder)

        for n in r:
            self.session_combo.addItem(n)

        self.audio_in_comb = QtWidgets.QComboBox()
        r = self.Access_Dir(audio_in_dir)

        for n in r:
            self.audio_in_comb.addItem(n)

        r = self.Access_Dir(audio_out_dir)

        self.audio_out_comb = QtWidgets.QComboBox()
        self.Access_Dir(audio_out_dir)

        for n in r:
            self.audio_out_comb.addItem(n)

        self._audio_out_folder = audio_out_dir

        self.hbox.addWidget(self.label)
        self.hbox.addWidget(self.button)
        self.hbox.addWidget(self.session_combo)
        self.hbox.addWidget(self.audio_in_comb)
        self.hbox.addWidget(self.audio_out_comb)
        self.setLayout(self.hbox)


    def Access_Dir(self, dir):
        return os.listdir(dir)

class Scroller(QtWidgets.QScrollArea):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        vbox = QtWidgets.QVBoxLayout()
        for n in ['ADAT', 'MADI', 'S/PDIF', 'Analog']:
            o = TestCase(name=n,session_folder=project_dir,
                         audio_in_folder=project_dir, audio_out_folder=project_dir)
            vbox.addWidget(o)

        base_widget = QtWidgets.QWidget()
        base_widget.setLayout(vbox)
        self.setWidget(base_widget)


def window():
    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()
    vbox = QtWidgets.QVBoxLayout()

    scroller = Scroller()
    vbox.addWidget(scroller)

    w.setLayout(vbox)
    w.setWindowTitle("Antelope Test Tool")

    w.show()
    sys.exit(app.exec_())

window()
