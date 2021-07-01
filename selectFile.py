import hou

obj_dir = hou.ui.selectFile()
obj_path = hou.expandString(obj_dir)


print obj_path
