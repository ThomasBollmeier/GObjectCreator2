#! coding=UTF-8

from tbparser.parser import Parser
from gobjcreator2.input.grammar.goc_grammar import GOCGrammar

class GOCParser(Parser):
    
    def __init__(self):
        
        Parser.__init__(self, GOCGrammar())
        
        self.enableLineComments()
        self.enableBlockComments()
