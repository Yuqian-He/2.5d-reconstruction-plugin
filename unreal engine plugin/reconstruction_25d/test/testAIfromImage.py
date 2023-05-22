import os,subprocess,sys,unreal
# import maya.cmds as cmds

@unreal.uclass()
class EditorUtils(unreal.GlobalEditorUtilityBase):
    pass

def run_ai():
    # ================================load path(input image)
    path = unreal.Paths.project_plugins_dir()
    selectedAssets=EditorUtils().get_selected_assets()[0]
    asset_path = unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(selectedAssets)
    fileName = selectedAssets.get_name()
    content_dir = unreal.Paths.project_content_dir()
    export_path = content_dir+'25d_reconstruction'
    unreal.AssetToolsHelpers.get_asset_tools().export_assets([asset_path], export_path)
    inputImage_path=export_path+'/Game/'+fileName+'.PNG'
    print(inputImage_path)

    # ======================================input argument
    Layer_num=int(sys.argv[1])
    createdAssetsName=str(sys.argv[2])
    
    # ===================================load path(python and project path)
    python_path=path+'reconstruction_25d/2.5d_ENV/bin/python'
    project_path=path+'reconstruction_25d/2.5d_algorithm/run.py'
    
    # ===================================load path(output image path)
    outputResult_path = os.path.abspath(path+'reconstruction_25d/2.5d_algorithm/save_output')

    Layer_num=str(Layer_num)
    abs_path=path+'reconstruction_25d/2.5d_algorithm/'
    arg=python_path+" "+project_path+" "+"--layer_num"+" "+Layer_num+" "+"--input_path"+" "+inputImage_path+" "+"--output_path"+" "+outputResult_path+" "+"--abs_path"+" "+abs_path
    result=subprocess.run(arg,stdout=subprocess.PIPE,shell=True)
    print(result)
    output=result.stdout.decode('utf-8')
    print(outputResult_path)
    print(output)

run_ai()