import os,sys,subprocess
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtWidgets,QtGui,QtCore
from PySide2.QtCore import Qt,QThread


path = cmds.internalVar(userAppDir=True)
print(path)
fileName=''

class AiThread(QThread):

    def __init__(self,input_path,input_layer,parent=None):
        super(AiThread,self).__init__(parent)
        self.input_path=input_path
        self.input_layer=str(input_layer)

    def run_ai(self):
        python_path=path+'2.5d_ENV/bin/python3'
        project_path=path+'2.5d_algorithm/run.py'
        inputImage_path = self.input_path
        # print(project_path)
        outputResult_path = os.path.abspath(path+'2.5d_algorithm/save_output')
        abs_path=path+'2.5d_algorithm/'

        arg=python_path+" "+project_path+" "+"--layer_num"+" "+self.input_layer+" "+"--input_path"+" "+inputImage_path+" "+"--output_path"+" "+outputResult_path+" "+"--abs_path"+" "+abs_path
        result=subprocess.run(arg,stdout=subprocess.PIPE,shell=True)
        output=result.stdout.decode('utf-8')
        print(output)

    def showMesh(self):

        path_image=path+'2.5d_algorithm/save_output/'
        files=os.listdir(path_image)
        num=0
        for i in range(len(files)):
            num=num+1
            image_plane_name = "ImagePlane"+str(num)
            print(i)
            image_path = path_image + str(i+1)+".png"

            print(fileName)
            cmds.imagePlane(name=image_plane_name)
            cmds.setAttr(image_plane_name+'.imageName', image_path, type="string")
            cmds.select(image_plane_name)
            cmds.scale(1.6,1.2,1)
            cmds.move(0, 0, num*1.8,image_plane_name,absolute=True)


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
        self.timer.start(100)
        self.grid_layout.addWidget(self.image,2,1,1,1)

        # button "generate"
        self.generate_image=QtWidgets.QPushButton("generate",self)
        self.generate_image.setFixedSize(350, 25)
        self.grid_layout.addWidget(self.generate_image,4, 0, 1, 3, Qt.AlignHCenter)
        self.generate_image.clicked.connect(self.generate_image_fuc)

    def generate_image_fuc(self):
        input_layer=self.spin_box.value()
        print(input_layer)
        input_path=self.path
        ai_thread=AiThread(input_path,input_layer)
        ai_thread.run_ai()
        ai_thread.showMesh()
        self.close()

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

if __name__=="__main__":
    try:
        image_dialog.close()
        image_dialog.deleteLater()
    except:
        pass
    
    image_dialog=ImageGenerator()
    image_dialog.show()
