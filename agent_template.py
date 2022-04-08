import hou

NAME = 'crowd_setup'

#aNode = hou.selectedNodes()[0]

geo_node = hou.node('/obj/' + NAME)

if not geo_node:
   #obj_path = hou.node('/obj')
    geo_node = hou.node('/obj').createNode('geo', NAME)
    #null_node = geo_node.createNode('sphere', 'AGENT')
    agent_node = geo_node.createNode('agent', 'agent')
    agent_node_parm = agent_node.parm('objsubnet')
    agent_node_parm.set('Hi Hans')
    agentclip_node = agent_node.createOutputNode('agentclip::2.0')
    
