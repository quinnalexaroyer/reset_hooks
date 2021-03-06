# You may want to run reset_pose.py first to clear transforms on the armature bones before running this script.

import bpy

for o in bpy.data.objects:
	bpy.context.view_layer.objects.active = o
	if o.type == "MESH":
		print(o)
		bpy.ops.object.mode_set(mode="EDIT")
		for i in o.modifiers:
			if i.type == "HOOK":
				bpy.ops.object.hook_reset(modifier=i.name)
		bpy.ops.object.mode_set(mode="OBJECT")
