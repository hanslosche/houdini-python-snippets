import hou

approvedCategories = ['Sop', 'Driver', 'Cop2', 'Chop', 'Vop', 'Object', 'Dop']

if hou.selectedNodes():
    node = hou.selectedNodes()[0]
curCategory = node.type().category().name()
print curCategory

if curCategory in approvedCategories:
    print ("Houdini Level Detected: {}").format(curCategory)
else:
    print "No Valid"
