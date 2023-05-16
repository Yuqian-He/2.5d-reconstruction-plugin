import os,subprocess
import maya.cmds as cmds

path = cmds.internalVar(userAppDir=True)
print(path)
fileName=''

def run_ai():
    python_path=path+'2.5d_ENV/bin/python3'
    project_path=path+'2.5d_algorithm/run.py'
    inputImage_path = '/Users/naname/Downloads/test01.jpg'
    # print(project_path)
    outputResult_path = os.path.abspath(path+'2.5d_algorithm/save_output')
    abs_path=path+'2.5d_algorithm/'

    arg=python_path+" "+project_path+" "+"--layer_num 3"+" "+"--input_path"+" "+inputImage_path+" "+"--output_path"+" "+outputResult_path+" "+"--abs_path"+" "+abs_path
    result=subprocess.run(arg,stdout=subprocess.PIPE,shell=True)
    output=result.stdout.decode('utf-8')
    print(output)

def showMesh():
    cmds.select(all=True)
    cmds.delete()
    path_image=path+'2.5d_algorithm/save_output/'
    files=os.listdir(path_image)
    num=0
    for i in files:
        num=num+1
        image_plane_name = "ImagePlane"+str(num)
        print(num)
        image_path = path_image + i

        print(fileName)
        cmds.imagePlane(name=image_plane_name)
        cmds.setAttr(image_plane_name+'.imageName', image_path, type="string")
        cmds.select(image_plane_name)
        cmds.move(0, 0, -num*1,image_plane_name,absolute=True)

def delectImage():
    cmds.select("ImagePlane1")
    # cmds.select("ImagePlane2")
    # cmds.select("ImagePlane3")

run_ai()
showMesh()
delectImage()
