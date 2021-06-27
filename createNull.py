import hou

aNode = hou.selectedNodes()[0]
null = aNode.createOutputNode('null', 'OUT_{0}'.format(aNode.name()))
