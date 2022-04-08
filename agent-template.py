import hou

OBJ = hou.node('/obj')

geometry = OBJ.createNode('geo', 'name')
selectedNode = hou.selectedNodes()[0]

print("".join(selectedNode.path()))

sphere_node = geometry.createNode('sphere', 'mySphere')
xform_node = sphere_node.createOutputNode('xform', 'myXform')
agent_node = xform_node.createOutputNode('agent', 'myAgent')
agent_node.setParms({"agentname":"Hans", "currentclip":"walk", "objsubnet":"".join(selectedNode.path())})

agent_node.setDisplayFlag(True)
