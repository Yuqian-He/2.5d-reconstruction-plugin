import os,subprocess,sys,unreal
# import maya.cmds as cmds

@unreal.uclass()
class EditorUtils(unreal.GlobalEditorUtilityBase):
    pass

path = unreal.Paths.project_plugins_dir()
fileName=''

def run_ai():
    # ================================load path(input image)
    selectedAssets=EditorUtils().get_selected_assets()[0]
    asset_path = unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(selectedAssets)
    content_dir = unreal.Paths.project_content_dir()
    relative_path = asset_path.replace(content_dir, "")
    if relative_path.startswith("/"):
        relative_path = relative_path[6:]
    inputImage_path=content_dir+relative_path

    Layer_num=int(sys.argv[1])
    createdAssetsName=str(sys.argv[2])
    
    # ===================================load path(python and project path)
    python_path=path+'reconstrucation25d/2.5d_ENV/bin/python'
    project_path=path+'reconstrucation25d/2.5d_algorithm/run.py'

    # ===================================load path(output image path)
    outputResult_path = os.path.abspath(path+'reconstrucation25d/2.5d_algorithm/save_output')

    Layer_num=str(Layer_num)
    abs_path=path+'2.5d_algorithm/'
    arg=python_path+" "+project_path+" "+"--layer_num"+" "+Layer_num+" "+"--input_path"+" "+inputImage_path+" "+"--output_path"+" "+outputResult_path+" "+"--abs_path"+" "+abs_path
    result=subprocess.run(arg,stdout=subprocess.PIPE,shell=True)
    output=result.stdout.decode('utf-8')
    print(output)

run_ai()