import hou

def get_value(value):
    values = []
    node = hou.selectedNodes()[0]
    geo = node.geometry()

    for p in geo.points():
        values.append(p.attribValue('{}'.join(value)))
        return values
    
