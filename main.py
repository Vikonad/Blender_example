import bpy

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

mesh = bpy.data.meshes.new(name="SquareMesh")
obj = bpy.data.objects.new(name="Square", object_data=mesh)

scene = bpy.context.scene
scene.collection.objects.link(obj)

vertices = [
    (-1, -1, 0), # Vertice 1
    ( 1, -1, 0), # Vertice 2
    ( 1,  1, 0), # Vertice 3
    (-1,  1, 0)  # Vertice 4
]

faces = [
    (0, 1, 2, 3) # Faccia che unisce i quattro vertici
]

mesh.from_pydata(vertices, [], faces)
mesh.update()

bpy.context.view_layer.objects.active = obj
obj.select_set(True)
