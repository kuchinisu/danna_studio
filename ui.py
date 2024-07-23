import bpy

from .material.material_collage import crear_material, cambiar_valor_de_difuminacion_agua_a

class MyProperties(bpy.types.PropertyGroup):
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        min=0.0, max=1.0,
        size=3,
        default=(1.0, 1.0, 1.0)
    )
    brush_type: bpy.props.EnumProperty(
        name="Tipo de Pincelada",
        items=[
            ('COLLAGE', "Pincel Collage", ""),
            ('BRUSH', "Pincel", "")
        ],
        default='BRUSH'
    )
    effect_intensity: bpy.props.FloatProperty(
        name="Intensidad del Efecto",
        min=0.0, max=1.0,
        default=0.5
    )
    
    # Opciones de Pincel Collage
    adjust_whites_blacks: bpy.props.FloatProperty(
        name="Ajuste de Blancos y Negros",
        min=0.0, max=1.0,
        default=0.5
    )
    adjust_black_values: bpy.props.FloatVectorProperty(
        name="Ajuste de Valores de Negros",
        subtype='COLOR',
        min=0.0, max=1.0,
        size=3,
        default=(0.0, 0.0, 0.0)
    )
    adjust_white_values: bpy.props.FloatVectorProperty(
        name="Ajuste de Valores de Blancos",
        subtype='COLOR',
        min=0.0, max=1.0,
        size=3,
        default=(1.0, 1.0, 1.0)
    )
    width: bpy.props.FloatProperty(
        name="W",
        precision=3
    )
    brush_fineness: bpy.props.FloatProperty(
        name="Finura de Pinceladas",
        precision=3
    )
    diffused_brush_strokes: bpy.props.FloatProperty(
        name="Capas de Pinceladas Difuminadas",
        precision=3,
        min=0.0, max=15.0
    )
    roughness: bpy.props.FloatProperty(
        name="Rugosidad",
        min=0.0, max=1.0
    )
    diffused_brush_size: bpy.props.FloatProperty(
        name="Tamaño de Pinceladas Difuminadas",
        precision=3
    )
    brush_freedom: bpy.props.FloatProperty(
        name="Libertad de Pinceladas",
        min=0.0, max=1.0
    )
    pattern_repeat_x: bpy.props.FloatProperty(
        name="Repetición de Patrón en X",
        precision=3
    )
    pattern_repeat_y: bpy.props.FloatProperty(
        name="Repetición de Patrón en Y",
        precision=3
    )
    pattern_rotation: bpy.props.FloatProperty(
        name="Rotación de Patrón",
        precision=3,
        min=0.0, max=180.0
    )
    water_blur_a: bpy.props.FloatProperty(
        name="Difuminación con Agua A",
        precision=3,
        min=0.0, max=180.0,
        update=lambda self, context: cambiar_valor_de_rangos("Mapping", )
    )
    water_blur_b: bpy.props.FloatProperty(
        name="Difuminación de Agua B",
        precision=3,
        min=0.0, max=180.0
    )
    pattern_offset_x: bpy.props.FloatProperty(
        name="Desplazamiento de Patrón X",
        precision=3
    )
    pattern_offset_y: bpy.props.FloatProperty(
        name="Desplazamiento de Patrón Y",
        precision=3
    )
    pattern_offset_z: bpy.props.FloatProperty(
        name="Desplazamiento de Patrón Z",
        precision=3
    )
    cleanliness_level: bpy.props.FloatProperty(
        name="Nivel de Limpieza",
        min=0.0, max=1.0
    )
    dirt_scale: bpy.props.FloatProperty(
        name="Escala de Suciedad",
        precision=3
    )
    dirt_detail: bpy.props.FloatProperty(
        name="Detalle de Suciedad",
        precision=3,
        min=0.0, max=15.0
    )
    grain: bpy.props.FloatProperty(
        name="Grano",
        min=0.0, max=1.0
    )
    dirt_blur: bpy.props.FloatProperty(
        name="Difuminación de Suciedad",
        precision=3
    )

    # Opciones de Pincel
    hardness: bpy.props.FloatProperty(
        name="Dureza",
        min=0.0, max=1.0,
        default=0.5
    )

class CrearMaterialOperator(bpy.types.Operator):
    """Operador que muestra un mensaje 'Hello World'"""
    bl_idname = "wm.crear_material"
    bl_label = "Say Hello"

    def execute(self, context):
        nodes_list = crear_material()
        return nodes_list

class HelloWorldPanel(bpy.types.Panel):
    bl_label = "Custom Panel"
    bl_idname = "PT_HelloWorldPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Test'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        layout.operator("wm.crear_material", text="Crear Material a Objeto")
        layout.prop(mytool, "color")
        layout.prop(mytool, "brush_type")
        layout.prop(mytool, "effect_intensity")
        
        if mytool.brush_type == 'BRUSH':
            layout.prop(mytool, "hardness")
        
        elif mytool.brush_type == 'COLLAGE':
            layout.prop(mytool, "adjust_whites_blacks")
            layout.prop(mytool, "adjust_black_values")
            layout.prop(mytool, "adjust_white_values")
            layout.prop(mytool, "width")
            layout.prop(mytool, "brush_fineness")
            layout.prop(mytool, "diffused_brush_strokes")
            layout.prop(mytool, "roughness")
            layout.prop(mytool, "diffused_brush_size")
            layout.prop(mytool, "brush_freedom")
            layout.prop(mytool, "pattern_repeat_x")
            layout.prop(mytool, "pattern_repeat_y")
            layout.prop(mytool, "pattern_rotation")
            layout.prop(mytool, "water_blur_a")
            layout.prop(mytool, "water_blur_b")
            layout.prop(mytool, "pattern_offset_x")
            layout.prop(mytool, "pattern_offset_y")
            layout.prop(mytool, "pattern_offset_z")
            layout.prop(mytool, "cleanliness_level")
            layout.prop(mytool, "dirt_scale")
            layout.prop(mytool, "dirt_detail")
            layout.prop(mytool, "grain")
            layout.prop(mytool, "dirt_blur")

class HelloWorldOperator(bpy.types.Operator):
    bl_label = "Hello World Operator"
    bl_idname = "wm.hello_world"
    
    def execute(self, context):
        self.report({'INFO'}, "Hello World")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(HelloWorldPanel)
    bpy.utils.register_class(HelloWorldOperator)
    bpy.utils.register_class(MyProperties)
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=MyProperties)

def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)
    bpy.utils.unregister_class(HelloWorldOperator)
    bpy.utils.unregister_class(MyProperties)
    del bpy.types.Scene.my_tool

if __name__ == "__main__":
    register()
