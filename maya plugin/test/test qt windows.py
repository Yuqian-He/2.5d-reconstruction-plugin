import os,sys,subprocess
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtWidgets,QtGui,QtCore
from PySide2.QtCore import Qt

path = cmds.internalVar(userAppDir=True)

def get_mainwindow():
    window=omui.MQtUtil.mainWindow()
    return wrapInstance(int(window),QtWidgets.QDialog)
    
class ImageGenerator(QtWidgets.QDialog):

    def __init__(self,parent=get_mainwindow()):
        super().__init__(parent)
        self.progress_dialog=None
        self.path=' '
        self.name=' '
        self.setWindowTitle("Mono Camera 2.5D Scene Reconstruction")
        self.resize(380,250)

        # select image
        self.grid_layout=QtWidgets.QGridLayout(self)
        self.selectImage_text=QtWidgets.QLabel()
        self.selectImage_text.setText("Select Image: ")
        self.grid_layout.addWidget(self.selectImage_text,0,0,1,1)
        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setReadOnly(True)
        self.grid_layout.addWidget(self.line_edit,0,1,1,1)
        self.load_image=QtWidgets.QPushButton("browse",self)
        self.load_image.clicked.connect(self.load_file)
        self.grid_layout.addWidget(self.load_image,0,2,1,1)

        # select layer
        self.selectLayer_text=QtWidgets.QLabel()
        self.selectLayer_text.setText("Select Layer Num: ")
        self.grid_layout.addWidget(self.selectLayer_text,1,0,1,1)
        self.spin_box = QtWidgets.QSpinBox()
        self.spin_box.setMinimum(1)
        self.spin_box.setMaximum(10)
        self.spin_box.setFixedSize(50, 25)
        self.spin_box.valueChanged.connect(self.select_integer)
        self.grid_layout.addWidget(self.spin_box,1,1,1,1)

        # image preview
        self.image_prview=QtWidgets.QLabel()
        self.image_prview.setText("Image Preview: ")
        self.image_prview.setAlignment(QtCore.Qt.AlignTop)
        self.grid_layout.addWidget(self.image_prview,2,0,1,1)
        self.image=QtWidgets.QLabel()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.show_image)
        self.timer.start(500)
        self.grid_layout.addWidget(self.image,2,1,1,1)

        # button "generate"
        self.generate_image=QtWidgets.QPushButton("generate",self)
        self.generate_image.setFixedSize(350, 25)
        self.grid_layout.addWidget(self.generate_image,4, 0, 1, 3, Qt.AlignHCenter)
        self.generate_image.clicked.connect(self.generate_image_fuc)
    
    def generate_image_fuc(self):
        input_layer=self.spin_box.value()
        print(input_layer)
    
    def show_image(self):
        if self.path==' ':
            self.previewPath=path+'2.5d_algorithm/Empty_image.png'
            img=QtGui.QPixmap(self.previewPath)
            scaled_image = img.scaled(200, 160, Qt.KeepAspectRatio)
            self.image.setPixmap(scaled_image)
        else :
            img=QtGui.QPixmap(self.path)
            scaled_image = img.scaled(200, 160, Qt.KeepAspectRatio)
            self.image.setPixmap(scaled_image)
            return self.path
        
    def load_file(self):
            self.ext=' '
            self.path=cmds.fileDialog2(fm=1)[0]
            self.name=os.path.basename(self.path)
            self.name,self.ext=os.path.splitext(self.name)
            print(self.path)

            IMG_EXTENSIONS = [
            '.jpg', '.JPG', '.jpeg', '.JPEG',
            '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP','.tif',
            ]   

            if self.ext not in IMG_EXTENSIONS:
                QtWidgets.QMessageBox.critical(self,"Critial Error","Not valid file type",QtWidgets.QMessageBox.StandardButton.Abort)
                raise ValueError('Invalid file type, please select image file')
            else:
                self.line_edit.setText(self.path)

    def select_integer(value):
        selected_objects = cmds.ls(selection=True)
        if selected_objects:
            for obj in selected_objects:
                cmds.addAttr(obj, longName="customInt", attributeType="long", defaultValue=value, keyable=True)


# def generate_mesh(self):
#     input_path=self.path
#     ai_thread=AiThread(input_path)
#     ai_thread.run_ai()
#     ai_thread.showMesh()
#     self.close()

# def process_window(self):
#     setValue=100000
#     self.progress_dialog = QProgressDialog("Generating Mesh...", "Cancel", 0, 100, self)
#     self.progress_dialog.setWindowModality(Qt.WindowModal)
#     self.progress_dialog.setAutoClose(True)
#     self.progress_dialog.setAutoReset(True)
#     self.progress_dialog.setValue(0)
#     self.progress_dialog.show()

#     for i in range(setValue):
#         self.progress_dialog.setValue(i/1000)



if __name__=="__main__":
    try:
        image_dialog.close()
        image_dialog.deleteLater()
    except:
        pass
    
    image_dialog=ImageGenerator()
    image_dialog.show()
