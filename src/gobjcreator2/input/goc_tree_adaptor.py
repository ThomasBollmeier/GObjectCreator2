from antlr3.tree import CommonTreeAdaptor, CommonTree, CommonToken

class GOCTreeAdaptor(CommonTreeAdaptor):
    
    def __init__(self):
        
        CommonTreeAdaptor.__init__(self)
        self._curr_goc_file = ""
        
    def set_goc_file_path(self, path):
        
        self._curr_goc_file = path
        
    def dupNode(self, treeNode):
        
        if treeNode is None:
            return None
        
        return treeNode.dupNode()
        
    def createWithPayload(self, payload):
        
        return GOCNode(payload, self._curr_goc_file)

    def createToken(self, fromToken=None, tokenType=None, text=None):
        """
        Tell me how to create a token for use with imaginary token nodes.
        For example, there is probably no input symbol associated with imaginary
        token DECL, but you need to create it as a payload or whatever for
        the DECL node as in ^(DECL type ID).

        If you care what the token payload objects' type is, you should
        override this method and any other createToken variant.
        """
        
        if fromToken is not None:
            return CommonToken(oldToken=fromToken)

        return CommonToken(type=tokenType, text=text)

class GOCNode(CommonTree):
    
    def __init__(self, payload, goc_file_path):
        
        CommonTree.__init__(self, payload)
        self._goc_file_path = goc_file_path
        
    def _get_goc_file_path(self):
        
        return self._goc_file_path
    
    goc_file_path = property(_get_goc_file_path)
        