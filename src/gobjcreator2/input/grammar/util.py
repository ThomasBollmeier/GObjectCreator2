#! coding=UTF-8

def addChild(origin, newParent, ident, clearId=True):
    
    node = origin.getChildById(ident)
    if clearId:
        node.setId('')
    newParent.addChild(node)
        
def addOptionalChild(origin, newParent, ident, clearId=True):
    
    node = origin.getChildById(ident)
    if node:
        if clearId:
            node.setId('')
        newParent.addChild(node)
        
def addOptionalChildren(origin, newParent, ident, clearId=True):
    
    for node in origin.getChildrenById(ident): 
        if clearId:
            node.setId('')
        newParent.addChild(node)
