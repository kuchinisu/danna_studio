import bpy
from mathutils import Euler
def crear_material():
    
    cube = bpy.context.object


    material = bpy.data.materials.new(name="Collage")

    material.use_nodes = True

    nodes_list = {}

    principled_bsdf = material.node_tree.nodes.get('Principled BSDF')
    

    nodes_list['principled_bsdf']=principled_bsdf

    if not principled_bsdf:
        principled_bsdf = material.node_tree.nodes.new('ShaderNodeBsdfPrincipled')

    principled_bsdf.inputs['Base Color'].default_value = (1, 0, 0, 1)  # Rojo
    principled_bsdf.inputs['Roughness'].default_value = 0.5


    material_output = material.node_tree.nodes.get('Material Output')

    

    if not material_output:
        material_output = material.node_tree.nodes.new('ShaderNodeOutputMaterial')

    material_output.name = "Material Output"

    nodes_list['material_output']=material_output
    
    material.node_tree.links.new(principled_bsdf.outputs['BSDF'], material_output.inputs['Surface'])


    if cube.data.materials:
        cube.data.materials[0] = material
    else:
        cube.data.materials.append(material)

    node_tree = material.node_tree
    nodes = node_tree.nodes
    links = node_tree.links

    shader_rgb = nodes.new(type="ShaderNodeRGB")
    shader_rgb.name = "RGB"
    nodes_list['shader_rgb'] = shader_rgb

    shader_rgb_output_color=shader_rgb.outputs["Color"]

    mix_color = nodes.new(type="ShaderNodeMix")
    mix_color.data_type = "RGBA"
    mix_color.blend_type = "MULTIPLY"
    mix_color.name = "Mix Color"
    nodes_list.append(mix_color)

    input_a_mix_color = mix_color.inputs["A"]
    input_a_mix_color = mix_color.inputs["A"]
    links.new(shader_rgb_output_color, input_a_mix_color)

    result_output_mix_color = mix_color.outputs["Result"]
    bsdf_input_base_color = principled_bsdf.inputs["Base Color"]
    links.new(result_output_mix_color, bsdf_input_base_color)

    color_ramp = nodes.new(type="ShaderNodeValToRGB")
    color_ramp.name = "Color Ramp"
    color_ramp_output_color = color_ramp.outputs["Color"]
    nodes_list.append(color_ramp)

    mix_color_input_b = mix_color.inputs["B"]
    links.new(color_ramp_output_color, mix_color_input_b)

    mix_color_2 = nodes.new(type="ShaderNodeMix")
    mix_color_2.name = "Mix Color 2"
    mix_color_2.data_type = 'RGBA'
    mix_color_2.blend_type = 'MIX'
    nodes_list.append(mix_color_2)

    mix_color_2_result_output = mix_color_2.outputs["Result"]
    color_ramp_fac_input = color_ramp.inputs["Fac"]
    links.new(mix_color_2_result_output, color_ramp_fac_input)
    
    mix_color_3 = nodes.new(type="ShaderNodeMix")
    mix_color_3.data_type = 'RGBA'
    mix_color_3.blend_type = 'MIX'
    mix_color_3.name = "Mix Color 3"
    nodes_list.append(mix_color_3)

    noise_texture = nodes.new(type="ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    nodes_list.append(noise_texture)

    noise_texture_output_fac = noise_texture.outputs["Fac"]
    mix_color_3_input_b = mix_color_3.inputs["B"]
    links.new(noise_texture_output_fac, mix_color_3_input_b)

    mix_color_3_output_result = mix_color_3.outputs["Result"]
    mix_color_2_input_a = mix_color_2.inputs["A"]
    links.new(mix_color_3_output_result, mix_color_2_input_a)

    voronoi_texture = nodes.new(type="ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.voronoi_dimensions = '4D'
    voronoi_texture_output_color = voronoi_texture.outputs["Color"]
    mix_color_2_input_b = mix_color_2.inputs["B"]
    nodes_list.append(voronoi_texture)
    links.new(voronoi_texture_output_color, mix_color_2_input_b)

    mapping = nodes.new(type="ShaderNodeMapping")
    mapping.name = "Mapping"
    nodes_list.append(mapping)

    texture_coord = nodes.new(type="ShaderNodeTexCoord")
    texture_coord.name = "Texture Coordinate"
    nodes_list.append(texture_coord)

    voronoi_texture_input_vector = voronoi_texture.inputs["Vector"]
    mapping_output_vector = mapping.outputs["Vector"]
    links.new(mapping_output_vector, voronoi_texture_input_vector)


    texture_coord_output_uv = texture_coord.outputs["UV"]
    mapping_input_vector = mapping.inputs["Vector"]
    links.new(texture_coord_output_uv, mapping_input_vector)
    
    
    return nodes_list


def cambiar_valor_de_difuminacion_agua_a(valor):
    
    cube = bpy.context.object
    
    if cube is None:
        print("No hay un objeto seleccionado.")
        return {'CANCELLED'}
    
   
    if not cube.data.materials:
        print("El objeto no tiene materiales.")
        return {'CANCELLED'}
    
    material = cube.data.materials.get("Collage")
    if material is None:
        print("El material 'Collage' no existe en el objeto.")
        return {'CANCELLED'}
    
    nodes = material.node_tree.nodes
    node = nodes.get("Mapping")
    if node is None:
        print(f"El nodo '{node}' no existe en el material.")
        return {'CANCELLED'}
    
    input = node.inputs.get("Rotation")
    if input is None:
        print(f"La entrada '{input}' no existe en el nodo '{node.name}'.")
        return {'CANCELLED'}
    
    input.default_value = Euler(valor, input[1], input[2], 'XYZ')
    
    print(f"Valor de '{input}' en el nodo '{node.name}' cambiado a {valor}.")

    return {'FINISHED'}
    
def cambiar_valor_de_difuminacion_agua(input_letter, valor):
    
    cube = bpy.context.object
    
    if cube is None:
        print("No hay un objeto seleccionado.")
        return {'CANCELLED'}
    
   
    if not cube.data.materials:
        print("El objeto no tiene materiales.")
        return {'CANCELLED'}
    
    material = cube.data.materials.get("Collage")
    if material is None:
        print("El material 'Collage' no existe en el objeto.")
        return {'CANCELLED'}
    
    nodes = material.node_tree.nodes
    node = nodes.get("Mapping")
    if node is None:
        print(f"El nodo '{node}' no existe en el material.")
        return {'CANCELLED'}
    
    input = node.inputs.get("Rotation")
    if input is None:
        print(f"La entrada '{input}' no existe en el nodo '{node.name}'.")
        return {'CANCELLED'}
    if input_letter == "A":
        input.default_value = Euler(valor, input[1], input[2], 'XYZ')
    if input_letter == "B":
        input.default_value = Euler(input[0], valor, input[2], 'XYZ')
    
    print(f"Valor de '{input}' en el nodo '{node.name}' cambiado a {valor}.")

    return {'FINISHED'}
    

def cambiar_valor_rgb(nodo, valor):
    return {'FINISHED'}