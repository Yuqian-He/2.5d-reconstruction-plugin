import os,subprocess,sys,unreal
# import maya.cmds as cmds

@unreal.uclass()
class EditorUtils(unreal.GlobalEditorUtilityBase):
    pass

path = unreal.Paths.project_plugins_dir()

def showImage():
    # ===============import into unreal
    Layer_num=int(sys.argv[1])
    import_tasks = []
    for i in range(Layer_num):
        outputFile_path=os.path.abspath(path+'reconstruction_25d/2.5d_algorithm/save_output')
        num='/'+str(i)
        outputImage_path=outputFile_path+num+'.png'
        print(outputImage_path)
        destination_path = "/Game/25d_reconstruction/Game"
        import_task = unreal.AssetImportTask()
        import_task.filename = outputImage_path
        import_task.destination_path = destination_path
        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
        asset_tools.import_asset_tasks([import_task])

showImage()
