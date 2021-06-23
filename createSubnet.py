import hou

def create_main_subnet():
    subnet_node = hou.node('/obj').createNode('subnet', 'extract_animation')
    subnet_node.moveToGoodPosition()
    return subnet_node


def create_divide_into_parts_geo_node(parent_node):
    divide_geo_node = parent_node.createNode('geo', 'divide_into_parts')
    divide_geo_node.moveToGoodPosition()
    return divide_geo_node
    
    
subnet = create_main_subnet()
divide_node = create_divide_into_parts_geo_node(subnet)
