import hou 


obj = hou.node('/obj')
geometry = obj.createNode('geo', 'crowd_source')

agent1 = hou.selectedNodes()[0]
agent2 = hou.selectedNodes()[1]


agent_node = geometry.createNode('agent', 'myAgent')
agent_node.setParms({'agentname':'human_test', 'clipname':'Rest', 'currentclip':'Rest', 'objsubnet': ''.join(agent1.path())})

agentclip_node = agent_node.createOutputNode('agentclip::2.0', 'agentclip_walk')
agentclip_node.setParms({'name1':'Walk','setcurrentclip':'1', 'currentclip':'Walk', 'objsubnet1':  ''.join(agent2.path())})


agentclip_node.setDisplayFlag(True)
agentclip_node.setRenderFlag(True)
