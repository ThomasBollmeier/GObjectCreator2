# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 GOC.g 2011-03-20 19:20:48

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
PACKAGE=51
PREFIX=30
GTYPENAME=46
PROP_ACCESS=11
PROP_DEFAULT=16
GTYPE=27
OCTAL_ESC=55
EOF=-1
INHERITANCE=42
TYPE=36
T__93=93
T__94=94
T__91=91
T__92=92
T__90=90
ENUMERATION=24
INCLUDE=5
PARAMETER=43
SUPER=28
COMMENT=48
GOBJECT=21
T__97=97
T__96=96
T__95=95
T__80=80
T__81=81
REF_TO=8
VISIBILITY=40
T__82=82
BOOLVALUE=50
T__83=83
GINTERFACE=22
INT=25
T__85=85
T__84=84
T__87=87
T__86=86
T__89=89
T__88=88
T__71=71
WS=49
T__72=72
T__70=70
PROPERTY=37
T__76=76
T__75=75
T__74=74
T__73=73
CONSTRUCTOR=32
T__79=79
T__78=78
T__77=77
T__68=68
T__69=69
T__66=66
T__67=67
T__64=64
T__65=65
T__62=62
T__63=63
LIST_OF=9
FLAGS=26
SIGNAL_ID=7
PROP_DESC=12
ATTRIBUTE=35
ABSTRACT=29
INIT_PROPERTIES=44
T__61=61
ID=20
T__60=60
MODIFIERS=45
T__56=56
T__57=57
T__58=58
ESC_SEQ=52
IMPLEMENTS=31
SCOPE=41
T__59=59
SIGNAL=38
TYPE_NAME=6
PROP_TYPE=10
AUTO_CREATE=47
ERROR_DOMAIN=23
PROP_MIN=14
INIT_PROPERTY=18
UNICODE_ESC=54
HEX_DIGIT=53
RESULT=39
ROOT=4
BIND_PROPERTY=17
PROP_MAX=15
OVERRIDE=34
PROP_GTYPE=13
METHOD=33
STRING=19

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ROOT", "INCLUDE", "TYPE_NAME", "SIGNAL_ID", "REF_TO", "LIST_OF", "PROP_TYPE", 
    "PROP_ACCESS", "PROP_DESC", "PROP_GTYPE", "PROP_MIN", "PROP_MAX", "PROP_DEFAULT", 
    "BIND_PROPERTY", "INIT_PROPERTY", "STRING", "ID", "GOBJECT", "GINTERFACE", 
    "ERROR_DOMAIN", "ENUMERATION", "INT", "FLAGS", "GTYPE", "SUPER", "ABSTRACT", 
    "PREFIX", "IMPLEMENTS", "CONSTRUCTOR", "METHOD", "OVERRIDE", "ATTRIBUTE", 
    "TYPE", "PROPERTY", "SIGNAL", "RESULT", "VISIBILITY", "SCOPE", "INHERITANCE", 
    "PARAMETER", "INIT_PROPERTIES", "MODIFIERS", "GTYPENAME", "AUTO_CREATE", 
    "COMMENT", "WS", "BOOLVALUE", "PACKAGE", "ESC_SEQ", "HEX_DIGIT", "UNICODE_ESC", 
    "OCTAL_ESC", "'include'", "'{'", "'}'", "';'", "'code'", "'value'", 
    "':'", "'public'", "'protected'", "'private'", "'instance'", "'static'", 
    "'final'", "'virtual'", "'bind_property'", "'.'", "'const'", "'boolean'", 
    "'integer'", "'float'", "'double'", "'string'", "'pointer'", "'object'", 
    "'enumeration'", "'access'", "'read-only'", "'initial-write'", "'read-write'", 
    "'description'", "'('", "')'", "'min'", "'max'", "'default'", "'unsigned '", 
    "'long'", "'null'", "'ref'", "'list'", "'::'", "'-'"
]



class classMember_scope(object):
    def __init__(self):
        self.with_constructor = None


class GOCParser(Parser):
    grammarFileName = "GOC.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(GOCParser, self).__init__(input, state, *args, **kwargs)

        self.dfa34 = self.DFA34(
            self, 34,
            eot = self.DFA34_eot,
            eof = self.DFA34_eof,
            min = self.DFA34_min,
            max = self.DFA34_max,
            accept = self.DFA34_accept,
            special = self.DFA34_special,
            transition = self.DFA34_transition
            )


	self.classMember_stack = []





        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class defFile_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.defFile_return, self).__init__()

            self.tree = None




    # $ANTLR start "defFile"
    # GOC.g:26:1: defFile : ( stmt )* -> ^( ROOT ( stmt )* ) ;
    def defFile(self, ):

        retval = self.defFile_return()
        retval.start = self.input.LT(1)

        root_0 = None

        stmt1 = None


        stream_stmt = RewriteRuleSubtreeStream(self._adaptor, "rule stmt")
        try:
            try:
                # GOC.g:27:2: ( ( stmt )* -> ^( ROOT ( stmt )* ) )
                # GOC.g:27:5: ( stmt )*
                pass 
                # GOC.g:27:5: ( stmt )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((GOBJECT <= LA1_0 <= ENUMERATION) or (FLAGS <= LA1_0 <= GTYPE) or LA1_0 == PACKAGE or LA1_0 == 56) :
                        alt1 = 1


                    if alt1 == 1:
                        # GOC.g:27:5: stmt
                        pass 
                        self._state.following.append(self.FOLLOW_stmt_in_defFile143)
                        stmt1 = self.stmt()

                        self._state.following.pop()
                        stream_stmt.add(stmt1.tree)


                    else:
                        break #loop1

                # AST Rewrite
                # elements: stmt
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 27:11: -> ^( ROOT ( stmt )* )
                # GOC.g:27:14: ^( ROOT ( stmt )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ROOT, "ROOT"), root_1)

                # GOC.g:27:21: ( stmt )*
                while stream_stmt.hasNext():
                    self._adaptor.addChild(root_1, stream_stmt.nextTree())


                stream_stmt.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "defFile"

    class stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.stmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "stmt"
    # GOC.g:30:1: stmt : ( classDef | intfDef | errorDomainDef | enumDef | flagsDef | packageDef | typeDecl | includeStmt );
    def stmt(self, ):

        retval = self.stmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        classDef2 = None

        intfDef3 = None

        errorDomainDef4 = None

        enumDef5 = None

        flagsDef6 = None

        packageDef7 = None

        typeDecl8 = None

        includeStmt9 = None



        try:
            try:
                # GOC.g:31:2: ( classDef | intfDef | errorDomainDef | enumDef | flagsDef | packageDef | typeDecl | includeStmt )
                alt2 = 8
                LA2 = self.input.LA(1)
                if LA2 == GOBJECT:
                    alt2 = 1
                elif LA2 == GINTERFACE:
                    alt2 = 2
                elif LA2 == ERROR_DOMAIN:
                    alt2 = 3
                elif LA2 == ENUMERATION:
                    alt2 = 4
                elif LA2 == FLAGS:
                    alt2 = 5
                elif LA2 == PACKAGE:
                    alt2 = 6
                elif LA2 == GTYPE:
                    alt2 = 7
                elif LA2 == 56:
                    alt2 = 8
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # GOC.g:31:4: classDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_classDef_in_stmt165)
                    classDef2 = self.classDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, classDef2.tree)


                elif alt2 == 2:
                    # GOC.g:32:4: intfDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_intfDef_in_stmt170)
                    intfDef3 = self.intfDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, intfDef3.tree)


                elif alt2 == 3:
                    # GOC.g:33:6: errorDomainDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_errorDomainDef_in_stmt177)
                    errorDomainDef4 = self.errorDomainDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, errorDomainDef4.tree)


                elif alt2 == 4:
                    # GOC.g:34:6: enumDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_enumDef_in_stmt184)
                    enumDef5 = self.enumDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, enumDef5.tree)


                elif alt2 == 5:
                    # GOC.g:35:6: flagsDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_flagsDef_in_stmt191)
                    flagsDef6 = self.flagsDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, flagsDef6.tree)


                elif alt2 == 6:
                    # GOC.g:36:4: packageDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_packageDef_in_stmt196)
                    packageDef7 = self.packageDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, packageDef7.tree)


                elif alt2 == 7:
                    # GOC.g:37:6: typeDecl
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_typeDecl_in_stmt203)
                    typeDecl8 = self.typeDecl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, typeDecl8.tree)


                elif alt2 == 8:
                    # GOC.g:38:6: includeStmt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_includeStmt_in_stmt210)
                    includeStmt9 = self.includeStmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, includeStmt9.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "stmt"

    class includeStmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.includeStmt_return, self).__init__()

            self.tree = None




    # $ANTLR start "includeStmt"
    # GOC.g:41:1: includeStmt : 'include' path= STRING -> ^( INCLUDE $path) ;
    def includeStmt(self, ):

        retval = self.includeStmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        path = None
        string_literal10 = None

        path_tree = None
        string_literal10_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")

        try:
            try:
                # GOC.g:42:5: ( 'include' path= STRING -> ^( INCLUDE $path) )
                # GOC.g:42:9: 'include' path= STRING
                pass 
                string_literal10=self.match(self.input, 56, self.FOLLOW_56_in_includeStmt226) 
                stream_56.add(string_literal10)
                path=self.match(self.input, STRING, self.FOLLOW_STRING_in_includeStmt230) 
                stream_STRING.add(path)

                # AST Rewrite
                # elements: path
                # token labels: path
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0
                stream_path = RewriteRuleTokenStream(self._adaptor, "token path", path)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 42:31: -> ^( INCLUDE $path)
                # GOC.g:42:34: ^( INCLUDE $path)
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(INCLUDE, "INCLUDE"), root_1)

                self._adaptor.addChild(root_1, stream_path.nextNode())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "includeStmt"

    class packageDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.packageDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "packageDef"
    # GOC.g:45:1: packageDef : 'package' ID '{' ( packageElement )* '}' -> ^( 'package' ID ( packageElement )* ) ;
    def packageDef(self, ):

        retval = self.packageDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal11 = None
        ID12 = None
        char_literal13 = None
        char_literal15 = None
        packageElement14 = None


        string_literal11_tree = None
        ID12_tree = None
        char_literal13_tree = None
        char_literal15_tree = None
        stream_PACKAGE = RewriteRuleTokenStream(self._adaptor, "token PACKAGE")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_packageElement = RewriteRuleSubtreeStream(self._adaptor, "rule packageElement")
        try:
            try:
                # GOC.g:46:2: ( 'package' ID '{' ( packageElement )* '}' -> ^( 'package' ID ( packageElement )* ) )
                # GOC.g:46:4: 'package' ID '{' ( packageElement )* '}'
                pass 
                string_literal11=self.match(self.input, PACKAGE, self.FOLLOW_PACKAGE_in_packageDef253) 
                stream_PACKAGE.add(string_literal11)
                ID12=self.match(self.input, ID, self.FOLLOW_ID_in_packageDef255) 
                stream_ID.add(ID12)
                char_literal13=self.match(self.input, 57, self.FOLLOW_57_in_packageDef257) 
                stream_57.add(char_literal13)
                # GOC.g:46:21: ( packageElement )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((GOBJECT <= LA3_0 <= ENUMERATION) or (FLAGS <= LA3_0 <= GTYPE) or LA3_0 == PACKAGE) :
                        alt3 = 1


                    if alt3 == 1:
                        # GOC.g:46:21: packageElement
                        pass 
                        self._state.following.append(self.FOLLOW_packageElement_in_packageDef259)
                        packageElement14 = self.packageElement()

                        self._state.following.pop()
                        stream_packageElement.add(packageElement14.tree)


                    else:
                        break #loop3
                char_literal15=self.match(self.input, 58, self.FOLLOW_58_in_packageDef262) 
                stream_58.add(char_literal15)

                # AST Rewrite
                # elements: PACKAGE, packageElement, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 47:2: -> ^( 'package' ID ( packageElement )* )
                # GOC.g:47:6: ^( 'package' ID ( packageElement )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_PACKAGE.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_ID.nextNode())
                # GOC.g:47:21: ( packageElement )*
                while stream_packageElement.hasNext():
                    self._adaptor.addChild(root_1, stream_packageElement.nextTree())


                stream_packageElement.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "packageDef"

    class packageElement_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.packageElement_return, self).__init__()

            self.tree = None




    # $ANTLR start "packageElement"
    # GOC.g:50:1: packageElement : ( packageDef | classDef | intfDef | errorDomainDef | enumDef | flagsDef | typeDecl );
    def packageElement(self, ):

        retval = self.packageElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        packageDef16 = None

        classDef17 = None

        intfDef18 = None

        errorDomainDef19 = None

        enumDef20 = None

        flagsDef21 = None

        typeDecl22 = None



        try:
            try:
                # GOC.g:51:2: ( packageDef | classDef | intfDef | errorDomainDef | enumDef | flagsDef | typeDecl )
                alt4 = 7
                LA4 = self.input.LA(1)
                if LA4 == PACKAGE:
                    alt4 = 1
                elif LA4 == GOBJECT:
                    alt4 = 2
                elif LA4 == GINTERFACE:
                    alt4 = 3
                elif LA4 == ERROR_DOMAIN:
                    alt4 = 4
                elif LA4 == ENUMERATION:
                    alt4 = 5
                elif LA4 == FLAGS:
                    alt4 = 6
                elif LA4 == GTYPE:
                    alt4 = 7
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # GOC.g:51:4: packageDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_packageDef_in_packageElement287)
                    packageDef16 = self.packageDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, packageDef16.tree)


                elif alt4 == 2:
                    # GOC.g:52:4: classDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_classDef_in_packageElement292)
                    classDef17 = self.classDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, classDef17.tree)


                elif alt4 == 3:
                    # GOC.g:53:4: intfDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_intfDef_in_packageElement297)
                    intfDef18 = self.intfDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, intfDef18.tree)


                elif alt4 == 4:
                    # GOC.g:54:6: errorDomainDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_errorDomainDef_in_packageElement304)
                    errorDomainDef19 = self.errorDomainDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, errorDomainDef19.tree)


                elif alt4 == 5:
                    # GOC.g:55:6: enumDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_enumDef_in_packageElement311)
                    enumDef20 = self.enumDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, enumDef20.tree)


                elif alt4 == 6:
                    # GOC.g:56:6: flagsDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_flagsDef_in_packageElement318)
                    flagsDef21 = self.flagsDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, flagsDef21.tree)


                elif alt4 == 7:
                    # GOC.g:57:6: typeDecl
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_typeDecl_in_packageElement325)
                    typeDecl22 = self.typeDecl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, typeDecl22.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "packageElement"

    class classDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.classDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "classDef"
    # GOC.g:60:1: classDef : GOBJECT className= ID ( '{' ( classMember )* '}' | ';' ) -> ^( GOBJECT $className ( classMember )* ) ;
    def classDef(self, ):

        retval = self.classDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        className = None
        GOBJECT23 = None
        char_literal24 = None
        char_literal26 = None
        char_literal27 = None
        classMember25 = None


        className_tree = None
        GOBJECT23_tree = None
        char_literal24_tree = None
        char_literal26_tree = None
        char_literal27_tree = None
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_GOBJECT = RewriteRuleTokenStream(self._adaptor, "token GOBJECT")
        stream_classMember = RewriteRuleSubtreeStream(self._adaptor, "rule classMember")
        try:
            try:
                # GOC.g:61:2: ( GOBJECT className= ID ( '{' ( classMember )* '}' | ';' ) -> ^( GOBJECT $className ( classMember )* ) )
                # GOC.g:61:4: GOBJECT className= ID ( '{' ( classMember )* '}' | ';' )
                pass 
                GOBJECT23=self.match(self.input, GOBJECT, self.FOLLOW_GOBJECT_in_classDef336) 
                stream_GOBJECT.add(GOBJECT23)
                className=self.match(self.input, ID, self.FOLLOW_ID_in_classDef340) 
                stream_ID.add(className)
                # GOC.g:61:25: ( '{' ( classMember )* '}' | ';' )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 57) :
                    alt6 = 1
                elif (LA6_0 == 59) :
                    alt6 = 2
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # GOC.g:61:26: '{' ( classMember )* '}'
                    pass 
                    char_literal24=self.match(self.input, 57, self.FOLLOW_57_in_classDef343) 
                    stream_57.add(char_literal24)
                    # GOC.g:61:30: ( classMember )*
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if ((SUPER <= LA5_0 <= ATTRIBUTE) or (PROPERTY <= LA5_0 <= SIGNAL)) :
                            alt5 = 1


                        if alt5 == 1:
                            # GOC.g:61:30: classMember
                            pass 
                            self._state.following.append(self.FOLLOW_classMember_in_classDef345)
                            classMember25 = self.classMember()

                            self._state.following.pop()
                            stream_classMember.add(classMember25.tree)


                        else:
                            break #loop5
                    char_literal26=self.match(self.input, 58, self.FOLLOW_58_in_classDef348) 
                    stream_58.add(char_literal26)


                elif alt6 == 2:
                    # GOC.g:61:47: ';'
                    pass 
                    char_literal27=self.match(self.input, 59, self.FOLLOW_59_in_classDef350) 
                    stream_59.add(char_literal27)




                # AST Rewrite
                # elements: className, classMember, GOBJECT
                # token labels: className
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0
                stream_className = RewriteRuleTokenStream(self._adaptor, "token className", className)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 62:2: -> ^( GOBJECT $className ( classMember )* )
                # GOC.g:62:5: ^( GOBJECT $className ( classMember )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_GOBJECT.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_className.nextNode())
                # GOC.g:62:26: ( classMember )*
                while stream_classMember.hasNext():
                    self._adaptor.addChild(root_1, stream_classMember.nextTree())


                stream_classMember.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "classDef"

    class intfDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.intfDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "intfDef"
    # GOC.g:65:1: intfDef : GINTERFACE intfName= ID ( '{' ( intfMember )* '}' | ';' ) -> ^( GINTERFACE $intfName ( intfMember )* ) ;
    def intfDef(self, ):

        retval = self.intfDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        intfName = None
        GINTERFACE28 = None
        char_literal29 = None
        char_literal31 = None
        char_literal32 = None
        intfMember30 = None


        intfName_tree = None
        GINTERFACE28_tree = None
        char_literal29_tree = None
        char_literal31_tree = None
        char_literal32_tree = None
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_GINTERFACE = RewriteRuleTokenStream(self._adaptor, "token GINTERFACE")
        stream_intfMember = RewriteRuleSubtreeStream(self._adaptor, "rule intfMember")
        try:
            try:
                # GOC.g:66:2: ( GINTERFACE intfName= ID ( '{' ( intfMember )* '}' | ';' ) -> ^( GINTERFACE $intfName ( intfMember )* ) )
                # GOC.g:66:4: GINTERFACE intfName= ID ( '{' ( intfMember )* '}' | ';' )
                pass 
                GINTERFACE28=self.match(self.input, GINTERFACE, self.FOLLOW_GINTERFACE_in_intfDef377) 
                stream_GINTERFACE.add(GINTERFACE28)
                intfName=self.match(self.input, ID, self.FOLLOW_ID_in_intfDef381) 
                stream_ID.add(intfName)
                # GOC.g:66:27: ( '{' ( intfMember )* '}' | ';' )
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == 57) :
                    alt8 = 1
                elif (LA8_0 == 59) :
                    alt8 = 2
                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # GOC.g:66:28: '{' ( intfMember )* '}'
                    pass 
                    char_literal29=self.match(self.input, 57, self.FOLLOW_57_in_intfDef384) 
                    stream_57.add(char_literal29)
                    # GOC.g:66:32: ( intfMember )*
                    while True: #loop7
                        alt7 = 2
                        LA7_0 = self.input.LA(1)

                        if (LA7_0 == PREFIX or LA7_0 == METHOD or LA7_0 == SIGNAL) :
                            alt7 = 1


                        if alt7 == 1:
                            # GOC.g:66:32: intfMember
                            pass 
                            self._state.following.append(self.FOLLOW_intfMember_in_intfDef386)
                            intfMember30 = self.intfMember()

                            self._state.following.pop()
                            stream_intfMember.add(intfMember30.tree)


                        else:
                            break #loop7
                    char_literal31=self.match(self.input, 58, self.FOLLOW_58_in_intfDef389) 
                    stream_58.add(char_literal31)


                elif alt8 == 2:
                    # GOC.g:66:48: ';'
                    pass 
                    char_literal32=self.match(self.input, 59, self.FOLLOW_59_in_intfDef391) 
                    stream_59.add(char_literal32)




                # AST Rewrite
                # elements: intfName, intfMember, GINTERFACE
                # token labels: intfName
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0
                stream_intfName = RewriteRuleTokenStream(self._adaptor, "token intfName", intfName)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 67:2: -> ^( GINTERFACE $intfName ( intfMember )* )
                # GOC.g:67:5: ^( GINTERFACE $intfName ( intfMember )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_GINTERFACE.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_intfName.nextNode())
                # GOC.g:67:28: ( intfMember )*
                while stream_intfMember.hasNext():
                    self._adaptor.addChild(root_1, stream_intfMember.nextTree())


                stream_intfMember.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "intfDef"

    class errorDomainDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.errorDomainDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "errorDomainDef"
    # GOC.g:70:1: errorDomainDef : ERROR_DOMAIN ID '{' ( errorDomainElement )+ '}' -> ^( ERROR_DOMAIN ID ( errorDomainElement )+ ) ;
    def errorDomainDef(self, ):

        retval = self.errorDomainDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ERROR_DOMAIN33 = None
        ID34 = None
        char_literal35 = None
        char_literal37 = None
        errorDomainElement36 = None


        ERROR_DOMAIN33_tree = None
        ID34_tree = None
        char_literal35_tree = None
        char_literal37_tree = None
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_ERROR_DOMAIN = RewriteRuleTokenStream(self._adaptor, "token ERROR_DOMAIN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_errorDomainElement = RewriteRuleSubtreeStream(self._adaptor, "rule errorDomainElement")
        try:
            try:
                # GOC.g:71:5: ( ERROR_DOMAIN ID '{' ( errorDomainElement )+ '}' -> ^( ERROR_DOMAIN ID ( errorDomainElement )+ ) )
                # GOC.g:71:9: ERROR_DOMAIN ID '{' ( errorDomainElement )+ '}'
                pass 
                ERROR_DOMAIN33=self.match(self.input, ERROR_DOMAIN, self.FOLLOW_ERROR_DOMAIN_in_errorDomainDef422) 
                stream_ERROR_DOMAIN.add(ERROR_DOMAIN33)
                ID34=self.match(self.input, ID, self.FOLLOW_ID_in_errorDomainDef424) 
                stream_ID.add(ID34)
                char_literal35=self.match(self.input, 57, self.FOLLOW_57_in_errorDomainDef426) 
                stream_57.add(char_literal35)
                # GOC.g:71:29: ( errorDomainElement )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 60) :
                        alt9 = 1


                    if alt9 == 1:
                        # GOC.g:71:29: errorDomainElement
                        pass 
                        self._state.following.append(self.FOLLOW_errorDomainElement_in_errorDomainDef428)
                        errorDomainElement36 = self.errorDomainElement()

                        self._state.following.pop()
                        stream_errorDomainElement.add(errorDomainElement36.tree)


                    else:
                        if cnt9 >= 1:
                            break #loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1
                char_literal37=self.match(self.input, 58, self.FOLLOW_58_in_errorDomainDef431) 
                stream_58.add(char_literal37)

                # AST Rewrite
                # elements: errorDomainElement, ID, ERROR_DOMAIN
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 72:5: -> ^( ERROR_DOMAIN ID ( errorDomainElement )+ )
                # GOC.g:72:9: ^( ERROR_DOMAIN ID ( errorDomainElement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_ERROR_DOMAIN.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_ID.nextNode())
                # GOC.g:72:27: ( errorDomainElement )+
                if not (stream_errorDomainElement.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_errorDomainElement.hasNext():
                    self._adaptor.addChild(root_1, stream_errorDomainElement.nextTree())


                stream_errorDomainElement.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "errorDomainDef"

    class errorDomainElement_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.errorDomainElement_return, self).__init__()

            self.tree = None




    # $ANTLR start "errorDomainElement"
    # GOC.g:75:1: errorDomainElement : 'code' ID ';' -> ^( ID ) ;
    def errorDomainElement(self, ):

        retval = self.errorDomainElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal38 = None
        ID39 = None
        char_literal40 = None

        string_literal38_tree = None
        ID39_tree = None
        char_literal40_tree = None
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")

        try:
            try:
                # GOC.g:76:5: ( 'code' ID ';' -> ^( ID ) )
                # GOC.g:76:9: 'code' ID ';'
                pass 
                string_literal38=self.match(self.input, 60, self.FOLLOW_60_in_errorDomainElement466) 
                stream_60.add(string_literal38)
                ID39=self.match(self.input, ID, self.FOLLOW_ID_in_errorDomainElement468) 
                stream_ID.add(ID39)
                char_literal40=self.match(self.input, 59, self.FOLLOW_59_in_errorDomainElement470) 
                stream_59.add(char_literal40)

                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 76:23: -> ^( ID )
                # GOC.g:76:26: ^( ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_ID.nextNode(), root_1)

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "errorDomainElement"

    class enumDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.enumDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "enumDef"
    # GOC.g:79:1: enumDef : ENUMERATION ID '{' ( enumElement )+ '}' -> ^( ENUMERATION ID ( enumElement )+ ) ;
    def enumDef(self, ):

        retval = self.enumDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ENUMERATION41 = None
        ID42 = None
        char_literal43 = None
        char_literal45 = None
        enumElement44 = None


        ENUMERATION41_tree = None
        ID42_tree = None
        char_literal43_tree = None
        char_literal45_tree = None
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_ENUMERATION = RewriteRuleTokenStream(self._adaptor, "token ENUMERATION")
        stream_enumElement = RewriteRuleSubtreeStream(self._adaptor, "rule enumElement")
        try:
            try:
                # GOC.g:80:5: ( ENUMERATION ID '{' ( enumElement )+ '}' -> ^( ENUMERATION ID ( enumElement )+ ) )
                # GOC.g:80:9: ENUMERATION ID '{' ( enumElement )+ '}'
                pass 
                ENUMERATION41=self.match(self.input, ENUMERATION, self.FOLLOW_ENUMERATION_in_enumDef495) 
                stream_ENUMERATION.add(ENUMERATION41)
                ID42=self.match(self.input, ID, self.FOLLOW_ID_in_enumDef497) 
                stream_ID.add(ID42)
                char_literal43=self.match(self.input, 57, self.FOLLOW_57_in_enumDef499) 
                stream_57.add(char_literal43)
                # GOC.g:80:28: ( enumElement )+
                cnt10 = 0
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == 60) :
                        alt10 = 1


                    if alt10 == 1:
                        # GOC.g:80:28: enumElement
                        pass 
                        self._state.following.append(self.FOLLOW_enumElement_in_enumDef501)
                        enumElement44 = self.enumElement()

                        self._state.following.pop()
                        stream_enumElement.add(enumElement44.tree)


                    else:
                        if cnt10 >= 1:
                            break #loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1
                char_literal45=self.match(self.input, 58, self.FOLLOW_58_in_enumDef504) 
                stream_58.add(char_literal45)

                # AST Rewrite
                # elements: ID, ENUMERATION, enumElement
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 81:5: -> ^( ENUMERATION ID ( enumElement )+ )
                # GOC.g:81:9: ^( ENUMERATION ID ( enumElement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_ENUMERATION.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_ID.nextNode())
                # GOC.g:81:26: ( enumElement )+
                if not (stream_enumElement.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_enumElement.hasNext():
                    self._adaptor.addChild(root_1, stream_enumElement.nextTree())


                stream_enumElement.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "enumDef"

    class enumElement_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.enumElement_return, self).__init__()

            self.tree = None




    # $ANTLR start "enumElement"
    # GOC.g:84:1: enumElement : 'code' ID ( ';' | '{' 'value' ':' INT ';' '}' ) -> ^( 'code' ID ( INT )? ) ;
    def enumElement(self, ):

        retval = self.enumElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal46 = None
        ID47 = None
        char_literal48 = None
        char_literal49 = None
        string_literal50 = None
        char_literal51 = None
        INT52 = None
        char_literal53 = None
        char_literal54 = None

        string_literal46_tree = None
        ID47_tree = None
        char_literal48_tree = None
        char_literal49_tree = None
        string_literal50_tree = None
        char_literal51_tree = None
        INT52_tree = None
        char_literal53_tree = None
        char_literal54_tree = None
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_61 = RewriteRuleTokenStream(self._adaptor, "token 61")

        try:
            try:
                # GOC.g:85:5: ( 'code' ID ( ';' | '{' 'value' ':' INT ';' '}' ) -> ^( 'code' ID ( INT )? ) )
                # GOC.g:85:9: 'code' ID ( ';' | '{' 'value' ':' INT ';' '}' )
                pass 
                string_literal46=self.match(self.input, 60, self.FOLLOW_60_in_enumElement539) 
                stream_60.add(string_literal46)
                ID47=self.match(self.input, ID, self.FOLLOW_ID_in_enumElement541) 
                stream_ID.add(ID47)
                # GOC.g:85:19: ( ';' | '{' 'value' ':' INT ';' '}' )
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == 59) :
                    alt11 = 1
                elif (LA11_0 == 57) :
                    alt11 = 2
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # GOC.g:85:20: ';'
                    pass 
                    char_literal48=self.match(self.input, 59, self.FOLLOW_59_in_enumElement544) 
                    stream_59.add(char_literal48)


                elif alt11 == 2:
                    # GOC.g:85:24: '{' 'value' ':' INT ';' '}'
                    pass 
                    char_literal49=self.match(self.input, 57, self.FOLLOW_57_in_enumElement546) 
                    stream_57.add(char_literal49)
                    string_literal50=self.match(self.input, 61, self.FOLLOW_61_in_enumElement548) 
                    stream_61.add(string_literal50)
                    char_literal51=self.match(self.input, 62, self.FOLLOW_62_in_enumElement550) 
                    stream_62.add(char_literal51)
                    INT52=self.match(self.input, INT, self.FOLLOW_INT_in_enumElement552) 
                    stream_INT.add(INT52)
                    char_literal53=self.match(self.input, 59, self.FOLLOW_59_in_enumElement554) 
                    stream_59.add(char_literal53)
                    char_literal54=self.match(self.input, 58, self.FOLLOW_58_in_enumElement556) 
                    stream_58.add(char_literal54)




                # AST Rewrite
                # elements: 60, ID, INT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 86:5: -> ^( 'code' ID ( INT )? )
                # GOC.g:86:9: ^( 'code' ID ( INT )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_60.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_ID.nextNode())
                # GOC.g:86:21: ( INT )?
                if stream_INT.hasNext():
                    self._adaptor.addChild(root_1, stream_INT.nextNode())


                stream_INT.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "enumElement"

    class flagsDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.flagsDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "flagsDef"
    # GOC.g:89:1: flagsDef : FLAGS ID '{' ( flagsElement )+ '}' -> ^( FLAGS ID ( flagsElement )+ ) ;
    def flagsDef(self, ):

        retval = self.flagsDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FLAGS55 = None
        ID56 = None
        char_literal57 = None
        char_literal59 = None
        flagsElement58 = None


        FLAGS55_tree = None
        ID56_tree = None
        char_literal57_tree = None
        char_literal59_tree = None
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_FLAGS = RewriteRuleTokenStream(self._adaptor, "token FLAGS")
        stream_flagsElement = RewriteRuleSubtreeStream(self._adaptor, "rule flagsElement")
        try:
            try:
                # GOC.g:90:5: ( FLAGS ID '{' ( flagsElement )+ '}' -> ^( FLAGS ID ( flagsElement )+ ) )
                # GOC.g:90:9: FLAGS ID '{' ( flagsElement )+ '}'
                pass 
                FLAGS55=self.match(self.input, FLAGS, self.FOLLOW_FLAGS_in_flagsDef592) 
                stream_FLAGS.add(FLAGS55)
                ID56=self.match(self.input, ID, self.FOLLOW_ID_in_flagsDef594) 
                stream_ID.add(ID56)
                char_literal57=self.match(self.input, 57, self.FOLLOW_57_in_flagsDef596) 
                stream_57.add(char_literal57)
                # GOC.g:90:22: ( flagsElement )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == 60) :
                        alt12 = 1


                    if alt12 == 1:
                        # GOC.g:90:22: flagsElement
                        pass 
                        self._state.following.append(self.FOLLOW_flagsElement_in_flagsDef598)
                        flagsElement58 = self.flagsElement()

                        self._state.following.pop()
                        stream_flagsElement.add(flagsElement58.tree)


                    else:
                        if cnt12 >= 1:
                            break #loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1
                char_literal59=self.match(self.input, 58, self.FOLLOW_58_in_flagsDef601) 
                stream_58.add(char_literal59)

                # AST Rewrite
                # elements: FLAGS, ID, flagsElement
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 91:5: -> ^( FLAGS ID ( flagsElement )+ )
                # GOC.g:91:9: ^( FLAGS ID ( flagsElement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_FLAGS.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_ID.nextNode())
                # GOC.g:91:20: ( flagsElement )+
                if not (stream_flagsElement.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_flagsElement.hasNext():
                    self._adaptor.addChild(root_1, stream_flagsElement.nextTree())


                stream_flagsElement.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "flagsDef"

    class flagsElement_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.flagsElement_return, self).__init__()

            self.tree = None




    # $ANTLR start "flagsElement"
    # GOC.g:94:1: flagsElement : 'code' ID ';' -> ^( ID ) ;
    def flagsElement(self, ):

        retval = self.flagsElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal60 = None
        ID61 = None
        char_literal62 = None

        string_literal60_tree = None
        ID61_tree = None
        char_literal62_tree = None
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")

        try:
            try:
                # GOC.g:95:5: ( 'code' ID ';' -> ^( ID ) )
                # GOC.g:95:9: 'code' ID ';'
                pass 
                string_literal60=self.match(self.input, 60, self.FOLLOW_60_in_flagsElement636) 
                stream_60.add(string_literal60)
                ID61=self.match(self.input, ID, self.FOLLOW_ID_in_flagsElement638) 
                stream_ID.add(ID61)
                char_literal62=self.match(self.input, 59, self.FOLLOW_59_in_flagsElement640) 
                stream_59.add(char_literal62)

                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 95:23: -> ^( ID )
                # GOC.g:95:26: ^( ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_ID.nextNode(), root_1)

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "flagsElement"

    class typeDecl_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.typeDecl_return, self).__init__()

            self.tree = None




    # $ANTLR start "typeDecl"
    # GOC.g:98:1: typeDecl : GTYPE ID ';' -> ^( GTYPE ID ) ;
    def typeDecl(self, ):

        retval = self.typeDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        GTYPE63 = None
        ID64 = None
        char_literal65 = None

        GTYPE63_tree = None
        ID64_tree = None
        char_literal65_tree = None
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_GTYPE = RewriteRuleTokenStream(self._adaptor, "token GTYPE")

        try:
            try:
                # GOC.g:99:5: ( GTYPE ID ';' -> ^( GTYPE ID ) )
                # GOC.g:99:9: GTYPE ID ';'
                pass 
                GTYPE63=self.match(self.input, GTYPE, self.FOLLOW_GTYPE_in_typeDecl665) 
                stream_GTYPE.add(GTYPE63)
                ID64=self.match(self.input, ID, self.FOLLOW_ID_in_typeDecl667) 
                stream_ID.add(ID64)
                char_literal65=self.match(self.input, 59, self.FOLLOW_59_in_typeDecl669) 
                stream_59.add(char_literal65)

                # AST Rewrite
                # elements: ID, GTYPE
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 99:22: -> ^( GTYPE ID )
                # GOC.g:99:25: ^( GTYPE ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_GTYPE.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_ID.nextNode())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "typeDecl"

    class classMember_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.classMember_return, self).__init__()

            self.tree = None




    # $ANTLR start "classMember"
    # GOC.g:102:1: classMember : ( SUPER typeName ';' -> ^( SUPER typeName ) | ABSTRACT ';' | PREFIX ID ';' -> ^( PREFIX ID ) | IMPLEMENTS typeName ';' -> ^( IMPLEMENTS typeName ) | CONSTRUCTOR '{' ( constructorElement )* '}' -> ^( CONSTRUCTOR ( constructorElement )* ) | METHOD ID '{' ( methodElement )* '}' -> ^( METHOD ID ( methodElement )* ) | OVERRIDE ID ';' -> ^( OVERRIDE ID ) | ATTRIBUTE ID '{' TYPE ':' typeArg ';' ( attributeElement )* '}' -> ^( ATTRIBUTE ID typeArg ( attributeElement )* ) | PROPERTY ID '{' ( propertyElement )+ '}' -> ^( PROPERTY ID ( propertyElement )+ ) | SIGNAL signalID '{' ( signalElement )* '}' -> ^( SIGNAL signalID ( signalElement )* ) );
    def classMember(self, ):
        self.classMember_stack.append(classMember_scope())
        retval = self.classMember_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SUPER66 = None
        char_literal68 = None
        ABSTRACT69 = None
        char_literal70 = None
        PREFIX71 = None
        ID72 = None
        char_literal73 = None
        IMPLEMENTS74 = None
        char_literal76 = None
        CONSTRUCTOR77 = None
        char_literal78 = None
        char_literal80 = None
        METHOD81 = None
        ID82 = None
        char_literal83 = None
        char_literal85 = None
        OVERRIDE86 = None
        ID87 = None
        char_literal88 = None
        ATTRIBUTE89 = None
        ID90 = None
        char_literal91 = None
        TYPE92 = None
        char_literal93 = None
        char_literal95 = None
        char_literal97 = None
        PROPERTY98 = None
        ID99 = None
        char_literal100 = None
        char_literal102 = None
        SIGNAL103 = None
        char_literal105 = None
        char_literal107 = None
        typeName67 = None

        typeName75 = None

        constructorElement79 = None

        methodElement84 = None

        typeArg94 = None

        attributeElement96 = None

        propertyElement101 = None

        signalID104 = None

        signalElement106 = None


        SUPER66_tree = None
        char_literal68_tree = None
        ABSTRACT69_tree = None
        char_literal70_tree = None
        PREFIX71_tree = None
        ID72_tree = None
        char_literal73_tree = None
        IMPLEMENTS74_tree = None
        char_literal76_tree = None
        CONSTRUCTOR77_tree = None
        char_literal78_tree = None
        char_literal80_tree = None
        METHOD81_tree = None
        ID82_tree = None
        char_literal83_tree = None
        char_literal85_tree = None
        OVERRIDE86_tree = None
        ID87_tree = None
        char_literal88_tree = None
        ATTRIBUTE89_tree = None
        ID90_tree = None
        char_literal91_tree = None
        TYPE92_tree = None
        char_literal93_tree = None
        char_literal95_tree = None
        char_literal97_tree = None
        PROPERTY98_tree = None
        ID99_tree = None
        char_literal100_tree = None
        char_literal102_tree = None
        SIGNAL103_tree = None
        char_literal105_tree = None
        char_literal107_tree = None
        stream_PREFIX = RewriteRuleTokenStream(self._adaptor, "token PREFIX")
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_IMPLEMENTS = RewriteRuleTokenStream(self._adaptor, "token IMPLEMENTS")
        stream_PROPERTY = RewriteRuleTokenStream(self._adaptor, "token PROPERTY")
        stream_OVERRIDE = RewriteRuleTokenStream(self._adaptor, "token OVERRIDE")
        stream_SIGNAL = RewriteRuleTokenStream(self._adaptor, "token SIGNAL")
        stream_ATTRIBUTE = RewriteRuleTokenStream(self._adaptor, "token ATTRIBUTE")
        stream_SUPER = RewriteRuleTokenStream(self._adaptor, "token SUPER")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_CONSTRUCTOR = RewriteRuleTokenStream(self._adaptor, "token CONSTRUCTOR")
        stream_METHOD = RewriteRuleTokenStream(self._adaptor, "token METHOD")
        stream_TYPE = RewriteRuleTokenStream(self._adaptor, "token TYPE")
        stream_typeName = RewriteRuleSubtreeStream(self._adaptor, "rule typeName")
        stream_constructorElement = RewriteRuleSubtreeStream(self._adaptor, "rule constructorElement")
        stream_propertyElement = RewriteRuleSubtreeStream(self._adaptor, "rule propertyElement")
        stream_typeArg = RewriteRuleSubtreeStream(self._adaptor, "rule typeArg")
        stream_methodElement = RewriteRuleSubtreeStream(self._adaptor, "rule methodElement")
        stream_attributeElement = RewriteRuleSubtreeStream(self._adaptor, "rule attributeElement")
        stream_signalElement = RewriteRuleSubtreeStream(self._adaptor, "rule signalElement")
        stream_signalID = RewriteRuleSubtreeStream(self._adaptor, "rule signalID")
               
        self.classMember_stack[-1].with_constructor = False

        try:
            try:
                # GOC.g:109:2: ( SUPER typeName ';' -> ^( SUPER typeName ) | ABSTRACT ';' | PREFIX ID ';' -> ^( PREFIX ID ) | IMPLEMENTS typeName ';' -> ^( IMPLEMENTS typeName ) | CONSTRUCTOR '{' ( constructorElement )* '}' -> ^( CONSTRUCTOR ( constructorElement )* ) | METHOD ID '{' ( methodElement )* '}' -> ^( METHOD ID ( methodElement )* ) | OVERRIDE ID ';' -> ^( OVERRIDE ID ) | ATTRIBUTE ID '{' TYPE ':' typeArg ';' ( attributeElement )* '}' -> ^( ATTRIBUTE ID typeArg ( attributeElement )* ) | PROPERTY ID '{' ( propertyElement )+ '}' -> ^( PROPERTY ID ( propertyElement )+ ) | SIGNAL signalID '{' ( signalElement )* '}' -> ^( SIGNAL signalID ( signalElement )* ) )
                alt18 = 10
                LA18 = self.input.LA(1)
                if LA18 == SUPER:
                    alt18 = 1
                elif LA18 == ABSTRACT:
                    alt18 = 2
                elif LA18 == PREFIX:
                    alt18 = 3
                elif LA18 == IMPLEMENTS:
                    alt18 = 4
                elif LA18 == CONSTRUCTOR:
                    alt18 = 5
                elif LA18 == METHOD:
                    alt18 = 6
                elif LA18 == OVERRIDE:
                    alt18 = 7
                elif LA18 == ATTRIBUTE:
                    alt18 = 8
                elif LA18 == PROPERTY:
                    alt18 = 9
                elif LA18 == SIGNAL:
                    alt18 = 10
                else:
                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae

                if alt18 == 1:
                    # GOC.g:109:4: SUPER typeName ';'
                    pass 
                    SUPER66=self.match(self.input, SUPER, self.FOLLOW_SUPER_in_classMember700) 
                    stream_SUPER.add(SUPER66)
                    self._state.following.append(self.FOLLOW_typeName_in_classMember702)
                    typeName67 = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(typeName67.tree)
                    char_literal68=self.match(self.input, 59, self.FOLLOW_59_in_classMember704) 
                    stream_59.add(char_literal68)

                    # AST Rewrite
                    # elements: typeName, SUPER
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 110:2: -> ^( SUPER typeName )
                    # GOC.g:110:5: ^( SUPER typeName )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_SUPER.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_typeName.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt18 == 2:
                    # GOC.g:111:6: ABSTRACT ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    ABSTRACT69=self.match(self.input, ABSTRACT, self.FOLLOW_ABSTRACT_in_classMember720)

                    ABSTRACT69_tree = self._adaptor.createWithPayload(ABSTRACT69)
                    root_0 = self._adaptor.becomeRoot(ABSTRACT69_tree, root_0)

                    char_literal70=self.match(self.input, 59, self.FOLLOW_59_in_classMember723)

                    char_literal70_tree = self._adaptor.createWithPayload(char_literal70)
                    self._adaptor.addChild(root_0, char_literal70_tree)



                elif alt18 == 3:
                    # GOC.g:112:6: PREFIX ID ';'
                    pass 
                    PREFIX71=self.match(self.input, PREFIX, self.FOLLOW_PREFIX_in_classMember730) 
                    stream_PREFIX.add(PREFIX71)
                    ID72=self.match(self.input, ID, self.FOLLOW_ID_in_classMember732) 
                    stream_ID.add(ID72)
                    char_literal73=self.match(self.input, 59, self.FOLLOW_59_in_classMember734) 
                    stream_59.add(char_literal73)

                    # AST Rewrite
                    # elements: ID, PREFIX
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 112:20: -> ^( PREFIX ID )
                    # GOC.g:112:23: ^( PREFIX ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_PREFIX.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt18 == 4:
                    # GOC.g:113:4: IMPLEMENTS typeName ';'
                    pass 
                    IMPLEMENTS74=self.match(self.input, IMPLEMENTS, self.FOLLOW_IMPLEMENTS_in_classMember747) 
                    stream_IMPLEMENTS.add(IMPLEMENTS74)
                    self._state.following.append(self.FOLLOW_typeName_in_classMember749)
                    typeName75 = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(typeName75.tree)
                    char_literal76=self.match(self.input, 59, self.FOLLOW_59_in_classMember751) 
                    stream_59.add(char_literal76)

                    # AST Rewrite
                    # elements: typeName, IMPLEMENTS
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 113:28: -> ^( IMPLEMENTS typeName )
                    # GOC.g:113:31: ^( IMPLEMENTS typeName )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_IMPLEMENTS.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_typeName.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt18 == 5:
                    # GOC.g:114:4: CONSTRUCTOR '{' ( constructorElement )* '}'
                    pass 
                    #action start
                    self.classMember_stack[-1].with_constructor = True 
                    #action end
                    CONSTRUCTOR77=self.match(self.input, CONSTRUCTOR, self.FOLLOW_CONSTRUCTOR_in_classMember771) 
                    stream_CONSTRUCTOR.add(CONSTRUCTOR77)
                    char_literal78=self.match(self.input, 57, self.FOLLOW_57_in_classMember773) 
                    stream_57.add(char_literal78)
                    # GOC.g:115:22: ( constructorElement )*
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == PARAMETER) :
                            alt13 = 1
                        elif (LA13_0 == INIT_PROPERTIES) and ((self.classMember_stack[-1].with_constructor)):
                            alt13 = 1


                        if alt13 == 1:
                            # GOC.g:115:22: constructorElement
                            pass 
                            self._state.following.append(self.FOLLOW_constructorElement_in_classMember775)
                            constructorElement79 = self.constructorElement()

                            self._state.following.pop()
                            stream_constructorElement.add(constructorElement79.tree)


                        else:
                            break #loop13
                    char_literal80=self.match(self.input, 58, self.FOLLOW_58_in_classMember778) 
                    stream_58.add(char_literal80)
                    #action start
                    self.classMember_stack[-1].with_constructor = False 
                    #action end

                    # AST Rewrite
                    # elements: constructorElement, CONSTRUCTOR
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 117:6: -> ^( CONSTRUCTOR ( constructorElement )* )
                    # GOC.g:117:9: ^( CONSTRUCTOR ( constructorElement )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_CONSTRUCTOR.nextNode(), root_1)

                    # GOC.g:117:23: ( constructorElement )*
                    while stream_constructorElement.hasNext():
                        self._adaptor.addChild(root_1, stream_constructorElement.nextTree())


                    stream_constructorElement.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt18 == 6:
                    # GOC.g:118:6: METHOD ID '{' ( methodElement )* '}'
                    pass 
                    METHOD81=self.match(self.input, METHOD, self.FOLLOW_METHOD_in_classMember806) 
                    stream_METHOD.add(METHOD81)
                    ID82=self.match(self.input, ID, self.FOLLOW_ID_in_classMember808) 
                    stream_ID.add(ID82)
                    char_literal83=self.match(self.input, 57, self.FOLLOW_57_in_classMember810) 
                    stream_57.add(char_literal83)
                    # GOC.g:118:20: ( methodElement )*
                    while True: #loop14
                        alt14 = 2
                        LA14_0 = self.input.LA(1)

                        if (LA14_0 == PARAMETER) :
                            alt14 = 1
                        elif (LA14_0 == INIT_PROPERTIES) and ((self.classMember_stack[-1].with_constructor)):
                            alt14 = 1
                        elif ((RESULT <= LA14_0 <= INHERITANCE)) :
                            alt14 = 1


                        if alt14 == 1:
                            # GOC.g:118:20: methodElement
                            pass 
                            self._state.following.append(self.FOLLOW_methodElement_in_classMember812)
                            methodElement84 = self.methodElement()

                            self._state.following.pop()
                            stream_methodElement.add(methodElement84.tree)


                        else:
                            break #loop14
                    char_literal85=self.match(self.input, 58, self.FOLLOW_58_in_classMember815) 
                    stream_58.add(char_literal85)

                    # AST Rewrite
                    # elements: METHOD, ID, methodElement
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 118:39: -> ^( METHOD ID ( methodElement )* )
                    # GOC.g:118:42: ^( METHOD ID ( methodElement )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_METHOD.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())
                    # GOC.g:118:54: ( methodElement )*
                    while stream_methodElement.hasNext():
                        self._adaptor.addChild(root_1, stream_methodElement.nextTree())


                    stream_methodElement.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt18 == 7:
                    # GOC.g:119:5: OVERRIDE ID ';'
                    pass 
                    OVERRIDE86=self.match(self.input, OVERRIDE, self.FOLLOW_OVERRIDE_in_classMember832) 
                    stream_OVERRIDE.add(OVERRIDE86)
                    ID87=self.match(self.input, ID, self.FOLLOW_ID_in_classMember834) 
                    stream_ID.add(ID87)
                    char_literal88=self.match(self.input, 59, self.FOLLOW_59_in_classMember836) 
                    stream_59.add(char_literal88)

                    # AST Rewrite
                    # elements: ID, OVERRIDE
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 119:21: -> ^( OVERRIDE ID )
                    # GOC.g:119:24: ^( OVERRIDE ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_OVERRIDE.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt18 == 8:
                    # GOC.g:120:4: ATTRIBUTE ID '{' TYPE ':' typeArg ';' ( attributeElement )* '}'
                    pass 
                    ATTRIBUTE89=self.match(self.input, ATTRIBUTE, self.FOLLOW_ATTRIBUTE_in_classMember849) 
                    stream_ATTRIBUTE.add(ATTRIBUTE89)
                    ID90=self.match(self.input, ID, self.FOLLOW_ID_in_classMember851) 
                    stream_ID.add(ID90)
                    char_literal91=self.match(self.input, 57, self.FOLLOW_57_in_classMember853) 
                    stream_57.add(char_literal91)
                    TYPE92=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_classMember855) 
                    stream_TYPE.add(TYPE92)
                    char_literal93=self.match(self.input, 62, self.FOLLOW_62_in_classMember857) 
                    stream_62.add(char_literal93)
                    self._state.following.append(self.FOLLOW_typeArg_in_classMember859)
                    typeArg94 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg94.tree)
                    char_literal95=self.match(self.input, 59, self.FOLLOW_59_in_classMember861) 
                    stream_59.add(char_literal95)
                    # GOC.g:120:42: ( attributeElement )*
                    while True: #loop15
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if ((VISIBILITY <= LA15_0 <= SCOPE)) :
                            alt15 = 1


                        if alt15 == 1:
                            # GOC.g:120:42: attributeElement
                            pass 
                            self._state.following.append(self.FOLLOW_attributeElement_in_classMember863)
                            attributeElement96 = self.attributeElement()

                            self._state.following.pop()
                            stream_attributeElement.add(attributeElement96.tree)


                        else:
                            break #loop15
                    char_literal97=self.match(self.input, 58, self.FOLLOW_58_in_classMember866) 
                    stream_58.add(char_literal97)

                    # AST Rewrite
                    # elements: attributeElement, ID, ATTRIBUTE, typeArg
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 121:2: -> ^( ATTRIBUTE ID typeArg ( attributeElement )* )
                    # GOC.g:121:5: ^( ATTRIBUTE ID typeArg ( attributeElement )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_ATTRIBUTE.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())
                    self._adaptor.addChild(root_1, stream_typeArg.nextTree())
                    # GOC.g:121:28: ( attributeElement )*
                    while stream_attributeElement.hasNext():
                        self._adaptor.addChild(root_1, stream_attributeElement.nextTree())


                    stream_attributeElement.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt18 == 9:
                    # GOC.g:122:4: PROPERTY ID '{' ( propertyElement )+ '}'
                    pass 
                    PROPERTY98=self.match(self.input, PROPERTY, self.FOLLOW_PROPERTY_in_classMember885) 
                    stream_PROPERTY.add(PROPERTY98)
                    ID99=self.match(self.input, ID, self.FOLLOW_ID_in_classMember887) 
                    stream_ID.add(ID99)
                    char_literal100=self.match(self.input, 57, self.FOLLOW_57_in_classMember889) 
                    stream_57.add(char_literal100)
                    # GOC.g:122:20: ( propertyElement )+
                    cnt16 = 0
                    while True: #loop16
                        alt16 = 2
                        LA16_0 = self.input.LA(1)

                        if (LA16_0 == GTYPE or LA16_0 == TYPE or LA16_0 == AUTO_CREATE or LA16_0 == 81 or LA16_0 == 85 or (88 <= LA16_0 <= 90)) :
                            alt16 = 1


                        if alt16 == 1:
                            # GOC.g:122:20: propertyElement
                            pass 
                            self._state.following.append(self.FOLLOW_propertyElement_in_classMember891)
                            propertyElement101 = self.propertyElement()

                            self._state.following.pop()
                            stream_propertyElement.add(propertyElement101.tree)


                        else:
                            if cnt16 >= 1:
                                break #loop16

                            eee = EarlyExitException(16, self.input)
                            raise eee

                        cnt16 += 1
                    char_literal102=self.match(self.input, 58, self.FOLLOW_58_in_classMember894) 
                    stream_58.add(char_literal102)

                    # AST Rewrite
                    # elements: propertyElement, PROPERTY, ID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 122:41: -> ^( PROPERTY ID ( propertyElement )+ )
                    # GOC.g:122:44: ^( PROPERTY ID ( propertyElement )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_PROPERTY.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())
                    # GOC.g:122:58: ( propertyElement )+
                    if not (stream_propertyElement.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_propertyElement.hasNext():
                        self._adaptor.addChild(root_1, stream_propertyElement.nextTree())


                    stream_propertyElement.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt18 == 10:
                    # GOC.g:123:4: SIGNAL signalID '{' ( signalElement )* '}'
                    pass 
                    SIGNAL103=self.match(self.input, SIGNAL, self.FOLLOW_SIGNAL_in_classMember910) 
                    stream_SIGNAL.add(SIGNAL103)
                    self._state.following.append(self.FOLLOW_signalID_in_classMember912)
                    signalID104 = self.signalID()

                    self._state.following.pop()
                    stream_signalID.add(signalID104.tree)
                    char_literal105=self.match(self.input, 57, self.FOLLOW_57_in_classMember914) 
                    stream_57.add(char_literal105)
                    # GOC.g:123:24: ( signalElement )*
                    while True: #loop17
                        alt17 = 2
                        LA17_0 = self.input.LA(1)

                        if (LA17_0 == RESULT or LA17_0 == PARAMETER) :
                            alt17 = 1


                        if alt17 == 1:
                            # GOC.g:123:24: signalElement
                            pass 
                            self._state.following.append(self.FOLLOW_signalElement_in_classMember916)
                            signalElement106 = self.signalElement()

                            self._state.following.pop()
                            stream_signalElement.add(signalElement106.tree)


                        else:
                            break #loop17
                    char_literal107=self.match(self.input, 58, self.FOLLOW_58_in_classMember919) 
                    stream_58.add(char_literal107)

                    # AST Rewrite
                    # elements: SIGNAL, signalElement, signalID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 123:43: -> ^( SIGNAL signalID ( signalElement )* )
                    # GOC.g:123:46: ^( SIGNAL signalID ( signalElement )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_SIGNAL.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_signalID.nextTree())
                    # GOC.g:123:64: ( signalElement )*
                    while stream_signalElement.hasNext():
                        self._adaptor.addChild(root_1, stream_signalElement.nextTree())


                    stream_signalElement.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            self.classMember_stack.pop()
            pass
        return retval

    # $ANTLR end "classMember"

    class intfMember_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.intfMember_return, self).__init__()

            self.tree = None




    # $ANTLR start "intfMember"
    # GOC.g:126:1: intfMember : ( PREFIX ID ';' -> ^( PREFIX ID ) | METHOD ID '{' ( methodElement )* '}' -> ^( METHOD ID ( methodElement )* ) | SIGNAL signalID '{' ( signalElement )* '}' -> ^( SIGNAL signalID ( signalElement )* ) );
    def intfMember(self, ):

        retval = self.intfMember_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PREFIX108 = None
        ID109 = None
        char_literal110 = None
        METHOD111 = None
        ID112 = None
        char_literal113 = None
        char_literal115 = None
        SIGNAL116 = None
        char_literal118 = None
        char_literal120 = None
        methodElement114 = None

        signalID117 = None

        signalElement119 = None


        PREFIX108_tree = None
        ID109_tree = None
        char_literal110_tree = None
        METHOD111_tree = None
        ID112_tree = None
        char_literal113_tree = None
        char_literal115_tree = None
        SIGNAL116_tree = None
        char_literal118_tree = None
        char_literal120_tree = None
        stream_PREFIX = RewriteRuleTokenStream(self._adaptor, "token PREFIX")
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_METHOD = RewriteRuleTokenStream(self._adaptor, "token METHOD")
        stream_SIGNAL = RewriteRuleTokenStream(self._adaptor, "token SIGNAL")
        stream_methodElement = RewriteRuleSubtreeStream(self._adaptor, "rule methodElement")
        stream_signalElement = RewriteRuleSubtreeStream(self._adaptor, "rule signalElement")
        stream_signalID = RewriteRuleSubtreeStream(self._adaptor, "rule signalID")
        try:
            try:
                # GOC.g:127:2: ( PREFIX ID ';' -> ^( PREFIX ID ) | METHOD ID '{' ( methodElement )* '}' -> ^( METHOD ID ( methodElement )* ) | SIGNAL signalID '{' ( signalElement )* '}' -> ^( SIGNAL signalID ( signalElement )* ) )
                alt21 = 3
                LA21 = self.input.LA(1)
                if LA21 == PREFIX:
                    alt21 = 1
                elif LA21 == METHOD:
                    alt21 = 2
                elif LA21 == SIGNAL:
                    alt21 = 3
                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # GOC.g:127:4: PREFIX ID ';'
                    pass 
                    PREFIX108=self.match(self.input, PREFIX, self.FOLLOW_PREFIX_in_intfMember942) 
                    stream_PREFIX.add(PREFIX108)
                    ID109=self.match(self.input, ID, self.FOLLOW_ID_in_intfMember944) 
                    stream_ID.add(ID109)
                    char_literal110=self.match(self.input, 59, self.FOLLOW_59_in_intfMember946) 
                    stream_59.add(char_literal110)

                    # AST Rewrite
                    # elements: ID, PREFIX
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 127:18: -> ^( PREFIX ID )
                    # GOC.g:127:21: ^( PREFIX ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_PREFIX.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt21 == 2:
                    # GOC.g:128:6: METHOD ID '{' ( methodElement )* '}'
                    pass 
                    METHOD111=self.match(self.input, METHOD, self.FOLLOW_METHOD_in_intfMember961) 
                    stream_METHOD.add(METHOD111)
                    ID112=self.match(self.input, ID, self.FOLLOW_ID_in_intfMember963) 
                    stream_ID.add(ID112)
                    char_literal113=self.match(self.input, 57, self.FOLLOW_57_in_intfMember965) 
                    stream_57.add(char_literal113)
                    # GOC.g:128:20: ( methodElement )*
                    while True: #loop19
                        alt19 = 2
                        LA19_0 = self.input.LA(1)

                        if (LA19_0 == PARAMETER) :
                            alt19 = 1
                        elif (LA19_0 == INIT_PROPERTIES) and ((self.classMember_stack[-1].with_constructor)):
                            alt19 = 1
                        elif ((RESULT <= LA19_0 <= INHERITANCE)) :
                            alt19 = 1


                        if alt19 == 1:
                            # GOC.g:128:20: methodElement
                            pass 
                            self._state.following.append(self.FOLLOW_methodElement_in_intfMember967)
                            methodElement114 = self.methodElement()

                            self._state.following.pop()
                            stream_methodElement.add(methodElement114.tree)


                        else:
                            break #loop19
                    char_literal115=self.match(self.input, 58, self.FOLLOW_58_in_intfMember970) 
                    stream_58.add(char_literal115)

                    # AST Rewrite
                    # elements: ID, METHOD, methodElement
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 128:39: -> ^( METHOD ID ( methodElement )* )
                    # GOC.g:128:42: ^( METHOD ID ( methodElement )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_METHOD.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())
                    # GOC.g:128:54: ( methodElement )*
                    while stream_methodElement.hasNext():
                        self._adaptor.addChild(root_1, stream_methodElement.nextTree())


                    stream_methodElement.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt21 == 3:
                    # GOC.g:129:9: SIGNAL signalID '{' ( signalElement )* '}'
                    pass 
                    SIGNAL116=self.match(self.input, SIGNAL, self.FOLLOW_SIGNAL_in_intfMember991) 
                    stream_SIGNAL.add(SIGNAL116)
                    self._state.following.append(self.FOLLOW_signalID_in_intfMember993)
                    signalID117 = self.signalID()

                    self._state.following.pop()
                    stream_signalID.add(signalID117.tree)
                    char_literal118=self.match(self.input, 57, self.FOLLOW_57_in_intfMember995) 
                    stream_57.add(char_literal118)
                    # GOC.g:129:29: ( signalElement )*
                    while True: #loop20
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if (LA20_0 == RESULT or LA20_0 == PARAMETER) :
                            alt20 = 1


                        if alt20 == 1:
                            # GOC.g:129:29: signalElement
                            pass 
                            self._state.following.append(self.FOLLOW_signalElement_in_intfMember997)
                            signalElement119 = self.signalElement()

                            self._state.following.pop()
                            stream_signalElement.add(signalElement119.tree)


                        else:
                            break #loop20
                    char_literal120=self.match(self.input, 58, self.FOLLOW_58_in_intfMember1000) 
                    stream_58.add(char_literal120)

                    # AST Rewrite
                    # elements: signalElement, signalID, SIGNAL
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 129:48: -> ^( SIGNAL signalID ( signalElement )* )
                    # GOC.g:129:51: ^( SIGNAL signalID ( signalElement )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_SIGNAL.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_signalID.nextTree())
                    # GOC.g:129:69: ( signalElement )*
                    while stream_signalElement.hasNext():
                        self._adaptor.addChild(root_1, stream_signalElement.nextTree())


                    stream_signalElement.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "intfMember"

    class resultDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.resultDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "resultDef"
    # GOC.g:132:1: resultDef : RESULT '{' TYPE ':' typeArg ';' ( modifiers )? '}' -> ^( RESULT typeArg ( modifiers )? ) ;
    def resultDef(self, ):

        retval = self.resultDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RESULT121 = None
        char_literal122 = None
        TYPE123 = None
        char_literal124 = None
        char_literal126 = None
        char_literal128 = None
        typeArg125 = None

        modifiers127 = None


        RESULT121_tree = None
        char_literal122_tree = None
        TYPE123_tree = None
        char_literal124_tree = None
        char_literal126_tree = None
        char_literal128_tree = None
        stream_RESULT = RewriteRuleTokenStream(self._adaptor, "token RESULT")
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_TYPE = RewriteRuleTokenStream(self._adaptor, "token TYPE")
        stream_typeArg = RewriteRuleSubtreeStream(self._adaptor, "rule typeArg")
        stream_modifiers = RewriteRuleSubtreeStream(self._adaptor, "rule modifiers")
        try:
            try:
                # GOC.g:133:2: ( RESULT '{' TYPE ':' typeArg ';' ( modifiers )? '}' -> ^( RESULT typeArg ( modifiers )? ) )
                # GOC.g:133:4: RESULT '{' TYPE ':' typeArg ';' ( modifiers )? '}'
                pass 
                RESULT121=self.match(self.input, RESULT, self.FOLLOW_RESULT_in_resultDef1023) 
                stream_RESULT.add(RESULT121)
                char_literal122=self.match(self.input, 57, self.FOLLOW_57_in_resultDef1025) 
                stream_57.add(char_literal122)
                TYPE123=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_resultDef1027) 
                stream_TYPE.add(TYPE123)
                char_literal124=self.match(self.input, 62, self.FOLLOW_62_in_resultDef1029) 
                stream_62.add(char_literal124)
                self._state.following.append(self.FOLLOW_typeArg_in_resultDef1031)
                typeArg125 = self.typeArg()

                self._state.following.pop()
                stream_typeArg.add(typeArg125.tree)
                char_literal126=self.match(self.input, 59, self.FOLLOW_59_in_resultDef1033) 
                stream_59.add(char_literal126)
                # GOC.g:133:36: ( modifiers )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == MODIFIERS) :
                    alt22 = 1
                if alt22 == 1:
                    # GOC.g:133:36: modifiers
                    pass 
                    self._state.following.append(self.FOLLOW_modifiers_in_resultDef1035)
                    modifiers127 = self.modifiers()

                    self._state.following.pop()
                    stream_modifiers.add(modifiers127.tree)



                char_literal128=self.match(self.input, 58, self.FOLLOW_58_in_resultDef1038) 
                stream_58.add(char_literal128)

                # AST Rewrite
                # elements: modifiers, typeArg, RESULT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 134:2: -> ^( RESULT typeArg ( modifiers )? )
                # GOC.g:134:5: ^( RESULT typeArg ( modifiers )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_RESULT.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_typeArg.nextTree())
                # GOC.g:134:22: ( modifiers )?
                if stream_modifiers.hasNext():
                    self._adaptor.addChild(root_1, stream_modifiers.nextTree())


                stream_modifiers.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "resultDef"

    class methodElement_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.methodElement_return, self).__init__()

            self.tree = None




    # $ANTLR start "methodElement"
    # GOC.g:137:1: methodElement : ( constructorElement | resultDef | VISIBILITY ':' (val= 'public' | val= 'protected' | val= 'private' ) ';' -> ^( VISIBILITY $val) | SCOPE ':' (val= 'instance' | val= 'static' ) ';' -> ^( SCOPE $val) | INHERITANCE ':' (val= 'final' | val= 'virtual' | val= 'abstract' ) ';' -> ^( INHERITANCE $val) );
    def methodElement(self, ):

        retval = self.methodElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        val = None
        VISIBILITY131 = None
        char_literal132 = None
        char_literal133 = None
        SCOPE134 = None
        char_literal135 = None
        char_literal136 = None
        INHERITANCE137 = None
        char_literal138 = None
        char_literal139 = None
        constructorElement129 = None

        resultDef130 = None


        val_tree = None
        VISIBILITY131_tree = None
        char_literal132_tree = None
        char_literal133_tree = None
        SCOPE134_tree = None
        char_literal135_tree = None
        char_literal136_tree = None
        INHERITANCE137_tree = None
        char_literal138_tree = None
        char_literal139_tree = None
        stream_67 = RewriteRuleTokenStream(self._adaptor, "token 67")
        stream_66 = RewriteRuleTokenStream(self._adaptor, "token 66")
        stream_69 = RewriteRuleTokenStream(self._adaptor, "token 69")
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_68 = RewriteRuleTokenStream(self._adaptor, "token 68")
        stream_VISIBILITY = RewriteRuleTokenStream(self._adaptor, "token VISIBILITY")
        stream_SCOPE = RewriteRuleTokenStream(self._adaptor, "token SCOPE")
        stream_ABSTRACT = RewriteRuleTokenStream(self._adaptor, "token ABSTRACT")
        stream_64 = RewriteRuleTokenStream(self._adaptor, "token 64")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_63 = RewriteRuleTokenStream(self._adaptor, "token 63")
        stream_INHERITANCE = RewriteRuleTokenStream(self._adaptor, "token INHERITANCE")

        try:
            try:
                # GOC.g:138:2: ( constructorElement | resultDef | VISIBILITY ':' (val= 'public' | val= 'protected' | val= 'private' ) ';' -> ^( VISIBILITY $val) | SCOPE ':' (val= 'instance' | val= 'static' ) ';' -> ^( SCOPE $val) | INHERITANCE ':' (val= 'final' | val= 'virtual' | val= 'abstract' ) ';' -> ^( INHERITANCE $val) )
                alt26 = 5
                LA26_0 = self.input.LA(1)

                if (LA26_0 == PARAMETER) :
                    alt26 = 1
                elif (LA26_0 == INIT_PROPERTIES) and ((self.classMember_stack[-1].with_constructor)):
                    alt26 = 1
                elif (LA26_0 == RESULT) :
                    alt26 = 2
                elif (LA26_0 == VISIBILITY) :
                    alt26 = 3
                elif (LA26_0 == SCOPE) :
                    alt26 = 4
                elif (LA26_0 == INHERITANCE) :
                    alt26 = 5
                else:
                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae

                if alt26 == 1:
                    # GOC.g:138:4: constructorElement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_constructorElement_in_methodElement1061)
                    constructorElement129 = self.constructorElement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, constructorElement129.tree)


                elif alt26 == 2:
                    # GOC.g:139:4: resultDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_resultDef_in_methodElement1066)
                    resultDef130 = self.resultDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, resultDef130.tree)


                elif alt26 == 3:
                    # GOC.g:140:4: VISIBILITY ':' (val= 'public' | val= 'protected' | val= 'private' ) ';'
                    pass 
                    VISIBILITY131=self.match(self.input, VISIBILITY, self.FOLLOW_VISIBILITY_in_methodElement1071) 
                    stream_VISIBILITY.add(VISIBILITY131)
                    char_literal132=self.match(self.input, 62, self.FOLLOW_62_in_methodElement1073) 
                    stream_62.add(char_literal132)
                    # GOC.g:140:19: (val= 'public' | val= 'protected' | val= 'private' )
                    alt23 = 3
                    LA23 = self.input.LA(1)
                    if LA23 == 63:
                        alt23 = 1
                    elif LA23 == 64:
                        alt23 = 2
                    elif LA23 == 65:
                        alt23 = 3
                    else:
                        nvae = NoViableAltException("", 23, 0, self.input)

                        raise nvae

                    if alt23 == 1:
                        # GOC.g:140:20: val= 'public'
                        pass 
                        val=self.match(self.input, 63, self.FOLLOW_63_in_methodElement1078) 
                        stream_63.add(val)


                    elif alt23 == 2:
                        # GOC.g:140:33: val= 'protected'
                        pass 
                        val=self.match(self.input, 64, self.FOLLOW_64_in_methodElement1082) 
                        stream_64.add(val)


                    elif alt23 == 3:
                        # GOC.g:140:49: val= 'private'
                        pass 
                        val=self.match(self.input, 65, self.FOLLOW_65_in_methodElement1086) 
                        stream_65.add(val)



                    char_literal133=self.match(self.input, 59, self.FOLLOW_59_in_methodElement1089) 
                    stream_59.add(char_literal133)

                    # AST Rewrite
                    # elements: VISIBILITY, val
                    # token labels: val
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 141:2: -> ^( VISIBILITY $val)
                    # GOC.g:141:5: ^( VISIBILITY $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_VISIBILITY.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt26 == 4:
                    # GOC.g:142:4: SCOPE ':' (val= 'instance' | val= 'static' ) ';'
                    pass 
                    SCOPE134=self.match(self.input, SCOPE, self.FOLLOW_SCOPE_in_methodElement1104) 
                    stream_SCOPE.add(SCOPE134)
                    char_literal135=self.match(self.input, 62, self.FOLLOW_62_in_methodElement1106) 
                    stream_62.add(char_literal135)
                    # GOC.g:142:14: (val= 'instance' | val= 'static' )
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == 66) :
                        alt24 = 1
                    elif (LA24_0 == 67) :
                        alt24 = 2
                    else:
                        nvae = NoViableAltException("", 24, 0, self.input)

                        raise nvae

                    if alt24 == 1:
                        # GOC.g:142:15: val= 'instance'
                        pass 
                        val=self.match(self.input, 66, self.FOLLOW_66_in_methodElement1111) 
                        stream_66.add(val)


                    elif alt24 == 2:
                        # GOC.g:142:30: val= 'static'
                        pass 
                        val=self.match(self.input, 67, self.FOLLOW_67_in_methodElement1115) 
                        stream_67.add(val)



                    char_literal136=self.match(self.input, 59, self.FOLLOW_59_in_methodElement1118) 
                    stream_59.add(char_literal136)

                    # AST Rewrite
                    # elements: val, SCOPE
                    # token labels: val
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 143:2: -> ^( SCOPE $val)
                    # GOC.g:143:5: ^( SCOPE $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_SCOPE.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt26 == 5:
                    # GOC.g:144:5: INHERITANCE ':' (val= 'final' | val= 'virtual' | val= 'abstract' ) ';'
                    pass 
                    INHERITANCE137=self.match(self.input, INHERITANCE, self.FOLLOW_INHERITANCE_in_methodElement1134) 
                    stream_INHERITANCE.add(INHERITANCE137)
                    char_literal138=self.match(self.input, 62, self.FOLLOW_62_in_methodElement1136) 
                    stream_62.add(char_literal138)
                    # GOC.g:144:21: (val= 'final' | val= 'virtual' | val= 'abstract' )
                    alt25 = 3
                    LA25 = self.input.LA(1)
                    if LA25 == 68:
                        alt25 = 1
                    elif LA25 == 69:
                        alt25 = 2
                    elif LA25 == ABSTRACT:
                        alt25 = 3
                    else:
                        nvae = NoViableAltException("", 25, 0, self.input)

                        raise nvae

                    if alt25 == 1:
                        # GOC.g:144:22: val= 'final'
                        pass 
                        val=self.match(self.input, 68, self.FOLLOW_68_in_methodElement1141) 
                        stream_68.add(val)


                    elif alt25 == 2:
                        # GOC.g:144:34: val= 'virtual'
                        pass 
                        val=self.match(self.input, 69, self.FOLLOW_69_in_methodElement1145) 
                        stream_69.add(val)


                    elif alt25 == 3:
                        # GOC.g:144:48: val= 'abstract'
                        pass 
                        val=self.match(self.input, ABSTRACT, self.FOLLOW_ABSTRACT_in_methodElement1149) 
                        stream_ABSTRACT.add(val)



                    char_literal139=self.match(self.input, 59, self.FOLLOW_59_in_methodElement1152) 
                    stream_59.add(char_literal139)

                    # AST Rewrite
                    # elements: INHERITANCE, val
                    # token labels: val
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 145:2: -> ^( INHERITANCE $val)
                    # GOC.g:145:5: ^( INHERITANCE $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_INHERITANCE.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "methodElement"

    class constructorElement_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.constructorElement_return, self).__init__()

            self.tree = None




    # $ANTLR start "constructorElement"
    # GOC.g:148:1: constructorElement : ( PARAMETER ID '{' 'type' ':' typeArg ';' ( parameterElement )? '}' -> ^( PARAMETER ID typeArg ( parameterElement )? ) | {...}? => INIT_PROPERTIES '{' ( init_prop )+ '}' -> ^( INIT_PROPERTIES ( init_prop )+ ) );
    def constructorElement(self, ):

        retval = self.constructorElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PARAMETER140 = None
        ID141 = None
        char_literal142 = None
        string_literal143 = None
        char_literal144 = None
        char_literal146 = None
        char_literal148 = None
        INIT_PROPERTIES149 = None
        char_literal150 = None
        char_literal152 = None
        typeArg145 = None

        parameterElement147 = None

        init_prop151 = None


        PARAMETER140_tree = None
        ID141_tree = None
        char_literal142_tree = None
        string_literal143_tree = None
        char_literal144_tree = None
        char_literal146_tree = None
        char_literal148_tree = None
        INIT_PROPERTIES149_tree = None
        char_literal150_tree = None
        char_literal152_tree = None
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_INIT_PROPERTIES = RewriteRuleTokenStream(self._adaptor, "token INIT_PROPERTIES")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_PARAMETER = RewriteRuleTokenStream(self._adaptor, "token PARAMETER")
        stream_TYPE = RewriteRuleTokenStream(self._adaptor, "token TYPE")
        stream_typeArg = RewriteRuleSubtreeStream(self._adaptor, "rule typeArg")
        stream_parameterElement = RewriteRuleSubtreeStream(self._adaptor, "rule parameterElement")
        stream_init_prop = RewriteRuleSubtreeStream(self._adaptor, "rule init_prop")
        try:
            try:
                # GOC.g:149:2: ( PARAMETER ID '{' 'type' ':' typeArg ';' ( parameterElement )? '}' -> ^( PARAMETER ID typeArg ( parameterElement )? ) | {...}? => INIT_PROPERTIES '{' ( init_prop )+ '}' -> ^( INIT_PROPERTIES ( init_prop )+ ) )
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == PARAMETER) :
                    alt29 = 1
                elif (LA29_0 == INIT_PROPERTIES) and ((self.classMember_stack[-1].with_constructor)):
                    alt29 = 2
                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae

                if alt29 == 1:
                    # GOC.g:149:4: PARAMETER ID '{' 'type' ':' typeArg ';' ( parameterElement )? '}'
                    pass 
                    PARAMETER140=self.match(self.input, PARAMETER, self.FOLLOW_PARAMETER_in_constructorElement1174) 
                    stream_PARAMETER.add(PARAMETER140)
                    ID141=self.match(self.input, ID, self.FOLLOW_ID_in_constructorElement1176) 
                    stream_ID.add(ID141)
                    char_literal142=self.match(self.input, 57, self.FOLLOW_57_in_constructorElement1178) 
                    stream_57.add(char_literal142)
                    string_literal143=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_constructorElement1180) 
                    stream_TYPE.add(string_literal143)
                    char_literal144=self.match(self.input, 62, self.FOLLOW_62_in_constructorElement1182) 
                    stream_62.add(char_literal144)
                    self._state.following.append(self.FOLLOW_typeArg_in_constructorElement1184)
                    typeArg145 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg145.tree)
                    char_literal146=self.match(self.input, 59, self.FOLLOW_59_in_constructorElement1186) 
                    stream_59.add(char_literal146)
                    # GOC.g:149:44: ( parameterElement )?
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == MODIFIERS) :
                        alt27 = 1
                    elif (LA27_0 == 70) and ((self.classMember_stack[-1].with_constructor)):
                        alt27 = 1
                    if alt27 == 1:
                        # GOC.g:149:44: parameterElement
                        pass 
                        self._state.following.append(self.FOLLOW_parameterElement_in_constructorElement1188)
                        parameterElement147 = self.parameterElement()

                        self._state.following.pop()
                        stream_parameterElement.add(parameterElement147.tree)



                    char_literal148=self.match(self.input, 58, self.FOLLOW_58_in_constructorElement1191) 
                    stream_58.add(char_literal148)

                    # AST Rewrite
                    # elements: parameterElement, PARAMETER, typeArg, ID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 150:2: -> ^( PARAMETER ID typeArg ( parameterElement )? )
                    # GOC.g:150:6: ^( PARAMETER ID typeArg ( parameterElement )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_PARAMETER.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())
                    self._adaptor.addChild(root_1, stream_typeArg.nextTree())
                    # GOC.g:150:29: ( parameterElement )?
                    if stream_parameterElement.hasNext():
                        self._adaptor.addChild(root_1, stream_parameterElement.nextTree())


                    stream_parameterElement.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt29 == 2:
                    # GOC.g:151:6: {...}? => INIT_PROPERTIES '{' ( init_prop )+ '}'
                    pass 
                    if not ((self.classMember_stack[-1].with_constructor)):
                        raise FailedPredicateException(self.input, "constructorElement", "$classMember::with_constructor")

                    INIT_PROPERTIES149=self.match(self.input, INIT_PROPERTIES, self.FOLLOW_INIT_PROPERTIES_in_constructorElement1216) 
                    stream_INIT_PROPERTIES.add(INIT_PROPERTIES149)
                    char_literal150=self.match(self.input, 57, self.FOLLOW_57_in_constructorElement1218) 
                    stream_57.add(char_literal150)
                    # GOC.g:151:62: ( init_prop )+
                    cnt28 = 0
                    while True: #loop28
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if (LA28_0 == ID) :
                            alt28 = 1


                        if alt28 == 1:
                            # GOC.g:151:62: init_prop
                            pass 
                            self._state.following.append(self.FOLLOW_init_prop_in_constructorElement1220)
                            init_prop151 = self.init_prop()

                            self._state.following.pop()
                            stream_init_prop.add(init_prop151.tree)


                        else:
                            if cnt28 >= 1:
                                break #loop28

                            eee = EarlyExitException(28, self.input)
                            raise eee

                        cnt28 += 1
                    char_literal152=self.match(self.input, 58, self.FOLLOW_58_in_constructorElement1223) 
                    stream_58.add(char_literal152)

                    # AST Rewrite
                    # elements: INIT_PROPERTIES, init_prop
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 152:2: -> ^( INIT_PROPERTIES ( init_prop )+ )
                    # GOC.g:152:6: ^( INIT_PROPERTIES ( init_prop )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_INIT_PROPERTIES.nextNode(), root_1)

                    # GOC.g:152:24: ( init_prop )+
                    if not (stream_init_prop.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_init_prop.hasNext():
                        self._adaptor.addChild(root_1, stream_init_prop.nextTree())


                    stream_init_prop.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "constructorElement"

    class parameterElement_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.parameterElement_return, self).__init__()

            self.tree = None




    # $ANTLR start "parameterElement"
    # GOC.g:155:1: parameterElement : ( modifiers | {...}? => 'bind_property' ':' ID ';' -> ^( BIND_PROPERTY ID ) );
    def parameterElement(self, ):

        retval = self.parameterElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal154 = None
        char_literal155 = None
        ID156 = None
        char_literal157 = None
        modifiers153 = None


        string_literal154_tree = None
        char_literal155_tree = None
        ID156_tree = None
        char_literal157_tree = None
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_70 = RewriteRuleTokenStream(self._adaptor, "token 70")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")

        try:
            try:
                # GOC.g:156:5: ( modifiers | {...}? => 'bind_property' ':' ID ';' -> ^( BIND_PROPERTY ID ) )
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == MODIFIERS) :
                    alt30 = 1
                elif (LA30_0 == 70) and ((self.classMember_stack[-1].with_constructor)):
                    alt30 = 2
                else:
                    nvae = NoViableAltException("", 30, 0, self.input)

                    raise nvae

                if alt30 == 1:
                    # GOC.g:156:9: modifiers
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_modifiers_in_parameterElement1250)
                    modifiers153 = self.modifiers()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, modifiers153.tree)


                elif alt30 == 2:
                    # GOC.g:157:9: {...}? => 'bind_property' ':' ID ';'
                    pass 
                    if not ((self.classMember_stack[-1].with_constructor)):
                        raise FailedPredicateException(self.input, "parameterElement", "$classMember::with_constructor")

                    string_literal154=self.match(self.input, 70, self.FOLLOW_70_in_parameterElement1263) 
                    stream_70.add(string_literal154)
                    char_literal155=self.match(self.input, 62, self.FOLLOW_62_in_parameterElement1265) 
                    stream_62.add(char_literal155)
                    ID156=self.match(self.input, ID, self.FOLLOW_ID_in_parameterElement1267) 
                    stream_ID.add(ID156)
                    char_literal157=self.match(self.input, 59, self.FOLLOW_59_in_parameterElement1269) 
                    stream_59.add(char_literal157)

                    # AST Rewrite
                    # elements: ID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 157:72: -> ^( BIND_PROPERTY ID )
                    # GOC.g:157:75: ^( BIND_PROPERTY ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BIND_PROPERTY, "BIND_PROPERTY"), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "parameterElement"

    class init_prop_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.init_prop_return, self).__init__()

            self.tree = None




    # $ANTLR start "init_prop"
    # GOC.g:160:1: init_prop : (name= ID ':' value= STRING ';' -> ^( INIT_PROPERTY $name $value) | name= ID ':' enum= typeName '.' code= ID ';' -> ^( INIT_PROPERTY $name $enum $code) );
    def init_prop(self, ):

        retval = self.init_prop_return()
        retval.start = self.input.LT(1)

        root_0 = None

        name = None
        value = None
        code = None
        char_literal158 = None
        char_literal159 = None
        char_literal160 = None
        char_literal161 = None
        char_literal162 = None
        enum = None


        name_tree = None
        value_tree = None
        code_tree = None
        char_literal158_tree = None
        char_literal159_tree = None
        char_literal160_tree = None
        char_literal161_tree = None
        char_literal162_tree = None
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_71 = RewriteRuleTokenStream(self._adaptor, "token 71")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")
        stream_typeName = RewriteRuleSubtreeStream(self._adaptor, "rule typeName")
        try:
            try:
                # GOC.g:161:5: (name= ID ':' value= STRING ';' -> ^( INIT_PROPERTY $name $value) | name= ID ':' enum= typeName '.' code= ID ';' -> ^( INIT_PROPERTY $name $enum $code) )
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == ID) :
                    LA31_1 = self.input.LA(2)

                    if (LA31_1 == 62) :
                        LA31_2 = self.input.LA(3)

                        if (LA31_2 == STRING) :
                            alt31 = 1
                        elif (LA31_2 == ID or (73 <= LA31_2 <= 78) or (91 <= LA31_2 <= 93) or LA31_2 == 96) :
                            alt31 = 2
                        else:
                            nvae = NoViableAltException("", 31, 2, self.input)

                            raise nvae

                    else:
                        nvae = NoViableAltException("", 31, 1, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 31, 0, self.input)

                    raise nvae

                if alt31 == 1:
                    # GOC.g:161:9: name= ID ':' value= STRING ';'
                    pass 
                    name=self.match(self.input, ID, self.FOLLOW_ID_in_init_prop1298) 
                    stream_ID.add(name)
                    char_literal158=self.match(self.input, 62, self.FOLLOW_62_in_init_prop1300) 
                    stream_62.add(char_literal158)
                    value=self.match(self.input, STRING, self.FOLLOW_STRING_in_init_prop1304) 
                    stream_STRING.add(value)
                    char_literal159=self.match(self.input, 59, self.FOLLOW_59_in_init_prop1306) 
                    stream_59.add(char_literal159)

                    # AST Rewrite
                    # elements: name, value
                    # token labels: name, value
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0
                    stream_name = RewriteRuleTokenStream(self._adaptor, "token name", name)
                    stream_value = RewriteRuleTokenStream(self._adaptor, "token value", value)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 162:5: -> ^( INIT_PROPERTY $name $value)
                    # GOC.g:162:9: ^( INIT_PROPERTY $name $value)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(INIT_PROPERTY, "INIT_PROPERTY"), root_1)

                    self._adaptor.addChild(root_1, stream_name.nextNode())
                    self._adaptor.addChild(root_1, stream_value.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt31 == 2:
                    # GOC.g:163:9: name= ID ':' enum= typeName '.' code= ID ';'
                    pass 
                    name=self.match(self.input, ID, self.FOLLOW_ID_in_init_prop1335) 
                    stream_ID.add(name)
                    char_literal160=self.match(self.input, 62, self.FOLLOW_62_in_init_prop1337) 
                    stream_62.add(char_literal160)
                    self._state.following.append(self.FOLLOW_typeName_in_init_prop1341)
                    enum = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(enum.tree)
                    char_literal161=self.match(self.input, 71, self.FOLLOW_71_in_init_prop1343) 
                    stream_71.add(char_literal161)
                    code=self.match(self.input, ID, self.FOLLOW_ID_in_init_prop1347) 
                    stream_ID.add(code)
                    char_literal162=self.match(self.input, 59, self.FOLLOW_59_in_init_prop1349) 
                    stream_59.add(char_literal162)

                    # AST Rewrite
                    # elements: enum, name, code
                    # token labels: name, code
                    # rule labels: retval, enum
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0
                    stream_name = RewriteRuleTokenStream(self._adaptor, "token name", name)
                    stream_code = RewriteRuleTokenStream(self._adaptor, "token code", code)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if enum is not None:
                        stream_enum = RewriteRuleSubtreeStream(self._adaptor, "rule enum", enum.tree)
                    else:
                        stream_enum = RewriteRuleSubtreeStream(self._adaptor, "token enum", None)


                    root_0 = self._adaptor.nil()
                    # 164:5: -> ^( INIT_PROPERTY $name $enum $code)
                    # GOC.g:164:9: ^( INIT_PROPERTY $name $enum $code)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(INIT_PROPERTY, "INIT_PROPERTY"), root_1)

                    self._adaptor.addChild(root_1, stream_name.nextNode())
                    self._adaptor.addChild(root_1, stream_enum.nextTree())
                    self._adaptor.addChild(root_1, stream_code.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "init_prop"

    class modifiers_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.modifiers_return, self).__init__()

            self.tree = None




    # $ANTLR start "modifiers"
    # GOC.g:167:1: modifiers : MODIFIERS ':' 'const' ';' -> ^( MODIFIERS 'const' ) ;
    def modifiers(self, ):

        retval = self.modifiers_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MODIFIERS163 = None
        char_literal164 = None
        string_literal165 = None
        char_literal166 = None

        MODIFIERS163_tree = None
        char_literal164_tree = None
        string_literal165_tree = None
        char_literal166_tree = None
        stream_MODIFIERS = RewriteRuleTokenStream(self._adaptor, "token MODIFIERS")
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_72 = RewriteRuleTokenStream(self._adaptor, "token 72")

        try:
            try:
                # GOC.g:168:2: ( MODIFIERS ':' 'const' ';' -> ^( MODIFIERS 'const' ) )
                # GOC.g:168:4: MODIFIERS ':' 'const' ';'
                pass 
                MODIFIERS163=self.match(self.input, MODIFIERS, self.FOLLOW_MODIFIERS_in_modifiers1383) 
                stream_MODIFIERS.add(MODIFIERS163)
                char_literal164=self.match(self.input, 62, self.FOLLOW_62_in_modifiers1385) 
                stream_62.add(char_literal164)
                string_literal165=self.match(self.input, 72, self.FOLLOW_72_in_modifiers1387) 
                stream_72.add(string_literal165)
                char_literal166=self.match(self.input, 59, self.FOLLOW_59_in_modifiers1389) 
                stream_59.add(char_literal166)

                # AST Rewrite
                # elements: 72, MODIFIERS
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 168:30: -> ^( MODIFIERS 'const' )
                # GOC.g:168:33: ^( MODIFIERS 'const' )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_MODIFIERS.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_72.nextNode())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "modifiers"

    class propertyElement_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.propertyElement_return, self).__init__()

            self.tree = None




    # $ANTLR start "propertyElement"
    # GOC.g:171:1: propertyElement : ( 'type' ':' (val= 'boolean' | val= 'integer' | val= 'float' | val= 'double' | val= 'string' | val= 'pointer' | val= 'object' | val= 'enumeration' ) ';' -> ^( PROP_TYPE $val) | 'access' ':' (val= 'read-only' | val= 'initial-write' | val= 'read-write' ) ';' -> ^( PROP_ACCESS $val) | 'description' ':' STRING ';' -> ^( PROP_DESC STRING ) | 'gtype' ':' ID ';' -> ^( PROP_GTYPE ID ) | 'gtype' ':' GTYPENAME '(' typeName ')' ';' -> ^( PROP_GTYPE ^( GTYPENAME typeName ) ) | 'min' ':' STRING ';' -> ^( PROP_MIN STRING ) | 'min' ':' enum= typeName '.' code= ID ';' -> ^( PROP_MIN $enum $code) | 'max' ':' STRING ';' -> ^( PROP_MAX STRING ) | 'max' ':' enum= typeName '.' code= ID ';' -> ^( PROP_MAX $enum $code) | 'default' ':' STRING ';' -> ^( PROP_DEFAULT STRING ) | 'default' ':' enum= typeName '.' code= ID ';' -> ^( PROP_DEFAULT $enum $code) | AUTO_CREATE ';' );
    def propertyElement(self, ):

        retval = self.propertyElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        val = None
        code = None
        string_literal167 = None
        char_literal168 = None
        char_literal169 = None
        string_literal170 = None
        char_literal171 = None
        char_literal172 = None
        string_literal173 = None
        char_literal174 = None
        STRING175 = None
        char_literal176 = None
        string_literal177 = None
        char_literal178 = None
        ID179 = None
        char_literal180 = None
        string_literal181 = None
        char_literal182 = None
        GTYPENAME183 = None
        char_literal184 = None
        char_literal186 = None
        char_literal187 = None
        string_literal188 = None
        char_literal189 = None
        STRING190 = None
        char_literal191 = None
        string_literal192 = None
        char_literal193 = None
        char_literal194 = None
        char_literal195 = None
        string_literal196 = None
        char_literal197 = None
        STRING198 = None
        char_literal199 = None
        string_literal200 = None
        char_literal201 = None
        char_literal202 = None
        char_literal203 = None
        string_literal204 = None
        char_literal205 = None
        STRING206 = None
        char_literal207 = None
        string_literal208 = None
        char_literal209 = None
        char_literal210 = None
        char_literal211 = None
        AUTO_CREATE212 = None
        char_literal213 = None
        enum = None

        typeName185 = None


        val_tree = None
        code_tree = None
        string_literal167_tree = None
        char_literal168_tree = None
        char_literal169_tree = None
        string_literal170_tree = None
        char_literal171_tree = None
        char_literal172_tree = None
        string_literal173_tree = None
        char_literal174_tree = None
        STRING175_tree = None
        char_literal176_tree = None
        string_literal177_tree = None
        char_literal178_tree = None
        ID179_tree = None
        char_literal180_tree = None
        string_literal181_tree = None
        char_literal182_tree = None
        GTYPENAME183_tree = None
        char_literal184_tree = None
        char_literal186_tree = None
        char_literal187_tree = None
        string_literal188_tree = None
        char_literal189_tree = None
        STRING190_tree = None
        char_literal191_tree = None
        string_literal192_tree = None
        char_literal193_tree = None
        char_literal194_tree = None
        char_literal195_tree = None
        string_literal196_tree = None
        char_literal197_tree = None
        STRING198_tree = None
        char_literal199_tree = None
        string_literal200_tree = None
        char_literal201_tree = None
        char_literal202_tree = None
        char_literal203_tree = None
        string_literal204_tree = None
        char_literal205_tree = None
        STRING206_tree = None
        char_literal207_tree = None
        string_literal208_tree = None
        char_literal209_tree = None
        char_literal210_tree = None
        char_literal211_tree = None
        AUTO_CREATE212_tree = None
        char_literal213_tree = None
        stream_79 = RewriteRuleTokenStream(self._adaptor, "token 79")
        stream_78 = RewriteRuleTokenStream(self._adaptor, "token 78")
        stream_77 = RewriteRuleTokenStream(self._adaptor, "token 77")
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_GTYPENAME = RewriteRuleTokenStream(self._adaptor, "token GTYPENAME")
        stream_GTYPE = RewriteRuleTokenStream(self._adaptor, "token GTYPE")
        stream_82 = RewriteRuleTokenStream(self._adaptor, "token 82")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_83 = RewriteRuleTokenStream(self._adaptor, "token 83")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_80 = RewriteRuleTokenStream(self._adaptor, "token 80")
        stream_81 = RewriteRuleTokenStream(self._adaptor, "token 81")
        stream_86 = RewriteRuleTokenStream(self._adaptor, "token 86")
        stream_87 = RewriteRuleTokenStream(self._adaptor, "token 87")
        stream_TYPE = RewriteRuleTokenStream(self._adaptor, "token TYPE")
        stream_84 = RewriteRuleTokenStream(self._adaptor, "token 84")
        stream_85 = RewriteRuleTokenStream(self._adaptor, "token 85")
        stream_90 = RewriteRuleTokenStream(self._adaptor, "token 90")
        stream_71 = RewriteRuleTokenStream(self._adaptor, "token 71")
        stream_73 = RewriteRuleTokenStream(self._adaptor, "token 73")
        stream_74 = RewriteRuleTokenStream(self._adaptor, "token 74")
        stream_75 = RewriteRuleTokenStream(self._adaptor, "token 75")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")
        stream_88 = RewriteRuleTokenStream(self._adaptor, "token 88")
        stream_76 = RewriteRuleTokenStream(self._adaptor, "token 76")
        stream_89 = RewriteRuleTokenStream(self._adaptor, "token 89")
        stream_typeName = RewriteRuleSubtreeStream(self._adaptor, "rule typeName")
        try:
            try:
                # GOC.g:172:5: ( 'type' ':' (val= 'boolean' | val= 'integer' | val= 'float' | val= 'double' | val= 'string' | val= 'pointer' | val= 'object' | val= 'enumeration' ) ';' -> ^( PROP_TYPE $val) | 'access' ':' (val= 'read-only' | val= 'initial-write' | val= 'read-write' ) ';' -> ^( PROP_ACCESS $val) | 'description' ':' STRING ';' -> ^( PROP_DESC STRING ) | 'gtype' ':' ID ';' -> ^( PROP_GTYPE ID ) | 'gtype' ':' GTYPENAME '(' typeName ')' ';' -> ^( PROP_GTYPE ^( GTYPENAME typeName ) ) | 'min' ':' STRING ';' -> ^( PROP_MIN STRING ) | 'min' ':' enum= typeName '.' code= ID ';' -> ^( PROP_MIN $enum $code) | 'max' ':' STRING ';' -> ^( PROP_MAX STRING ) | 'max' ':' enum= typeName '.' code= ID ';' -> ^( PROP_MAX $enum $code) | 'default' ':' STRING ';' -> ^( PROP_DEFAULT STRING ) | 'default' ':' enum= typeName '.' code= ID ';' -> ^( PROP_DEFAULT $enum $code) | AUTO_CREATE ';' )
                alt34 = 12
                alt34 = self.dfa34.predict(self.input)
                if alt34 == 1:
                    # GOC.g:172:9: 'type' ':' (val= 'boolean' | val= 'integer' | val= 'float' | val= 'double' | val= 'string' | val= 'pointer' | val= 'object' | val= 'enumeration' ) ';'
                    pass 
                    string_literal167=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_propertyElement1413) 
                    stream_TYPE.add(string_literal167)
                    char_literal168=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1415) 
                    stream_62.add(char_literal168)
                    # GOC.g:172:20: (val= 'boolean' | val= 'integer' | val= 'float' | val= 'double' | val= 'string' | val= 'pointer' | val= 'object' | val= 'enumeration' )
                    alt32 = 8
                    LA32 = self.input.LA(1)
                    if LA32 == 73:
                        alt32 = 1
                    elif LA32 == 74:
                        alt32 = 2
                    elif LA32 == 75:
                        alt32 = 3
                    elif LA32 == 76:
                        alt32 = 4
                    elif LA32 == 77:
                        alt32 = 5
                    elif LA32 == 78:
                        alt32 = 6
                    elif LA32 == 79:
                        alt32 = 7
                    elif LA32 == 80:
                        alt32 = 8
                    else:
                        nvae = NoViableAltException("", 32, 0, self.input)

                        raise nvae

                    if alt32 == 1:
                        # GOC.g:172:21: val= 'boolean'
                        pass 
                        val=self.match(self.input, 73, self.FOLLOW_73_in_propertyElement1420) 
                        stream_73.add(val)


                    elif alt32 == 2:
                        # GOC.g:172:35: val= 'integer'
                        pass 
                        val=self.match(self.input, 74, self.FOLLOW_74_in_propertyElement1424) 
                        stream_74.add(val)


                    elif alt32 == 3:
                        # GOC.g:172:49: val= 'float'
                        pass 
                        val=self.match(self.input, 75, self.FOLLOW_75_in_propertyElement1428) 
                        stream_75.add(val)


                    elif alt32 == 4:
                        # GOC.g:172:61: val= 'double'
                        pass 
                        val=self.match(self.input, 76, self.FOLLOW_76_in_propertyElement1432) 
                        stream_76.add(val)


                    elif alt32 == 5:
                        # GOC.g:173:5: val= 'string'
                        pass 
                        val=self.match(self.input, 77, self.FOLLOW_77_in_propertyElement1441) 
                        stream_77.add(val)


                    elif alt32 == 6:
                        # GOC.g:173:18: val= 'pointer'
                        pass 
                        val=self.match(self.input, 78, self.FOLLOW_78_in_propertyElement1445) 
                        stream_78.add(val)


                    elif alt32 == 7:
                        # GOC.g:173:32: val= 'object'
                        pass 
                        val=self.match(self.input, 79, self.FOLLOW_79_in_propertyElement1449) 
                        stream_79.add(val)


                    elif alt32 == 8:
                        # GOC.g:173:45: val= 'enumeration'
                        pass 
                        val=self.match(self.input, 80, self.FOLLOW_80_in_propertyElement1453) 
                        stream_80.add(val)



                    char_literal169=self.match(self.input, 59, self.FOLLOW_59_in_propertyElement1456) 
                    stream_59.add(char_literal169)

                    # AST Rewrite
                    # elements: val
                    # token labels: val
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 174:5: -> ^( PROP_TYPE $val)
                    # GOC.g:174:9: ^( PROP_TYPE $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_TYPE, "PROP_TYPE"), root_1)

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt34 == 2:
                    # GOC.g:175:9: 'access' ':' (val= 'read-only' | val= 'initial-write' | val= 'read-write' ) ';'
                    pass 
                    string_literal170=self.match(self.input, 81, self.FOLLOW_81_in_propertyElement1480) 
                    stream_81.add(string_literal170)
                    char_literal171=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1482) 
                    stream_62.add(char_literal171)
                    # GOC.g:175:22: (val= 'read-only' | val= 'initial-write' | val= 'read-write' )
                    alt33 = 3
                    LA33 = self.input.LA(1)
                    if LA33 == 82:
                        alt33 = 1
                    elif LA33 == 83:
                        alt33 = 2
                    elif LA33 == 84:
                        alt33 = 3
                    else:
                        nvae = NoViableAltException("", 33, 0, self.input)

                        raise nvae

                    if alt33 == 1:
                        # GOC.g:175:23: val= 'read-only'
                        pass 
                        val=self.match(self.input, 82, self.FOLLOW_82_in_propertyElement1487) 
                        stream_82.add(val)


                    elif alt33 == 2:
                        # GOC.g:175:39: val= 'initial-write'
                        pass 
                        val=self.match(self.input, 83, self.FOLLOW_83_in_propertyElement1491) 
                        stream_83.add(val)


                    elif alt33 == 3:
                        # GOC.g:175:59: val= 'read-write'
                        pass 
                        val=self.match(self.input, 84, self.FOLLOW_84_in_propertyElement1495) 
                        stream_84.add(val)



                    char_literal172=self.match(self.input, 59, self.FOLLOW_59_in_propertyElement1498) 
                    stream_59.add(char_literal172)

                    # AST Rewrite
                    # elements: val
                    # token labels: val
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 176:5: -> ^( PROP_ACCESS $val)
                    # GOC.g:176:9: ^( PROP_ACCESS $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_ACCESS, "PROP_ACCESS"), root_1)

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt34 == 3:
                    # GOC.g:177:9: 'description' ':' STRING ';'
                    pass 
                    string_literal173=self.match(self.input, 85, self.FOLLOW_85_in_propertyElement1522) 
                    stream_85.add(string_literal173)
                    char_literal174=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1524) 
                    stream_62.add(char_literal174)
                    STRING175=self.match(self.input, STRING, self.FOLLOW_STRING_in_propertyElement1526) 
                    stream_STRING.add(STRING175)
                    char_literal176=self.match(self.input, 59, self.FOLLOW_59_in_propertyElement1528) 
                    stream_59.add(char_literal176)

                    # AST Rewrite
                    # elements: STRING
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 177:38: -> ^( PROP_DESC STRING )
                    # GOC.g:177:41: ^( PROP_DESC STRING )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_DESC, "PROP_DESC"), root_1)

                    self._adaptor.addChild(root_1, stream_STRING.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt34 == 4:
                    # GOC.g:178:9: 'gtype' ':' ID ';'
                    pass 
                    string_literal177=self.match(self.input, GTYPE, self.FOLLOW_GTYPE_in_propertyElement1546) 
                    stream_GTYPE.add(string_literal177)
                    char_literal178=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1548) 
                    stream_62.add(char_literal178)
                    ID179=self.match(self.input, ID, self.FOLLOW_ID_in_propertyElement1550) 
                    stream_ID.add(ID179)
                    char_literal180=self.match(self.input, 59, self.FOLLOW_59_in_propertyElement1552) 
                    stream_59.add(char_literal180)

                    # AST Rewrite
                    # elements: ID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 179:5: -> ^( PROP_GTYPE ID )
                    # GOC.g:179:9: ^( PROP_GTYPE ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_GTYPE, "PROP_GTYPE"), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt34 == 5:
                    # GOC.g:180:9: 'gtype' ':' GTYPENAME '(' typeName ')' ';'
                    pass 
                    string_literal181=self.match(self.input, GTYPE, self.FOLLOW_GTYPE_in_propertyElement1575) 
                    stream_GTYPE.add(string_literal181)
                    char_literal182=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1577) 
                    stream_62.add(char_literal182)
                    GTYPENAME183=self.match(self.input, GTYPENAME, self.FOLLOW_GTYPENAME_in_propertyElement1579) 
                    stream_GTYPENAME.add(GTYPENAME183)
                    char_literal184=self.match(self.input, 86, self.FOLLOW_86_in_propertyElement1581) 
                    stream_86.add(char_literal184)
                    self._state.following.append(self.FOLLOW_typeName_in_propertyElement1583)
                    typeName185 = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(typeName185.tree)
                    char_literal186=self.match(self.input, 87, self.FOLLOW_87_in_propertyElement1585) 
                    stream_87.add(char_literal186)
                    char_literal187=self.match(self.input, 59, self.FOLLOW_59_in_propertyElement1587) 
                    stream_59.add(char_literal187)

                    # AST Rewrite
                    # elements: typeName, GTYPENAME
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 181:5: -> ^( PROP_GTYPE ^( GTYPENAME typeName ) )
                    # GOC.g:181:9: ^( PROP_GTYPE ^( GTYPENAME typeName ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_GTYPE, "PROP_GTYPE"), root_1)

                    # GOC.g:181:22: ^( GTYPENAME typeName )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(stream_GTYPENAME.nextNode(), root_2)

                    self._adaptor.addChild(root_2, stream_typeName.nextTree())

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt34 == 6:
                    # GOC.g:182:9: 'min' ':' STRING ';'
                    pass 
                    string_literal188=self.match(self.input, 88, self.FOLLOW_88_in_propertyElement1614) 
                    stream_88.add(string_literal188)
                    char_literal189=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1616) 
                    stream_62.add(char_literal189)
                    STRING190=self.match(self.input, STRING, self.FOLLOW_STRING_in_propertyElement1618) 
                    stream_STRING.add(STRING190)
                    char_literal191=self.match(self.input, 59, self.FOLLOW_59_in_propertyElement1620) 
                    stream_59.add(char_literal191)

                    # AST Rewrite
                    # elements: STRING
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 182:30: -> ^( PROP_MIN STRING )
                    # GOC.g:182:33: ^( PROP_MIN STRING )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_MIN, "PROP_MIN"), root_1)

                    self._adaptor.addChild(root_1, stream_STRING.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt34 == 7:
                    # GOC.g:183:7: 'min' ':' enum= typeName '.' code= ID ';'
                    pass 
                    string_literal192=self.match(self.input, 88, self.FOLLOW_88_in_propertyElement1636) 
                    stream_88.add(string_literal192)
                    char_literal193=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1638) 
                    stream_62.add(char_literal193)
                    self._state.following.append(self.FOLLOW_typeName_in_propertyElement1642)
                    enum = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(enum.tree)
                    char_literal194=self.match(self.input, 71, self.FOLLOW_71_in_propertyElement1644) 
                    stream_71.add(char_literal194)
                    code=self.match(self.input, ID, self.FOLLOW_ID_in_propertyElement1648) 
                    stream_ID.add(code)
                    char_literal195=self.match(self.input, 59, self.FOLLOW_59_in_propertyElement1650) 
                    stream_59.add(char_literal195)

                    # AST Rewrite
                    # elements: enum, code
                    # token labels: code
                    # rule labels: retval, enum
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0
                    stream_code = RewriteRuleTokenStream(self._adaptor, "token code", code)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if enum is not None:
                        stream_enum = RewriteRuleSubtreeStream(self._adaptor, "rule enum", enum.tree)
                    else:
                        stream_enum = RewriteRuleSubtreeStream(self._adaptor, "token enum", None)


                    root_0 = self._adaptor.nil()
                    # 183:47: -> ^( PROP_MIN $enum $code)
                    # GOC.g:183:50: ^( PROP_MIN $enum $code)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_MIN, "PROP_MIN"), root_1)

                    self._adaptor.addChild(root_1, stream_enum.nextTree())
                    self._adaptor.addChild(root_1, stream_code.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt34 == 8:
                    # GOC.g:184:9: 'max' ':' STRING ';'
                    pass 
                    string_literal196=self.match(self.input, 89, self.FOLLOW_89_in_propertyElement1672) 
                    stream_89.add(string_literal196)
                    char_literal197=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1674) 
                    stream_62.add(char_literal197)
                    STRING198=self.match(self.input, STRING, self.FOLLOW_STRING_in_propertyElement1676) 
                    stream_STRING.add(STRING198)
                    char_literal199=self.match(self.input, 59, self.FOLLOW_59_in_propertyElement1678) 
                    stream_59.add(char_literal199)

                    # AST Rewrite
                    # elements: STRING
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 184:30: -> ^( PROP_MAX STRING )
                    # GOC.g:184:33: ^( PROP_MAX STRING )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_MAX, "PROP_MAX"), root_1)

                    self._adaptor.addChild(root_1, stream_STRING.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt34 == 9:
                    # GOC.g:185:7: 'max' ':' enum= typeName '.' code= ID ';'
                    pass 
                    string_literal200=self.match(self.input, 89, self.FOLLOW_89_in_propertyElement1694) 
                    stream_89.add(string_literal200)
                    char_literal201=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1696) 
                    stream_62.add(char_literal201)
                    self._state.following.append(self.FOLLOW_typeName_in_propertyElement1700)
                    enum = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(enum.tree)
                    char_literal202=self.match(self.input, 71, self.FOLLOW_71_in_propertyElement1702) 
                    stream_71.add(char_literal202)
                    code=self.match(self.input, ID, self.FOLLOW_ID_in_propertyElement1706) 
                    stream_ID.add(code)
                    char_literal203=self.match(self.input, 59, self.FOLLOW_59_in_propertyElement1708) 
                    stream_59.add(char_literal203)

                    # AST Rewrite
                    # elements: code, enum
                    # token labels: code
                    # rule labels: retval, enum
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0
                    stream_code = RewriteRuleTokenStream(self._adaptor, "token code", code)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if enum is not None:
                        stream_enum = RewriteRuleSubtreeStream(self._adaptor, "rule enum", enum.tree)
                    else:
                        stream_enum = RewriteRuleSubtreeStream(self._adaptor, "token enum", None)


                    root_0 = self._adaptor.nil()
                    # 185:47: -> ^( PROP_MAX $enum $code)
                    # GOC.g:185:50: ^( PROP_MAX $enum $code)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_MAX, "PROP_MAX"), root_1)

                    self._adaptor.addChild(root_1, stream_enum.nextTree())
                    self._adaptor.addChild(root_1, stream_code.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt34 == 10:
                    # GOC.g:186:9: 'default' ':' STRING ';'
                    pass 
                    string_literal204=self.match(self.input, 90, self.FOLLOW_90_in_propertyElement1730) 
                    stream_90.add(string_literal204)
                    char_literal205=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1732) 
                    stream_62.add(char_literal205)
                    STRING206=self.match(self.input, STRING, self.FOLLOW_STRING_in_propertyElement1734) 
                    stream_STRING.add(STRING206)
                    char_literal207=self.match(self.input, 59, self.FOLLOW_59_in_propertyElement1736) 
                    stream_59.add(char_literal207)

                    # AST Rewrite
                    # elements: STRING
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 186:34: -> ^( PROP_DEFAULT STRING )
                    # GOC.g:186:37: ^( PROP_DEFAULT STRING )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_DEFAULT, "PROP_DEFAULT"), root_1)

                    self._adaptor.addChild(root_1, stream_STRING.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt34 == 11:
                    # GOC.g:187:7: 'default' ':' enum= typeName '.' code= ID ';'
                    pass 
                    string_literal208=self.match(self.input, 90, self.FOLLOW_90_in_propertyElement1752) 
                    stream_90.add(string_literal208)
                    char_literal209=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1754) 
                    stream_62.add(char_literal209)
                    self._state.following.append(self.FOLLOW_typeName_in_propertyElement1758)
                    enum = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(enum.tree)
                    char_literal210=self.match(self.input, 71, self.FOLLOW_71_in_propertyElement1760) 
                    stream_71.add(char_literal210)
                    code=self.match(self.input, ID, self.FOLLOW_ID_in_propertyElement1764) 
                    stream_ID.add(code)
                    char_literal211=self.match(self.input, 59, self.FOLLOW_59_in_propertyElement1766) 
                    stream_59.add(char_literal211)

                    # AST Rewrite
                    # elements: enum, code
                    # token labels: code
                    # rule labels: retval, enum
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0
                    stream_code = RewriteRuleTokenStream(self._adaptor, "token code", code)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if enum is not None:
                        stream_enum = RewriteRuleSubtreeStream(self._adaptor, "rule enum", enum.tree)
                    else:
                        stream_enum = RewriteRuleSubtreeStream(self._adaptor, "token enum", None)


                    root_0 = self._adaptor.nil()
                    # 187:51: -> ^( PROP_DEFAULT $enum $code)
                    # GOC.g:187:54: ^( PROP_DEFAULT $enum $code)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_DEFAULT, "PROP_DEFAULT"), root_1)

                    self._adaptor.addChild(root_1, stream_enum.nextTree())
                    self._adaptor.addChild(root_1, stream_code.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt34 == 12:
                    # GOC.g:188:9: AUTO_CREATE ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    AUTO_CREATE212=self.match(self.input, AUTO_CREATE, self.FOLLOW_AUTO_CREATE_in_propertyElement1788)

                    AUTO_CREATE212_tree = self._adaptor.createWithPayload(AUTO_CREATE212)
                    root_0 = self._adaptor.becomeRoot(AUTO_CREATE212_tree, root_0)

                    char_literal213=self.match(self.input, 59, self.FOLLOW_59_in_propertyElement1791)

                    char_literal213_tree = self._adaptor.createWithPayload(char_literal213)
                    self._adaptor.addChild(root_0, char_literal213_tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "propertyElement"

    class signalElement_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.signalElement_return, self).__init__()

            self.tree = None




    # $ANTLR start "signalElement"
    # GOC.g:191:1: signalElement : ( RESULT '{' 'type' ':' typeArg ';' '}' -> ^( RESULT typeArg ) | PARAMETER ID '{' 'type' ':' typeArg ';' '}' -> ^( PARAMETER ID typeArg ) );
    def signalElement(self, ):

        retval = self.signalElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RESULT214 = None
        char_literal215 = None
        string_literal216 = None
        char_literal217 = None
        char_literal219 = None
        char_literal220 = None
        PARAMETER221 = None
        ID222 = None
        char_literal223 = None
        string_literal224 = None
        char_literal225 = None
        char_literal227 = None
        char_literal228 = None
        typeArg218 = None

        typeArg226 = None


        RESULT214_tree = None
        char_literal215_tree = None
        string_literal216_tree = None
        char_literal217_tree = None
        char_literal219_tree = None
        char_literal220_tree = None
        PARAMETER221_tree = None
        ID222_tree = None
        char_literal223_tree = None
        string_literal224_tree = None
        char_literal225_tree = None
        char_literal227_tree = None
        char_literal228_tree = None
        stream_RESULT = RewriteRuleTokenStream(self._adaptor, "token RESULT")
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_PARAMETER = RewriteRuleTokenStream(self._adaptor, "token PARAMETER")
        stream_TYPE = RewriteRuleTokenStream(self._adaptor, "token TYPE")
        stream_typeArg = RewriteRuleSubtreeStream(self._adaptor, "rule typeArg")
        try:
            try:
                # GOC.g:192:5: ( RESULT '{' 'type' ':' typeArg ';' '}' -> ^( RESULT typeArg ) | PARAMETER ID '{' 'type' ':' typeArg ';' '}' -> ^( PARAMETER ID typeArg ) )
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == RESULT) :
                    alt35 = 1
                elif (LA35_0 == PARAMETER) :
                    alt35 = 2
                else:
                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae

                if alt35 == 1:
                    # GOC.g:192:9: RESULT '{' 'type' ':' typeArg ';' '}'
                    pass 
                    RESULT214=self.match(self.input, RESULT, self.FOLLOW_RESULT_in_signalElement1810) 
                    stream_RESULT.add(RESULT214)
                    char_literal215=self.match(self.input, 57, self.FOLLOW_57_in_signalElement1812) 
                    stream_57.add(char_literal215)
                    string_literal216=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_signalElement1814) 
                    stream_TYPE.add(string_literal216)
                    char_literal217=self.match(self.input, 62, self.FOLLOW_62_in_signalElement1816) 
                    stream_62.add(char_literal217)
                    self._state.following.append(self.FOLLOW_typeArg_in_signalElement1818)
                    typeArg218 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg218.tree)
                    char_literal219=self.match(self.input, 59, self.FOLLOW_59_in_signalElement1820) 
                    stream_59.add(char_literal219)
                    char_literal220=self.match(self.input, 58, self.FOLLOW_58_in_signalElement1822) 
                    stream_58.add(char_literal220)

                    # AST Rewrite
                    # elements: typeArg, RESULT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 192:47: -> ^( RESULT typeArg )
                    # GOC.g:192:50: ^( RESULT typeArg )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_RESULT.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_typeArg.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt35 == 2:
                    # GOC.g:193:9: PARAMETER ID '{' 'type' ':' typeArg ';' '}'
                    pass 
                    PARAMETER221=self.match(self.input, PARAMETER, self.FOLLOW_PARAMETER_in_signalElement1840) 
                    stream_PARAMETER.add(PARAMETER221)
                    ID222=self.match(self.input, ID, self.FOLLOW_ID_in_signalElement1842) 
                    stream_ID.add(ID222)
                    char_literal223=self.match(self.input, 57, self.FOLLOW_57_in_signalElement1844) 
                    stream_57.add(char_literal223)
                    string_literal224=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_signalElement1846) 
                    stream_TYPE.add(string_literal224)
                    char_literal225=self.match(self.input, 62, self.FOLLOW_62_in_signalElement1848) 
                    stream_62.add(char_literal225)
                    self._state.following.append(self.FOLLOW_typeArg_in_signalElement1850)
                    typeArg226 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg226.tree)
                    char_literal227=self.match(self.input, 59, self.FOLLOW_59_in_signalElement1852) 
                    stream_59.add(char_literal227)
                    char_literal228=self.match(self.input, 58, self.FOLLOW_58_in_signalElement1854) 
                    stream_58.add(char_literal228)

                    # AST Rewrite
                    # elements: PARAMETER, ID, typeArg
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 193:53: -> ^( PARAMETER ID typeArg )
                    # GOC.g:193:56: ^( PARAMETER ID typeArg )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_PARAMETER.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())
                    self._adaptor.addChild(root_1, stream_typeArg.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "signalElement"

    class attributeElement_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.attributeElement_return, self).__init__()

            self.tree = None




    # $ANTLR start "attributeElement"
    # GOC.g:196:1: attributeElement : ( SCOPE ':' (val= 'static' | val= 'instance' ) ';' -> ^( SCOPE $val) | VISIBILITY ':' (val= 'public' | val= 'protected' | val= 'private' ) ';' -> ^( VISIBILITY $val) );
    def attributeElement(self, ):

        retval = self.attributeElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        val = None
        SCOPE229 = None
        char_literal230 = None
        char_literal231 = None
        VISIBILITY232 = None
        char_literal233 = None
        char_literal234 = None

        val_tree = None
        SCOPE229_tree = None
        char_literal230_tree = None
        char_literal231_tree = None
        VISIBILITY232_tree = None
        char_literal233_tree = None
        char_literal234_tree = None
        stream_67 = RewriteRuleTokenStream(self._adaptor, "token 67")
        stream_66 = RewriteRuleTokenStream(self._adaptor, "token 66")
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_VISIBILITY = RewriteRuleTokenStream(self._adaptor, "token VISIBILITY")
        stream_SCOPE = RewriteRuleTokenStream(self._adaptor, "token SCOPE")
        stream_64 = RewriteRuleTokenStream(self._adaptor, "token 64")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_63 = RewriteRuleTokenStream(self._adaptor, "token 63")

        try:
            try:
                # GOC.g:197:2: ( SCOPE ':' (val= 'static' | val= 'instance' ) ';' -> ^( SCOPE $val) | VISIBILITY ':' (val= 'public' | val= 'protected' | val= 'private' ) ';' -> ^( VISIBILITY $val) )
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (LA38_0 == SCOPE) :
                    alt38 = 1
                elif (LA38_0 == VISIBILITY) :
                    alt38 = 2
                else:
                    nvae = NoViableAltException("", 38, 0, self.input)

                    raise nvae

                if alt38 == 1:
                    # GOC.g:197:4: SCOPE ':' (val= 'static' | val= 'instance' ) ';'
                    pass 
                    SCOPE229=self.match(self.input, SCOPE, self.FOLLOW_SCOPE_in_attributeElement1878) 
                    stream_SCOPE.add(SCOPE229)
                    char_literal230=self.match(self.input, 62, self.FOLLOW_62_in_attributeElement1880) 
                    stream_62.add(char_literal230)
                    # GOC.g:197:14: (val= 'static' | val= 'instance' )
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == 67) :
                        alt36 = 1
                    elif (LA36_0 == 66) :
                        alt36 = 2
                    else:
                        nvae = NoViableAltException("", 36, 0, self.input)

                        raise nvae

                    if alt36 == 1:
                        # GOC.g:197:15: val= 'static'
                        pass 
                        val=self.match(self.input, 67, self.FOLLOW_67_in_attributeElement1885) 
                        stream_67.add(val)


                    elif alt36 == 2:
                        # GOC.g:197:28: val= 'instance'
                        pass 
                        val=self.match(self.input, 66, self.FOLLOW_66_in_attributeElement1889) 
                        stream_66.add(val)



                    char_literal231=self.match(self.input, 59, self.FOLLOW_59_in_attributeElement1892) 
                    stream_59.add(char_literal231)

                    # AST Rewrite
                    # elements: SCOPE, val
                    # token labels: val
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 197:48: -> ^( SCOPE $val)
                    # GOC.g:197:51: ^( SCOPE $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_SCOPE.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt38 == 2:
                    # GOC.g:198:4: VISIBILITY ':' (val= 'public' | val= 'protected' | val= 'private' ) ';'
                    pass 
                    VISIBILITY232=self.match(self.input, VISIBILITY, self.FOLLOW_VISIBILITY_in_attributeElement1906) 
                    stream_VISIBILITY.add(VISIBILITY232)
                    char_literal233=self.match(self.input, 62, self.FOLLOW_62_in_attributeElement1908) 
                    stream_62.add(char_literal233)
                    # GOC.g:198:19: (val= 'public' | val= 'protected' | val= 'private' )
                    alt37 = 3
                    LA37 = self.input.LA(1)
                    if LA37 == 63:
                        alt37 = 1
                    elif LA37 == 64:
                        alt37 = 2
                    elif LA37 == 65:
                        alt37 = 3
                    else:
                        nvae = NoViableAltException("", 37, 0, self.input)

                        raise nvae

                    if alt37 == 1:
                        # GOC.g:198:20: val= 'public'
                        pass 
                        val=self.match(self.input, 63, self.FOLLOW_63_in_attributeElement1913) 
                        stream_63.add(val)


                    elif alt37 == 2:
                        # GOC.g:198:33: val= 'protected'
                        pass 
                        val=self.match(self.input, 64, self.FOLLOW_64_in_attributeElement1917) 
                        stream_64.add(val)


                    elif alt37 == 3:
                        # GOC.g:198:49: val= 'private'
                        pass 
                        val=self.match(self.input, 65, self.FOLLOW_65_in_attributeElement1921) 
                        stream_65.add(val)



                    char_literal234=self.match(self.input, 59, self.FOLLOW_59_in_attributeElement1924) 
                    stream_59.add(char_literal234)

                    # AST Rewrite
                    # elements: VISIBILITY, val
                    # token labels: val
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 198:68: -> ^( VISIBILITY $val)
                    # GOC.g:198:71: ^( VISIBILITY $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_VISIBILITY.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "attributeElement"

    class typeName_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.typeName_return, self).__init__()

            self.tree = None




    # $ANTLR start "typeName"
    # GOC.g:201:1: typeName : ( typePath -> ^( TYPE_NAME typePath ) | ( 'unsigned ' )? 'integer' -> ^( TYPE_NAME ( 'unsigned ' )? 'integer' ) | ( 'unsigned ' )? 'long' -> ^( TYPE_NAME ( 'unsigned ' )? 'long' ) | (val= 'null' | val= 'boolean' | val= 'string' | val= 'float' | val= 'double' | val= 'pointer' ) -> ^( TYPE_NAME $val) );
    def typeName(self, ):

        retval = self.typeName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        val = None
        string_literal236 = None
        string_literal237 = None
        string_literal238 = None
        string_literal239 = None
        typePath235 = None


        val_tree = None
        string_literal236_tree = None
        string_literal237_tree = None
        string_literal238_tree = None
        string_literal239_tree = None
        stream_78 = RewriteRuleTokenStream(self._adaptor, "token 78")
        stream_77 = RewriteRuleTokenStream(self._adaptor, "token 77")
        stream_93 = RewriteRuleTokenStream(self._adaptor, "token 93")
        stream_92 = RewriteRuleTokenStream(self._adaptor, "token 92")
        stream_91 = RewriteRuleTokenStream(self._adaptor, "token 91")
        stream_73 = RewriteRuleTokenStream(self._adaptor, "token 73")
        stream_74 = RewriteRuleTokenStream(self._adaptor, "token 74")
        stream_75 = RewriteRuleTokenStream(self._adaptor, "token 75")
        stream_76 = RewriteRuleTokenStream(self._adaptor, "token 76")
        stream_typePath = RewriteRuleSubtreeStream(self._adaptor, "rule typePath")
        try:
            try:
                # GOC.g:202:2: ( typePath -> ^( TYPE_NAME typePath ) | ( 'unsigned ' )? 'integer' -> ^( TYPE_NAME ( 'unsigned ' )? 'integer' ) | ( 'unsigned ' )? 'long' -> ^( TYPE_NAME ( 'unsigned ' )? 'long' ) | (val= 'null' | val= 'boolean' | val= 'string' | val= 'float' | val= 'double' | val= 'pointer' ) -> ^( TYPE_NAME $val) )
                alt42 = 4
                LA42 = self.input.LA(1)
                if LA42 == ID or LA42 == 96:
                    alt42 = 1
                elif LA42 == 91:
                    LA42_2 = self.input.LA(2)

                    if (LA42_2 == 74) :
                        alt42 = 2
                    elif (LA42_2 == 92) :
                        alt42 = 3
                    else:
                        nvae = NoViableAltException("", 42, 2, self.input)

                        raise nvae

                elif LA42 == 74:
                    alt42 = 2
                elif LA42 == 92:
                    alt42 = 3
                elif LA42 == 73 or LA42 == 75 or LA42 == 76 or LA42 == 77 or LA42 == 78 or LA42 == 93:
                    alt42 = 4
                else:
                    nvae = NoViableAltException("", 42, 0, self.input)

                    raise nvae

                if alt42 == 1:
                    # GOC.g:202:6: typePath
                    pass 
                    self._state.following.append(self.FOLLOW_typePath_in_typeName1946)
                    typePath235 = self.typePath()

                    self._state.following.pop()
                    stream_typePath.add(typePath235.tree)

                    # AST Rewrite
                    # elements: typePath
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 202:15: -> ^( TYPE_NAME typePath )
                    # GOC.g:202:18: ^( TYPE_NAME typePath )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE_NAME, "TYPE_NAME"), root_1)

                    self._adaptor.addChild(root_1, stream_typePath.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt42 == 2:
                    # GOC.g:203:6: ( 'unsigned ' )? 'integer'
                    pass 
                    # GOC.g:203:6: ( 'unsigned ' )?
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 == 91) :
                        alt39 = 1
                    if alt39 == 1:
                        # GOC.g:203:6: 'unsigned '
                        pass 
                        string_literal236=self.match(self.input, 91, self.FOLLOW_91_in_typeName1961) 
                        stream_91.add(string_literal236)



                    string_literal237=self.match(self.input, 74, self.FOLLOW_74_in_typeName1964) 
                    stream_74.add(string_literal237)

                    # AST Rewrite
                    # elements: 91, 74
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 203:29: -> ^( TYPE_NAME ( 'unsigned ' )? 'integer' )
                    # GOC.g:203:32: ^( TYPE_NAME ( 'unsigned ' )? 'integer' )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE_NAME, "TYPE_NAME"), root_1)

                    # GOC.g:203:44: ( 'unsigned ' )?
                    if stream_91.hasNext():
                        self._adaptor.addChild(root_1, stream_91.nextNode())


                    stream_91.reset();
                    self._adaptor.addChild(root_1, stream_74.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt42 == 3:
                    # GOC.g:204:6: ( 'unsigned ' )? 'long'
                    pass 
                    # GOC.g:204:6: ( 'unsigned ' )?
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == 91) :
                        alt40 = 1
                    if alt40 == 1:
                        # GOC.g:204:6: 'unsigned '
                        pass 
                        string_literal238=self.match(self.input, 91, self.FOLLOW_91_in_typeName1982) 
                        stream_91.add(string_literal238)



                    string_literal239=self.match(self.input, 92, self.FOLLOW_92_in_typeName1985) 
                    stream_92.add(string_literal239)

                    # AST Rewrite
                    # elements: 92, 91
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 204:26: -> ^( TYPE_NAME ( 'unsigned ' )? 'long' )
                    # GOC.g:204:29: ^( TYPE_NAME ( 'unsigned ' )? 'long' )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE_NAME, "TYPE_NAME"), root_1)

                    # GOC.g:204:41: ( 'unsigned ' )?
                    if stream_91.hasNext():
                        self._adaptor.addChild(root_1, stream_91.nextNode())


                    stream_91.reset();
                    self._adaptor.addChild(root_1, stream_92.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt42 == 4:
                    # GOC.g:205:4: (val= 'null' | val= 'boolean' | val= 'string' | val= 'float' | val= 'double' | val= 'pointer' )
                    pass 
                    # GOC.g:205:4: (val= 'null' | val= 'boolean' | val= 'string' | val= 'float' | val= 'double' | val= 'pointer' )
                    alt41 = 6
                    LA41 = self.input.LA(1)
                    if LA41 == 93:
                        alt41 = 1
                    elif LA41 == 73:
                        alt41 = 2
                    elif LA41 == 77:
                        alt41 = 3
                    elif LA41 == 75:
                        alt41 = 4
                    elif LA41 == 76:
                        alt41 = 5
                    elif LA41 == 78:
                        alt41 = 6
                    else:
                        nvae = NoViableAltException("", 41, 0, self.input)

                        raise nvae

                    if alt41 == 1:
                        # GOC.g:205:5: val= 'null'
                        pass 
                        val=self.match(self.input, 93, self.FOLLOW_93_in_typeName2004) 
                        stream_93.add(val)


                    elif alt41 == 2:
                        # GOC.g:206:6: val= 'boolean'
                        pass 
                        val=self.match(self.input, 73, self.FOLLOW_73_in_typeName2013) 
                        stream_73.add(val)


                    elif alt41 == 3:
                        # GOC.g:207:4: val= 'string'
                        pass 
                        val=self.match(self.input, 77, self.FOLLOW_77_in_typeName2020) 
                        stream_77.add(val)


                    elif alt41 == 4:
                        # GOC.g:208:4: val= 'float'
                        pass 
                        val=self.match(self.input, 75, self.FOLLOW_75_in_typeName2027) 
                        stream_75.add(val)


                    elif alt41 == 5:
                        # GOC.g:209:4: val= 'double'
                        pass 
                        val=self.match(self.input, 76, self.FOLLOW_76_in_typeName2034) 
                        stream_76.add(val)


                    elif alt41 == 6:
                        # GOC.g:210:6: val= 'pointer'
                        pass 
                        val=self.match(self.input, 78, self.FOLLOW_78_in_typeName2043) 
                        stream_78.add(val)




                    # AST Rewrite
                    # elements: val
                    # token labels: val
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0
                    stream_val = RewriteRuleTokenStream(self._adaptor, "token val", val)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 210:21: -> ^( TYPE_NAME $val)
                    # GOC.g:210:24: ^( TYPE_NAME $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE_NAME, "TYPE_NAME"), root_1)

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "typeName"

    class typeArg_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.typeArg_return, self).__init__()

            self.tree = None




    # $ANTLR start "typeArg"
    # GOC.g:213:1: typeArg : ( typeName | 'ref' '(' typeArg ')' -> ^( REF_TO typeArg ) | 'list' '(' typeArg ')' -> ^( LIST_OF typeArg ) );
    def typeArg(self, ):

        retval = self.typeArg_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal241 = None
        char_literal242 = None
        char_literal244 = None
        string_literal245 = None
        char_literal246 = None
        char_literal248 = None
        typeName240 = None

        typeArg243 = None

        typeArg247 = None


        string_literal241_tree = None
        char_literal242_tree = None
        char_literal244_tree = None
        string_literal245_tree = None
        char_literal246_tree = None
        char_literal248_tree = None
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_94 = RewriteRuleTokenStream(self._adaptor, "token 94")
        stream_86 = RewriteRuleTokenStream(self._adaptor, "token 86")
        stream_87 = RewriteRuleTokenStream(self._adaptor, "token 87")
        stream_typeArg = RewriteRuleSubtreeStream(self._adaptor, "rule typeArg")
        try:
            try:
                # GOC.g:214:5: ( typeName | 'ref' '(' typeArg ')' -> ^( REF_TO typeArg ) | 'list' '(' typeArg ')' -> ^( LIST_OF typeArg ) )
                alt43 = 3
                LA43 = self.input.LA(1)
                if LA43 == ID or LA43 == 73 or LA43 == 74 or LA43 == 75 or LA43 == 76 or LA43 == 77 or LA43 == 78 or LA43 == 91 or LA43 == 92 or LA43 == 93 or LA43 == 96:
                    alt43 = 1
                elif LA43 == 94:
                    alt43 = 2
                elif LA43 == 95:
                    alt43 = 3
                else:
                    nvae = NoViableAltException("", 43, 0, self.input)

                    raise nvae

                if alt43 == 1:
                    # GOC.g:214:9: typeName
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_typeName_in_typeArg2069)
                    typeName240 = self.typeName()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, typeName240.tree)


                elif alt43 == 2:
                    # GOC.g:215:9: 'ref' '(' typeArg ')'
                    pass 
                    string_literal241=self.match(self.input, 94, self.FOLLOW_94_in_typeArg2079) 
                    stream_94.add(string_literal241)
                    char_literal242=self.match(self.input, 86, self.FOLLOW_86_in_typeArg2081) 
                    stream_86.add(char_literal242)
                    self._state.following.append(self.FOLLOW_typeArg_in_typeArg2083)
                    typeArg243 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg243.tree)
                    char_literal244=self.match(self.input, 87, self.FOLLOW_87_in_typeArg2085) 
                    stream_87.add(char_literal244)

                    # AST Rewrite
                    # elements: typeArg
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 215:31: -> ^( REF_TO typeArg )
                    # GOC.g:215:34: ^( REF_TO typeArg )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(REF_TO, "REF_TO"), root_1)

                    self._adaptor.addChild(root_1, stream_typeArg.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt43 == 3:
                    # GOC.g:216:9: 'list' '(' typeArg ')'
                    pass 
                    string_literal245=self.match(self.input, 95, self.FOLLOW_95_in_typeArg2103) 
                    stream_95.add(string_literal245)
                    char_literal246=self.match(self.input, 86, self.FOLLOW_86_in_typeArg2105) 
                    stream_86.add(char_literal246)
                    self._state.following.append(self.FOLLOW_typeArg_in_typeArg2107)
                    typeArg247 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg247.tree)
                    char_literal248=self.match(self.input, 87, self.FOLLOW_87_in_typeArg2109) 
                    stream_87.add(char_literal248)

                    # AST Rewrite
                    # elements: typeArg
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 216:32: -> ^( LIST_OF typeArg )
                    # GOC.g:216:35: ^( LIST_OF typeArg )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LIST_OF, "LIST_OF"), root_1)

                    self._adaptor.addChild(root_1, stream_typeArg.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "typeArg"

    class typePath_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.typePath_return, self).__init__()

            self.tree = None




    # $ANTLR start "typePath"
    # GOC.g:219:1: typePath : ( '::' ID '::' )? ( ID '::' )* ID ;
    def typePath(self, ):

        retval = self.typePath_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal249 = None
        ID250 = None
        string_literal251 = None
        ID252 = None
        string_literal253 = None
        ID254 = None

        string_literal249_tree = None
        ID250_tree = None
        string_literal251_tree = None
        ID252_tree = None
        string_literal253_tree = None
        ID254_tree = None

        try:
            try:
                # GOC.g:220:5: ( ( '::' ID '::' )? ( ID '::' )* ID )
                # GOC.g:220:9: ( '::' ID '::' )? ( ID '::' )* ID
                pass 
                root_0 = self._adaptor.nil()

                # GOC.g:220:9: ( '::' ID '::' )?
                alt44 = 2
                LA44_0 = self.input.LA(1)

                if (LA44_0 == 96) :
                    alt44 = 1
                if alt44 == 1:
                    # GOC.g:220:10: '::' ID '::'
                    pass 
                    string_literal249=self.match(self.input, 96, self.FOLLOW_96_in_typePath2137)

                    string_literal249_tree = self._adaptor.createWithPayload(string_literal249)
                    self._adaptor.addChild(root_0, string_literal249_tree)

                    ID250=self.match(self.input, ID, self.FOLLOW_ID_in_typePath2139)

                    ID250_tree = self._adaptor.createWithPayload(ID250)
                    self._adaptor.addChild(root_0, ID250_tree)

                    string_literal251=self.match(self.input, 96, self.FOLLOW_96_in_typePath2141)

                    string_literal251_tree = self._adaptor.createWithPayload(string_literal251)
                    self._adaptor.addChild(root_0, string_literal251_tree)




                # GOC.g:220:24: ( ID '::' )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == ID) :
                        LA45_1 = self.input.LA(2)

                        if (LA45_1 == 96) :
                            alt45 = 1




                    if alt45 == 1:
                        # GOC.g:220:25: ID '::'
                        pass 
                        ID252=self.match(self.input, ID, self.FOLLOW_ID_in_typePath2145)

                        ID252_tree = self._adaptor.createWithPayload(ID252)
                        self._adaptor.addChild(root_0, ID252_tree)

                        string_literal253=self.match(self.input, 96, self.FOLLOW_96_in_typePath2147)

                        string_literal253_tree = self._adaptor.createWithPayload(string_literal253)
                        self._adaptor.addChild(root_0, string_literal253_tree)



                    else:
                        break #loop45
                ID254=self.match(self.input, ID, self.FOLLOW_ID_in_typePath2151)

                ID254_tree = self._adaptor.createWithPayload(ID254)
                self._adaptor.addChild(root_0, ID254_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "typePath"

    class signalID_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.signalID_return, self).__init__()

            self.tree = None




    # $ANTLR start "signalID"
    # GOC.g:349:1: signalID : part1= ID ( '-' part2+= ID )* -> ^( SIGNAL_ID $part1 ( $part2)* ) ;
    def signalID(self, ):

        retval = self.signalID_return()
        retval.start = self.input.LT(1)

        root_0 = None

        part1 = None
        char_literal255 = None
        part2 = None
        list_part2 = None

        part1_tree = None
        char_literal255_tree = None
        part2_tree = None
        stream_97 = RewriteRuleTokenStream(self._adaptor, "token 97")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # GOC.g:350:5: (part1= ID ( '-' part2+= ID )* -> ^( SIGNAL_ID $part1 ( $part2)* ) )
                # GOC.g:350:9: part1= ID ( '-' part2+= ID )*
                pass 
                part1=self.match(self.input, ID, self.FOLLOW_ID_in_signalID2754) 
                stream_ID.add(part1)
                # GOC.g:350:18: ( '-' part2+= ID )*
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == 97) :
                        alt46 = 1


                    if alt46 == 1:
                        # GOC.g:350:19: '-' part2+= ID
                        pass 
                        char_literal255=self.match(self.input, 97, self.FOLLOW_97_in_signalID2757) 
                        stream_97.add(char_literal255)
                        part2=self.match(self.input, ID, self.FOLLOW_ID_in_signalID2761) 
                        stream_ID.add(part2)
                        if list_part2 is None:
                            list_part2 = []
                        list_part2.append(part2)



                    else:
                        break #loop46

                # AST Rewrite
                # elements: part1, part2
                # token labels: part1
                # rule labels: retval
                # token list labels: part2
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0
                stream_part1 = RewriteRuleTokenStream(self._adaptor, "token part1", part1)
                stream_part2 = RewriteRuleTokenStream(self._adaptor, "token part2", list_part2)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 350:35: -> ^( SIGNAL_ID $part1 ( $part2)* )
                # GOC.g:350:38: ^( SIGNAL_ID $part1 ( $part2)* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(SIGNAL_ID, "SIGNAL_ID"), root_1)

                self._adaptor.addChild(root_1, stream_part1.nextNode())
                # GOC.g:350:57: ( $part2)*
                while stream_part2.hasNext():
                    self._adaptor.addChild(root_1, stream_part2.nextNode())


                stream_part2.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "signalID"


    # Delegated rules


    # lookup tables for DFA #34

    DFA34_eot = DFA.unpack(
        u"\25\uffff"
        )

    DFA34_eof = DFA.unpack(
        u"\25\uffff"
        )

    DFA34_min = DFA.unpack(
        u"\1\33\3\uffff\4\76\1\uffff\1\24\3\23\10\uffff"
        )

    DFA34_max = DFA.unpack(
        u"\1\132\3\uffff\4\76\1\uffff\1\56\3\140\10\uffff"
        )

    DFA34_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\4\uffff\1\14\4\uffff\1\4\1\5\1\6\1\7\1\10"
        u"\1\11\1\12\1\13"
        )

    DFA34_special = DFA.unpack(
        u"\25\uffff"
        )

            
    DFA34_transition = [
        DFA.unpack(u"\1\4\10\uffff\1\1\12\uffff\1\10\41\uffff\1\2\3\uffff"
        u"\1\3\2\uffff\1\5\1\6\1\7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\11"),
        DFA.unpack(u"\1\12"),
        DFA.unpack(u"\1\13"),
        DFA.unpack(u"\1\14"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\15\31\uffff\1\16"),
        DFA.unpack(u"\1\17\1\20\64\uffff\6\20\14\uffff\3\20\2\uffff\1\20"),
        DFA.unpack(u"\1\21\1\22\64\uffff\6\22\14\uffff\3\22\2\uffff\1\22"),
        DFA.unpack(u"\1\23\1\24\64\uffff\6\24\14\uffff\3\24\2\uffff\1\24"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #34

    class DFA34(DFA):
        pass


 

    FOLLOW_stmt_in_defFile143 = frozenset([1, 21, 22, 23, 24, 26, 27, 51, 56])
    FOLLOW_classDef_in_stmt165 = frozenset([1])
    FOLLOW_intfDef_in_stmt170 = frozenset([1])
    FOLLOW_errorDomainDef_in_stmt177 = frozenset([1])
    FOLLOW_enumDef_in_stmt184 = frozenset([1])
    FOLLOW_flagsDef_in_stmt191 = frozenset([1])
    FOLLOW_packageDef_in_stmt196 = frozenset([1])
    FOLLOW_typeDecl_in_stmt203 = frozenset([1])
    FOLLOW_includeStmt_in_stmt210 = frozenset([1])
    FOLLOW_56_in_includeStmt226 = frozenset([19])
    FOLLOW_STRING_in_includeStmt230 = frozenset([1])
    FOLLOW_PACKAGE_in_packageDef253 = frozenset([20])
    FOLLOW_ID_in_packageDef255 = frozenset([57])
    FOLLOW_57_in_packageDef257 = frozenset([21, 22, 23, 24, 26, 27, 51, 58])
    FOLLOW_packageElement_in_packageDef259 = frozenset([21, 22, 23, 24, 26, 27, 51, 58])
    FOLLOW_58_in_packageDef262 = frozenset([1])
    FOLLOW_packageDef_in_packageElement287 = frozenset([1])
    FOLLOW_classDef_in_packageElement292 = frozenset([1])
    FOLLOW_intfDef_in_packageElement297 = frozenset([1])
    FOLLOW_errorDomainDef_in_packageElement304 = frozenset([1])
    FOLLOW_enumDef_in_packageElement311 = frozenset([1])
    FOLLOW_flagsDef_in_packageElement318 = frozenset([1])
    FOLLOW_typeDecl_in_packageElement325 = frozenset([1])
    FOLLOW_GOBJECT_in_classDef336 = frozenset([20])
    FOLLOW_ID_in_classDef340 = frozenset([57, 59])
    FOLLOW_57_in_classDef343 = frozenset([28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 58])
    FOLLOW_classMember_in_classDef345 = frozenset([28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 58])
    FOLLOW_58_in_classDef348 = frozenset([1])
    FOLLOW_59_in_classDef350 = frozenset([1])
    FOLLOW_GINTERFACE_in_intfDef377 = frozenset([20])
    FOLLOW_ID_in_intfDef381 = frozenset([57, 59])
    FOLLOW_57_in_intfDef384 = frozenset([30, 33, 38, 58])
    FOLLOW_intfMember_in_intfDef386 = frozenset([30, 33, 38, 58])
    FOLLOW_58_in_intfDef389 = frozenset([1])
    FOLLOW_59_in_intfDef391 = frozenset([1])
    FOLLOW_ERROR_DOMAIN_in_errorDomainDef422 = frozenset([20])
    FOLLOW_ID_in_errorDomainDef424 = frozenset([57])
    FOLLOW_57_in_errorDomainDef426 = frozenset([60])
    FOLLOW_errorDomainElement_in_errorDomainDef428 = frozenset([58, 60])
    FOLLOW_58_in_errorDomainDef431 = frozenset([1])
    FOLLOW_60_in_errorDomainElement466 = frozenset([20])
    FOLLOW_ID_in_errorDomainElement468 = frozenset([59])
    FOLLOW_59_in_errorDomainElement470 = frozenset([1])
    FOLLOW_ENUMERATION_in_enumDef495 = frozenset([20])
    FOLLOW_ID_in_enumDef497 = frozenset([57])
    FOLLOW_57_in_enumDef499 = frozenset([60])
    FOLLOW_enumElement_in_enumDef501 = frozenset([58, 60])
    FOLLOW_58_in_enumDef504 = frozenset([1])
    FOLLOW_60_in_enumElement539 = frozenset([20])
    FOLLOW_ID_in_enumElement541 = frozenset([57, 59])
    FOLLOW_59_in_enumElement544 = frozenset([1])
    FOLLOW_57_in_enumElement546 = frozenset([61])
    FOLLOW_61_in_enumElement548 = frozenset([62])
    FOLLOW_62_in_enumElement550 = frozenset([25])
    FOLLOW_INT_in_enumElement552 = frozenset([59])
    FOLLOW_59_in_enumElement554 = frozenset([58])
    FOLLOW_58_in_enumElement556 = frozenset([1])
    FOLLOW_FLAGS_in_flagsDef592 = frozenset([20])
    FOLLOW_ID_in_flagsDef594 = frozenset([57])
    FOLLOW_57_in_flagsDef596 = frozenset([60])
    FOLLOW_flagsElement_in_flagsDef598 = frozenset([58, 60])
    FOLLOW_58_in_flagsDef601 = frozenset([1])
    FOLLOW_60_in_flagsElement636 = frozenset([20])
    FOLLOW_ID_in_flagsElement638 = frozenset([59])
    FOLLOW_59_in_flagsElement640 = frozenset([1])
    FOLLOW_GTYPE_in_typeDecl665 = frozenset([20])
    FOLLOW_ID_in_typeDecl667 = frozenset([59])
    FOLLOW_59_in_typeDecl669 = frozenset([1])
    FOLLOW_SUPER_in_classMember700 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 96])
    FOLLOW_typeName_in_classMember702 = frozenset([59])
    FOLLOW_59_in_classMember704 = frozenset([1])
    FOLLOW_ABSTRACT_in_classMember720 = frozenset([59])
    FOLLOW_59_in_classMember723 = frozenset([1])
    FOLLOW_PREFIX_in_classMember730 = frozenset([20])
    FOLLOW_ID_in_classMember732 = frozenset([59])
    FOLLOW_59_in_classMember734 = frozenset([1])
    FOLLOW_IMPLEMENTS_in_classMember747 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 96])
    FOLLOW_typeName_in_classMember749 = frozenset([59])
    FOLLOW_59_in_classMember751 = frozenset([1])
    FOLLOW_CONSTRUCTOR_in_classMember771 = frozenset([57])
    FOLLOW_57_in_classMember773 = frozenset([43, 44, 58])
    FOLLOW_constructorElement_in_classMember775 = frozenset([43, 44, 58])
    FOLLOW_58_in_classMember778 = frozenset([1])
    FOLLOW_METHOD_in_classMember806 = frozenset([20])
    FOLLOW_ID_in_classMember808 = frozenset([57])
    FOLLOW_57_in_classMember810 = frozenset([39, 40, 41, 42, 43, 44, 58])
    FOLLOW_methodElement_in_classMember812 = frozenset([39, 40, 41, 42, 43, 44, 58])
    FOLLOW_58_in_classMember815 = frozenset([1])
    FOLLOW_OVERRIDE_in_classMember832 = frozenset([20])
    FOLLOW_ID_in_classMember834 = frozenset([59])
    FOLLOW_59_in_classMember836 = frozenset([1])
    FOLLOW_ATTRIBUTE_in_classMember849 = frozenset([20])
    FOLLOW_ID_in_classMember851 = frozenset([57])
    FOLLOW_57_in_classMember853 = frozenset([36])
    FOLLOW_TYPE_in_classMember855 = frozenset([62])
    FOLLOW_62_in_classMember857 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 94, 95, 96])
    FOLLOW_typeArg_in_classMember859 = frozenset([59])
    FOLLOW_59_in_classMember861 = frozenset([40, 41, 58])
    FOLLOW_attributeElement_in_classMember863 = frozenset([40, 41, 58])
    FOLLOW_58_in_classMember866 = frozenset([1])
    FOLLOW_PROPERTY_in_classMember885 = frozenset([20])
    FOLLOW_ID_in_classMember887 = frozenset([57])
    FOLLOW_57_in_classMember889 = frozenset([27, 36, 47, 81, 85, 88, 89, 90])
    FOLLOW_propertyElement_in_classMember891 = frozenset([27, 36, 47, 58, 81, 85, 88, 89, 90])
    FOLLOW_58_in_classMember894 = frozenset([1])
    FOLLOW_SIGNAL_in_classMember910 = frozenset([20])
    FOLLOW_signalID_in_classMember912 = frozenset([57])
    FOLLOW_57_in_classMember914 = frozenset([39, 43, 58])
    FOLLOW_signalElement_in_classMember916 = frozenset([39, 43, 58])
    FOLLOW_58_in_classMember919 = frozenset([1])
    FOLLOW_PREFIX_in_intfMember942 = frozenset([20])
    FOLLOW_ID_in_intfMember944 = frozenset([59])
    FOLLOW_59_in_intfMember946 = frozenset([1])
    FOLLOW_METHOD_in_intfMember961 = frozenset([20])
    FOLLOW_ID_in_intfMember963 = frozenset([57])
    FOLLOW_57_in_intfMember965 = frozenset([39, 40, 41, 42, 43, 44, 58])
    FOLLOW_methodElement_in_intfMember967 = frozenset([39, 40, 41, 42, 43, 44, 58])
    FOLLOW_58_in_intfMember970 = frozenset([1])
    FOLLOW_SIGNAL_in_intfMember991 = frozenset([20])
    FOLLOW_signalID_in_intfMember993 = frozenset([57])
    FOLLOW_57_in_intfMember995 = frozenset([39, 43, 58])
    FOLLOW_signalElement_in_intfMember997 = frozenset([39, 43, 58])
    FOLLOW_58_in_intfMember1000 = frozenset([1])
    FOLLOW_RESULT_in_resultDef1023 = frozenset([57])
    FOLLOW_57_in_resultDef1025 = frozenset([36])
    FOLLOW_TYPE_in_resultDef1027 = frozenset([62])
    FOLLOW_62_in_resultDef1029 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 94, 95, 96])
    FOLLOW_typeArg_in_resultDef1031 = frozenset([59])
    FOLLOW_59_in_resultDef1033 = frozenset([45, 58])
    FOLLOW_modifiers_in_resultDef1035 = frozenset([58])
    FOLLOW_58_in_resultDef1038 = frozenset([1])
    FOLLOW_constructorElement_in_methodElement1061 = frozenset([1])
    FOLLOW_resultDef_in_methodElement1066 = frozenset([1])
    FOLLOW_VISIBILITY_in_methodElement1071 = frozenset([62])
    FOLLOW_62_in_methodElement1073 = frozenset([63, 64, 65])
    FOLLOW_63_in_methodElement1078 = frozenset([59])
    FOLLOW_64_in_methodElement1082 = frozenset([59])
    FOLLOW_65_in_methodElement1086 = frozenset([59])
    FOLLOW_59_in_methodElement1089 = frozenset([1])
    FOLLOW_SCOPE_in_methodElement1104 = frozenset([62])
    FOLLOW_62_in_methodElement1106 = frozenset([66, 67])
    FOLLOW_66_in_methodElement1111 = frozenset([59])
    FOLLOW_67_in_methodElement1115 = frozenset([59])
    FOLLOW_59_in_methodElement1118 = frozenset([1])
    FOLLOW_INHERITANCE_in_methodElement1134 = frozenset([62])
    FOLLOW_62_in_methodElement1136 = frozenset([29, 68, 69])
    FOLLOW_68_in_methodElement1141 = frozenset([59])
    FOLLOW_69_in_methodElement1145 = frozenset([59])
    FOLLOW_ABSTRACT_in_methodElement1149 = frozenset([59])
    FOLLOW_59_in_methodElement1152 = frozenset([1])
    FOLLOW_PARAMETER_in_constructorElement1174 = frozenset([20])
    FOLLOW_ID_in_constructorElement1176 = frozenset([57])
    FOLLOW_57_in_constructorElement1178 = frozenset([36])
    FOLLOW_TYPE_in_constructorElement1180 = frozenset([62])
    FOLLOW_62_in_constructorElement1182 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 94, 95, 96])
    FOLLOW_typeArg_in_constructorElement1184 = frozenset([59])
    FOLLOW_59_in_constructorElement1186 = frozenset([45, 58, 70])
    FOLLOW_parameterElement_in_constructorElement1188 = frozenset([58])
    FOLLOW_58_in_constructorElement1191 = frozenset([1])
    FOLLOW_INIT_PROPERTIES_in_constructorElement1216 = frozenset([57])
    FOLLOW_57_in_constructorElement1218 = frozenset([20])
    FOLLOW_init_prop_in_constructorElement1220 = frozenset([20, 58])
    FOLLOW_58_in_constructorElement1223 = frozenset([1])
    FOLLOW_modifiers_in_parameterElement1250 = frozenset([1])
    FOLLOW_70_in_parameterElement1263 = frozenset([62])
    FOLLOW_62_in_parameterElement1265 = frozenset([20])
    FOLLOW_ID_in_parameterElement1267 = frozenset([59])
    FOLLOW_59_in_parameterElement1269 = frozenset([1])
    FOLLOW_ID_in_init_prop1298 = frozenset([62])
    FOLLOW_62_in_init_prop1300 = frozenset([19])
    FOLLOW_STRING_in_init_prop1304 = frozenset([59])
    FOLLOW_59_in_init_prop1306 = frozenset([1])
    FOLLOW_ID_in_init_prop1335 = frozenset([62])
    FOLLOW_62_in_init_prop1337 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 96])
    FOLLOW_typeName_in_init_prop1341 = frozenset([71])
    FOLLOW_71_in_init_prop1343 = frozenset([20])
    FOLLOW_ID_in_init_prop1347 = frozenset([59])
    FOLLOW_59_in_init_prop1349 = frozenset([1])
    FOLLOW_MODIFIERS_in_modifiers1383 = frozenset([62])
    FOLLOW_62_in_modifiers1385 = frozenset([72])
    FOLLOW_72_in_modifiers1387 = frozenset([59])
    FOLLOW_59_in_modifiers1389 = frozenset([1])
    FOLLOW_TYPE_in_propertyElement1413 = frozenset([62])
    FOLLOW_62_in_propertyElement1415 = frozenset([73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_73_in_propertyElement1420 = frozenset([59])
    FOLLOW_74_in_propertyElement1424 = frozenset([59])
    FOLLOW_75_in_propertyElement1428 = frozenset([59])
    FOLLOW_76_in_propertyElement1432 = frozenset([59])
    FOLLOW_77_in_propertyElement1441 = frozenset([59])
    FOLLOW_78_in_propertyElement1445 = frozenset([59])
    FOLLOW_79_in_propertyElement1449 = frozenset([59])
    FOLLOW_80_in_propertyElement1453 = frozenset([59])
    FOLLOW_59_in_propertyElement1456 = frozenset([1])
    FOLLOW_81_in_propertyElement1480 = frozenset([62])
    FOLLOW_62_in_propertyElement1482 = frozenset([82, 83, 84])
    FOLLOW_82_in_propertyElement1487 = frozenset([59])
    FOLLOW_83_in_propertyElement1491 = frozenset([59])
    FOLLOW_84_in_propertyElement1495 = frozenset([59])
    FOLLOW_59_in_propertyElement1498 = frozenset([1])
    FOLLOW_85_in_propertyElement1522 = frozenset([62])
    FOLLOW_62_in_propertyElement1524 = frozenset([19])
    FOLLOW_STRING_in_propertyElement1526 = frozenset([59])
    FOLLOW_59_in_propertyElement1528 = frozenset([1])
    FOLLOW_GTYPE_in_propertyElement1546 = frozenset([62])
    FOLLOW_62_in_propertyElement1548 = frozenset([20])
    FOLLOW_ID_in_propertyElement1550 = frozenset([59])
    FOLLOW_59_in_propertyElement1552 = frozenset([1])
    FOLLOW_GTYPE_in_propertyElement1575 = frozenset([62])
    FOLLOW_62_in_propertyElement1577 = frozenset([46])
    FOLLOW_GTYPENAME_in_propertyElement1579 = frozenset([86])
    FOLLOW_86_in_propertyElement1581 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 96])
    FOLLOW_typeName_in_propertyElement1583 = frozenset([87])
    FOLLOW_87_in_propertyElement1585 = frozenset([59])
    FOLLOW_59_in_propertyElement1587 = frozenset([1])
    FOLLOW_88_in_propertyElement1614 = frozenset([62])
    FOLLOW_62_in_propertyElement1616 = frozenset([19])
    FOLLOW_STRING_in_propertyElement1618 = frozenset([59])
    FOLLOW_59_in_propertyElement1620 = frozenset([1])
    FOLLOW_88_in_propertyElement1636 = frozenset([62])
    FOLLOW_62_in_propertyElement1638 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 96])
    FOLLOW_typeName_in_propertyElement1642 = frozenset([71])
    FOLLOW_71_in_propertyElement1644 = frozenset([20])
    FOLLOW_ID_in_propertyElement1648 = frozenset([59])
    FOLLOW_59_in_propertyElement1650 = frozenset([1])
    FOLLOW_89_in_propertyElement1672 = frozenset([62])
    FOLLOW_62_in_propertyElement1674 = frozenset([19])
    FOLLOW_STRING_in_propertyElement1676 = frozenset([59])
    FOLLOW_59_in_propertyElement1678 = frozenset([1])
    FOLLOW_89_in_propertyElement1694 = frozenset([62])
    FOLLOW_62_in_propertyElement1696 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 96])
    FOLLOW_typeName_in_propertyElement1700 = frozenset([71])
    FOLLOW_71_in_propertyElement1702 = frozenset([20])
    FOLLOW_ID_in_propertyElement1706 = frozenset([59])
    FOLLOW_59_in_propertyElement1708 = frozenset([1])
    FOLLOW_90_in_propertyElement1730 = frozenset([62])
    FOLLOW_62_in_propertyElement1732 = frozenset([19])
    FOLLOW_STRING_in_propertyElement1734 = frozenset([59])
    FOLLOW_59_in_propertyElement1736 = frozenset([1])
    FOLLOW_90_in_propertyElement1752 = frozenset([62])
    FOLLOW_62_in_propertyElement1754 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 96])
    FOLLOW_typeName_in_propertyElement1758 = frozenset([71])
    FOLLOW_71_in_propertyElement1760 = frozenset([20])
    FOLLOW_ID_in_propertyElement1764 = frozenset([59])
    FOLLOW_59_in_propertyElement1766 = frozenset([1])
    FOLLOW_AUTO_CREATE_in_propertyElement1788 = frozenset([59])
    FOLLOW_59_in_propertyElement1791 = frozenset([1])
    FOLLOW_RESULT_in_signalElement1810 = frozenset([57])
    FOLLOW_57_in_signalElement1812 = frozenset([36])
    FOLLOW_TYPE_in_signalElement1814 = frozenset([62])
    FOLLOW_62_in_signalElement1816 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 94, 95, 96])
    FOLLOW_typeArg_in_signalElement1818 = frozenset([59])
    FOLLOW_59_in_signalElement1820 = frozenset([58])
    FOLLOW_58_in_signalElement1822 = frozenset([1])
    FOLLOW_PARAMETER_in_signalElement1840 = frozenset([20])
    FOLLOW_ID_in_signalElement1842 = frozenset([57])
    FOLLOW_57_in_signalElement1844 = frozenset([36])
    FOLLOW_TYPE_in_signalElement1846 = frozenset([62])
    FOLLOW_62_in_signalElement1848 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 94, 95, 96])
    FOLLOW_typeArg_in_signalElement1850 = frozenset([59])
    FOLLOW_59_in_signalElement1852 = frozenset([58])
    FOLLOW_58_in_signalElement1854 = frozenset([1])
    FOLLOW_SCOPE_in_attributeElement1878 = frozenset([62])
    FOLLOW_62_in_attributeElement1880 = frozenset([66, 67])
    FOLLOW_67_in_attributeElement1885 = frozenset([59])
    FOLLOW_66_in_attributeElement1889 = frozenset([59])
    FOLLOW_59_in_attributeElement1892 = frozenset([1])
    FOLLOW_VISIBILITY_in_attributeElement1906 = frozenset([62])
    FOLLOW_62_in_attributeElement1908 = frozenset([63, 64, 65])
    FOLLOW_63_in_attributeElement1913 = frozenset([59])
    FOLLOW_64_in_attributeElement1917 = frozenset([59])
    FOLLOW_65_in_attributeElement1921 = frozenset([59])
    FOLLOW_59_in_attributeElement1924 = frozenset([1])
    FOLLOW_typePath_in_typeName1946 = frozenset([1])
    FOLLOW_91_in_typeName1961 = frozenset([74])
    FOLLOW_74_in_typeName1964 = frozenset([1])
    FOLLOW_91_in_typeName1982 = frozenset([92])
    FOLLOW_92_in_typeName1985 = frozenset([1])
    FOLLOW_93_in_typeName2004 = frozenset([1])
    FOLLOW_73_in_typeName2013 = frozenset([1])
    FOLLOW_77_in_typeName2020 = frozenset([1])
    FOLLOW_75_in_typeName2027 = frozenset([1])
    FOLLOW_76_in_typeName2034 = frozenset([1])
    FOLLOW_78_in_typeName2043 = frozenset([1])
    FOLLOW_typeName_in_typeArg2069 = frozenset([1])
    FOLLOW_94_in_typeArg2079 = frozenset([86])
    FOLLOW_86_in_typeArg2081 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 94, 95, 96])
    FOLLOW_typeArg_in_typeArg2083 = frozenset([87])
    FOLLOW_87_in_typeArg2085 = frozenset([1])
    FOLLOW_95_in_typeArg2103 = frozenset([86])
    FOLLOW_86_in_typeArg2105 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 94, 95, 96])
    FOLLOW_typeArg_in_typeArg2107 = frozenset([87])
    FOLLOW_87_in_typeArg2109 = frozenset([1])
    FOLLOW_96_in_typePath2137 = frozenset([20])
    FOLLOW_ID_in_typePath2139 = frozenset([96])
    FOLLOW_96_in_typePath2141 = frozenset([20])
    FOLLOW_ID_in_typePath2145 = frozenset([96])
    FOLLOW_96_in_typePath2147 = frozenset([20])
    FOLLOW_ID_in_typePath2151 = frozenset([1])
    FOLLOW_ID_in_signalID2754 = frozenset([1, 97])
    FOLLOW_97_in_signalID2757 = frozenset([20])
    FOLLOW_ID_in_signalID2761 = frozenset([1, 97])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("GOCLexer", GOCParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
