import os,subprocess
import maya.cmds as cmds

cmds.select(all=True)
cmds.delete()
path = cmds.internalVar(userAppDir=True)
fileName=''

def showMesh():

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

showMesh()
