import os,subprocess
import maya.cmds as cmds

path = cmds.internalVar(userAppDir=True)
# print(path)
fileName=''

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
    print(output)
run_ai()
