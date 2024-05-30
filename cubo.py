import bpy

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

mesh = bpy.data.meshes.new(name="CubeMesh")
obj = bpy.data.objects.new(name="Cube", object_data=mesh)

scene = bpy.context.scene
scene.collection.objects.link(obj)

vertices = [
    (-1, -1, -1),
    ( 1, -1, -1),
    ( 1,  1, -1),
    (-1,  1, -1),
    (-1, -1,  1),
    ( 1, -1,  1),
    ( 1,  1,  1),
    (-1,  1,  1)
]

faces = [
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (0, 1, 5, 4),
    (1, 2, 6, 5),
    (2, 3, 7, 6),
    (3, 0, 4, 7)
]

mesh.from_pydata(vertices, [], faces)
mesh.update()

bpy.context.view_layer.objects.active = obj
obj.select_set(True)
