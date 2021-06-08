node = hou.pwd()
geo = node.geometry()

import os
nodes = hou.selectedNodes()
nodes = [n for n in nodes if 'sphere' in n.type().name()]

for n in nodes:
    parm = n.parm('scale')
    parm.set(0.2)
    
    n.setName('foo', unique_name=True)
