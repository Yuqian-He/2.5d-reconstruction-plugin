3import os,subprocess,sys,unreal
# import maya.cmds as cmds

@unreal.uclass()
class EditorUtils(unreal.GlobalEditorUtilityBase):
    pass

path = unreal.Paths.project_plugins_dir()
PATH = []

def run_ai():
    # ================================load path(input image)==================================
    selectedAssets=EditorUtils().get_selected_assets()[0]
    asset_path = unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(selectedAssets)
    fileName = selectedAssets.get_name()
    content_dir = unreal.Paths.project_content_dir()
    export_path = content_dir+'25d_reconstruction'
    unreal.AssetToolsHelpers.get_asset_tools().export_assets([asset_path], export_path)
    inputImage_path=export_path+'/Game/'+fileName+'.PNG'
    print(inputImage_path)

    # ======================================input argument==================================
    Layer_num=int(sys.argv[1])
    createdAssetsName=str(sys.argv[2])
    
    # ===================================load path(python and project path)==================================
    python_path=path+'reconstruction_25d/2.5d_ENV/bin/python3'
    project_path=path+'reconstruction_25d/2.5d_algorithm/run.py'
    
    # ===================================load path(output image path)==================================
    outputResult_path = os.path.abspath(path+'reconstruction_25d/2.5d_algorithm/save_output')

    Layer_num=str(Layer_num)
    abs_path=path+'reconstruction_25d/2.5d_algorithm/'
    arg=python_path+" "+project_path+" "+"--layer_num"+" "+Layer_num+" "+"--input_path"+" "+inputImage_path+" "+"--output_path"+" "+outputResult_path+" "+"--abs_path"+" "+abs_path
    result=subprocess.run(arg,stdout=subprocess.PIPE,shell=True)
    print(result)
    output=result.stdout.decode('utf-8')
    print(outputResult_path)
    print(output)

def importImage():
    # =================================================import into unreal==================================
    Layer_num=int(sys.argv[1])

    for i in range(Layer_num):
        outputFile_path=os.path.abspath(path+'reconstruction_25d/2.5d_algorithm/save_output')
        num='/'+str(i+1)
        outputImage_path=outputFile_path+num+'.png'
        destination_path = "/Game/25d_reconstruction/Game"
        import_task = unreal.AssetImportTask()
        import_task.filename = outputImage_path
        import_task.destination_path = destination_path
        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
        asset_tools.import_asset_tasks([import_task])
        imageImportPath=destination_path+num+'.'+str(i+1)
        print(imageImportPath)
        PATH.append(imageImportPath)
        i-=1

def showImage():
    name=0
    for i in PATH:
        name+=1
        asset = unreal.EditorAssetLibrary.load_asset(i)
        destination_path = "/Game/25d_reconstruction/Game"

        # ===================================================create material and set property======================================
        mf = unreal.MaterialFactoryNew()
        assetTools = unreal.AssetToolsHelpers.get_asset_tools()
        mat_closure = assetTools.create_asset("M_%s" % name, "%s/" % destination_path, unreal.Material, mf)
        # mat_closure.set_editor_property('BlendMode', unreal.BlendMode.BLEND_TRANSLUCENT)

        unreal.EditorAssetLibrary.save_asset(mat_closure.get_path_name())

        # =================================================Create a texturesample expression and connect==============================
        base_color = unreal.MaterialEditingLibrary.create_material_expression(mat_closure, unreal.MaterialExpressionTextureSample)
        base_color.texture = asset
        unreal.MaterialEditingLibrary.connect_material_property(base_color, 'RGB', unreal.MaterialProperty.MP_BASE_COLOR)
        unreal.MaterialEditingLibrary.connect_material_property(base_color, 'A', unreal.MaterialProperty.MP_OPACITY)
        mat_closure.set_editor_property('blend_mode', unreal.BlendMode.BLEND_TRANSLUCENT)

        # ==================================================create actor blueprint==================================
        blueprint_factory = unreal.BlueprintFactory()
        blueprint_factory.set_editor_property("ParentClass", unreal.Actor)
        blueprint = unreal.AssetToolsHelpers.get_asset_tools().create_asset("Blueprint_%s" % name, destination_path, unreal.Blueprint, blueprint_factory)
        
        unreal.EditorAssetLibrary.save_asset("/Game/25d_reconstruction/Game/Blueprint_"+str(name),only_if_is_dirty=True)

        # =====================================Add a widget component to the blueprint=====================================
        subsystem = unreal.get_engine_subsystem(unreal.SubobjectDataSubsystem)
        root_data_handle = subsystem.k2_gather_subobject_data_for_blueprint(blueprint)[0]
        sub_handle,FaileReason=subsystem.add_new_subobject(unreal.AddNewSubobjectParams(parent_handle=root_data_handle,new_class=unreal.WidgetComponent,blueprint_context=blueprint))
        subsystem.attach_subobject( root_data_handle, sub_handle )

        unreal.EditorAssetLibrary.save_asset("/Game/25d_reconstruction/Game/Blueprint_"+str(name),only_if_is_dirty=True)

        # =====================set material to this widget component=================
        actor_class=unreal.EditorAssetLibrary.load_blueprint_class(destination_path+'/Blueprint_'+str(name))
        dis=float(sys.argv[2])
        print(dis)
        actor_location=unreal.Vector(name*dis,0,20)
        actor_rotation=unreal.Rotator(0.0,0.0,0.0)
        spawned_actor=unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class,actor_location,actor_rotation)
        widget_component=spawned_actor.get_components_by_class(component_class=unreal.WidgetComponent)[0]
        widget_component.set_material(0,mat_closure)

        current_scale = spawned_actor.get_actor_scale3d()
        scale_factor = unreal.Vector(1, 1.5, 1)
        new_scale = current_scale * scale_factor
        spawned_actor.set_actor_scale3d(new_scale)


run_ai()
importImage()
showImage()
