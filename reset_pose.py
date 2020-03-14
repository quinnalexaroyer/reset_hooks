# This file resets the pose of all armatures whose name ends in ".arm".

import bpy

for i in bpy.data.objects:
	if i.name[-4:] == ".arm":
		bpy.context.view_layer.objects.active = i
		bpy.ops.object.mode_set(mode="POSE")
		bpy.ops.pose.select_all(action="SELECT")
		bpy.ops.pose.rot_clear()
		bpy.ops.pose.scale_clear()
		bpy.ops.pose.transforms_clear()
		bpy.ops.object.mode_set(mode="OBJECT")
