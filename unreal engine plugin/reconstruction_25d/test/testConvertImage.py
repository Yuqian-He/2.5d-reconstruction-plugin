import os,subprocess,sys,unreal
# import maya.cmds as cmds

@unreal.uclass()
class EditorUtils(unreal.GlobalEditorUtilityBase):
    pass

path = unreal.Paths.project_plugins_dir()

path = unreal.Paths.project_plugins_dir()
selectedAssets=EditorUtils().get_selected_assets()[0]
asset_path = unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(selectedAssets)
fileName = selectedAssets.get_name()
content_dir = unreal.Paths.project_content_dir()
export_task = unreal.AssetExportTask()
export_task.object = selectedAssets
export_path = content_dir+'25d_reconstruction'
exported_paths = unreal.AssetToolsHelpers.get_asset_tools().export_assets([asset_path], export_path)
inputImage_path=export_path+'/Game/'+fileName+'.PNG'
print(inputImage_path)