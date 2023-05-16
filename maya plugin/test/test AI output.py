import os,sys,subprocess
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtWidgets,QtGui,QtCore
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog,QProgressDialog,QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget


path = cmds.internalVar(userAppDir=True)
# print(path)
fileName=''

def get_mainwindow():
    window=omui.MQtUtil.mainWindow()
    return wrapInstance(int(window),QtWidgets.QDialog)

class SubWindow(QDialog):
    def __init__(self,parent=get_mainwindow()):
        super().__init__(parent)

        self.setWindowTitle("Subwindow")
        self.resize(180,100)

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.text_edit = QtWidgets.QLabel()
        layout.addWidget(self.text_edit)

    def set_output(self, output):
        self.text_edit.setText(output)


def run_ai():
    python_path=path+'2.5d_ENV/bin/python'
    project_path=path+'2.5d_algorithm/run.py'
    inputImage_path = '/Users/naname/Downloads/test01.jpg'
    # print(project_path)
    outputResult_path = os.path.abspath(path+'2.5d_algorithm/save_output')
    # outputResult_path='/Users/naname/Downloads/test'

    abs_path=path+'2.5d_algorithm/'
    arg=python_path+" "+project_path+" "+"--layer_num 4"+" "+"--input_path"+" "+inputImage_path+" "+"--output_path"+" "+outputResult_path+" "+"--abs_path"+" "+abs_path
    result=subprocess.run(arg,stdout=subprocess.PIPE,shell=True)
    print(outputResult_path)
    output=result.stdout.decode('utf-8')
    return output

def generate_dialog():
    subwindow = SubWindow()
    subwindow.show()
    timer = QtCore.QTimer()

    output=run_ai()
    timer.timeout.connect(subwindow.set_output(output))
    timer.start(500)




generate_dialog()
