import unreal
import sys
# # =====================================================read the assets

# @unreal.uclass()
# class EditorUtils(unreal.GlobalEditorUtilityBase):
#     pass

# selectedAssets=EditorUtils().get_selected_assets()

# for asset in selectedAssets:
#     unreal.log(asset.get_full_name())
#     unreal.log(asset.get_fname())
#     unreal.log(asset.get_class())
#     unreal.log("**************************************")


# =========================================================create blueprint
blueprintName="test_blueprint"
blueprintPath='/Game/Blueprint'

createdAssetsCout=int(sys.argv[1])
createdAssetsName=str(sys.argv[2])
# createdAssetsName+='\d'

factory=unreal.BlueprintFactory()
factory.set_editor_property("ParentClass", unreal.GameMode)

assetTools=unreal.AssetToolsHelpers.get_asset_tools()

for x in range(createdAssetsCout):
    myFile=assetTools.create_asset(createdAssetsName+str(x),blueprintPath,None,factory)
    unreal.EditorAssetLibrary.save_loaded_asset(myFile)

