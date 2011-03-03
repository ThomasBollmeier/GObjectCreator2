# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 GOC.g 2011-03-03 20:27:10

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
    "OCTAL_ESC", "'include'", "';'", "'{'", "'}'", "'code'", "'value'", 
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
    # GOC.g:41:1: includeStmt : 'include' filename= STRING ';' -> ^( INCLUDE $filename) ;
    def includeStmt(self, ):

        retval = self.includeStmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        filename = None
        string_literal10 = None
        char_literal11 = None

        filename_tree = None
        string_literal10_tree = None
        char_literal11_tree = None
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")

        try:
            try:
                # GOC.g:42:5: ( 'include' filename= STRING ';' -> ^( INCLUDE $filename) )
                # GOC.g:42:9: 'include' filename= STRING ';'
                pass 
                string_literal10=self.match(self.input, 56, self.FOLLOW_56_in_includeStmt226) 
                stream_56.add(string_literal10)
                filename=self.match(self.input, STRING, self.FOLLOW_STRING_in_includeStmt230) 
                stream_STRING.add(filename)
                char_literal11=self.match(self.input, 57, self.FOLLOW_57_in_includeStmt232) 
                stream_57.add(char_literal11)

                # AST Rewrite
                # elements: filename
                # token labels: filename
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0
                stream_filename = RewriteRuleTokenStream(self._adaptor, "token filename", filename)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 42:39: -> ^( INCLUDE $filename)
                # GOC.g:42:42: ^( INCLUDE $filename)
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(INCLUDE, "INCLUDE"), root_1)

                self._adaptor.addChild(root_1, stream_filename.nextNode())

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

        string_literal12 = None
        ID13 = None
        char_literal14 = None
        char_literal16 = None
        packageElement15 = None


        string_literal12_tree = None
        ID13_tree = None
        char_literal14_tree = None
        char_literal16_tree = None
        stream_PACKAGE = RewriteRuleTokenStream(self._adaptor, "token PACKAGE")
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_packageElement = RewriteRuleSubtreeStream(self._adaptor, "rule packageElement")
        try:
            try:
                # GOC.g:46:2: ( 'package' ID '{' ( packageElement )* '}' -> ^( 'package' ID ( packageElement )* ) )
                # GOC.g:46:4: 'package' ID '{' ( packageElement )* '}'
                pass 
                string_literal12=self.match(self.input, PACKAGE, self.FOLLOW_PACKAGE_in_packageDef255) 
                stream_PACKAGE.add(string_literal12)
                ID13=self.match(self.input, ID, self.FOLLOW_ID_in_packageDef257) 
                stream_ID.add(ID13)
                char_literal14=self.match(self.input, 58, self.FOLLOW_58_in_packageDef259) 
                stream_58.add(char_literal14)
                # GOC.g:46:21: ( packageElement )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((GOBJECT <= LA3_0 <= ENUMERATION) or (FLAGS <= LA3_0 <= GTYPE) or LA3_0 == PACKAGE) :
                        alt3 = 1


                    if alt3 == 1:
                        # GOC.g:46:21: packageElement
                        pass 
                        self._state.following.append(self.FOLLOW_packageElement_in_packageDef261)
                        packageElement15 = self.packageElement()

                        self._state.following.pop()
                        stream_packageElement.add(packageElement15.tree)


                    else:
                        break #loop3
                char_literal16=self.match(self.input, 59, self.FOLLOW_59_in_packageDef264) 
                stream_59.add(char_literal16)

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

        packageDef17 = None

        classDef18 = None

        intfDef19 = None

        errorDomainDef20 = None

        enumDef21 = None

        flagsDef22 = None

        typeDecl23 = None



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

                    self._state.following.append(self.FOLLOW_packageDef_in_packageElement289)
                    packageDef17 = self.packageDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, packageDef17.tree)


                elif alt4 == 2:
                    # GOC.g:52:4: classDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_classDef_in_packageElement294)
                    classDef18 = self.classDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, classDef18.tree)


                elif alt4 == 3:
                    # GOC.g:53:4: intfDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_intfDef_in_packageElement299)
                    intfDef19 = self.intfDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, intfDef19.tree)


                elif alt4 == 4:
                    # GOC.g:54:6: errorDomainDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_errorDomainDef_in_packageElement306)
                    errorDomainDef20 = self.errorDomainDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, errorDomainDef20.tree)


                elif alt4 == 5:
                    # GOC.g:55:6: enumDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_enumDef_in_packageElement313)
                    enumDef21 = self.enumDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, enumDef21.tree)


                elif alt4 == 6:
                    # GOC.g:56:6: flagsDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_flagsDef_in_packageElement320)
                    flagsDef22 = self.flagsDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, flagsDef22.tree)


                elif alt4 == 7:
                    # GOC.g:57:6: typeDecl
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_typeDecl_in_packageElement327)
                    typeDecl23 = self.typeDecl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, typeDecl23.tree)


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
        GOBJECT24 = None
        char_literal25 = None
        char_literal27 = None
        char_literal28 = None
        classMember26 = None


        className_tree = None
        GOBJECT24_tree = None
        char_literal25_tree = None
        char_literal27_tree = None
        char_literal28_tree = None
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
                GOBJECT24=self.match(self.input, GOBJECT, self.FOLLOW_GOBJECT_in_classDef338) 
                stream_GOBJECT.add(GOBJECT24)
                className=self.match(self.input, ID, self.FOLLOW_ID_in_classDef342) 
                stream_ID.add(className)
                # GOC.g:61:25: ( '{' ( classMember )* '}' | ';' )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 58) :
                    alt6 = 1
                elif (LA6_0 == 57) :
                    alt6 = 2
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # GOC.g:61:26: '{' ( classMember )* '}'
                    pass 
                    char_literal25=self.match(self.input, 58, self.FOLLOW_58_in_classDef345) 
                    stream_58.add(char_literal25)
                    # GOC.g:61:30: ( classMember )*
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if ((SUPER <= LA5_0 <= ATTRIBUTE) or (PROPERTY <= LA5_0 <= SIGNAL)) :
                            alt5 = 1


                        if alt5 == 1:
                            # GOC.g:61:30: classMember
                            pass 
                            self._state.following.append(self.FOLLOW_classMember_in_classDef347)
                            classMember26 = self.classMember()

                            self._state.following.pop()
                            stream_classMember.add(classMember26.tree)


                        else:
                            break #loop5
                    char_literal27=self.match(self.input, 59, self.FOLLOW_59_in_classDef350) 
                    stream_59.add(char_literal27)


                elif alt6 == 2:
                    # GOC.g:61:47: ';'
                    pass 
                    char_literal28=self.match(self.input, 57, self.FOLLOW_57_in_classDef352) 
                    stream_57.add(char_literal28)




                # AST Rewrite
                # elements: className, GOBJECT, classMember
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
        GINTERFACE29 = None
        char_literal30 = None
        char_literal32 = None
        char_literal33 = None
        intfMember31 = None


        intfName_tree = None
        GINTERFACE29_tree = None
        char_literal30_tree = None
        char_literal32_tree = None
        char_literal33_tree = None
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
                GINTERFACE29=self.match(self.input, GINTERFACE, self.FOLLOW_GINTERFACE_in_intfDef379) 
                stream_GINTERFACE.add(GINTERFACE29)
                intfName=self.match(self.input, ID, self.FOLLOW_ID_in_intfDef383) 
                stream_ID.add(intfName)
                # GOC.g:66:27: ( '{' ( intfMember )* '}' | ';' )
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == 58) :
                    alt8 = 1
                elif (LA8_0 == 57) :
                    alt8 = 2
                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # GOC.g:66:28: '{' ( intfMember )* '}'
                    pass 
                    char_literal30=self.match(self.input, 58, self.FOLLOW_58_in_intfDef386) 
                    stream_58.add(char_literal30)
                    # GOC.g:66:32: ( intfMember )*
                    while True: #loop7
                        alt7 = 2
                        LA7_0 = self.input.LA(1)

                        if (LA7_0 == PREFIX or LA7_0 == METHOD or LA7_0 == SIGNAL) :
                            alt7 = 1


                        if alt7 == 1:
                            # GOC.g:66:32: intfMember
                            pass 
                            self._state.following.append(self.FOLLOW_intfMember_in_intfDef388)
                            intfMember31 = self.intfMember()

                            self._state.following.pop()
                            stream_intfMember.add(intfMember31.tree)


                        else:
                            break #loop7
                    char_literal32=self.match(self.input, 59, self.FOLLOW_59_in_intfDef391) 
                    stream_59.add(char_literal32)


                elif alt8 == 2:
                    # GOC.g:66:48: ';'
                    pass 
                    char_literal33=self.match(self.input, 57, self.FOLLOW_57_in_intfDef393) 
                    stream_57.add(char_literal33)




                # AST Rewrite
                # elements: GINTERFACE, intfName, intfMember
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

        ERROR_DOMAIN34 = None
        ID35 = None
        char_literal36 = None
        char_literal38 = None
        errorDomainElement37 = None


        ERROR_DOMAIN34_tree = None
        ID35_tree = None
        char_literal36_tree = None
        char_literal38_tree = None
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_ERROR_DOMAIN = RewriteRuleTokenStream(self._adaptor, "token ERROR_DOMAIN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_errorDomainElement = RewriteRuleSubtreeStream(self._adaptor, "rule errorDomainElement")
        try:
            try:
                # GOC.g:71:5: ( ERROR_DOMAIN ID '{' ( errorDomainElement )+ '}' -> ^( ERROR_DOMAIN ID ( errorDomainElement )+ ) )
                # GOC.g:71:9: ERROR_DOMAIN ID '{' ( errorDomainElement )+ '}'
                pass 
                ERROR_DOMAIN34=self.match(self.input, ERROR_DOMAIN, self.FOLLOW_ERROR_DOMAIN_in_errorDomainDef424) 
                stream_ERROR_DOMAIN.add(ERROR_DOMAIN34)
                ID35=self.match(self.input, ID, self.FOLLOW_ID_in_errorDomainDef426) 
                stream_ID.add(ID35)
                char_literal36=self.match(self.input, 58, self.FOLLOW_58_in_errorDomainDef428) 
                stream_58.add(char_literal36)
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
                        self._state.following.append(self.FOLLOW_errorDomainElement_in_errorDomainDef430)
                        errorDomainElement37 = self.errorDomainElement()

                        self._state.following.pop()
                        stream_errorDomainElement.add(errorDomainElement37.tree)


                    else:
                        if cnt9 >= 1:
                            break #loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1
                char_literal38=self.match(self.input, 59, self.FOLLOW_59_in_errorDomainDef433) 
                stream_59.add(char_literal38)

                # AST Rewrite
                # elements: ERROR_DOMAIN, ID, errorDomainElement
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

        string_literal39 = None
        ID40 = None
        char_literal41 = None

        string_literal39_tree = None
        ID40_tree = None
        char_literal41_tree = None
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")

        try:
            try:
                # GOC.g:76:5: ( 'code' ID ';' -> ^( ID ) )
                # GOC.g:76:9: 'code' ID ';'
                pass 
                string_literal39=self.match(self.input, 60, self.FOLLOW_60_in_errorDomainElement468) 
                stream_60.add(string_literal39)
                ID40=self.match(self.input, ID, self.FOLLOW_ID_in_errorDomainElement470) 
                stream_ID.add(ID40)
                char_literal41=self.match(self.input, 57, self.FOLLOW_57_in_errorDomainElement472) 
                stream_57.add(char_literal41)

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

        ENUMERATION42 = None
        ID43 = None
        char_literal44 = None
        char_literal46 = None
        enumElement45 = None


        ENUMERATION42_tree = None
        ID43_tree = None
        char_literal44_tree = None
        char_literal46_tree = None
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_ENUMERATION = RewriteRuleTokenStream(self._adaptor, "token ENUMERATION")
        stream_enumElement = RewriteRuleSubtreeStream(self._adaptor, "rule enumElement")
        try:
            try:
                # GOC.g:80:5: ( ENUMERATION ID '{' ( enumElement )+ '}' -> ^( ENUMERATION ID ( enumElement )+ ) )
                # GOC.g:80:9: ENUMERATION ID '{' ( enumElement )+ '}'
                pass 
                ENUMERATION42=self.match(self.input, ENUMERATION, self.FOLLOW_ENUMERATION_in_enumDef497) 
                stream_ENUMERATION.add(ENUMERATION42)
                ID43=self.match(self.input, ID, self.FOLLOW_ID_in_enumDef499) 
                stream_ID.add(ID43)
                char_literal44=self.match(self.input, 58, self.FOLLOW_58_in_enumDef501) 
                stream_58.add(char_literal44)
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
                        self._state.following.append(self.FOLLOW_enumElement_in_enumDef503)
                        enumElement45 = self.enumElement()

                        self._state.following.pop()
                        stream_enumElement.add(enumElement45.tree)


                    else:
                        if cnt10 >= 1:
                            break #loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1
                char_literal46=self.match(self.input, 59, self.FOLLOW_59_in_enumDef506) 
                stream_59.add(char_literal46)

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

        string_literal47 = None
        ID48 = None
        char_literal49 = None
        char_literal50 = None
        string_literal51 = None
        char_literal52 = None
        INT53 = None
        char_literal54 = None
        char_literal55 = None

        string_literal47_tree = None
        ID48_tree = None
        char_literal49_tree = None
        char_literal50_tree = None
        string_literal51_tree = None
        char_literal52_tree = None
        INT53_tree = None
        char_literal54_tree = None
        char_literal55_tree = None
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")
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
                string_literal47=self.match(self.input, 60, self.FOLLOW_60_in_enumElement541) 
                stream_60.add(string_literal47)
                ID48=self.match(self.input, ID, self.FOLLOW_ID_in_enumElement543) 
                stream_ID.add(ID48)
                # GOC.g:85:19: ( ';' | '{' 'value' ':' INT ';' '}' )
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == 57) :
                    alt11 = 1
                elif (LA11_0 == 58) :
                    alt11 = 2
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # GOC.g:85:20: ';'
                    pass 
                    char_literal49=self.match(self.input, 57, self.FOLLOW_57_in_enumElement546) 
                    stream_57.add(char_literal49)


                elif alt11 == 2:
                    # GOC.g:85:24: '{' 'value' ':' INT ';' '}'
                    pass 
                    char_literal50=self.match(self.input, 58, self.FOLLOW_58_in_enumElement548) 
                    stream_58.add(char_literal50)
                    string_literal51=self.match(self.input, 61, self.FOLLOW_61_in_enumElement550) 
                    stream_61.add(string_literal51)
                    char_literal52=self.match(self.input, 62, self.FOLLOW_62_in_enumElement552) 
                    stream_62.add(char_literal52)
                    INT53=self.match(self.input, INT, self.FOLLOW_INT_in_enumElement554) 
                    stream_INT.add(INT53)
                    char_literal54=self.match(self.input, 57, self.FOLLOW_57_in_enumElement556) 
                    stream_57.add(char_literal54)
                    char_literal55=self.match(self.input, 59, self.FOLLOW_59_in_enumElement558) 
                    stream_59.add(char_literal55)




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

        FLAGS56 = None
        ID57 = None
        char_literal58 = None
        char_literal60 = None
        flagsElement59 = None


        FLAGS56_tree = None
        ID57_tree = None
        char_literal58_tree = None
        char_literal60_tree = None
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_FLAGS = RewriteRuleTokenStream(self._adaptor, "token FLAGS")
        stream_flagsElement = RewriteRuleSubtreeStream(self._adaptor, "rule flagsElement")
        try:
            try:
                # GOC.g:90:5: ( FLAGS ID '{' ( flagsElement )+ '}' -> ^( FLAGS ID ( flagsElement )+ ) )
                # GOC.g:90:9: FLAGS ID '{' ( flagsElement )+ '}'
                pass 
                FLAGS56=self.match(self.input, FLAGS, self.FOLLOW_FLAGS_in_flagsDef594) 
                stream_FLAGS.add(FLAGS56)
                ID57=self.match(self.input, ID, self.FOLLOW_ID_in_flagsDef596) 
                stream_ID.add(ID57)
                char_literal58=self.match(self.input, 58, self.FOLLOW_58_in_flagsDef598) 
                stream_58.add(char_literal58)
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
                        self._state.following.append(self.FOLLOW_flagsElement_in_flagsDef600)
                        flagsElement59 = self.flagsElement()

                        self._state.following.pop()
                        stream_flagsElement.add(flagsElement59.tree)


                    else:
                        if cnt12 >= 1:
                            break #loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1
                char_literal60=self.match(self.input, 59, self.FOLLOW_59_in_flagsDef603) 
                stream_59.add(char_literal60)

                # AST Rewrite
                # elements: flagsElement, ID, FLAGS
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

        string_literal61 = None
        ID62 = None
        char_literal63 = None

        string_literal61_tree = None
        ID62_tree = None
        char_literal63_tree = None
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")

        try:
            try:
                # GOC.g:95:5: ( 'code' ID ';' -> ^( ID ) )
                # GOC.g:95:9: 'code' ID ';'
                pass 
                string_literal61=self.match(self.input, 60, self.FOLLOW_60_in_flagsElement638) 
                stream_60.add(string_literal61)
                ID62=self.match(self.input, ID, self.FOLLOW_ID_in_flagsElement640) 
                stream_ID.add(ID62)
                char_literal63=self.match(self.input, 57, self.FOLLOW_57_in_flagsElement642) 
                stream_57.add(char_literal63)

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

        GTYPE64 = None
        ID65 = None
        char_literal66 = None

        GTYPE64_tree = None
        ID65_tree = None
        char_literal66_tree = None
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_GTYPE = RewriteRuleTokenStream(self._adaptor, "token GTYPE")

        try:
            try:
                # GOC.g:99:5: ( GTYPE ID ';' -> ^( GTYPE ID ) )
                # GOC.g:99:9: GTYPE ID ';'
                pass 
                GTYPE64=self.match(self.input, GTYPE, self.FOLLOW_GTYPE_in_typeDecl667) 
                stream_GTYPE.add(GTYPE64)
                ID65=self.match(self.input, ID, self.FOLLOW_ID_in_typeDecl669) 
                stream_ID.add(ID65)
                char_literal66=self.match(self.input, 57, self.FOLLOW_57_in_typeDecl671) 
                stream_57.add(char_literal66)

                # AST Rewrite
                # elements: GTYPE, ID
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

        SUPER67 = None
        char_literal69 = None
        ABSTRACT70 = None
        char_literal71 = None
        PREFIX72 = None
        ID73 = None
        char_literal74 = None
        IMPLEMENTS75 = None
        char_literal77 = None
        CONSTRUCTOR78 = None
        char_literal79 = None
        char_literal81 = None
        METHOD82 = None
        ID83 = None
        char_literal84 = None
        char_literal86 = None
        OVERRIDE87 = None
        ID88 = None
        char_literal89 = None
        ATTRIBUTE90 = None
        ID91 = None
        char_literal92 = None
        TYPE93 = None
        char_literal94 = None
        char_literal96 = None
        char_literal98 = None
        PROPERTY99 = None
        ID100 = None
        char_literal101 = None
        char_literal103 = None
        SIGNAL104 = None
        char_literal106 = None
        char_literal108 = None
        typeName68 = None

        typeName76 = None

        constructorElement80 = None

        methodElement85 = None

        typeArg95 = None

        attributeElement97 = None

        propertyElement102 = None

        signalID105 = None

        signalElement107 = None


        SUPER67_tree = None
        char_literal69_tree = None
        ABSTRACT70_tree = None
        char_literal71_tree = None
        PREFIX72_tree = None
        ID73_tree = None
        char_literal74_tree = None
        IMPLEMENTS75_tree = None
        char_literal77_tree = None
        CONSTRUCTOR78_tree = None
        char_literal79_tree = None
        char_literal81_tree = None
        METHOD82_tree = None
        ID83_tree = None
        char_literal84_tree = None
        char_literal86_tree = None
        OVERRIDE87_tree = None
        ID88_tree = None
        char_literal89_tree = None
        ATTRIBUTE90_tree = None
        ID91_tree = None
        char_literal92_tree = None
        TYPE93_tree = None
        char_literal94_tree = None
        char_literal96_tree = None
        char_literal98_tree = None
        PROPERTY99_tree = None
        ID100_tree = None
        char_literal101_tree = None
        char_literal103_tree = None
        SIGNAL104_tree = None
        char_literal106_tree = None
        char_literal108_tree = None
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
                    SUPER67=self.match(self.input, SUPER, self.FOLLOW_SUPER_in_classMember702) 
                    stream_SUPER.add(SUPER67)
                    self._state.following.append(self.FOLLOW_typeName_in_classMember704)
                    typeName68 = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(typeName68.tree)
                    char_literal69=self.match(self.input, 57, self.FOLLOW_57_in_classMember706) 
                    stream_57.add(char_literal69)

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

                    ABSTRACT70=self.match(self.input, ABSTRACT, self.FOLLOW_ABSTRACT_in_classMember722)

                    ABSTRACT70_tree = self._adaptor.createWithPayload(ABSTRACT70)
                    root_0 = self._adaptor.becomeRoot(ABSTRACT70_tree, root_0)

                    char_literal71=self.match(self.input, 57, self.FOLLOW_57_in_classMember725)

                    char_literal71_tree = self._adaptor.createWithPayload(char_literal71)
                    self._adaptor.addChild(root_0, char_literal71_tree)



                elif alt18 == 3:
                    # GOC.g:112:6: PREFIX ID ';'
                    pass 
                    PREFIX72=self.match(self.input, PREFIX, self.FOLLOW_PREFIX_in_classMember732) 
                    stream_PREFIX.add(PREFIX72)
                    ID73=self.match(self.input, ID, self.FOLLOW_ID_in_classMember734) 
                    stream_ID.add(ID73)
                    char_literal74=self.match(self.input, 57, self.FOLLOW_57_in_classMember736) 
                    stream_57.add(char_literal74)

                    # AST Rewrite
                    # elements: PREFIX, ID
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
                    IMPLEMENTS75=self.match(self.input, IMPLEMENTS, self.FOLLOW_IMPLEMENTS_in_classMember749) 
                    stream_IMPLEMENTS.add(IMPLEMENTS75)
                    self._state.following.append(self.FOLLOW_typeName_in_classMember751)
                    typeName76 = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(typeName76.tree)
                    char_literal77=self.match(self.input, 57, self.FOLLOW_57_in_classMember753) 
                    stream_57.add(char_literal77)

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
                    CONSTRUCTOR78=self.match(self.input, CONSTRUCTOR, self.FOLLOW_CONSTRUCTOR_in_classMember773) 
                    stream_CONSTRUCTOR.add(CONSTRUCTOR78)
                    char_literal79=self.match(self.input, 58, self.FOLLOW_58_in_classMember775) 
                    stream_58.add(char_literal79)
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
                            self._state.following.append(self.FOLLOW_constructorElement_in_classMember777)
                            constructorElement80 = self.constructorElement()

                            self._state.following.pop()
                            stream_constructorElement.add(constructorElement80.tree)


                        else:
                            break #loop13
                    char_literal81=self.match(self.input, 59, self.FOLLOW_59_in_classMember780) 
                    stream_59.add(char_literal81)
                    #action start
                    self.classMember_stack[-1].with_constructor = False 
                    #action end

                    # AST Rewrite
                    # elements: CONSTRUCTOR, constructorElement
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
                    METHOD82=self.match(self.input, METHOD, self.FOLLOW_METHOD_in_classMember808) 
                    stream_METHOD.add(METHOD82)
                    ID83=self.match(self.input, ID, self.FOLLOW_ID_in_classMember810) 
                    stream_ID.add(ID83)
                    char_literal84=self.match(self.input, 58, self.FOLLOW_58_in_classMember812) 
                    stream_58.add(char_literal84)
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
                            self._state.following.append(self.FOLLOW_methodElement_in_classMember814)
                            methodElement85 = self.methodElement()

                            self._state.following.pop()
                            stream_methodElement.add(methodElement85.tree)


                        else:
                            break #loop14
                    char_literal86=self.match(self.input, 59, self.FOLLOW_59_in_classMember817) 
                    stream_59.add(char_literal86)

                    # AST Rewrite
                    # elements: methodElement, METHOD, ID
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
                    OVERRIDE87=self.match(self.input, OVERRIDE, self.FOLLOW_OVERRIDE_in_classMember834) 
                    stream_OVERRIDE.add(OVERRIDE87)
                    ID88=self.match(self.input, ID, self.FOLLOW_ID_in_classMember836) 
                    stream_ID.add(ID88)
                    char_literal89=self.match(self.input, 57, self.FOLLOW_57_in_classMember838) 
                    stream_57.add(char_literal89)

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
                    ATTRIBUTE90=self.match(self.input, ATTRIBUTE, self.FOLLOW_ATTRIBUTE_in_classMember851) 
                    stream_ATTRIBUTE.add(ATTRIBUTE90)
                    ID91=self.match(self.input, ID, self.FOLLOW_ID_in_classMember853) 
                    stream_ID.add(ID91)
                    char_literal92=self.match(self.input, 58, self.FOLLOW_58_in_classMember855) 
                    stream_58.add(char_literal92)
                    TYPE93=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_classMember857) 
                    stream_TYPE.add(TYPE93)
                    char_literal94=self.match(self.input, 62, self.FOLLOW_62_in_classMember859) 
                    stream_62.add(char_literal94)
                    self._state.following.append(self.FOLLOW_typeArg_in_classMember861)
                    typeArg95 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg95.tree)
                    char_literal96=self.match(self.input, 57, self.FOLLOW_57_in_classMember863) 
                    stream_57.add(char_literal96)
                    # GOC.g:120:42: ( attributeElement )*
                    while True: #loop15
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if ((VISIBILITY <= LA15_0 <= SCOPE)) :
                            alt15 = 1


                        if alt15 == 1:
                            # GOC.g:120:42: attributeElement
                            pass 
                            self._state.following.append(self.FOLLOW_attributeElement_in_classMember865)
                            attributeElement97 = self.attributeElement()

                            self._state.following.pop()
                            stream_attributeElement.add(attributeElement97.tree)


                        else:
                            break #loop15
                    char_literal98=self.match(self.input, 59, self.FOLLOW_59_in_classMember868) 
                    stream_59.add(char_literal98)

                    # AST Rewrite
                    # elements: attributeElement, ATTRIBUTE, ID, typeArg
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
                    PROPERTY99=self.match(self.input, PROPERTY, self.FOLLOW_PROPERTY_in_classMember887) 
                    stream_PROPERTY.add(PROPERTY99)
                    ID100=self.match(self.input, ID, self.FOLLOW_ID_in_classMember889) 
                    stream_ID.add(ID100)
                    char_literal101=self.match(self.input, 58, self.FOLLOW_58_in_classMember891) 
                    stream_58.add(char_literal101)
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
                            self._state.following.append(self.FOLLOW_propertyElement_in_classMember893)
                            propertyElement102 = self.propertyElement()

                            self._state.following.pop()
                            stream_propertyElement.add(propertyElement102.tree)


                        else:
                            if cnt16 >= 1:
                                break #loop16

                            eee = EarlyExitException(16, self.input)
                            raise eee

                        cnt16 += 1
                    char_literal103=self.match(self.input, 59, self.FOLLOW_59_in_classMember896) 
                    stream_59.add(char_literal103)

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
                    SIGNAL104=self.match(self.input, SIGNAL, self.FOLLOW_SIGNAL_in_classMember912) 
                    stream_SIGNAL.add(SIGNAL104)
                    self._state.following.append(self.FOLLOW_signalID_in_classMember914)
                    signalID105 = self.signalID()

                    self._state.following.pop()
                    stream_signalID.add(signalID105.tree)
                    char_literal106=self.match(self.input, 58, self.FOLLOW_58_in_classMember916) 
                    stream_58.add(char_literal106)
                    # GOC.g:123:24: ( signalElement )*
                    while True: #loop17
                        alt17 = 2
                        LA17_0 = self.input.LA(1)

                        if (LA17_0 == RESULT or LA17_0 == PARAMETER) :
                            alt17 = 1


                        if alt17 == 1:
                            # GOC.g:123:24: signalElement
                            pass 
                            self._state.following.append(self.FOLLOW_signalElement_in_classMember918)
                            signalElement107 = self.signalElement()

                            self._state.following.pop()
                            stream_signalElement.add(signalElement107.tree)


                        else:
                            break #loop17
                    char_literal108=self.match(self.input, 59, self.FOLLOW_59_in_classMember921) 
                    stream_59.add(char_literal108)

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

        PREFIX109 = None
        ID110 = None
        char_literal111 = None
        METHOD112 = None
        ID113 = None
        char_literal114 = None
        char_literal116 = None
        SIGNAL117 = None
        char_literal119 = None
        char_literal121 = None
        methodElement115 = None

        signalID118 = None

        signalElement120 = None


        PREFIX109_tree = None
        ID110_tree = None
        char_literal111_tree = None
        METHOD112_tree = None
        ID113_tree = None
        char_literal114_tree = None
        char_literal116_tree = None
        SIGNAL117_tree = None
        char_literal119_tree = None
        char_literal121_tree = None
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
                    PREFIX109=self.match(self.input, PREFIX, self.FOLLOW_PREFIX_in_intfMember944) 
                    stream_PREFIX.add(PREFIX109)
                    ID110=self.match(self.input, ID, self.FOLLOW_ID_in_intfMember946) 
                    stream_ID.add(ID110)
                    char_literal111=self.match(self.input, 57, self.FOLLOW_57_in_intfMember948) 
                    stream_57.add(char_literal111)

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
                    METHOD112=self.match(self.input, METHOD, self.FOLLOW_METHOD_in_intfMember963) 
                    stream_METHOD.add(METHOD112)
                    ID113=self.match(self.input, ID, self.FOLLOW_ID_in_intfMember965) 
                    stream_ID.add(ID113)
                    char_literal114=self.match(self.input, 58, self.FOLLOW_58_in_intfMember967) 
                    stream_58.add(char_literal114)
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
                            self._state.following.append(self.FOLLOW_methodElement_in_intfMember969)
                            methodElement115 = self.methodElement()

                            self._state.following.pop()
                            stream_methodElement.add(methodElement115.tree)


                        else:
                            break #loop19
                    char_literal116=self.match(self.input, 59, self.FOLLOW_59_in_intfMember972) 
                    stream_59.add(char_literal116)

                    # AST Rewrite
                    # elements: ID, methodElement, METHOD
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
                    SIGNAL117=self.match(self.input, SIGNAL, self.FOLLOW_SIGNAL_in_intfMember993) 
                    stream_SIGNAL.add(SIGNAL117)
                    self._state.following.append(self.FOLLOW_signalID_in_intfMember995)
                    signalID118 = self.signalID()

                    self._state.following.pop()
                    stream_signalID.add(signalID118.tree)
                    char_literal119=self.match(self.input, 58, self.FOLLOW_58_in_intfMember997) 
                    stream_58.add(char_literal119)
                    # GOC.g:129:29: ( signalElement )*
                    while True: #loop20
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if (LA20_0 == RESULT or LA20_0 == PARAMETER) :
                            alt20 = 1


                        if alt20 == 1:
                            # GOC.g:129:29: signalElement
                            pass 
                            self._state.following.append(self.FOLLOW_signalElement_in_intfMember999)
                            signalElement120 = self.signalElement()

                            self._state.following.pop()
                            stream_signalElement.add(signalElement120.tree)


                        else:
                            break #loop20
                    char_literal121=self.match(self.input, 59, self.FOLLOW_59_in_intfMember1002) 
                    stream_59.add(char_literal121)

                    # AST Rewrite
                    # elements: signalID, SIGNAL, signalElement
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

        RESULT122 = None
        char_literal123 = None
        TYPE124 = None
        char_literal125 = None
        char_literal127 = None
        char_literal129 = None
        typeArg126 = None

        modifiers128 = None


        RESULT122_tree = None
        char_literal123_tree = None
        TYPE124_tree = None
        char_literal125_tree = None
        char_literal127_tree = None
        char_literal129_tree = None
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
                RESULT122=self.match(self.input, RESULT, self.FOLLOW_RESULT_in_resultDef1025) 
                stream_RESULT.add(RESULT122)
                char_literal123=self.match(self.input, 58, self.FOLLOW_58_in_resultDef1027) 
                stream_58.add(char_literal123)
                TYPE124=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_resultDef1029) 
                stream_TYPE.add(TYPE124)
                char_literal125=self.match(self.input, 62, self.FOLLOW_62_in_resultDef1031) 
                stream_62.add(char_literal125)
                self._state.following.append(self.FOLLOW_typeArg_in_resultDef1033)
                typeArg126 = self.typeArg()

                self._state.following.pop()
                stream_typeArg.add(typeArg126.tree)
                char_literal127=self.match(self.input, 57, self.FOLLOW_57_in_resultDef1035) 
                stream_57.add(char_literal127)
                # GOC.g:133:36: ( modifiers )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == MODIFIERS) :
                    alt22 = 1
                if alt22 == 1:
                    # GOC.g:133:36: modifiers
                    pass 
                    self._state.following.append(self.FOLLOW_modifiers_in_resultDef1037)
                    modifiers128 = self.modifiers()

                    self._state.following.pop()
                    stream_modifiers.add(modifiers128.tree)



                char_literal129=self.match(self.input, 59, self.FOLLOW_59_in_resultDef1040) 
                stream_59.add(char_literal129)

                # AST Rewrite
                # elements: RESULT, typeArg, modifiers
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
        VISIBILITY132 = None
        char_literal133 = None
        char_literal134 = None
        SCOPE135 = None
        char_literal136 = None
        char_literal137 = None
        INHERITANCE138 = None
        char_literal139 = None
        char_literal140 = None
        constructorElement130 = None

        resultDef131 = None


        val_tree = None
        VISIBILITY132_tree = None
        char_literal133_tree = None
        char_literal134_tree = None
        SCOPE135_tree = None
        char_literal136_tree = None
        char_literal137_tree = None
        INHERITANCE138_tree = None
        char_literal139_tree = None
        char_literal140_tree = None
        stream_67 = RewriteRuleTokenStream(self._adaptor, "token 67")
        stream_66 = RewriteRuleTokenStream(self._adaptor, "token 66")
        stream_69 = RewriteRuleTokenStream(self._adaptor, "token 69")
        stream_68 = RewriteRuleTokenStream(self._adaptor, "token 68")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
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

                    self._state.following.append(self.FOLLOW_constructorElement_in_methodElement1063)
                    constructorElement130 = self.constructorElement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, constructorElement130.tree)


                elif alt26 == 2:
                    # GOC.g:139:4: resultDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_resultDef_in_methodElement1068)
                    resultDef131 = self.resultDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, resultDef131.tree)


                elif alt26 == 3:
                    # GOC.g:140:4: VISIBILITY ':' (val= 'public' | val= 'protected' | val= 'private' ) ';'
                    pass 
                    VISIBILITY132=self.match(self.input, VISIBILITY, self.FOLLOW_VISIBILITY_in_methodElement1073) 
                    stream_VISIBILITY.add(VISIBILITY132)
                    char_literal133=self.match(self.input, 62, self.FOLLOW_62_in_methodElement1075) 
                    stream_62.add(char_literal133)
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
                        val=self.match(self.input, 63, self.FOLLOW_63_in_methodElement1080) 
                        stream_63.add(val)


                    elif alt23 == 2:
                        # GOC.g:140:33: val= 'protected'
                        pass 
                        val=self.match(self.input, 64, self.FOLLOW_64_in_methodElement1084) 
                        stream_64.add(val)


                    elif alt23 == 3:
                        # GOC.g:140:49: val= 'private'
                        pass 
                        val=self.match(self.input, 65, self.FOLLOW_65_in_methodElement1088) 
                        stream_65.add(val)



                    char_literal134=self.match(self.input, 57, self.FOLLOW_57_in_methodElement1091) 
                    stream_57.add(char_literal134)

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
                    SCOPE135=self.match(self.input, SCOPE, self.FOLLOW_SCOPE_in_methodElement1106) 
                    stream_SCOPE.add(SCOPE135)
                    char_literal136=self.match(self.input, 62, self.FOLLOW_62_in_methodElement1108) 
                    stream_62.add(char_literal136)
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
                        val=self.match(self.input, 66, self.FOLLOW_66_in_methodElement1113) 
                        stream_66.add(val)


                    elif alt24 == 2:
                        # GOC.g:142:30: val= 'static'
                        pass 
                        val=self.match(self.input, 67, self.FOLLOW_67_in_methodElement1117) 
                        stream_67.add(val)



                    char_literal137=self.match(self.input, 57, self.FOLLOW_57_in_methodElement1120) 
                    stream_57.add(char_literal137)

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
                    INHERITANCE138=self.match(self.input, INHERITANCE, self.FOLLOW_INHERITANCE_in_methodElement1136) 
                    stream_INHERITANCE.add(INHERITANCE138)
                    char_literal139=self.match(self.input, 62, self.FOLLOW_62_in_methodElement1138) 
                    stream_62.add(char_literal139)
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
                        val=self.match(self.input, 68, self.FOLLOW_68_in_methodElement1143) 
                        stream_68.add(val)


                    elif alt25 == 2:
                        # GOC.g:144:34: val= 'virtual'
                        pass 
                        val=self.match(self.input, 69, self.FOLLOW_69_in_methodElement1147) 
                        stream_69.add(val)


                    elif alt25 == 3:
                        # GOC.g:144:48: val= 'abstract'
                        pass 
                        val=self.match(self.input, ABSTRACT, self.FOLLOW_ABSTRACT_in_methodElement1151) 
                        stream_ABSTRACT.add(val)



                    char_literal140=self.match(self.input, 57, self.FOLLOW_57_in_methodElement1154) 
                    stream_57.add(char_literal140)

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

        PARAMETER141 = None
        ID142 = None
        char_literal143 = None
        string_literal144 = None
        char_literal145 = None
        char_literal147 = None
        char_literal149 = None
        INIT_PROPERTIES150 = None
        char_literal151 = None
        char_literal153 = None
        typeArg146 = None

        parameterElement148 = None

        init_prop152 = None


        PARAMETER141_tree = None
        ID142_tree = None
        char_literal143_tree = None
        string_literal144_tree = None
        char_literal145_tree = None
        char_literal147_tree = None
        char_literal149_tree = None
        INIT_PROPERTIES150_tree = None
        char_literal151_tree = None
        char_literal153_tree = None
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
                    PARAMETER141=self.match(self.input, PARAMETER, self.FOLLOW_PARAMETER_in_constructorElement1176) 
                    stream_PARAMETER.add(PARAMETER141)
                    ID142=self.match(self.input, ID, self.FOLLOW_ID_in_constructorElement1178) 
                    stream_ID.add(ID142)
                    char_literal143=self.match(self.input, 58, self.FOLLOW_58_in_constructorElement1180) 
                    stream_58.add(char_literal143)
                    string_literal144=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_constructorElement1182) 
                    stream_TYPE.add(string_literal144)
                    char_literal145=self.match(self.input, 62, self.FOLLOW_62_in_constructorElement1184) 
                    stream_62.add(char_literal145)
                    self._state.following.append(self.FOLLOW_typeArg_in_constructorElement1186)
                    typeArg146 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg146.tree)
                    char_literal147=self.match(self.input, 57, self.FOLLOW_57_in_constructorElement1188) 
                    stream_57.add(char_literal147)
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
                        self._state.following.append(self.FOLLOW_parameterElement_in_constructorElement1190)
                        parameterElement148 = self.parameterElement()

                        self._state.following.pop()
                        stream_parameterElement.add(parameterElement148.tree)



                    char_literal149=self.match(self.input, 59, self.FOLLOW_59_in_constructorElement1193) 
                    stream_59.add(char_literal149)

                    # AST Rewrite
                    # elements: ID, parameterElement, PARAMETER, typeArg
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

                    INIT_PROPERTIES150=self.match(self.input, INIT_PROPERTIES, self.FOLLOW_INIT_PROPERTIES_in_constructorElement1218) 
                    stream_INIT_PROPERTIES.add(INIT_PROPERTIES150)
                    char_literal151=self.match(self.input, 58, self.FOLLOW_58_in_constructorElement1220) 
                    stream_58.add(char_literal151)
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
                            self._state.following.append(self.FOLLOW_init_prop_in_constructorElement1222)
                            init_prop152 = self.init_prop()

                            self._state.following.pop()
                            stream_init_prop.add(init_prop152.tree)


                        else:
                            if cnt28 >= 1:
                                break #loop28

                            eee = EarlyExitException(28, self.input)
                            raise eee

                        cnt28 += 1
                    char_literal153=self.match(self.input, 59, self.FOLLOW_59_in_constructorElement1225) 
                    stream_59.add(char_literal153)

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

        string_literal155 = None
        char_literal156 = None
        ID157 = None
        char_literal158 = None
        modifiers154 = None


        string_literal155_tree = None
        char_literal156_tree = None
        ID157_tree = None
        char_literal158_tree = None
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
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

                    self._state.following.append(self.FOLLOW_modifiers_in_parameterElement1252)
                    modifiers154 = self.modifiers()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, modifiers154.tree)


                elif alt30 == 2:
                    # GOC.g:157:9: {...}? => 'bind_property' ':' ID ';'
                    pass 
                    if not ((self.classMember_stack[-1].with_constructor)):
                        raise FailedPredicateException(self.input, "parameterElement", "$classMember::with_constructor")

                    string_literal155=self.match(self.input, 70, self.FOLLOW_70_in_parameterElement1265) 
                    stream_70.add(string_literal155)
                    char_literal156=self.match(self.input, 62, self.FOLLOW_62_in_parameterElement1267) 
                    stream_62.add(char_literal156)
                    ID157=self.match(self.input, ID, self.FOLLOW_ID_in_parameterElement1269) 
                    stream_ID.add(ID157)
                    char_literal158=self.match(self.input, 57, self.FOLLOW_57_in_parameterElement1271) 
                    stream_57.add(char_literal158)

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
        char_literal159 = None
        char_literal160 = None
        char_literal161 = None
        char_literal162 = None
        char_literal163 = None
        enum = None


        name_tree = None
        value_tree = None
        code_tree = None
        char_literal159_tree = None
        char_literal160_tree = None
        char_literal161_tree = None
        char_literal162_tree = None
        char_literal163_tree = None
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
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
                    name=self.match(self.input, ID, self.FOLLOW_ID_in_init_prop1300) 
                    stream_ID.add(name)
                    char_literal159=self.match(self.input, 62, self.FOLLOW_62_in_init_prop1302) 
                    stream_62.add(char_literal159)
                    value=self.match(self.input, STRING, self.FOLLOW_STRING_in_init_prop1306) 
                    stream_STRING.add(value)
                    char_literal160=self.match(self.input, 57, self.FOLLOW_57_in_init_prop1308) 
                    stream_57.add(char_literal160)

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
                    name=self.match(self.input, ID, self.FOLLOW_ID_in_init_prop1337) 
                    stream_ID.add(name)
                    char_literal161=self.match(self.input, 62, self.FOLLOW_62_in_init_prop1339) 
                    stream_62.add(char_literal161)
                    self._state.following.append(self.FOLLOW_typeName_in_init_prop1343)
                    enum = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(enum.tree)
                    char_literal162=self.match(self.input, 71, self.FOLLOW_71_in_init_prop1345) 
                    stream_71.add(char_literal162)
                    code=self.match(self.input, ID, self.FOLLOW_ID_in_init_prop1349) 
                    stream_ID.add(code)
                    char_literal163=self.match(self.input, 57, self.FOLLOW_57_in_init_prop1351) 
                    stream_57.add(char_literal163)

                    # AST Rewrite
                    # elements: code, enum, name
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

        MODIFIERS164 = None
        char_literal165 = None
        string_literal166 = None
        char_literal167 = None

        MODIFIERS164_tree = None
        char_literal165_tree = None
        string_literal166_tree = None
        char_literal167_tree = None
        stream_MODIFIERS = RewriteRuleTokenStream(self._adaptor, "token MODIFIERS")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_72 = RewriteRuleTokenStream(self._adaptor, "token 72")

        try:
            try:
                # GOC.g:168:2: ( MODIFIERS ':' 'const' ';' -> ^( MODIFIERS 'const' ) )
                # GOC.g:168:4: MODIFIERS ':' 'const' ';'
                pass 
                MODIFIERS164=self.match(self.input, MODIFIERS, self.FOLLOW_MODIFIERS_in_modifiers1385) 
                stream_MODIFIERS.add(MODIFIERS164)
                char_literal165=self.match(self.input, 62, self.FOLLOW_62_in_modifiers1387) 
                stream_62.add(char_literal165)
                string_literal166=self.match(self.input, 72, self.FOLLOW_72_in_modifiers1389) 
                stream_72.add(string_literal166)
                char_literal167=self.match(self.input, 57, self.FOLLOW_57_in_modifiers1391) 
                stream_57.add(char_literal167)

                # AST Rewrite
                # elements: MODIFIERS, 72
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
    # GOC.g:171:1: propertyElement : ( 'type' ':' (val= 'boolean' | val= 'integer' | val= 'float' | val= 'double' | val= 'string' | val= 'pointer' | val= 'object' | val= 'enumeration' ) ';' -> ^( PROP_TYPE $val) | 'access' ':' (val= 'read-only' | val= 'initial-write' | val= 'read-write' ) ';' -> ^( PROP_ACCESS $val) | 'description' ':' STRING ';' -> ^( PROP_DESC STRING ) | 'gtype' ':' ID ';' -> ^( PROP_GTYPE ID ) | 'gtype' ':' GTYPENAME '(' typeName ')' ';' -> ^( PROP_GTYPE ^( GTYPENAME typeName ) ) | 'min' ':' STRING ';' -> ^( PROP_MIN STRING ) | 'max' ':' STRING ';' -> ^( PROP_MAX STRING ) | 'default' ':' STRING ';' -> ^( PROP_DEFAULT STRING ) | AUTO_CREATE ';' );
    def propertyElement(self, ):

        retval = self.propertyElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        val = None
        string_literal168 = None
        char_literal169 = None
        char_literal170 = None
        string_literal171 = None
        char_literal172 = None
        char_literal173 = None
        string_literal174 = None
        char_literal175 = None
        STRING176 = None
        char_literal177 = None
        string_literal178 = None
        char_literal179 = None
        ID180 = None
        char_literal181 = None
        string_literal182 = None
        char_literal183 = None
        GTYPENAME184 = None
        char_literal185 = None
        char_literal187 = None
        char_literal188 = None
        string_literal189 = None
        char_literal190 = None
        STRING191 = None
        char_literal192 = None
        string_literal193 = None
        char_literal194 = None
        STRING195 = None
        char_literal196 = None
        string_literal197 = None
        char_literal198 = None
        STRING199 = None
        char_literal200 = None
        AUTO_CREATE201 = None
        char_literal202 = None
        typeName186 = None


        val_tree = None
        string_literal168_tree = None
        char_literal169_tree = None
        char_literal170_tree = None
        string_literal171_tree = None
        char_literal172_tree = None
        char_literal173_tree = None
        string_literal174_tree = None
        char_literal175_tree = None
        STRING176_tree = None
        char_literal177_tree = None
        string_literal178_tree = None
        char_literal179_tree = None
        ID180_tree = None
        char_literal181_tree = None
        string_literal182_tree = None
        char_literal183_tree = None
        GTYPENAME184_tree = None
        char_literal185_tree = None
        char_literal187_tree = None
        char_literal188_tree = None
        string_literal189_tree = None
        char_literal190_tree = None
        STRING191_tree = None
        char_literal192_tree = None
        string_literal193_tree = None
        char_literal194_tree = None
        STRING195_tree = None
        char_literal196_tree = None
        string_literal197_tree = None
        char_literal198_tree = None
        STRING199_tree = None
        char_literal200_tree = None
        AUTO_CREATE201_tree = None
        char_literal202_tree = None
        stream_79 = RewriteRuleTokenStream(self._adaptor, "token 79")
        stream_78 = RewriteRuleTokenStream(self._adaptor, "token 78")
        stream_77 = RewriteRuleTokenStream(self._adaptor, "token 77")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
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
                # GOC.g:172:5: ( 'type' ':' (val= 'boolean' | val= 'integer' | val= 'float' | val= 'double' | val= 'string' | val= 'pointer' | val= 'object' | val= 'enumeration' ) ';' -> ^( PROP_TYPE $val) | 'access' ':' (val= 'read-only' | val= 'initial-write' | val= 'read-write' ) ';' -> ^( PROP_ACCESS $val) | 'description' ':' STRING ';' -> ^( PROP_DESC STRING ) | 'gtype' ':' ID ';' -> ^( PROP_GTYPE ID ) | 'gtype' ':' GTYPENAME '(' typeName ')' ';' -> ^( PROP_GTYPE ^( GTYPENAME typeName ) ) | 'min' ':' STRING ';' -> ^( PROP_MIN STRING ) | 'max' ':' STRING ';' -> ^( PROP_MAX STRING ) | 'default' ':' STRING ';' -> ^( PROP_DEFAULT STRING ) | AUTO_CREATE ';' )
                alt34 = 9
                alt34 = self.dfa34.predict(self.input)
                if alt34 == 1:
                    # GOC.g:172:9: 'type' ':' (val= 'boolean' | val= 'integer' | val= 'float' | val= 'double' | val= 'string' | val= 'pointer' | val= 'object' | val= 'enumeration' ) ';'
                    pass 
                    string_literal168=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_propertyElement1415) 
                    stream_TYPE.add(string_literal168)
                    char_literal169=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1417) 
                    stream_62.add(char_literal169)
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
                        val=self.match(self.input, 73, self.FOLLOW_73_in_propertyElement1422) 
                        stream_73.add(val)


                    elif alt32 == 2:
                        # GOC.g:172:35: val= 'integer'
                        pass 
                        val=self.match(self.input, 74, self.FOLLOW_74_in_propertyElement1426) 
                        stream_74.add(val)


                    elif alt32 == 3:
                        # GOC.g:172:49: val= 'float'
                        pass 
                        val=self.match(self.input, 75, self.FOLLOW_75_in_propertyElement1430) 
                        stream_75.add(val)


                    elif alt32 == 4:
                        # GOC.g:172:61: val= 'double'
                        pass 
                        val=self.match(self.input, 76, self.FOLLOW_76_in_propertyElement1434) 
                        stream_76.add(val)


                    elif alt32 == 5:
                        # GOC.g:173:5: val= 'string'
                        pass 
                        val=self.match(self.input, 77, self.FOLLOW_77_in_propertyElement1443) 
                        stream_77.add(val)


                    elif alt32 == 6:
                        # GOC.g:173:18: val= 'pointer'
                        pass 
                        val=self.match(self.input, 78, self.FOLLOW_78_in_propertyElement1447) 
                        stream_78.add(val)


                    elif alt32 == 7:
                        # GOC.g:173:32: val= 'object'
                        pass 
                        val=self.match(self.input, 79, self.FOLLOW_79_in_propertyElement1451) 
                        stream_79.add(val)


                    elif alt32 == 8:
                        # GOC.g:173:45: val= 'enumeration'
                        pass 
                        val=self.match(self.input, 80, self.FOLLOW_80_in_propertyElement1455) 
                        stream_80.add(val)



                    char_literal170=self.match(self.input, 57, self.FOLLOW_57_in_propertyElement1458) 
                    stream_57.add(char_literal170)

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
                    string_literal171=self.match(self.input, 81, self.FOLLOW_81_in_propertyElement1482) 
                    stream_81.add(string_literal171)
                    char_literal172=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1484) 
                    stream_62.add(char_literal172)
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
                        val=self.match(self.input, 82, self.FOLLOW_82_in_propertyElement1489) 
                        stream_82.add(val)


                    elif alt33 == 2:
                        # GOC.g:175:39: val= 'initial-write'
                        pass 
                        val=self.match(self.input, 83, self.FOLLOW_83_in_propertyElement1493) 
                        stream_83.add(val)


                    elif alt33 == 3:
                        # GOC.g:175:59: val= 'read-write'
                        pass 
                        val=self.match(self.input, 84, self.FOLLOW_84_in_propertyElement1497) 
                        stream_84.add(val)



                    char_literal173=self.match(self.input, 57, self.FOLLOW_57_in_propertyElement1500) 
                    stream_57.add(char_literal173)

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
                    string_literal174=self.match(self.input, 85, self.FOLLOW_85_in_propertyElement1524) 
                    stream_85.add(string_literal174)
                    char_literal175=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1526) 
                    stream_62.add(char_literal175)
                    STRING176=self.match(self.input, STRING, self.FOLLOW_STRING_in_propertyElement1528) 
                    stream_STRING.add(STRING176)
                    char_literal177=self.match(self.input, 57, self.FOLLOW_57_in_propertyElement1530) 
                    stream_57.add(char_literal177)

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
                    string_literal178=self.match(self.input, GTYPE, self.FOLLOW_GTYPE_in_propertyElement1548) 
                    stream_GTYPE.add(string_literal178)
                    char_literal179=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1550) 
                    stream_62.add(char_literal179)
                    ID180=self.match(self.input, ID, self.FOLLOW_ID_in_propertyElement1552) 
                    stream_ID.add(ID180)
                    char_literal181=self.match(self.input, 57, self.FOLLOW_57_in_propertyElement1554) 
                    stream_57.add(char_literal181)

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
                    string_literal182=self.match(self.input, GTYPE, self.FOLLOW_GTYPE_in_propertyElement1577) 
                    stream_GTYPE.add(string_literal182)
                    char_literal183=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1579) 
                    stream_62.add(char_literal183)
                    GTYPENAME184=self.match(self.input, GTYPENAME, self.FOLLOW_GTYPENAME_in_propertyElement1581) 
                    stream_GTYPENAME.add(GTYPENAME184)
                    char_literal185=self.match(self.input, 86, self.FOLLOW_86_in_propertyElement1583) 
                    stream_86.add(char_literal185)
                    self._state.following.append(self.FOLLOW_typeName_in_propertyElement1585)
                    typeName186 = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(typeName186.tree)
                    char_literal187=self.match(self.input, 87, self.FOLLOW_87_in_propertyElement1587) 
                    stream_87.add(char_literal187)
                    char_literal188=self.match(self.input, 57, self.FOLLOW_57_in_propertyElement1589) 
                    stream_57.add(char_literal188)

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
                    string_literal189=self.match(self.input, 88, self.FOLLOW_88_in_propertyElement1616) 
                    stream_88.add(string_literal189)
                    char_literal190=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1618) 
                    stream_62.add(char_literal190)
                    STRING191=self.match(self.input, STRING, self.FOLLOW_STRING_in_propertyElement1620) 
                    stream_STRING.add(STRING191)
                    char_literal192=self.match(self.input, 57, self.FOLLOW_57_in_propertyElement1622) 
                    stream_57.add(char_literal192)

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
                    # GOC.g:183:9: 'max' ':' STRING ';'
                    pass 
                    string_literal193=self.match(self.input, 89, self.FOLLOW_89_in_propertyElement1640) 
                    stream_89.add(string_literal193)
                    char_literal194=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1642) 
                    stream_62.add(char_literal194)
                    STRING195=self.match(self.input, STRING, self.FOLLOW_STRING_in_propertyElement1644) 
                    stream_STRING.add(STRING195)
                    char_literal196=self.match(self.input, 57, self.FOLLOW_57_in_propertyElement1646) 
                    stream_57.add(char_literal196)

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
                    # 183:30: -> ^( PROP_MAX STRING )
                    # GOC.g:183:33: ^( PROP_MAX STRING )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_MAX, "PROP_MAX"), root_1)

                    self._adaptor.addChild(root_1, stream_STRING.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt34 == 8:
                    # GOC.g:184:9: 'default' ':' STRING ';'
                    pass 
                    string_literal197=self.match(self.input, 90, self.FOLLOW_90_in_propertyElement1664) 
                    stream_90.add(string_literal197)
                    char_literal198=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1666) 
                    stream_62.add(char_literal198)
                    STRING199=self.match(self.input, STRING, self.FOLLOW_STRING_in_propertyElement1668) 
                    stream_STRING.add(STRING199)
                    char_literal200=self.match(self.input, 57, self.FOLLOW_57_in_propertyElement1670) 
                    stream_57.add(char_literal200)

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
                    # 184:34: -> ^( PROP_DEFAULT STRING )
                    # GOC.g:184:37: ^( PROP_DEFAULT STRING )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_DEFAULT, "PROP_DEFAULT"), root_1)

                    self._adaptor.addChild(root_1, stream_STRING.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt34 == 9:
                    # GOC.g:185:9: AUTO_CREATE ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    AUTO_CREATE201=self.match(self.input, AUTO_CREATE, self.FOLLOW_AUTO_CREATE_in_propertyElement1688)

                    AUTO_CREATE201_tree = self._adaptor.createWithPayload(AUTO_CREATE201)
                    root_0 = self._adaptor.becomeRoot(AUTO_CREATE201_tree, root_0)

                    char_literal202=self.match(self.input, 57, self.FOLLOW_57_in_propertyElement1691)

                    char_literal202_tree = self._adaptor.createWithPayload(char_literal202)
                    self._adaptor.addChild(root_0, char_literal202_tree)



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
    # GOC.g:188:1: signalElement : ( RESULT '{' 'type' ':' typeArg ';' '}' -> ^( RESULT typeArg ) | PARAMETER ID '{' 'type' ':' typeArg ';' '}' -> ^( PARAMETER ID typeArg ) );
    def signalElement(self, ):

        retval = self.signalElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RESULT203 = None
        char_literal204 = None
        string_literal205 = None
        char_literal206 = None
        char_literal208 = None
        char_literal209 = None
        PARAMETER210 = None
        ID211 = None
        char_literal212 = None
        string_literal213 = None
        char_literal214 = None
        char_literal216 = None
        char_literal217 = None
        typeArg207 = None

        typeArg215 = None


        RESULT203_tree = None
        char_literal204_tree = None
        string_literal205_tree = None
        char_literal206_tree = None
        char_literal208_tree = None
        char_literal209_tree = None
        PARAMETER210_tree = None
        ID211_tree = None
        char_literal212_tree = None
        string_literal213_tree = None
        char_literal214_tree = None
        char_literal216_tree = None
        char_literal217_tree = None
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
                # GOC.g:189:5: ( RESULT '{' 'type' ':' typeArg ';' '}' -> ^( RESULT typeArg ) | PARAMETER ID '{' 'type' ':' typeArg ';' '}' -> ^( PARAMETER ID typeArg ) )
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
                    # GOC.g:189:9: RESULT '{' 'type' ':' typeArg ';' '}'
                    pass 
                    RESULT203=self.match(self.input, RESULT, self.FOLLOW_RESULT_in_signalElement1710) 
                    stream_RESULT.add(RESULT203)
                    char_literal204=self.match(self.input, 58, self.FOLLOW_58_in_signalElement1712) 
                    stream_58.add(char_literal204)
                    string_literal205=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_signalElement1714) 
                    stream_TYPE.add(string_literal205)
                    char_literal206=self.match(self.input, 62, self.FOLLOW_62_in_signalElement1716) 
                    stream_62.add(char_literal206)
                    self._state.following.append(self.FOLLOW_typeArg_in_signalElement1718)
                    typeArg207 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg207.tree)
                    char_literal208=self.match(self.input, 57, self.FOLLOW_57_in_signalElement1720) 
                    stream_57.add(char_literal208)
                    char_literal209=self.match(self.input, 59, self.FOLLOW_59_in_signalElement1722) 
                    stream_59.add(char_literal209)

                    # AST Rewrite
                    # elements: RESULT, typeArg
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
                    # 189:47: -> ^( RESULT typeArg )
                    # GOC.g:189:50: ^( RESULT typeArg )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_RESULT.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_typeArg.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt35 == 2:
                    # GOC.g:190:9: PARAMETER ID '{' 'type' ':' typeArg ';' '}'
                    pass 
                    PARAMETER210=self.match(self.input, PARAMETER, self.FOLLOW_PARAMETER_in_signalElement1740) 
                    stream_PARAMETER.add(PARAMETER210)
                    ID211=self.match(self.input, ID, self.FOLLOW_ID_in_signalElement1742) 
                    stream_ID.add(ID211)
                    char_literal212=self.match(self.input, 58, self.FOLLOW_58_in_signalElement1744) 
                    stream_58.add(char_literal212)
                    string_literal213=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_signalElement1746) 
                    stream_TYPE.add(string_literal213)
                    char_literal214=self.match(self.input, 62, self.FOLLOW_62_in_signalElement1748) 
                    stream_62.add(char_literal214)
                    self._state.following.append(self.FOLLOW_typeArg_in_signalElement1750)
                    typeArg215 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg215.tree)
                    char_literal216=self.match(self.input, 57, self.FOLLOW_57_in_signalElement1752) 
                    stream_57.add(char_literal216)
                    char_literal217=self.match(self.input, 59, self.FOLLOW_59_in_signalElement1754) 
                    stream_59.add(char_literal217)

                    # AST Rewrite
                    # elements: ID, PARAMETER, typeArg
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
                    # 190:53: -> ^( PARAMETER ID typeArg )
                    # GOC.g:190:56: ^( PARAMETER ID typeArg )
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
    # GOC.g:193:1: attributeElement : ( SCOPE ':' (val= 'static' | val= 'instance' ) ';' -> ^( SCOPE $val) | VISIBILITY ':' (val= 'public' | val= 'protected' | val= 'private' ) ';' -> ^( VISIBILITY $val) );
    def attributeElement(self, ):

        retval = self.attributeElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        val = None
        SCOPE218 = None
        char_literal219 = None
        char_literal220 = None
        VISIBILITY221 = None
        char_literal222 = None
        char_literal223 = None

        val_tree = None
        SCOPE218_tree = None
        char_literal219_tree = None
        char_literal220_tree = None
        VISIBILITY221_tree = None
        char_literal222_tree = None
        char_literal223_tree = None
        stream_67 = RewriteRuleTokenStream(self._adaptor, "token 67")
        stream_66 = RewriteRuleTokenStream(self._adaptor, "token 66")
        stream_VISIBILITY = RewriteRuleTokenStream(self._adaptor, "token VISIBILITY")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_SCOPE = RewriteRuleTokenStream(self._adaptor, "token SCOPE")
        stream_64 = RewriteRuleTokenStream(self._adaptor, "token 64")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_63 = RewriteRuleTokenStream(self._adaptor, "token 63")

        try:
            try:
                # GOC.g:194:2: ( SCOPE ':' (val= 'static' | val= 'instance' ) ';' -> ^( SCOPE $val) | VISIBILITY ':' (val= 'public' | val= 'protected' | val= 'private' ) ';' -> ^( VISIBILITY $val) )
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
                    # GOC.g:194:4: SCOPE ':' (val= 'static' | val= 'instance' ) ';'
                    pass 
                    SCOPE218=self.match(self.input, SCOPE, self.FOLLOW_SCOPE_in_attributeElement1778) 
                    stream_SCOPE.add(SCOPE218)
                    char_literal219=self.match(self.input, 62, self.FOLLOW_62_in_attributeElement1780) 
                    stream_62.add(char_literal219)
                    # GOC.g:194:14: (val= 'static' | val= 'instance' )
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
                        # GOC.g:194:15: val= 'static'
                        pass 
                        val=self.match(self.input, 67, self.FOLLOW_67_in_attributeElement1785) 
                        stream_67.add(val)


                    elif alt36 == 2:
                        # GOC.g:194:28: val= 'instance'
                        pass 
                        val=self.match(self.input, 66, self.FOLLOW_66_in_attributeElement1789) 
                        stream_66.add(val)



                    char_literal220=self.match(self.input, 57, self.FOLLOW_57_in_attributeElement1792) 
                    stream_57.add(char_literal220)

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
                    # 194:48: -> ^( SCOPE $val)
                    # GOC.g:194:51: ^( SCOPE $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_SCOPE.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt38 == 2:
                    # GOC.g:195:4: VISIBILITY ':' (val= 'public' | val= 'protected' | val= 'private' ) ';'
                    pass 
                    VISIBILITY221=self.match(self.input, VISIBILITY, self.FOLLOW_VISIBILITY_in_attributeElement1806) 
                    stream_VISIBILITY.add(VISIBILITY221)
                    char_literal222=self.match(self.input, 62, self.FOLLOW_62_in_attributeElement1808) 
                    stream_62.add(char_literal222)
                    # GOC.g:195:19: (val= 'public' | val= 'protected' | val= 'private' )
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
                        # GOC.g:195:20: val= 'public'
                        pass 
                        val=self.match(self.input, 63, self.FOLLOW_63_in_attributeElement1813) 
                        stream_63.add(val)


                    elif alt37 == 2:
                        # GOC.g:195:33: val= 'protected'
                        pass 
                        val=self.match(self.input, 64, self.FOLLOW_64_in_attributeElement1817) 
                        stream_64.add(val)


                    elif alt37 == 3:
                        # GOC.g:195:49: val= 'private'
                        pass 
                        val=self.match(self.input, 65, self.FOLLOW_65_in_attributeElement1821) 
                        stream_65.add(val)



                    char_literal223=self.match(self.input, 57, self.FOLLOW_57_in_attributeElement1824) 
                    stream_57.add(char_literal223)

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
                    # 195:68: -> ^( VISIBILITY $val)
                    # GOC.g:195:71: ^( VISIBILITY $val)
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
    # GOC.g:198:1: typeName : ( typePath -> ^( TYPE_NAME typePath ) | ( 'unsigned ' )? 'integer' -> ^( TYPE_NAME ( 'unsigned ' )? 'integer' ) | ( 'unsigned ' )? 'long' -> ^( TYPE_NAME ( 'unsigned ' )? 'long' ) | (val= 'null' | val= 'boolean' | val= 'string' | val= 'float' | val= 'double' | val= 'pointer' ) -> ^( TYPE_NAME $val) );
    def typeName(self, ):

        retval = self.typeName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        val = None
        string_literal225 = None
        string_literal226 = None
        string_literal227 = None
        string_literal228 = None
        typePath224 = None


        val_tree = None
        string_literal225_tree = None
        string_literal226_tree = None
        string_literal227_tree = None
        string_literal228_tree = None
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
                # GOC.g:199:2: ( typePath -> ^( TYPE_NAME typePath ) | ( 'unsigned ' )? 'integer' -> ^( TYPE_NAME ( 'unsigned ' )? 'integer' ) | ( 'unsigned ' )? 'long' -> ^( TYPE_NAME ( 'unsigned ' )? 'long' ) | (val= 'null' | val= 'boolean' | val= 'string' | val= 'float' | val= 'double' | val= 'pointer' ) -> ^( TYPE_NAME $val) )
                alt42 = 4
                LA42 = self.input.LA(1)
                if LA42 == ID or LA42 == 96:
                    alt42 = 1
                elif LA42 == 91:
                    LA42_2 = self.input.LA(2)

                    if (LA42_2 == 92) :
                        alt42 = 3
                    elif (LA42_2 == 74) :
                        alt42 = 2
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
                    # GOC.g:199:6: typePath
                    pass 
                    self._state.following.append(self.FOLLOW_typePath_in_typeName1846)
                    typePath224 = self.typePath()

                    self._state.following.pop()
                    stream_typePath.add(typePath224.tree)

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
                    # 199:15: -> ^( TYPE_NAME typePath )
                    # GOC.g:199:18: ^( TYPE_NAME typePath )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE_NAME, "TYPE_NAME"), root_1)

                    self._adaptor.addChild(root_1, stream_typePath.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt42 == 2:
                    # GOC.g:200:6: ( 'unsigned ' )? 'integer'
                    pass 
                    # GOC.g:200:6: ( 'unsigned ' )?
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 == 91) :
                        alt39 = 1
                    if alt39 == 1:
                        # GOC.g:200:6: 'unsigned '
                        pass 
                        string_literal225=self.match(self.input, 91, self.FOLLOW_91_in_typeName1861) 
                        stream_91.add(string_literal225)



                    string_literal226=self.match(self.input, 74, self.FOLLOW_74_in_typeName1864) 
                    stream_74.add(string_literal226)

                    # AST Rewrite
                    # elements: 74, 91
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
                    # 200:29: -> ^( TYPE_NAME ( 'unsigned ' )? 'integer' )
                    # GOC.g:200:32: ^( TYPE_NAME ( 'unsigned ' )? 'integer' )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE_NAME, "TYPE_NAME"), root_1)

                    # GOC.g:200:44: ( 'unsigned ' )?
                    if stream_91.hasNext():
                        self._adaptor.addChild(root_1, stream_91.nextNode())


                    stream_91.reset();
                    self._adaptor.addChild(root_1, stream_74.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt42 == 3:
                    # GOC.g:201:6: ( 'unsigned ' )? 'long'
                    pass 
                    # GOC.g:201:6: ( 'unsigned ' )?
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == 91) :
                        alt40 = 1
                    if alt40 == 1:
                        # GOC.g:201:6: 'unsigned '
                        pass 
                        string_literal227=self.match(self.input, 91, self.FOLLOW_91_in_typeName1882) 
                        stream_91.add(string_literal227)



                    string_literal228=self.match(self.input, 92, self.FOLLOW_92_in_typeName1885) 
                    stream_92.add(string_literal228)

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
                    # 201:26: -> ^( TYPE_NAME ( 'unsigned ' )? 'long' )
                    # GOC.g:201:29: ^( TYPE_NAME ( 'unsigned ' )? 'long' )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE_NAME, "TYPE_NAME"), root_1)

                    # GOC.g:201:41: ( 'unsigned ' )?
                    if stream_91.hasNext():
                        self._adaptor.addChild(root_1, stream_91.nextNode())


                    stream_91.reset();
                    self._adaptor.addChild(root_1, stream_92.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt42 == 4:
                    # GOC.g:202:4: (val= 'null' | val= 'boolean' | val= 'string' | val= 'float' | val= 'double' | val= 'pointer' )
                    pass 
                    # GOC.g:202:4: (val= 'null' | val= 'boolean' | val= 'string' | val= 'float' | val= 'double' | val= 'pointer' )
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
                        # GOC.g:202:5: val= 'null'
                        pass 
                        val=self.match(self.input, 93, self.FOLLOW_93_in_typeName1904) 
                        stream_93.add(val)


                    elif alt41 == 2:
                        # GOC.g:203:6: val= 'boolean'
                        pass 
                        val=self.match(self.input, 73, self.FOLLOW_73_in_typeName1913) 
                        stream_73.add(val)


                    elif alt41 == 3:
                        # GOC.g:204:4: val= 'string'
                        pass 
                        val=self.match(self.input, 77, self.FOLLOW_77_in_typeName1920) 
                        stream_77.add(val)


                    elif alt41 == 4:
                        # GOC.g:205:4: val= 'float'
                        pass 
                        val=self.match(self.input, 75, self.FOLLOW_75_in_typeName1927) 
                        stream_75.add(val)


                    elif alt41 == 5:
                        # GOC.g:206:4: val= 'double'
                        pass 
                        val=self.match(self.input, 76, self.FOLLOW_76_in_typeName1934) 
                        stream_76.add(val)


                    elif alt41 == 6:
                        # GOC.g:207:6: val= 'pointer'
                        pass 
                        val=self.match(self.input, 78, self.FOLLOW_78_in_typeName1943) 
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
                    # 207:21: -> ^( TYPE_NAME $val)
                    # GOC.g:207:24: ^( TYPE_NAME $val)
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
    # GOC.g:210:1: typeArg : ( typeName | 'ref' '(' typeArg ')' -> ^( REF_TO typeArg ) | 'list' '(' typeArg ')' -> ^( LIST_OF typeArg ) );
    def typeArg(self, ):

        retval = self.typeArg_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal230 = None
        char_literal231 = None
        char_literal233 = None
        string_literal234 = None
        char_literal235 = None
        char_literal237 = None
        typeName229 = None

        typeArg232 = None

        typeArg236 = None


        string_literal230_tree = None
        char_literal231_tree = None
        char_literal233_tree = None
        string_literal234_tree = None
        char_literal235_tree = None
        char_literal237_tree = None
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_94 = RewriteRuleTokenStream(self._adaptor, "token 94")
        stream_86 = RewriteRuleTokenStream(self._adaptor, "token 86")
        stream_87 = RewriteRuleTokenStream(self._adaptor, "token 87")
        stream_typeArg = RewriteRuleSubtreeStream(self._adaptor, "rule typeArg")
        try:
            try:
                # GOC.g:211:5: ( typeName | 'ref' '(' typeArg ')' -> ^( REF_TO typeArg ) | 'list' '(' typeArg ')' -> ^( LIST_OF typeArg ) )
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
                    # GOC.g:211:9: typeName
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_typeName_in_typeArg1969)
                    typeName229 = self.typeName()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, typeName229.tree)


                elif alt43 == 2:
                    # GOC.g:212:9: 'ref' '(' typeArg ')'
                    pass 
                    string_literal230=self.match(self.input, 94, self.FOLLOW_94_in_typeArg1979) 
                    stream_94.add(string_literal230)
                    char_literal231=self.match(self.input, 86, self.FOLLOW_86_in_typeArg1981) 
                    stream_86.add(char_literal231)
                    self._state.following.append(self.FOLLOW_typeArg_in_typeArg1983)
                    typeArg232 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg232.tree)
                    char_literal233=self.match(self.input, 87, self.FOLLOW_87_in_typeArg1985) 
                    stream_87.add(char_literal233)

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
                    # 212:31: -> ^( REF_TO typeArg )
                    # GOC.g:212:34: ^( REF_TO typeArg )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(REF_TO, "REF_TO"), root_1)

                    self._adaptor.addChild(root_1, stream_typeArg.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt43 == 3:
                    # GOC.g:213:9: 'list' '(' typeArg ')'
                    pass 
                    string_literal234=self.match(self.input, 95, self.FOLLOW_95_in_typeArg2003) 
                    stream_95.add(string_literal234)
                    char_literal235=self.match(self.input, 86, self.FOLLOW_86_in_typeArg2005) 
                    stream_86.add(char_literal235)
                    self._state.following.append(self.FOLLOW_typeArg_in_typeArg2007)
                    typeArg236 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg236.tree)
                    char_literal237=self.match(self.input, 87, self.FOLLOW_87_in_typeArg2009) 
                    stream_87.add(char_literal237)

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
                    # 213:32: -> ^( LIST_OF typeArg )
                    # GOC.g:213:35: ^( LIST_OF typeArg )
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
    # GOC.g:216:1: typePath : ( '::' ID '::' )? ( ID '::' )* ID ;
    def typePath(self, ):

        retval = self.typePath_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal238 = None
        ID239 = None
        string_literal240 = None
        ID241 = None
        string_literal242 = None
        ID243 = None

        string_literal238_tree = None
        ID239_tree = None
        string_literal240_tree = None
        ID241_tree = None
        string_literal242_tree = None
        ID243_tree = None

        try:
            try:
                # GOC.g:217:5: ( ( '::' ID '::' )? ( ID '::' )* ID )
                # GOC.g:217:9: ( '::' ID '::' )? ( ID '::' )* ID
                pass 
                root_0 = self._adaptor.nil()

                # GOC.g:217:9: ( '::' ID '::' )?
                alt44 = 2
                LA44_0 = self.input.LA(1)

                if (LA44_0 == 96) :
                    alt44 = 1
                if alt44 == 1:
                    # GOC.g:217:10: '::' ID '::'
                    pass 
                    string_literal238=self.match(self.input, 96, self.FOLLOW_96_in_typePath2037)

                    string_literal238_tree = self._adaptor.createWithPayload(string_literal238)
                    self._adaptor.addChild(root_0, string_literal238_tree)

                    ID239=self.match(self.input, ID, self.FOLLOW_ID_in_typePath2039)

                    ID239_tree = self._adaptor.createWithPayload(ID239)
                    self._adaptor.addChild(root_0, ID239_tree)

                    string_literal240=self.match(self.input, 96, self.FOLLOW_96_in_typePath2041)

                    string_literal240_tree = self._adaptor.createWithPayload(string_literal240)
                    self._adaptor.addChild(root_0, string_literal240_tree)




                # GOC.g:217:24: ( ID '::' )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == ID) :
                        LA45_1 = self.input.LA(2)

                        if (LA45_1 == 96) :
                            alt45 = 1




                    if alt45 == 1:
                        # GOC.g:217:25: ID '::'
                        pass 
                        ID241=self.match(self.input, ID, self.FOLLOW_ID_in_typePath2045)

                        ID241_tree = self._adaptor.createWithPayload(ID241)
                        self._adaptor.addChild(root_0, ID241_tree)

                        string_literal242=self.match(self.input, 96, self.FOLLOW_96_in_typePath2047)

                        string_literal242_tree = self._adaptor.createWithPayload(string_literal242)
                        self._adaptor.addChild(root_0, string_literal242_tree)



                    else:
                        break #loop45
                ID243=self.match(self.input, ID, self.FOLLOW_ID_in_typePath2051)

                ID243_tree = self._adaptor.createWithPayload(ID243)
                self._adaptor.addChild(root_0, ID243_tree)




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
    # GOC.g:346:1: signalID : part1= ID ( '-' part2+= ID )* -> ^( SIGNAL_ID $part1 ( $part2)* ) ;
    def signalID(self, ):

        retval = self.signalID_return()
        retval.start = self.input.LT(1)

        root_0 = None

        part1 = None
        char_literal244 = None
        part2 = None
        list_part2 = None

        part1_tree = None
        char_literal244_tree = None
        part2_tree = None
        stream_97 = RewriteRuleTokenStream(self._adaptor, "token 97")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # GOC.g:347:5: (part1= ID ( '-' part2+= ID )* -> ^( SIGNAL_ID $part1 ( $part2)* ) )
                # GOC.g:347:9: part1= ID ( '-' part2+= ID )*
                pass 
                part1=self.match(self.input, ID, self.FOLLOW_ID_in_signalID2654) 
                stream_ID.add(part1)
                # GOC.g:347:18: ( '-' part2+= ID )*
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == 97) :
                        alt46 = 1


                    if alt46 == 1:
                        # GOC.g:347:19: '-' part2+= ID
                        pass 
                        char_literal244=self.match(self.input, 97, self.FOLLOW_97_in_signalID2657) 
                        stream_97.add(char_literal244)
                        part2=self.match(self.input, ID, self.FOLLOW_ID_in_signalID2661) 
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
                # 347:35: -> ^( SIGNAL_ID $part1 ( $part2)* )
                # GOC.g:347:38: ^( SIGNAL_ID $part1 ( $part2)* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(SIGNAL_ID, "SIGNAL_ID"), root_1)

                self._adaptor.addChild(root_1, stream_part1.nextNode())
                # GOC.g:347:57: ( $part2)*
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
        u"\14\uffff"
        )

    DFA34_eof = DFA.unpack(
        u"\14\uffff"
        )

    DFA34_min = DFA.unpack(
        u"\1\33\3\uffff\1\76\4\uffff\1\24\2\uffff"
        )

    DFA34_max = DFA.unpack(
        u"\1\132\3\uffff\1\76\4\uffff\1\56\2\uffff"
        )

    DFA34_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\uffff\1\6\1\7\1\10\1\11\1\uffff\1\4\1\5"
        )

    DFA34_special = DFA.unpack(
        u"\14\uffff"
        )

            
    DFA34_transition = [
        DFA.unpack(u"\1\4\10\uffff\1\1\12\uffff\1\10\41\uffff\1\2\3\uffff"
        u"\1\3\2\uffff\1\5\1\6\1\7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12\31\uffff\1\13"),
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
    FOLLOW_STRING_in_includeStmt230 = frozenset([57])
    FOLLOW_57_in_includeStmt232 = frozenset([1])
    FOLLOW_PACKAGE_in_packageDef255 = frozenset([20])
    FOLLOW_ID_in_packageDef257 = frozenset([58])
    FOLLOW_58_in_packageDef259 = frozenset([21, 22, 23, 24, 26, 27, 51, 59])
    FOLLOW_packageElement_in_packageDef261 = frozenset([21, 22, 23, 24, 26, 27, 51, 59])
    FOLLOW_59_in_packageDef264 = frozenset([1])
    FOLLOW_packageDef_in_packageElement289 = frozenset([1])
    FOLLOW_classDef_in_packageElement294 = frozenset([1])
    FOLLOW_intfDef_in_packageElement299 = frozenset([1])
    FOLLOW_errorDomainDef_in_packageElement306 = frozenset([1])
    FOLLOW_enumDef_in_packageElement313 = frozenset([1])
    FOLLOW_flagsDef_in_packageElement320 = frozenset([1])
    FOLLOW_typeDecl_in_packageElement327 = frozenset([1])
    FOLLOW_GOBJECT_in_classDef338 = frozenset([20])
    FOLLOW_ID_in_classDef342 = frozenset([57, 58])
    FOLLOW_58_in_classDef345 = frozenset([28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 59])
    FOLLOW_classMember_in_classDef347 = frozenset([28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 59])
    FOLLOW_59_in_classDef350 = frozenset([1])
    FOLLOW_57_in_classDef352 = frozenset([1])
    FOLLOW_GINTERFACE_in_intfDef379 = frozenset([20])
    FOLLOW_ID_in_intfDef383 = frozenset([57, 58])
    FOLLOW_58_in_intfDef386 = frozenset([30, 33, 38, 59])
    FOLLOW_intfMember_in_intfDef388 = frozenset([30, 33, 38, 59])
    FOLLOW_59_in_intfDef391 = frozenset([1])
    FOLLOW_57_in_intfDef393 = frozenset([1])
    FOLLOW_ERROR_DOMAIN_in_errorDomainDef424 = frozenset([20])
    FOLLOW_ID_in_errorDomainDef426 = frozenset([58])
    FOLLOW_58_in_errorDomainDef428 = frozenset([60])
    FOLLOW_errorDomainElement_in_errorDomainDef430 = frozenset([59, 60])
    FOLLOW_59_in_errorDomainDef433 = frozenset([1])
    FOLLOW_60_in_errorDomainElement468 = frozenset([20])
    FOLLOW_ID_in_errorDomainElement470 = frozenset([57])
    FOLLOW_57_in_errorDomainElement472 = frozenset([1])
    FOLLOW_ENUMERATION_in_enumDef497 = frozenset([20])
    FOLLOW_ID_in_enumDef499 = frozenset([58])
    FOLLOW_58_in_enumDef501 = frozenset([60])
    FOLLOW_enumElement_in_enumDef503 = frozenset([59, 60])
    FOLLOW_59_in_enumDef506 = frozenset([1])
    FOLLOW_60_in_enumElement541 = frozenset([20])
    FOLLOW_ID_in_enumElement543 = frozenset([57, 58])
    FOLLOW_57_in_enumElement546 = frozenset([1])
    FOLLOW_58_in_enumElement548 = frozenset([61])
    FOLLOW_61_in_enumElement550 = frozenset([62])
    FOLLOW_62_in_enumElement552 = frozenset([25])
    FOLLOW_INT_in_enumElement554 = frozenset([57])
    FOLLOW_57_in_enumElement556 = frozenset([59])
    FOLLOW_59_in_enumElement558 = frozenset([1])
    FOLLOW_FLAGS_in_flagsDef594 = frozenset([20])
    FOLLOW_ID_in_flagsDef596 = frozenset([58])
    FOLLOW_58_in_flagsDef598 = frozenset([60])
    FOLLOW_flagsElement_in_flagsDef600 = frozenset([59, 60])
    FOLLOW_59_in_flagsDef603 = frozenset([1])
    FOLLOW_60_in_flagsElement638 = frozenset([20])
    FOLLOW_ID_in_flagsElement640 = frozenset([57])
    FOLLOW_57_in_flagsElement642 = frozenset([1])
    FOLLOW_GTYPE_in_typeDecl667 = frozenset([20])
    FOLLOW_ID_in_typeDecl669 = frozenset([57])
    FOLLOW_57_in_typeDecl671 = frozenset([1])
    FOLLOW_SUPER_in_classMember702 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 96])
    FOLLOW_typeName_in_classMember704 = frozenset([57])
    FOLLOW_57_in_classMember706 = frozenset([1])
    FOLLOW_ABSTRACT_in_classMember722 = frozenset([57])
    FOLLOW_57_in_classMember725 = frozenset([1])
    FOLLOW_PREFIX_in_classMember732 = frozenset([20])
    FOLLOW_ID_in_classMember734 = frozenset([57])
    FOLLOW_57_in_classMember736 = frozenset([1])
    FOLLOW_IMPLEMENTS_in_classMember749 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 96])
    FOLLOW_typeName_in_classMember751 = frozenset([57])
    FOLLOW_57_in_classMember753 = frozenset([1])
    FOLLOW_CONSTRUCTOR_in_classMember773 = frozenset([58])
    FOLLOW_58_in_classMember775 = frozenset([43, 44, 59])
    FOLLOW_constructorElement_in_classMember777 = frozenset([43, 44, 59])
    FOLLOW_59_in_classMember780 = frozenset([1])
    FOLLOW_METHOD_in_classMember808 = frozenset([20])
    FOLLOW_ID_in_classMember810 = frozenset([58])
    FOLLOW_58_in_classMember812 = frozenset([39, 40, 41, 42, 43, 44, 59])
    FOLLOW_methodElement_in_classMember814 = frozenset([39, 40, 41, 42, 43, 44, 59])
    FOLLOW_59_in_classMember817 = frozenset([1])
    FOLLOW_OVERRIDE_in_classMember834 = frozenset([20])
    FOLLOW_ID_in_classMember836 = frozenset([57])
    FOLLOW_57_in_classMember838 = frozenset([1])
    FOLLOW_ATTRIBUTE_in_classMember851 = frozenset([20])
    FOLLOW_ID_in_classMember853 = frozenset([58])
    FOLLOW_58_in_classMember855 = frozenset([36])
    FOLLOW_TYPE_in_classMember857 = frozenset([62])
    FOLLOW_62_in_classMember859 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 94, 95, 96])
    FOLLOW_typeArg_in_classMember861 = frozenset([57])
    FOLLOW_57_in_classMember863 = frozenset([40, 41, 59])
    FOLLOW_attributeElement_in_classMember865 = frozenset([40, 41, 59])
    FOLLOW_59_in_classMember868 = frozenset([1])
    FOLLOW_PROPERTY_in_classMember887 = frozenset([20])
    FOLLOW_ID_in_classMember889 = frozenset([58])
    FOLLOW_58_in_classMember891 = frozenset([27, 36, 47, 81, 85, 88, 89, 90])
    FOLLOW_propertyElement_in_classMember893 = frozenset([27, 36, 47, 59, 81, 85, 88, 89, 90])
    FOLLOW_59_in_classMember896 = frozenset([1])
    FOLLOW_SIGNAL_in_classMember912 = frozenset([20])
    FOLLOW_signalID_in_classMember914 = frozenset([58])
    FOLLOW_58_in_classMember916 = frozenset([39, 43, 59])
    FOLLOW_signalElement_in_classMember918 = frozenset([39, 43, 59])
    FOLLOW_59_in_classMember921 = frozenset([1])
    FOLLOW_PREFIX_in_intfMember944 = frozenset([20])
    FOLLOW_ID_in_intfMember946 = frozenset([57])
    FOLLOW_57_in_intfMember948 = frozenset([1])
    FOLLOW_METHOD_in_intfMember963 = frozenset([20])
    FOLLOW_ID_in_intfMember965 = frozenset([58])
    FOLLOW_58_in_intfMember967 = frozenset([39, 40, 41, 42, 43, 44, 59])
    FOLLOW_methodElement_in_intfMember969 = frozenset([39, 40, 41, 42, 43, 44, 59])
    FOLLOW_59_in_intfMember972 = frozenset([1])
    FOLLOW_SIGNAL_in_intfMember993 = frozenset([20])
    FOLLOW_signalID_in_intfMember995 = frozenset([58])
    FOLLOW_58_in_intfMember997 = frozenset([39, 43, 59])
    FOLLOW_signalElement_in_intfMember999 = frozenset([39, 43, 59])
    FOLLOW_59_in_intfMember1002 = frozenset([1])
    FOLLOW_RESULT_in_resultDef1025 = frozenset([58])
    FOLLOW_58_in_resultDef1027 = frozenset([36])
    FOLLOW_TYPE_in_resultDef1029 = frozenset([62])
    FOLLOW_62_in_resultDef1031 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 94, 95, 96])
    FOLLOW_typeArg_in_resultDef1033 = frozenset([57])
    FOLLOW_57_in_resultDef1035 = frozenset([45, 59])
    FOLLOW_modifiers_in_resultDef1037 = frozenset([59])
    FOLLOW_59_in_resultDef1040 = frozenset([1])
    FOLLOW_constructorElement_in_methodElement1063 = frozenset([1])
    FOLLOW_resultDef_in_methodElement1068 = frozenset([1])
    FOLLOW_VISIBILITY_in_methodElement1073 = frozenset([62])
    FOLLOW_62_in_methodElement1075 = frozenset([63, 64, 65])
    FOLLOW_63_in_methodElement1080 = frozenset([57])
    FOLLOW_64_in_methodElement1084 = frozenset([57])
    FOLLOW_65_in_methodElement1088 = frozenset([57])
    FOLLOW_57_in_methodElement1091 = frozenset([1])
    FOLLOW_SCOPE_in_methodElement1106 = frozenset([62])
    FOLLOW_62_in_methodElement1108 = frozenset([66, 67])
    FOLLOW_66_in_methodElement1113 = frozenset([57])
    FOLLOW_67_in_methodElement1117 = frozenset([57])
    FOLLOW_57_in_methodElement1120 = frozenset([1])
    FOLLOW_INHERITANCE_in_methodElement1136 = frozenset([62])
    FOLLOW_62_in_methodElement1138 = frozenset([29, 68, 69])
    FOLLOW_68_in_methodElement1143 = frozenset([57])
    FOLLOW_69_in_methodElement1147 = frozenset([57])
    FOLLOW_ABSTRACT_in_methodElement1151 = frozenset([57])
    FOLLOW_57_in_methodElement1154 = frozenset([1])
    FOLLOW_PARAMETER_in_constructorElement1176 = frozenset([20])
    FOLLOW_ID_in_constructorElement1178 = frozenset([58])
    FOLLOW_58_in_constructorElement1180 = frozenset([36])
    FOLLOW_TYPE_in_constructorElement1182 = frozenset([62])
    FOLLOW_62_in_constructorElement1184 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 94, 95, 96])
    FOLLOW_typeArg_in_constructorElement1186 = frozenset([57])
    FOLLOW_57_in_constructorElement1188 = frozenset([45, 59, 70])
    FOLLOW_parameterElement_in_constructorElement1190 = frozenset([59])
    FOLLOW_59_in_constructorElement1193 = frozenset([1])
    FOLLOW_INIT_PROPERTIES_in_constructorElement1218 = frozenset([58])
    FOLLOW_58_in_constructorElement1220 = frozenset([20])
    FOLLOW_init_prop_in_constructorElement1222 = frozenset([20, 59])
    FOLLOW_59_in_constructorElement1225 = frozenset([1])
    FOLLOW_modifiers_in_parameterElement1252 = frozenset([1])
    FOLLOW_70_in_parameterElement1265 = frozenset([62])
    FOLLOW_62_in_parameterElement1267 = frozenset([20])
    FOLLOW_ID_in_parameterElement1269 = frozenset([57])
    FOLLOW_57_in_parameterElement1271 = frozenset([1])
    FOLLOW_ID_in_init_prop1300 = frozenset([62])
    FOLLOW_62_in_init_prop1302 = frozenset([19])
    FOLLOW_STRING_in_init_prop1306 = frozenset([57])
    FOLLOW_57_in_init_prop1308 = frozenset([1])
    FOLLOW_ID_in_init_prop1337 = frozenset([62])
    FOLLOW_62_in_init_prop1339 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 96])
    FOLLOW_typeName_in_init_prop1343 = frozenset([71])
    FOLLOW_71_in_init_prop1345 = frozenset([20])
    FOLLOW_ID_in_init_prop1349 = frozenset([57])
    FOLLOW_57_in_init_prop1351 = frozenset([1])
    FOLLOW_MODIFIERS_in_modifiers1385 = frozenset([62])
    FOLLOW_62_in_modifiers1387 = frozenset([72])
    FOLLOW_72_in_modifiers1389 = frozenset([57])
    FOLLOW_57_in_modifiers1391 = frozenset([1])
    FOLLOW_TYPE_in_propertyElement1415 = frozenset([62])
    FOLLOW_62_in_propertyElement1417 = frozenset([73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_73_in_propertyElement1422 = frozenset([57])
    FOLLOW_74_in_propertyElement1426 = frozenset([57])
    FOLLOW_75_in_propertyElement1430 = frozenset([57])
    FOLLOW_76_in_propertyElement1434 = frozenset([57])
    FOLLOW_77_in_propertyElement1443 = frozenset([57])
    FOLLOW_78_in_propertyElement1447 = frozenset([57])
    FOLLOW_79_in_propertyElement1451 = frozenset([57])
    FOLLOW_80_in_propertyElement1455 = frozenset([57])
    FOLLOW_57_in_propertyElement1458 = frozenset([1])
    FOLLOW_81_in_propertyElement1482 = frozenset([62])
    FOLLOW_62_in_propertyElement1484 = frozenset([82, 83, 84])
    FOLLOW_82_in_propertyElement1489 = frozenset([57])
    FOLLOW_83_in_propertyElement1493 = frozenset([57])
    FOLLOW_84_in_propertyElement1497 = frozenset([57])
    FOLLOW_57_in_propertyElement1500 = frozenset([1])
    FOLLOW_85_in_propertyElement1524 = frozenset([62])
    FOLLOW_62_in_propertyElement1526 = frozenset([19])
    FOLLOW_STRING_in_propertyElement1528 = frozenset([57])
    FOLLOW_57_in_propertyElement1530 = frozenset([1])
    FOLLOW_GTYPE_in_propertyElement1548 = frozenset([62])
    FOLLOW_62_in_propertyElement1550 = frozenset([20])
    FOLLOW_ID_in_propertyElement1552 = frozenset([57])
    FOLLOW_57_in_propertyElement1554 = frozenset([1])
    FOLLOW_GTYPE_in_propertyElement1577 = frozenset([62])
    FOLLOW_62_in_propertyElement1579 = frozenset([46])
    FOLLOW_GTYPENAME_in_propertyElement1581 = frozenset([86])
    FOLLOW_86_in_propertyElement1583 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 96])
    FOLLOW_typeName_in_propertyElement1585 = frozenset([87])
    FOLLOW_87_in_propertyElement1587 = frozenset([57])
    FOLLOW_57_in_propertyElement1589 = frozenset([1])
    FOLLOW_88_in_propertyElement1616 = frozenset([62])
    FOLLOW_62_in_propertyElement1618 = frozenset([19])
    FOLLOW_STRING_in_propertyElement1620 = frozenset([57])
    FOLLOW_57_in_propertyElement1622 = frozenset([1])
    FOLLOW_89_in_propertyElement1640 = frozenset([62])
    FOLLOW_62_in_propertyElement1642 = frozenset([19])
    FOLLOW_STRING_in_propertyElement1644 = frozenset([57])
    FOLLOW_57_in_propertyElement1646 = frozenset([1])
    FOLLOW_90_in_propertyElement1664 = frozenset([62])
    FOLLOW_62_in_propertyElement1666 = frozenset([19])
    FOLLOW_STRING_in_propertyElement1668 = frozenset([57])
    FOLLOW_57_in_propertyElement1670 = frozenset([1])
    FOLLOW_AUTO_CREATE_in_propertyElement1688 = frozenset([57])
    FOLLOW_57_in_propertyElement1691 = frozenset([1])
    FOLLOW_RESULT_in_signalElement1710 = frozenset([58])
    FOLLOW_58_in_signalElement1712 = frozenset([36])
    FOLLOW_TYPE_in_signalElement1714 = frozenset([62])
    FOLLOW_62_in_signalElement1716 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 94, 95, 96])
    FOLLOW_typeArg_in_signalElement1718 = frozenset([57])
    FOLLOW_57_in_signalElement1720 = frozenset([59])
    FOLLOW_59_in_signalElement1722 = frozenset([1])
    FOLLOW_PARAMETER_in_signalElement1740 = frozenset([20])
    FOLLOW_ID_in_signalElement1742 = frozenset([58])
    FOLLOW_58_in_signalElement1744 = frozenset([36])
    FOLLOW_TYPE_in_signalElement1746 = frozenset([62])
    FOLLOW_62_in_signalElement1748 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 94, 95, 96])
    FOLLOW_typeArg_in_signalElement1750 = frozenset([57])
    FOLLOW_57_in_signalElement1752 = frozenset([59])
    FOLLOW_59_in_signalElement1754 = frozenset([1])
    FOLLOW_SCOPE_in_attributeElement1778 = frozenset([62])
    FOLLOW_62_in_attributeElement1780 = frozenset([66, 67])
    FOLLOW_67_in_attributeElement1785 = frozenset([57])
    FOLLOW_66_in_attributeElement1789 = frozenset([57])
    FOLLOW_57_in_attributeElement1792 = frozenset([1])
    FOLLOW_VISIBILITY_in_attributeElement1806 = frozenset([62])
    FOLLOW_62_in_attributeElement1808 = frozenset([63, 64, 65])
    FOLLOW_63_in_attributeElement1813 = frozenset([57])
    FOLLOW_64_in_attributeElement1817 = frozenset([57])
    FOLLOW_65_in_attributeElement1821 = frozenset([57])
    FOLLOW_57_in_attributeElement1824 = frozenset([1])
    FOLLOW_typePath_in_typeName1846 = frozenset([1])
    FOLLOW_91_in_typeName1861 = frozenset([74])
    FOLLOW_74_in_typeName1864 = frozenset([1])
    FOLLOW_91_in_typeName1882 = frozenset([92])
    FOLLOW_92_in_typeName1885 = frozenset([1])
    FOLLOW_93_in_typeName1904 = frozenset([1])
    FOLLOW_73_in_typeName1913 = frozenset([1])
    FOLLOW_77_in_typeName1920 = frozenset([1])
    FOLLOW_75_in_typeName1927 = frozenset([1])
    FOLLOW_76_in_typeName1934 = frozenset([1])
    FOLLOW_78_in_typeName1943 = frozenset([1])
    FOLLOW_typeName_in_typeArg1969 = frozenset([1])
    FOLLOW_94_in_typeArg1979 = frozenset([86])
    FOLLOW_86_in_typeArg1981 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 94, 95, 96])
    FOLLOW_typeArg_in_typeArg1983 = frozenset([87])
    FOLLOW_87_in_typeArg1985 = frozenset([1])
    FOLLOW_95_in_typeArg2003 = frozenset([86])
    FOLLOW_86_in_typeArg2005 = frozenset([20, 73, 74, 75, 76, 77, 78, 91, 92, 93, 94, 95, 96])
    FOLLOW_typeArg_in_typeArg2007 = frozenset([87])
    FOLLOW_87_in_typeArg2009 = frozenset([1])
    FOLLOW_96_in_typePath2037 = frozenset([20])
    FOLLOW_ID_in_typePath2039 = frozenset([96])
    FOLLOW_96_in_typePath2041 = frozenset([20])
    FOLLOW_ID_in_typePath2045 = frozenset([96])
    FOLLOW_96_in_typePath2047 = frozenset([20])
    FOLLOW_ID_in_typePath2051 = frozenset([1])
    FOLLOW_ID_in_signalID2654 = frozenset([1, 97])
    FOLLOW_97_in_signalID2657 = frozenset([20])
    FOLLOW_ID_in_signalID2661 = frozenset([1, 97])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("GOCLexer", GOCParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
