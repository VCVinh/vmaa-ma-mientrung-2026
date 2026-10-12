"""
VMAA M&A MIỀN TRUNG 2026 — "ARCHITECTURE OF VALUE"
Deterministic Blender 4.2+ Procedural Scene & 4-Shot Camera Rig Generator
Licence: MIT / GPL-compatible open-source pipeline script
Run inside Blender:
    blender --background --python blender_architecture_of_value.py
or open in Blender Scripting workspace and click Run Script.
"""

import bpy
import math

def clear_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)

def setup_render_settings():
    scene = bpy.context.scene
    scene.render.engine = 'CYCLES'
    scene.cycles.samples = 128
    scene.cycles.use_denoising = True
    scene.render.resolution_x = 3840
    scene.render.resolution_y = 2160
    scene.render.fps = 60
    scene.frame_start = 1
    scene.frame_end = 1320  # 22.0 seconds @ 60fps

    # OpenColorIO AgX high-contrast institutional look
    try:
        scene.view_settings.view_transform = 'AgX'
        scene.view_settings.look = 'AgX - High Contrast'
    except Exception:
        pass

    # World background: Deep Obsidian (#070D20)
    world = bpy.data.worlds.new("VMAA_Obsidian_World")
    scene.world = world
    world.use_nodes = True
    bg_node = world.node_tree.nodes.get("Background")
    if bg_node:
        bg_node.inputs[0].default_value = (0.002, 0.004, 0.014, 1.0)  # Linear #070D20
        bg_node.inputs[1].default_value = 0.8

def create_materials():
    # 1. Brushed Obsidian Architectural Material (#070D20 / #101F45)
    mat_obs = bpy.data.materials.new(name="VMAA_Obsidian_Architecture")
    mat_obs.use_nodes = True
    bsdf = mat_obs.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (0.005, 0.012, 0.038, 1.0)
    bsdf.inputs["Metallic"].default_value = 0.82
    bsdf.inputs["Roughness"].default_value = 0.24

    # 2. Translucent Cobalt Glass Material (#245BFF)
    mat_glass = bpy.data.materials.new(name="VMAA_Cobalt_Fluted_Glass")
    mat_glass.use_nodes = True
    bsdf_g = mat_glass.node_tree.nodes.get("Principled BSDF")
    bsdf_g.inputs["Base Color"].default_value = (0.018, 0.105, 1.0, 1.0)
    bsdf_g.inputs["Roughness"].default_value = 0.08
    bsdf_g.inputs["IOR"].default_value = 1.52
    if "Transmission Weight" in bsdf_g.inputs:
        bsdf_g.inputs["Transmission Weight"].default_value = 0.88
    elif "Transmission" in bsdf_g.inputs:
        bsdf_g.inputs["Transmission"].default_value = 0.88

    # 3. Luminous Ice-Blue Data Filament Material (#63B4FF)
    mat_ice = bpy.data.materials.new(name="VMAA_IceBlue_Filament")
    mat_ice.use_nodes = True
    bsdf_i = mat_ice.node_tree.nodes.get("Principled BSDF")
    bsdf_i.inputs["Base Color"].default_value = (0.125, 0.45, 1.0, 1.0)
    if "Emission Color" in bsdf_i.inputs:
        bsdf_i.inputs["Emission Color"].default_value = (0.125, 0.45, 1.0, 1.0)
        bsdf_i.inputs["Emission Strength"].default_value = 6.5

    return mat_obs, mat_glass, mat_ice

def build_modular_architecture(mat_obs, mat_glass, mat_ice):
    # Specs: (name, size_xyz, start_loc_f1, aligned_loc_f850, is_glass)
    specs = [
        ("Core_Cobalt_Monolith", (1.5, 1.5, 5.6), (3.4, 5.0, 0.0), (3.4, 0.0, 0.0), True),
        ("Core_Cap_Upper",       (1.5, 1.5, 2.2), (3.4, 2.0, 7.8), (3.4, 0.0, 4.1), False),
        ("Core_Base_Lower",      (1.5, 1.5, 2.2), (3.4, -2.5, -7.8), (3.4, 0.0, -4.1), False),
        ("Wing_RealEstate_L1",   (1.2, 1.2, 4.2), (-3.8, 3.0, -2.2), (1.75, 0.4, -0.7), False),
        ("Wing_TechGlass_L2",    (1.2, 1.2, 1.8), (-2.5, -3.2, 5.0), (1.75, 0.4, 2.5), True),
        ("Wing_RealEstate_R1",   (1.3, 1.3, 3.8), (9.5, 4.0, 2.4), (5.05, 0.3, 0.4), False),
        ("Wing_TechGlass_R2",    (1.3, 1.3, 2.4), (8.2, -2.5, -5.5), (5.05, 0.3, -2.9), True),
        ("Horizontal_Bridge_U",  (2.2, 2.2, 0.7), (7.5, -4.0, 5.8), (3.4, -0.5, 2.85), True),
        ("Horizontal_Bridge_L",  (2.2, 2.2, 0.7), (-1.5, 4.0, -5.8), (3.4, -0.5, -2.85), True),
    ]

    for name, dims, start_pos, end_pos, is_glass in specs:
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=start_pos)
        obj = bpy.context.active_object
        obj.name = name
        obj.scale = (dims[0], dims[1], dims[2])
        obj.data.materials.append(mat_glass if is_glass else mat_obs)

        # Keyframe Scene 1 -> Scene 3 M&A Structural Alignment (Frame 120 to Frame 852 / 14.2s)
        obj.location = start_pos
        obj.keyframe_insert(data_path="location", frame=120)
        obj.location = end_pos
        obj.keyframe_insert(data_path="location", frame=852)

def setup_lighting_and_camera():
    # Cobalt Key Area Light
    bpy.ops.object.light_add(type='AREA', location=(8.0, -10.0, 12.0))
    key_light = bpy.context.active_object
    key_light.name = "VMAA_Cobalt_KeyLight"
    key_light.data.energy = 1800.0
    key_light.data.color = (0.14, 0.36, 1.0)
    key_light.data.size = 6.0

    # Ice-Blue Rim Light
    bpy.ops.object.light_add(type='AREA', location=(-6.0, 6.0, 8.0))
    rim_light = bpy.context.active_object
    rim_light.name = "VMAA_IceBlue_RimLight"
    rim_light.data.energy = 950.0
    rim_light.data.color = (0.39, 0.71, 1.0)
    rim_light.data.size = 4.0

    # 4-Scene Camera Choreography (50mm Architectural Lens)
    bpy.ops.object.camera_add(location=(0.0, -16.5, 1.8), rotation=(math.radians(86), 0.0, 0.0))
    cam = bpy.context.active_object
    cam.name = "VMAA_Opener_Camera"
    cam.data.lens = 50.0
    bpy.context.scene.camera = cam

    # Scene 1 (0-4s / f1-f240): Establish the World
    cam.location = (0.0, -16.5, 1.8)
    cam.keyframe_insert(data_path="location", frame=1)
    cam.location = (0.0, -13.5, 1.2)
    cam.keyframe_insert(data_path="location", frame=240)

    # Scene 2 (4-10s / f240-f600): Reveal the Connection
    cam.location = (0.8, -11.4, 0.6)
    cam.keyframe_insert(data_path="location", frame=600)

    # Scene 3 (10-16s / f600-f960): Transform into Unified System
    cam.location = (0.0, -9.8, 0.2)
    cam.keyframe_insert(data_path="location", frame=960)

    # Scene 4 (16-22s / f960-f1320): Locked Brand Reveal Hold (6.0 seconds stillness)
    cam.location = (0.0, -9.8, 0.2)
    cam.keyframe_insert(data_path="location", frame=1320)

if __name__ == "__main__":
    clear_scene()
    setup_render_settings()
    m_obs, m_glass, m_ice = create_materials()
    build_modular_architecture(m_obs, m_glass, m_ice)
    setup_lighting_and_camera()
    print("VMAA M&A Miền Trung 2026 — 'Architecture of Value' Blender 4.2 scene generated successfully.")
