# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 GOC.g 2011-02-17 22:48:38

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
PACKAGE=49
PREFIX=30
PROP_ACCESS=11
PROP_DEFAULT=16
GTYPE=27
OCTAL_ESC=53
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
COMMENT=46
GOBJECT=21
T__80=80
T__81=81
REF_TO=8
VISIBILITY=40
T__82=82
T__83=83
BOOLVALUE=48
GINTERFACE=22
INT=25
T__85=85
T__84=84
T__87=87
T__86=86
T__89=89
T__88=88
T__71=71
WS=47
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
T__61=61
ID=20
T__60=60
T__55=55
MODIFIERS=44
T__56=56
T__57=57
T__58=58
ESC_SEQ=50
IMPLEMENTS=31
T__54=54
SCOPE=41
T__59=59
SIGNAL=38
TYPE_NAME=6
PROP_TYPE=10
AUTO_CREATE=45
ERROR_DOMAIN=23
PROP_MIN=14
INIT_PROPERTY=18
UNICODE_ESC=52
HEX_DIGIT=51
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
    "PARAMETER", "MODIFIERS", "AUTO_CREATE", "COMMENT", "WS", "BOOLVALUE", 
    "PACKAGE", "ESC_SEQ", "HEX_DIGIT", "UNICODE_ESC", "OCTAL_ESC", "'include'", 
    "';'", "'{'", "'}'", "'code'", "'value'", "':'", "'public'", "'protected'", 
    "'private'", "'instance'", "'static'", "'final'", "'virtual'", "'bind_property'", 
    "'const'", "'boolean'", "'integer'", "'double'", "'string'", "'pointer'", 
    "'object'", "'enumeration'", "'access'", "'read-only'", "'initial-write'", 
    "'read-write'", "'description'", "'min'", "'max'", "'default'", "'null'", 
    "'float'", "'unsigned '", "'long'", "'ref'", "'('", "')'", "'list'", 
    "'::'", "'-'"
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

                    if ((GOBJECT <= LA1_0 <= ENUMERATION) or (FLAGS <= LA1_0 <= GTYPE) or LA1_0 == PACKAGE or LA1_0 == 54) :
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
                elif LA2 == 54:
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
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")

        try:
            try:
                # GOC.g:42:5: ( 'include' filename= STRING ';' -> ^( INCLUDE $filename) )
                # GOC.g:42:9: 'include' filename= STRING ';'
                pass 
                string_literal10=self.match(self.input, 54, self.FOLLOW_54_in_includeStmt226) 
                stream_54.add(string_literal10)
                filename=self.match(self.input, STRING, self.FOLLOW_STRING_in_includeStmt230) 
                stream_STRING.add(filename)
                char_literal11=self.match(self.input, 55, self.FOLLOW_55_in_includeStmt232) 
                stream_55.add(char_literal11)

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
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
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
                char_literal14=self.match(self.input, 56, self.FOLLOW_56_in_packageDef259) 
                stream_56.add(char_literal14)
                # GOC.g:46:21: ( packageElement )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((GOBJECT <= LA3_0 <= GINTERFACE) or LA3_0 == GTYPE or LA3_0 == PACKAGE) :
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
                char_literal16=self.match(self.input, 57, self.FOLLOW_57_in_packageDef264) 
                stream_57.add(char_literal16)

                # AST Rewrite
                # elements: ID, PACKAGE, packageElement
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
    # GOC.g:50:1: packageElement : ( packageDef | classDef | intfDef | typeDecl );
    def packageElement(self, ):

        retval = self.packageElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        packageDef17 = None

        classDef18 = None

        intfDef19 = None

        typeDecl20 = None



        try:
            try:
                # GOC.g:51:2: ( packageDef | classDef | intfDef | typeDecl )
                alt4 = 4
                LA4 = self.input.LA(1)
                if LA4 == PACKAGE:
                    alt4 = 1
                elif LA4 == GOBJECT:
                    alt4 = 2
                elif LA4 == GINTERFACE:
                    alt4 = 3
                elif LA4 == GTYPE:
                    alt4 = 4
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
                    # GOC.g:54:6: typeDecl
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_typeDecl_in_packageElement306)
                    typeDecl20 = self.typeDecl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, typeDecl20.tree)


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
    # GOC.g:57:1: classDef : GOBJECT className= ID ( '{' ( classMember )* '}' | ';' ) -> ^( GOBJECT $className ( classMember )* ) ;
    def classDef(self, ):

        retval = self.classDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        className = None
        GOBJECT21 = None
        char_literal22 = None
        char_literal24 = None
        char_literal25 = None
        classMember23 = None


        className_tree = None
        GOBJECT21_tree = None
        char_literal22_tree = None
        char_literal24_tree = None
        char_literal25_tree = None
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_GOBJECT = RewriteRuleTokenStream(self._adaptor, "token GOBJECT")
        stream_classMember = RewriteRuleSubtreeStream(self._adaptor, "rule classMember")
        try:
            try:
                # GOC.g:58:2: ( GOBJECT className= ID ( '{' ( classMember )* '}' | ';' ) -> ^( GOBJECT $className ( classMember )* ) )
                # GOC.g:58:4: GOBJECT className= ID ( '{' ( classMember )* '}' | ';' )
                pass 
                GOBJECT21=self.match(self.input, GOBJECT, self.FOLLOW_GOBJECT_in_classDef317) 
                stream_GOBJECT.add(GOBJECT21)
                className=self.match(self.input, ID, self.FOLLOW_ID_in_classDef321) 
                stream_ID.add(className)
                # GOC.g:58:25: ( '{' ( classMember )* '}' | ';' )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 56) :
                    alt6 = 1
                elif (LA6_0 == 55) :
                    alt6 = 2
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # GOC.g:58:26: '{' ( classMember )* '}'
                    pass 
                    char_literal22=self.match(self.input, 56, self.FOLLOW_56_in_classDef324) 
                    stream_56.add(char_literal22)
                    # GOC.g:58:30: ( classMember )*
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if ((SUPER <= LA5_0 <= ATTRIBUTE) or (PROPERTY <= LA5_0 <= SIGNAL)) :
                            alt5 = 1


                        if alt5 == 1:
                            # GOC.g:58:30: classMember
                            pass 
                            self._state.following.append(self.FOLLOW_classMember_in_classDef326)
                            classMember23 = self.classMember()

                            self._state.following.pop()
                            stream_classMember.add(classMember23.tree)


                        else:
                            break #loop5
                    char_literal24=self.match(self.input, 57, self.FOLLOW_57_in_classDef329) 
                    stream_57.add(char_literal24)


                elif alt6 == 2:
                    # GOC.g:58:47: ';'
                    pass 
                    char_literal25=self.match(self.input, 55, self.FOLLOW_55_in_classDef331) 
                    stream_55.add(char_literal25)




                # AST Rewrite
                # elements: GOBJECT, className, classMember
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
                # 59:2: -> ^( GOBJECT $className ( classMember )* )
                # GOC.g:59:5: ^( GOBJECT $className ( classMember )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_GOBJECT.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_className.nextNode())
                # GOC.g:59:26: ( classMember )*
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
    # GOC.g:62:1: intfDef : GINTERFACE intfName= ID ( '{' ( intfMember )* '}' | ';' ) -> ^( GINTERFACE $intfName ( intfMember )* ) ;
    def intfDef(self, ):

        retval = self.intfDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        intfName = None
        GINTERFACE26 = None
        char_literal27 = None
        char_literal29 = None
        char_literal30 = None
        intfMember28 = None


        intfName_tree = None
        GINTERFACE26_tree = None
        char_literal27_tree = None
        char_literal29_tree = None
        char_literal30_tree = None
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_GINTERFACE = RewriteRuleTokenStream(self._adaptor, "token GINTERFACE")
        stream_intfMember = RewriteRuleSubtreeStream(self._adaptor, "rule intfMember")
        try:
            try:
                # GOC.g:63:2: ( GINTERFACE intfName= ID ( '{' ( intfMember )* '}' | ';' ) -> ^( GINTERFACE $intfName ( intfMember )* ) )
                # GOC.g:63:4: GINTERFACE intfName= ID ( '{' ( intfMember )* '}' | ';' )
                pass 
                GINTERFACE26=self.match(self.input, GINTERFACE, self.FOLLOW_GINTERFACE_in_intfDef358) 
                stream_GINTERFACE.add(GINTERFACE26)
                intfName=self.match(self.input, ID, self.FOLLOW_ID_in_intfDef362) 
                stream_ID.add(intfName)
                # GOC.g:63:27: ( '{' ( intfMember )* '}' | ';' )
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == 56) :
                    alt8 = 1
                elif (LA8_0 == 55) :
                    alt8 = 2
                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # GOC.g:63:28: '{' ( intfMember )* '}'
                    pass 
                    char_literal27=self.match(self.input, 56, self.FOLLOW_56_in_intfDef365) 
                    stream_56.add(char_literal27)
                    # GOC.g:63:32: ( intfMember )*
                    while True: #loop7
                        alt7 = 2
                        LA7_0 = self.input.LA(1)

                        if (LA7_0 == METHOD or LA7_0 == SIGNAL) :
                            alt7 = 1


                        if alt7 == 1:
                            # GOC.g:63:32: intfMember
                            pass 
                            self._state.following.append(self.FOLLOW_intfMember_in_intfDef367)
                            intfMember28 = self.intfMember()

                            self._state.following.pop()
                            stream_intfMember.add(intfMember28.tree)


                        else:
                            break #loop7
                    char_literal29=self.match(self.input, 57, self.FOLLOW_57_in_intfDef370) 
                    stream_57.add(char_literal29)


                elif alt8 == 2:
                    # GOC.g:63:48: ';'
                    pass 
                    char_literal30=self.match(self.input, 55, self.FOLLOW_55_in_intfDef372) 
                    stream_55.add(char_literal30)




                # AST Rewrite
                # elements: GINTERFACE, intfMember, intfName
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
                # 64:2: -> ^( GINTERFACE $intfName ( intfMember )* )
                # GOC.g:64:5: ^( GINTERFACE $intfName ( intfMember )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_GINTERFACE.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_intfName.nextNode())
                # GOC.g:64:28: ( intfMember )*
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
    # GOC.g:67:1: errorDomainDef : ERROR_DOMAIN ID '{' ( errorDomainElement )+ '}' -> ^( ERROR_DOMAIN ID ( errorDomainElement )+ ) ;
    def errorDomainDef(self, ):

        retval = self.errorDomainDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ERROR_DOMAIN31 = None
        ID32 = None
        char_literal33 = None
        char_literal35 = None
        errorDomainElement34 = None


        ERROR_DOMAIN31_tree = None
        ID32_tree = None
        char_literal33_tree = None
        char_literal35_tree = None
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_ERROR_DOMAIN = RewriteRuleTokenStream(self._adaptor, "token ERROR_DOMAIN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_errorDomainElement = RewriteRuleSubtreeStream(self._adaptor, "rule errorDomainElement")
        try:
            try:
                # GOC.g:68:5: ( ERROR_DOMAIN ID '{' ( errorDomainElement )+ '}' -> ^( ERROR_DOMAIN ID ( errorDomainElement )+ ) )
                # GOC.g:68:9: ERROR_DOMAIN ID '{' ( errorDomainElement )+ '}'
                pass 
                ERROR_DOMAIN31=self.match(self.input, ERROR_DOMAIN, self.FOLLOW_ERROR_DOMAIN_in_errorDomainDef403) 
                stream_ERROR_DOMAIN.add(ERROR_DOMAIN31)
                ID32=self.match(self.input, ID, self.FOLLOW_ID_in_errorDomainDef405) 
                stream_ID.add(ID32)
                char_literal33=self.match(self.input, 56, self.FOLLOW_56_in_errorDomainDef407) 
                stream_56.add(char_literal33)
                # GOC.g:68:29: ( errorDomainElement )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 58) :
                        alt9 = 1


                    if alt9 == 1:
                        # GOC.g:68:29: errorDomainElement
                        pass 
                        self._state.following.append(self.FOLLOW_errorDomainElement_in_errorDomainDef409)
                        errorDomainElement34 = self.errorDomainElement()

                        self._state.following.pop()
                        stream_errorDomainElement.add(errorDomainElement34.tree)


                    else:
                        if cnt9 >= 1:
                            break #loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1
                char_literal35=self.match(self.input, 57, self.FOLLOW_57_in_errorDomainDef412) 
                stream_57.add(char_literal35)

                # AST Rewrite
                # elements: ERROR_DOMAIN, errorDomainElement, ID
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
                # 69:5: -> ^( ERROR_DOMAIN ID ( errorDomainElement )+ )
                # GOC.g:69:9: ^( ERROR_DOMAIN ID ( errorDomainElement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_ERROR_DOMAIN.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_ID.nextNode())
                # GOC.g:69:27: ( errorDomainElement )+
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
    # GOC.g:72:1: errorDomainElement : 'code' ID ';' -> ^( ID ) ;
    def errorDomainElement(self, ):

        retval = self.errorDomainElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal36 = None
        ID37 = None
        char_literal38 = None

        string_literal36_tree = None
        ID37_tree = None
        char_literal38_tree = None
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # GOC.g:73:5: ( 'code' ID ';' -> ^( ID ) )
                # GOC.g:73:9: 'code' ID ';'
                pass 
                string_literal36=self.match(self.input, 58, self.FOLLOW_58_in_errorDomainElement447) 
                stream_58.add(string_literal36)
                ID37=self.match(self.input, ID, self.FOLLOW_ID_in_errorDomainElement449) 
                stream_ID.add(ID37)
                char_literal38=self.match(self.input, 55, self.FOLLOW_55_in_errorDomainElement451) 
                stream_55.add(char_literal38)

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
                # 73:23: -> ^( ID )
                # GOC.g:73:26: ^( ID )
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
    # GOC.g:76:1: enumDef : ENUMERATION ID '{' ( enumElement )+ '}' -> ^( ENUMERATION ID ( enumElement )+ ) ;
    def enumDef(self, ):

        retval = self.enumDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ENUMERATION39 = None
        ID40 = None
        char_literal41 = None
        char_literal43 = None
        enumElement42 = None


        ENUMERATION39_tree = None
        ID40_tree = None
        char_literal41_tree = None
        char_literal43_tree = None
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_ENUMERATION = RewriteRuleTokenStream(self._adaptor, "token ENUMERATION")
        stream_enumElement = RewriteRuleSubtreeStream(self._adaptor, "rule enumElement")
        try:
            try:
                # GOC.g:77:5: ( ENUMERATION ID '{' ( enumElement )+ '}' -> ^( ENUMERATION ID ( enumElement )+ ) )
                # GOC.g:77:9: ENUMERATION ID '{' ( enumElement )+ '}'
                pass 
                ENUMERATION39=self.match(self.input, ENUMERATION, self.FOLLOW_ENUMERATION_in_enumDef476) 
                stream_ENUMERATION.add(ENUMERATION39)
                ID40=self.match(self.input, ID, self.FOLLOW_ID_in_enumDef478) 
                stream_ID.add(ID40)
                char_literal41=self.match(self.input, 56, self.FOLLOW_56_in_enumDef480) 
                stream_56.add(char_literal41)
                # GOC.g:77:28: ( enumElement )+
                cnt10 = 0
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == 58) :
                        alt10 = 1


                    if alt10 == 1:
                        # GOC.g:77:28: enumElement
                        pass 
                        self._state.following.append(self.FOLLOW_enumElement_in_enumDef482)
                        enumElement42 = self.enumElement()

                        self._state.following.pop()
                        stream_enumElement.add(enumElement42.tree)


                    else:
                        if cnt10 >= 1:
                            break #loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1
                char_literal43=self.match(self.input, 57, self.FOLLOW_57_in_enumDef485) 
                stream_57.add(char_literal43)

                # AST Rewrite
                # elements: ENUMERATION, ID, enumElement
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
                # 78:5: -> ^( ENUMERATION ID ( enumElement )+ )
                # GOC.g:78:9: ^( ENUMERATION ID ( enumElement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_ENUMERATION.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_ID.nextNode())
                # GOC.g:78:26: ( enumElement )+
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
    # GOC.g:81:1: enumElement : 'code' ID ( ';' | '{' 'value' ':' INT ';' '}' ) -> ^( 'code' ID ( INT )? ) ;
    def enumElement(self, ):

        retval = self.enumElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal44 = None
        ID45 = None
        char_literal46 = None
        char_literal47 = None
        string_literal48 = None
        char_literal49 = None
        INT50 = None
        char_literal51 = None
        char_literal52 = None

        string_literal44_tree = None
        ID45_tree = None
        char_literal46_tree = None
        char_literal47_tree = None
        string_literal48_tree = None
        char_literal49_tree = None
        INT50_tree = None
        char_literal51_tree = None
        char_literal52_tree = None
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")

        try:
            try:
                # GOC.g:82:5: ( 'code' ID ( ';' | '{' 'value' ':' INT ';' '}' ) -> ^( 'code' ID ( INT )? ) )
                # GOC.g:82:9: 'code' ID ( ';' | '{' 'value' ':' INT ';' '}' )
                pass 
                string_literal44=self.match(self.input, 58, self.FOLLOW_58_in_enumElement520) 
                stream_58.add(string_literal44)
                ID45=self.match(self.input, ID, self.FOLLOW_ID_in_enumElement522) 
                stream_ID.add(ID45)
                # GOC.g:82:19: ( ';' | '{' 'value' ':' INT ';' '}' )
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == 55) :
                    alt11 = 1
                elif (LA11_0 == 56) :
                    alt11 = 2
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # GOC.g:82:20: ';'
                    pass 
                    char_literal46=self.match(self.input, 55, self.FOLLOW_55_in_enumElement525) 
                    stream_55.add(char_literal46)


                elif alt11 == 2:
                    # GOC.g:82:24: '{' 'value' ':' INT ';' '}'
                    pass 
                    char_literal47=self.match(self.input, 56, self.FOLLOW_56_in_enumElement527) 
                    stream_56.add(char_literal47)
                    string_literal48=self.match(self.input, 59, self.FOLLOW_59_in_enumElement529) 
                    stream_59.add(string_literal48)
                    char_literal49=self.match(self.input, 60, self.FOLLOW_60_in_enumElement531) 
                    stream_60.add(char_literal49)
                    INT50=self.match(self.input, INT, self.FOLLOW_INT_in_enumElement533) 
                    stream_INT.add(INT50)
                    char_literal51=self.match(self.input, 55, self.FOLLOW_55_in_enumElement535) 
                    stream_55.add(char_literal51)
                    char_literal52=self.match(self.input, 57, self.FOLLOW_57_in_enumElement537) 
                    stream_57.add(char_literal52)




                # AST Rewrite
                # elements: INT, 58, ID
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
                # 83:5: -> ^( 'code' ID ( INT )? )
                # GOC.g:83:9: ^( 'code' ID ( INT )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_58.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_ID.nextNode())
                # GOC.g:83:21: ( INT )?
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
    # GOC.g:86:1: flagsDef : FLAGS ID '{' ( flagsElement )+ '}' -> ^( FLAGS ID ( flagsElement )+ ) ;
    def flagsDef(self, ):

        retval = self.flagsDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FLAGS53 = None
        ID54 = None
        char_literal55 = None
        char_literal57 = None
        flagsElement56 = None


        FLAGS53_tree = None
        ID54_tree = None
        char_literal55_tree = None
        char_literal57_tree = None
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_FLAGS = RewriteRuleTokenStream(self._adaptor, "token FLAGS")
        stream_flagsElement = RewriteRuleSubtreeStream(self._adaptor, "rule flagsElement")
        try:
            try:
                # GOC.g:87:5: ( FLAGS ID '{' ( flagsElement )+ '}' -> ^( FLAGS ID ( flagsElement )+ ) )
                # GOC.g:87:9: FLAGS ID '{' ( flagsElement )+ '}'
                pass 
                FLAGS53=self.match(self.input, FLAGS, self.FOLLOW_FLAGS_in_flagsDef573) 
                stream_FLAGS.add(FLAGS53)
                ID54=self.match(self.input, ID, self.FOLLOW_ID_in_flagsDef575) 
                stream_ID.add(ID54)
                char_literal55=self.match(self.input, 56, self.FOLLOW_56_in_flagsDef577) 
                stream_56.add(char_literal55)
                # GOC.g:87:22: ( flagsElement )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == 58) :
                        alt12 = 1


                    if alt12 == 1:
                        # GOC.g:87:22: flagsElement
                        pass 
                        self._state.following.append(self.FOLLOW_flagsElement_in_flagsDef579)
                        flagsElement56 = self.flagsElement()

                        self._state.following.pop()
                        stream_flagsElement.add(flagsElement56.tree)


                    else:
                        if cnt12 >= 1:
                            break #loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1
                char_literal57=self.match(self.input, 57, self.FOLLOW_57_in_flagsDef582) 
                stream_57.add(char_literal57)

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
                # 88:5: -> ^( FLAGS ID ( flagsElement )+ )
                # GOC.g:88:9: ^( FLAGS ID ( flagsElement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_FLAGS.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_ID.nextNode())
                # GOC.g:88:20: ( flagsElement )+
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
    # GOC.g:91:1: flagsElement : 'code' ID ';' -> ^( ID ) ;
    def flagsElement(self, ):

        retval = self.flagsElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal58 = None
        ID59 = None
        char_literal60 = None

        string_literal58_tree = None
        ID59_tree = None
        char_literal60_tree = None
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # GOC.g:92:5: ( 'code' ID ';' -> ^( ID ) )
                # GOC.g:92:9: 'code' ID ';'
                pass 
                string_literal58=self.match(self.input, 58, self.FOLLOW_58_in_flagsElement617) 
                stream_58.add(string_literal58)
                ID59=self.match(self.input, ID, self.FOLLOW_ID_in_flagsElement619) 
                stream_ID.add(ID59)
                char_literal60=self.match(self.input, 55, self.FOLLOW_55_in_flagsElement621) 
                stream_55.add(char_literal60)

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
                # 92:23: -> ^( ID )
                # GOC.g:92:26: ^( ID )
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
    # GOC.g:95:1: typeDecl : GTYPE ID ';' -> ^( GTYPE ID ) ;
    def typeDecl(self, ):

        retval = self.typeDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        GTYPE61 = None
        ID62 = None
        char_literal63 = None

        GTYPE61_tree = None
        ID62_tree = None
        char_literal63_tree = None
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_GTYPE = RewriteRuleTokenStream(self._adaptor, "token GTYPE")

        try:
            try:
                # GOC.g:96:5: ( GTYPE ID ';' -> ^( GTYPE ID ) )
                # GOC.g:96:9: GTYPE ID ';'
                pass 
                GTYPE61=self.match(self.input, GTYPE, self.FOLLOW_GTYPE_in_typeDecl646) 
                stream_GTYPE.add(GTYPE61)
                ID62=self.match(self.input, ID, self.FOLLOW_ID_in_typeDecl648) 
                stream_ID.add(ID62)
                char_literal63=self.match(self.input, 55, self.FOLLOW_55_in_typeDecl650) 
                stream_55.add(char_literal63)

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
                # 96:22: -> ^( GTYPE ID )
                # GOC.g:96:25: ^( GTYPE ID )
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
    # GOC.g:99:1: classMember : ( SUPER typeName ';' -> ^( SUPER typeName ) | ABSTRACT ';' | PREFIX ID ';' -> ^( PREFIX ID ) | IMPLEMENTS typeName ';' -> ^( IMPLEMENTS typeName ) | CONSTRUCTOR '{' ( constructorElement )* '}' -> ^( CONSTRUCTOR ( constructorElement )* ) | METHOD ID '{' ( methodElement )* '}' -> ^( METHOD ID ( methodElement )* ) | OVERRIDE ID ';' -> ^( OVERRIDE ID ) | ATTRIBUTE ID '{' TYPE ':' typeArg ';' ( attributeElement )* '}' -> ^( ATTRIBUTE ID typeArg ( attributeElement )* ) | PROPERTY ID '{' ( propertyElement )+ '}' -> ^( PROPERTY ID ( propertyElement )+ ) | SIGNAL signalID '{' ( signalElement )* '}' -> ^( SIGNAL signalID ( signalElement )* ) );
    def classMember(self, ):
        self.classMember_stack.append(classMember_scope())
        retval = self.classMember_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SUPER64 = None
        char_literal66 = None
        ABSTRACT67 = None
        char_literal68 = None
        PREFIX69 = None
        ID70 = None
        char_literal71 = None
        IMPLEMENTS72 = None
        char_literal74 = None
        CONSTRUCTOR75 = None
        char_literal76 = None
        char_literal78 = None
        METHOD79 = None
        ID80 = None
        char_literal81 = None
        char_literal83 = None
        OVERRIDE84 = None
        ID85 = None
        char_literal86 = None
        ATTRIBUTE87 = None
        ID88 = None
        char_literal89 = None
        TYPE90 = None
        char_literal91 = None
        char_literal93 = None
        char_literal95 = None
        PROPERTY96 = None
        ID97 = None
        char_literal98 = None
        char_literal100 = None
        SIGNAL101 = None
        char_literal103 = None
        char_literal105 = None
        typeName65 = None

        typeName73 = None

        constructorElement77 = None

        methodElement82 = None

        typeArg92 = None

        attributeElement94 = None

        propertyElement99 = None

        signalID102 = None

        signalElement104 = None


        SUPER64_tree = None
        char_literal66_tree = None
        ABSTRACT67_tree = None
        char_literal68_tree = None
        PREFIX69_tree = None
        ID70_tree = None
        char_literal71_tree = None
        IMPLEMENTS72_tree = None
        char_literal74_tree = None
        CONSTRUCTOR75_tree = None
        char_literal76_tree = None
        char_literal78_tree = None
        METHOD79_tree = None
        ID80_tree = None
        char_literal81_tree = None
        char_literal83_tree = None
        OVERRIDE84_tree = None
        ID85_tree = None
        char_literal86_tree = None
        ATTRIBUTE87_tree = None
        ID88_tree = None
        char_literal89_tree = None
        TYPE90_tree = None
        char_literal91_tree = None
        char_literal93_tree = None
        char_literal95_tree = None
        PROPERTY96_tree = None
        ID97_tree = None
        char_literal98_tree = None
        char_literal100_tree = None
        SIGNAL101_tree = None
        char_literal103_tree = None
        char_literal105_tree = None
        stream_PREFIX = RewriteRuleTokenStream(self._adaptor, "token PREFIX")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_IMPLEMENTS = RewriteRuleTokenStream(self._adaptor, "token IMPLEMENTS")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_PROPERTY = RewriteRuleTokenStream(self._adaptor, "token PROPERTY")
        stream_OVERRIDE = RewriteRuleTokenStream(self._adaptor, "token OVERRIDE")
        stream_SIGNAL = RewriteRuleTokenStream(self._adaptor, "token SIGNAL")
        stream_ATTRIBUTE = RewriteRuleTokenStream(self._adaptor, "token ATTRIBUTE")
        stream_SUPER = RewriteRuleTokenStream(self._adaptor, "token SUPER")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CONSTRUCTOR = RewriteRuleTokenStream(self._adaptor, "token CONSTRUCTOR")
        stream_METHOD = RewriteRuleTokenStream(self._adaptor, "token METHOD")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
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
                # GOC.g:106:2: ( SUPER typeName ';' -> ^( SUPER typeName ) | ABSTRACT ';' | PREFIX ID ';' -> ^( PREFIX ID ) | IMPLEMENTS typeName ';' -> ^( IMPLEMENTS typeName ) | CONSTRUCTOR '{' ( constructorElement )* '}' -> ^( CONSTRUCTOR ( constructorElement )* ) | METHOD ID '{' ( methodElement )* '}' -> ^( METHOD ID ( methodElement )* ) | OVERRIDE ID ';' -> ^( OVERRIDE ID ) | ATTRIBUTE ID '{' TYPE ':' typeArg ';' ( attributeElement )* '}' -> ^( ATTRIBUTE ID typeArg ( attributeElement )* ) | PROPERTY ID '{' ( propertyElement )+ '}' -> ^( PROPERTY ID ( propertyElement )+ ) | SIGNAL signalID '{' ( signalElement )* '}' -> ^( SIGNAL signalID ( signalElement )* ) )
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
                    # GOC.g:106:4: SUPER typeName ';'
                    pass 
                    SUPER64=self.match(self.input, SUPER, self.FOLLOW_SUPER_in_classMember681) 
                    stream_SUPER.add(SUPER64)
                    self._state.following.append(self.FOLLOW_typeName_in_classMember683)
                    typeName65 = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(typeName65.tree)
                    char_literal66=self.match(self.input, 55, self.FOLLOW_55_in_classMember685) 
                    stream_55.add(char_literal66)

                    # AST Rewrite
                    # elements: SUPER, typeName
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
                    # 107:2: -> ^( SUPER typeName )
                    # GOC.g:107:5: ^( SUPER typeName )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_SUPER.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_typeName.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt18 == 2:
                    # GOC.g:108:6: ABSTRACT ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    ABSTRACT67=self.match(self.input, ABSTRACT, self.FOLLOW_ABSTRACT_in_classMember701)

                    ABSTRACT67_tree = self._adaptor.createWithPayload(ABSTRACT67)
                    root_0 = self._adaptor.becomeRoot(ABSTRACT67_tree, root_0)

                    char_literal68=self.match(self.input, 55, self.FOLLOW_55_in_classMember704)

                    char_literal68_tree = self._adaptor.createWithPayload(char_literal68)
                    self._adaptor.addChild(root_0, char_literal68_tree)



                elif alt18 == 3:
                    # GOC.g:109:6: PREFIX ID ';'
                    pass 
                    PREFIX69=self.match(self.input, PREFIX, self.FOLLOW_PREFIX_in_classMember711) 
                    stream_PREFIX.add(PREFIX69)
                    ID70=self.match(self.input, ID, self.FOLLOW_ID_in_classMember713) 
                    stream_ID.add(ID70)
                    char_literal71=self.match(self.input, 55, self.FOLLOW_55_in_classMember715) 
                    stream_55.add(char_literal71)

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
                    # 109:20: -> ^( PREFIX ID )
                    # GOC.g:109:23: ^( PREFIX ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_PREFIX.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt18 == 4:
                    # GOC.g:110:4: IMPLEMENTS typeName ';'
                    pass 
                    IMPLEMENTS72=self.match(self.input, IMPLEMENTS, self.FOLLOW_IMPLEMENTS_in_classMember728) 
                    stream_IMPLEMENTS.add(IMPLEMENTS72)
                    self._state.following.append(self.FOLLOW_typeName_in_classMember730)
                    typeName73 = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(typeName73.tree)
                    char_literal74=self.match(self.input, 55, self.FOLLOW_55_in_classMember732) 
                    stream_55.add(char_literal74)

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
                    # 110:28: -> ^( IMPLEMENTS typeName )
                    # GOC.g:110:31: ^( IMPLEMENTS typeName )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_IMPLEMENTS.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_typeName.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt18 == 5:
                    # GOC.g:111:4: CONSTRUCTOR '{' ( constructorElement )* '}'
                    pass 
                    #action start
                    self.classMember_stack[-1].with_constructor = True 
                    #action end
                    CONSTRUCTOR75=self.match(self.input, CONSTRUCTOR, self.FOLLOW_CONSTRUCTOR_in_classMember752) 
                    stream_CONSTRUCTOR.add(CONSTRUCTOR75)
                    char_literal76=self.match(self.input, 56, self.FOLLOW_56_in_classMember754) 
                    stream_56.add(char_literal76)
                    # GOC.g:112:22: ( constructorElement )*
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == PARAMETER) :
                            alt13 = 1


                        if alt13 == 1:
                            # GOC.g:112:22: constructorElement
                            pass 
                            self._state.following.append(self.FOLLOW_constructorElement_in_classMember756)
                            constructorElement77 = self.constructorElement()

                            self._state.following.pop()
                            stream_constructorElement.add(constructorElement77.tree)


                        else:
                            break #loop13
                    char_literal78=self.match(self.input, 57, self.FOLLOW_57_in_classMember759) 
                    stream_57.add(char_literal78)
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
                    # 114:6: -> ^( CONSTRUCTOR ( constructorElement )* )
                    # GOC.g:114:9: ^( CONSTRUCTOR ( constructorElement )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_CONSTRUCTOR.nextNode(), root_1)

                    # GOC.g:114:23: ( constructorElement )*
                    while stream_constructorElement.hasNext():
                        self._adaptor.addChild(root_1, stream_constructorElement.nextTree())


                    stream_constructorElement.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt18 == 6:
                    # GOC.g:115:6: METHOD ID '{' ( methodElement )* '}'
                    pass 
                    METHOD79=self.match(self.input, METHOD, self.FOLLOW_METHOD_in_classMember787) 
                    stream_METHOD.add(METHOD79)
                    ID80=self.match(self.input, ID, self.FOLLOW_ID_in_classMember789) 
                    stream_ID.add(ID80)
                    char_literal81=self.match(self.input, 56, self.FOLLOW_56_in_classMember791) 
                    stream_56.add(char_literal81)
                    # GOC.g:115:20: ( methodElement )*
                    while True: #loop14
                        alt14 = 2
                        LA14_0 = self.input.LA(1)

                        if ((RESULT <= LA14_0 <= PARAMETER)) :
                            alt14 = 1


                        if alt14 == 1:
                            # GOC.g:115:20: methodElement
                            pass 
                            self._state.following.append(self.FOLLOW_methodElement_in_classMember793)
                            methodElement82 = self.methodElement()

                            self._state.following.pop()
                            stream_methodElement.add(methodElement82.tree)


                        else:
                            break #loop14
                    char_literal83=self.match(self.input, 57, self.FOLLOW_57_in_classMember796) 
                    stream_57.add(char_literal83)

                    # AST Rewrite
                    # elements: METHOD, methodElement, ID
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
                    # 115:39: -> ^( METHOD ID ( methodElement )* )
                    # GOC.g:115:42: ^( METHOD ID ( methodElement )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_METHOD.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())
                    # GOC.g:115:54: ( methodElement )*
                    while stream_methodElement.hasNext():
                        self._adaptor.addChild(root_1, stream_methodElement.nextTree())


                    stream_methodElement.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt18 == 7:
                    # GOC.g:116:5: OVERRIDE ID ';'
                    pass 
                    OVERRIDE84=self.match(self.input, OVERRIDE, self.FOLLOW_OVERRIDE_in_classMember813) 
                    stream_OVERRIDE.add(OVERRIDE84)
                    ID85=self.match(self.input, ID, self.FOLLOW_ID_in_classMember815) 
                    stream_ID.add(ID85)
                    char_literal86=self.match(self.input, 55, self.FOLLOW_55_in_classMember817) 
                    stream_55.add(char_literal86)

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
                    # 116:21: -> ^( OVERRIDE ID )
                    # GOC.g:116:24: ^( OVERRIDE ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_OVERRIDE.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt18 == 8:
                    # GOC.g:117:4: ATTRIBUTE ID '{' TYPE ':' typeArg ';' ( attributeElement )* '}'
                    pass 
                    ATTRIBUTE87=self.match(self.input, ATTRIBUTE, self.FOLLOW_ATTRIBUTE_in_classMember830) 
                    stream_ATTRIBUTE.add(ATTRIBUTE87)
                    ID88=self.match(self.input, ID, self.FOLLOW_ID_in_classMember832) 
                    stream_ID.add(ID88)
                    char_literal89=self.match(self.input, 56, self.FOLLOW_56_in_classMember834) 
                    stream_56.add(char_literal89)
                    TYPE90=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_classMember836) 
                    stream_TYPE.add(TYPE90)
                    char_literal91=self.match(self.input, 60, self.FOLLOW_60_in_classMember838) 
                    stream_60.add(char_literal91)
                    self._state.following.append(self.FOLLOW_typeArg_in_classMember840)
                    typeArg92 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg92.tree)
                    char_literal93=self.match(self.input, 55, self.FOLLOW_55_in_classMember842) 
                    stream_55.add(char_literal93)
                    # GOC.g:117:42: ( attributeElement )*
                    while True: #loop15
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if ((VISIBILITY <= LA15_0 <= SCOPE)) :
                            alt15 = 1


                        if alt15 == 1:
                            # GOC.g:117:42: attributeElement
                            pass 
                            self._state.following.append(self.FOLLOW_attributeElement_in_classMember844)
                            attributeElement94 = self.attributeElement()

                            self._state.following.pop()
                            stream_attributeElement.add(attributeElement94.tree)


                        else:
                            break #loop15
                    char_literal95=self.match(self.input, 57, self.FOLLOW_57_in_classMember847) 
                    stream_57.add(char_literal95)

                    # AST Rewrite
                    # elements: typeArg, ATTRIBUTE, ID, attributeElement
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
                    # 118:2: -> ^( ATTRIBUTE ID typeArg ( attributeElement )* )
                    # GOC.g:118:5: ^( ATTRIBUTE ID typeArg ( attributeElement )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_ATTRIBUTE.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())
                    self._adaptor.addChild(root_1, stream_typeArg.nextTree())
                    # GOC.g:118:28: ( attributeElement )*
                    while stream_attributeElement.hasNext():
                        self._adaptor.addChild(root_1, stream_attributeElement.nextTree())


                    stream_attributeElement.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt18 == 9:
                    # GOC.g:119:4: PROPERTY ID '{' ( propertyElement )+ '}'
                    pass 
                    PROPERTY96=self.match(self.input, PROPERTY, self.FOLLOW_PROPERTY_in_classMember866) 
                    stream_PROPERTY.add(PROPERTY96)
                    ID97=self.match(self.input, ID, self.FOLLOW_ID_in_classMember868) 
                    stream_ID.add(ID97)
                    char_literal98=self.match(self.input, 56, self.FOLLOW_56_in_classMember870) 
                    stream_56.add(char_literal98)
                    # GOC.g:119:20: ( propertyElement )+
                    cnt16 = 0
                    while True: #loop16
                        alt16 = 2
                        LA16_0 = self.input.LA(1)

                        if (LA16_0 == GTYPE or LA16_0 == TYPE or LA16_0 == AUTO_CREATE or LA16_0 == 77 or (81 <= LA16_0 <= 84)) :
                            alt16 = 1


                        if alt16 == 1:
                            # GOC.g:119:20: propertyElement
                            pass 
                            self._state.following.append(self.FOLLOW_propertyElement_in_classMember872)
                            propertyElement99 = self.propertyElement()

                            self._state.following.pop()
                            stream_propertyElement.add(propertyElement99.tree)


                        else:
                            if cnt16 >= 1:
                                break #loop16

                            eee = EarlyExitException(16, self.input)
                            raise eee

                        cnt16 += 1
                    char_literal100=self.match(self.input, 57, self.FOLLOW_57_in_classMember875) 
                    stream_57.add(char_literal100)

                    # AST Rewrite
                    # elements: ID, PROPERTY, propertyElement
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
                    # 119:41: -> ^( PROPERTY ID ( propertyElement )+ )
                    # GOC.g:119:44: ^( PROPERTY ID ( propertyElement )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_PROPERTY.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())
                    # GOC.g:119:58: ( propertyElement )+
                    if not (stream_propertyElement.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_propertyElement.hasNext():
                        self._adaptor.addChild(root_1, stream_propertyElement.nextTree())


                    stream_propertyElement.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt18 == 10:
                    # GOC.g:120:4: SIGNAL signalID '{' ( signalElement )* '}'
                    pass 
                    SIGNAL101=self.match(self.input, SIGNAL, self.FOLLOW_SIGNAL_in_classMember891) 
                    stream_SIGNAL.add(SIGNAL101)
                    self._state.following.append(self.FOLLOW_signalID_in_classMember893)
                    signalID102 = self.signalID()

                    self._state.following.pop()
                    stream_signalID.add(signalID102.tree)
                    char_literal103=self.match(self.input, 56, self.FOLLOW_56_in_classMember895) 
                    stream_56.add(char_literal103)
                    # GOC.g:120:24: ( signalElement )*
                    while True: #loop17
                        alt17 = 2
                        LA17_0 = self.input.LA(1)

                        if (LA17_0 == RESULT or LA17_0 == PARAMETER) :
                            alt17 = 1


                        if alt17 == 1:
                            # GOC.g:120:24: signalElement
                            pass 
                            self._state.following.append(self.FOLLOW_signalElement_in_classMember897)
                            signalElement104 = self.signalElement()

                            self._state.following.pop()
                            stream_signalElement.add(signalElement104.tree)


                        else:
                            break #loop17
                    char_literal105=self.match(self.input, 57, self.FOLLOW_57_in_classMember900) 
                    stream_57.add(char_literal105)

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
                    # 120:43: -> ^( SIGNAL signalID ( signalElement )* )
                    # GOC.g:120:46: ^( SIGNAL signalID ( signalElement )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_SIGNAL.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_signalID.nextTree())
                    # GOC.g:120:64: ( signalElement )*
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
    # GOC.g:123:1: intfMember : ( METHOD ID '{' ( methodElement )* '}' -> ^( METHOD ID ( methodElement )* ) | SIGNAL signalID '{' ( signalElement )* '}' -> ^( SIGNAL signalID ( signalElement )* ) );
    def intfMember(self, ):

        retval = self.intfMember_return()
        retval.start = self.input.LT(1)

        root_0 = None

        METHOD106 = None
        ID107 = None
        char_literal108 = None
        char_literal110 = None
        SIGNAL111 = None
        char_literal113 = None
        char_literal115 = None
        methodElement109 = None

        signalID112 = None

        signalElement114 = None


        METHOD106_tree = None
        ID107_tree = None
        char_literal108_tree = None
        char_literal110_tree = None
        SIGNAL111_tree = None
        char_literal113_tree = None
        char_literal115_tree = None
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_METHOD = RewriteRuleTokenStream(self._adaptor, "token METHOD")
        stream_SIGNAL = RewriteRuleTokenStream(self._adaptor, "token SIGNAL")
        stream_methodElement = RewriteRuleSubtreeStream(self._adaptor, "rule methodElement")
        stream_signalElement = RewriteRuleSubtreeStream(self._adaptor, "rule signalElement")
        stream_signalID = RewriteRuleSubtreeStream(self._adaptor, "rule signalID")
        try:
            try:
                # GOC.g:124:2: ( METHOD ID '{' ( methodElement )* '}' -> ^( METHOD ID ( methodElement )* ) | SIGNAL signalID '{' ( signalElement )* '}' -> ^( SIGNAL signalID ( signalElement )* ) )
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == METHOD) :
                    alt21 = 1
                elif (LA21_0 == SIGNAL) :
                    alt21 = 2
                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # GOC.g:124:4: METHOD ID '{' ( methodElement )* '}'
                    pass 
                    METHOD106=self.match(self.input, METHOD, self.FOLLOW_METHOD_in_intfMember923) 
                    stream_METHOD.add(METHOD106)
                    ID107=self.match(self.input, ID, self.FOLLOW_ID_in_intfMember925) 
                    stream_ID.add(ID107)
                    char_literal108=self.match(self.input, 56, self.FOLLOW_56_in_intfMember927) 
                    stream_56.add(char_literal108)
                    # GOC.g:124:18: ( methodElement )*
                    while True: #loop19
                        alt19 = 2
                        LA19_0 = self.input.LA(1)

                        if ((RESULT <= LA19_0 <= PARAMETER)) :
                            alt19 = 1


                        if alt19 == 1:
                            # GOC.g:124:18: methodElement
                            pass 
                            self._state.following.append(self.FOLLOW_methodElement_in_intfMember929)
                            methodElement109 = self.methodElement()

                            self._state.following.pop()
                            stream_methodElement.add(methodElement109.tree)


                        else:
                            break #loop19
                    char_literal110=self.match(self.input, 57, self.FOLLOW_57_in_intfMember932) 
                    stream_57.add(char_literal110)

                    # AST Rewrite
                    # elements: METHOD, methodElement, ID
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
                    # 124:37: -> ^( METHOD ID ( methodElement )* )
                    # GOC.g:124:40: ^( METHOD ID ( methodElement )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_METHOD.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())
                    # GOC.g:124:52: ( methodElement )*
                    while stream_methodElement.hasNext():
                        self._adaptor.addChild(root_1, stream_methodElement.nextTree())


                    stream_methodElement.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt21 == 2:
                    # GOC.g:125:9: SIGNAL signalID '{' ( signalElement )* '}'
                    pass 
                    SIGNAL111=self.match(self.input, SIGNAL, self.FOLLOW_SIGNAL_in_intfMember953) 
                    stream_SIGNAL.add(SIGNAL111)
                    self._state.following.append(self.FOLLOW_signalID_in_intfMember955)
                    signalID112 = self.signalID()

                    self._state.following.pop()
                    stream_signalID.add(signalID112.tree)
                    char_literal113=self.match(self.input, 56, self.FOLLOW_56_in_intfMember957) 
                    stream_56.add(char_literal113)
                    # GOC.g:125:29: ( signalElement )*
                    while True: #loop20
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if (LA20_0 == RESULT or LA20_0 == PARAMETER) :
                            alt20 = 1


                        if alt20 == 1:
                            # GOC.g:125:29: signalElement
                            pass 
                            self._state.following.append(self.FOLLOW_signalElement_in_intfMember959)
                            signalElement114 = self.signalElement()

                            self._state.following.pop()
                            stream_signalElement.add(signalElement114.tree)


                        else:
                            break #loop20
                    char_literal115=self.match(self.input, 57, self.FOLLOW_57_in_intfMember962) 
                    stream_57.add(char_literal115)

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
                    # 125:48: -> ^( SIGNAL signalID ( signalElement )* )
                    # GOC.g:125:51: ^( SIGNAL signalID ( signalElement )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_SIGNAL.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_signalID.nextTree())
                    # GOC.g:125:69: ( signalElement )*
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
    # GOC.g:128:1: resultDef : RESULT '{' TYPE ':' typeArg ';' ( modifiers )? '}' -> ^( RESULT typeArg ( modifiers )? ) ;
    def resultDef(self, ):

        retval = self.resultDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RESULT116 = None
        char_literal117 = None
        TYPE118 = None
        char_literal119 = None
        char_literal121 = None
        char_literal123 = None
        typeArg120 = None

        modifiers122 = None


        RESULT116_tree = None
        char_literal117_tree = None
        TYPE118_tree = None
        char_literal119_tree = None
        char_literal121_tree = None
        char_literal123_tree = None
        stream_RESULT = RewriteRuleTokenStream(self._adaptor, "token RESULT")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_TYPE = RewriteRuleTokenStream(self._adaptor, "token TYPE")
        stream_typeArg = RewriteRuleSubtreeStream(self._adaptor, "rule typeArg")
        stream_modifiers = RewriteRuleSubtreeStream(self._adaptor, "rule modifiers")
        try:
            try:
                # GOC.g:129:2: ( RESULT '{' TYPE ':' typeArg ';' ( modifiers )? '}' -> ^( RESULT typeArg ( modifiers )? ) )
                # GOC.g:129:4: RESULT '{' TYPE ':' typeArg ';' ( modifiers )? '}'
                pass 
                RESULT116=self.match(self.input, RESULT, self.FOLLOW_RESULT_in_resultDef985) 
                stream_RESULT.add(RESULT116)
                char_literal117=self.match(self.input, 56, self.FOLLOW_56_in_resultDef987) 
                stream_56.add(char_literal117)
                TYPE118=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_resultDef989) 
                stream_TYPE.add(TYPE118)
                char_literal119=self.match(self.input, 60, self.FOLLOW_60_in_resultDef991) 
                stream_60.add(char_literal119)
                self._state.following.append(self.FOLLOW_typeArg_in_resultDef993)
                typeArg120 = self.typeArg()

                self._state.following.pop()
                stream_typeArg.add(typeArg120.tree)
                char_literal121=self.match(self.input, 55, self.FOLLOW_55_in_resultDef995) 
                stream_55.add(char_literal121)
                # GOC.g:129:36: ( modifiers )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == MODIFIERS) :
                    alt22 = 1
                if alt22 == 1:
                    # GOC.g:129:36: modifiers
                    pass 
                    self._state.following.append(self.FOLLOW_modifiers_in_resultDef997)
                    modifiers122 = self.modifiers()

                    self._state.following.pop()
                    stream_modifiers.add(modifiers122.tree)



                char_literal123=self.match(self.input, 57, self.FOLLOW_57_in_resultDef1000) 
                stream_57.add(char_literal123)

                # AST Rewrite
                # elements: typeArg, RESULT, modifiers
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
                # 130:2: -> ^( RESULT typeArg ( modifiers )? )
                # GOC.g:130:5: ^( RESULT typeArg ( modifiers )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_RESULT.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_typeArg.nextTree())
                # GOC.g:130:22: ( modifiers )?
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
    # GOC.g:133:1: methodElement : ( constructorElement | resultDef | VISIBILITY ':' (val= 'public' | val= 'protected' | val= 'private' ) ';' -> ^( VISIBILITY $val) | SCOPE ':' (val= 'instance' | val= 'static' ) ';' -> ^( SCOPE $val) | INHERITANCE ':' (val= 'final' | val= 'virtual' | val= 'abstract' ) ';' -> ^( INHERITANCE $val) );
    def methodElement(self, ):

        retval = self.methodElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        val = None
        VISIBILITY126 = None
        char_literal127 = None
        char_literal128 = None
        SCOPE129 = None
        char_literal130 = None
        char_literal131 = None
        INHERITANCE132 = None
        char_literal133 = None
        char_literal134 = None
        constructorElement124 = None

        resultDef125 = None


        val_tree = None
        VISIBILITY126_tree = None
        char_literal127_tree = None
        char_literal128_tree = None
        SCOPE129_tree = None
        char_literal130_tree = None
        char_literal131_tree = None
        INHERITANCE132_tree = None
        char_literal133_tree = None
        char_literal134_tree = None
        stream_67 = RewriteRuleTokenStream(self._adaptor, "token 67")
        stream_66 = RewriteRuleTokenStream(self._adaptor, "token 66")
        stream_VISIBILITY = RewriteRuleTokenStream(self._adaptor, "token VISIBILITY")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_SCOPE = RewriteRuleTokenStream(self._adaptor, "token SCOPE")
        stream_ABSTRACT = RewriteRuleTokenStream(self._adaptor, "token ABSTRACT")
        stream_64 = RewriteRuleTokenStream(self._adaptor, "token 64")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_63 = RewriteRuleTokenStream(self._adaptor, "token 63")
        stream_INHERITANCE = RewriteRuleTokenStream(self._adaptor, "token INHERITANCE")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_61 = RewriteRuleTokenStream(self._adaptor, "token 61")

        try:
            try:
                # GOC.g:134:2: ( constructorElement | resultDef | VISIBILITY ':' (val= 'public' | val= 'protected' | val= 'private' ) ';' -> ^( VISIBILITY $val) | SCOPE ':' (val= 'instance' | val= 'static' ) ';' -> ^( SCOPE $val) | INHERITANCE ':' (val= 'final' | val= 'virtual' | val= 'abstract' ) ';' -> ^( INHERITANCE $val) )
                alt26 = 5
                LA26 = self.input.LA(1)
                if LA26 == PARAMETER:
                    alt26 = 1
                elif LA26 == RESULT:
                    alt26 = 2
                elif LA26 == VISIBILITY:
                    alt26 = 3
                elif LA26 == SCOPE:
                    alt26 = 4
                elif LA26 == INHERITANCE:
                    alt26 = 5
                else:
                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae

                if alt26 == 1:
                    # GOC.g:134:4: constructorElement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_constructorElement_in_methodElement1023)
                    constructorElement124 = self.constructorElement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, constructorElement124.tree)


                elif alt26 == 2:
                    # GOC.g:135:4: resultDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_resultDef_in_methodElement1028)
                    resultDef125 = self.resultDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, resultDef125.tree)


                elif alt26 == 3:
                    # GOC.g:136:4: VISIBILITY ':' (val= 'public' | val= 'protected' | val= 'private' ) ';'
                    pass 
                    VISIBILITY126=self.match(self.input, VISIBILITY, self.FOLLOW_VISIBILITY_in_methodElement1033) 
                    stream_VISIBILITY.add(VISIBILITY126)
                    char_literal127=self.match(self.input, 60, self.FOLLOW_60_in_methodElement1035) 
                    stream_60.add(char_literal127)
                    # GOC.g:136:19: (val= 'public' | val= 'protected' | val= 'private' )
                    alt23 = 3
                    LA23 = self.input.LA(1)
                    if LA23 == 61:
                        alt23 = 1
                    elif LA23 == 62:
                        alt23 = 2
                    elif LA23 == 63:
                        alt23 = 3
                    else:
                        nvae = NoViableAltException("", 23, 0, self.input)

                        raise nvae

                    if alt23 == 1:
                        # GOC.g:136:20: val= 'public'
                        pass 
                        val=self.match(self.input, 61, self.FOLLOW_61_in_methodElement1040) 
                        stream_61.add(val)


                    elif alt23 == 2:
                        # GOC.g:136:33: val= 'protected'
                        pass 
                        val=self.match(self.input, 62, self.FOLLOW_62_in_methodElement1044) 
                        stream_62.add(val)


                    elif alt23 == 3:
                        # GOC.g:136:49: val= 'private'
                        pass 
                        val=self.match(self.input, 63, self.FOLLOW_63_in_methodElement1048) 
                        stream_63.add(val)



                    char_literal128=self.match(self.input, 55, self.FOLLOW_55_in_methodElement1051) 
                    stream_55.add(char_literal128)

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
                    # 137:2: -> ^( VISIBILITY $val)
                    # GOC.g:137:5: ^( VISIBILITY $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_VISIBILITY.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt26 == 4:
                    # GOC.g:138:4: SCOPE ':' (val= 'instance' | val= 'static' ) ';'
                    pass 
                    SCOPE129=self.match(self.input, SCOPE, self.FOLLOW_SCOPE_in_methodElement1066) 
                    stream_SCOPE.add(SCOPE129)
                    char_literal130=self.match(self.input, 60, self.FOLLOW_60_in_methodElement1068) 
                    stream_60.add(char_literal130)
                    # GOC.g:138:14: (val= 'instance' | val= 'static' )
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == 64) :
                        alt24 = 1
                    elif (LA24_0 == 65) :
                        alt24 = 2
                    else:
                        nvae = NoViableAltException("", 24, 0, self.input)

                        raise nvae

                    if alt24 == 1:
                        # GOC.g:138:15: val= 'instance'
                        pass 
                        val=self.match(self.input, 64, self.FOLLOW_64_in_methodElement1073) 
                        stream_64.add(val)


                    elif alt24 == 2:
                        # GOC.g:138:30: val= 'static'
                        pass 
                        val=self.match(self.input, 65, self.FOLLOW_65_in_methodElement1077) 
                        stream_65.add(val)



                    char_literal131=self.match(self.input, 55, self.FOLLOW_55_in_methodElement1080) 
                    stream_55.add(char_literal131)

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
                    # 139:2: -> ^( SCOPE $val)
                    # GOC.g:139:5: ^( SCOPE $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_SCOPE.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt26 == 5:
                    # GOC.g:140:5: INHERITANCE ':' (val= 'final' | val= 'virtual' | val= 'abstract' ) ';'
                    pass 
                    INHERITANCE132=self.match(self.input, INHERITANCE, self.FOLLOW_INHERITANCE_in_methodElement1096) 
                    stream_INHERITANCE.add(INHERITANCE132)
                    char_literal133=self.match(self.input, 60, self.FOLLOW_60_in_methodElement1098) 
                    stream_60.add(char_literal133)
                    # GOC.g:140:21: (val= 'final' | val= 'virtual' | val= 'abstract' )
                    alt25 = 3
                    LA25 = self.input.LA(1)
                    if LA25 == 66:
                        alt25 = 1
                    elif LA25 == 67:
                        alt25 = 2
                    elif LA25 == ABSTRACT:
                        alt25 = 3
                    else:
                        nvae = NoViableAltException("", 25, 0, self.input)

                        raise nvae

                    if alt25 == 1:
                        # GOC.g:140:22: val= 'final'
                        pass 
                        val=self.match(self.input, 66, self.FOLLOW_66_in_methodElement1103) 
                        stream_66.add(val)


                    elif alt25 == 2:
                        # GOC.g:140:34: val= 'virtual'
                        pass 
                        val=self.match(self.input, 67, self.FOLLOW_67_in_methodElement1107) 
                        stream_67.add(val)


                    elif alt25 == 3:
                        # GOC.g:140:48: val= 'abstract'
                        pass 
                        val=self.match(self.input, ABSTRACT, self.FOLLOW_ABSTRACT_in_methodElement1111) 
                        stream_ABSTRACT.add(val)



                    char_literal134=self.match(self.input, 55, self.FOLLOW_55_in_methodElement1114) 
                    stream_55.add(char_literal134)

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
                    # 141:2: -> ^( INHERITANCE $val)
                    # GOC.g:141:5: ^( INHERITANCE $val)
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
    # GOC.g:144:1: constructorElement : PARAMETER ID '{' 'type' ':' typeArg ';' ( parameterElement )? '}' -> ^( PARAMETER ID typeArg ( parameterElement )? ) ;
    def constructorElement(self, ):

        retval = self.constructorElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PARAMETER135 = None
        ID136 = None
        char_literal137 = None
        string_literal138 = None
        char_literal139 = None
        char_literal141 = None
        char_literal143 = None
        typeArg140 = None

        parameterElement142 = None


        PARAMETER135_tree = None
        ID136_tree = None
        char_literal137_tree = None
        string_literal138_tree = None
        char_literal139_tree = None
        char_literal141_tree = None
        char_literal143_tree = None
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_PARAMETER = RewriteRuleTokenStream(self._adaptor, "token PARAMETER")
        stream_TYPE = RewriteRuleTokenStream(self._adaptor, "token TYPE")
        stream_typeArg = RewriteRuleSubtreeStream(self._adaptor, "rule typeArg")
        stream_parameterElement = RewriteRuleSubtreeStream(self._adaptor, "rule parameterElement")
        try:
            try:
                # GOC.g:145:2: ( PARAMETER ID '{' 'type' ':' typeArg ';' ( parameterElement )? '}' -> ^( PARAMETER ID typeArg ( parameterElement )? ) )
                # GOC.g:145:4: PARAMETER ID '{' 'type' ':' typeArg ';' ( parameterElement )? '}'
                pass 
                PARAMETER135=self.match(self.input, PARAMETER, self.FOLLOW_PARAMETER_in_constructorElement1136) 
                stream_PARAMETER.add(PARAMETER135)
                ID136=self.match(self.input, ID, self.FOLLOW_ID_in_constructorElement1138) 
                stream_ID.add(ID136)
                char_literal137=self.match(self.input, 56, self.FOLLOW_56_in_constructorElement1140) 
                stream_56.add(char_literal137)
                string_literal138=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_constructorElement1142) 
                stream_TYPE.add(string_literal138)
                char_literal139=self.match(self.input, 60, self.FOLLOW_60_in_constructorElement1144) 
                stream_60.add(char_literal139)
                self._state.following.append(self.FOLLOW_typeArg_in_constructorElement1146)
                typeArg140 = self.typeArg()

                self._state.following.pop()
                stream_typeArg.add(typeArg140.tree)
                char_literal141=self.match(self.input, 55, self.FOLLOW_55_in_constructorElement1148) 
                stream_55.add(char_literal141)
                # GOC.g:145:44: ( parameterElement )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == MODIFIERS) :
                    alt27 = 1
                elif (LA27_0 == 68) and ((self.classMember_stack[-1].with_constructor)):
                    alt27 = 1
                if alt27 == 1:
                    # GOC.g:145:44: parameterElement
                    pass 
                    self._state.following.append(self.FOLLOW_parameterElement_in_constructorElement1150)
                    parameterElement142 = self.parameterElement()

                    self._state.following.pop()
                    stream_parameterElement.add(parameterElement142.tree)



                char_literal143=self.match(self.input, 57, self.FOLLOW_57_in_constructorElement1153) 
                stream_57.add(char_literal143)

                # AST Rewrite
                # elements: typeArg, PARAMETER, ID, parameterElement
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
                # 146:2: -> ^( PARAMETER ID typeArg ( parameterElement )? )
                # GOC.g:146:5: ^( PARAMETER ID typeArg ( parameterElement )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_PARAMETER.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_ID.nextNode())
                self._adaptor.addChild(root_1, stream_typeArg.nextTree())
                # GOC.g:146:28: ( parameterElement )?
                if stream_parameterElement.hasNext():
                    self._adaptor.addChild(root_1, stream_parameterElement.nextTree())


                stream_parameterElement.reset();

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
    # GOC.g:149:1: parameterElement : ( modifiers | {...}? => 'bind_property' ':' ID ';' -> ^( BIND_PROPERTY ID ) );
    def parameterElement(self, ):

        retval = self.parameterElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal145 = None
        char_literal146 = None
        ID147 = None
        char_literal148 = None
        modifiers144 = None


        string_literal145_tree = None
        char_literal146_tree = None
        ID147_tree = None
        char_literal148_tree = None
        stream_68 = RewriteRuleTokenStream(self._adaptor, "token 68")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")

        try:
            try:
                # GOC.g:150:5: ( modifiers | {...}? => 'bind_property' ':' ID ';' -> ^( BIND_PROPERTY ID ) )
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == MODIFIERS) :
                    alt28 = 1
                elif (LA28_0 == 68) and ((self.classMember_stack[-1].with_constructor)):
                    alt28 = 2
                else:
                    nvae = NoViableAltException("", 28, 0, self.input)

                    raise nvae

                if alt28 == 1:
                    # GOC.g:150:9: modifiers
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_modifiers_in_parameterElement1183)
                    modifiers144 = self.modifiers()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, modifiers144.tree)


                elif alt28 == 2:
                    # GOC.g:151:9: {...}? => 'bind_property' ':' ID ';'
                    pass 
                    if not ((self.classMember_stack[-1].with_constructor)):
                        raise FailedPredicateException(self.input, "parameterElement", "$classMember::with_constructor")

                    string_literal145=self.match(self.input, 68, self.FOLLOW_68_in_parameterElement1196) 
                    stream_68.add(string_literal145)
                    char_literal146=self.match(self.input, 60, self.FOLLOW_60_in_parameterElement1198) 
                    stream_60.add(char_literal146)
                    ID147=self.match(self.input, ID, self.FOLLOW_ID_in_parameterElement1200) 
                    stream_ID.add(ID147)
                    char_literal148=self.match(self.input, 55, self.FOLLOW_55_in_parameterElement1202) 
                    stream_55.add(char_literal148)

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
                    # 151:72: -> ^( BIND_PROPERTY ID )
                    # GOC.g:151:75: ^( BIND_PROPERTY ID )
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

    class modifiers_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.modifiers_return, self).__init__()

            self.tree = None




    # $ANTLR start "modifiers"
    # GOC.g:154:1: modifiers : MODIFIERS ':' 'const' ';' -> ^( MODIFIERS 'const' ) ;
    def modifiers(self, ):

        retval = self.modifiers_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MODIFIERS149 = None
        char_literal150 = None
        string_literal151 = None
        char_literal152 = None

        MODIFIERS149_tree = None
        char_literal150_tree = None
        string_literal151_tree = None
        char_literal152_tree = None
        stream_MODIFIERS = RewriteRuleTokenStream(self._adaptor, "token MODIFIERS")
        stream_69 = RewriteRuleTokenStream(self._adaptor, "token 69")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")

        try:
            try:
                # GOC.g:155:2: ( MODIFIERS ':' 'const' ';' -> ^( MODIFIERS 'const' ) )
                # GOC.g:155:4: MODIFIERS ':' 'const' ';'
                pass 
                MODIFIERS149=self.match(self.input, MODIFIERS, self.FOLLOW_MODIFIERS_in_modifiers1224) 
                stream_MODIFIERS.add(MODIFIERS149)
                char_literal150=self.match(self.input, 60, self.FOLLOW_60_in_modifiers1226) 
                stream_60.add(char_literal150)
                string_literal151=self.match(self.input, 69, self.FOLLOW_69_in_modifiers1228) 
                stream_69.add(string_literal151)
                char_literal152=self.match(self.input, 55, self.FOLLOW_55_in_modifiers1230) 
                stream_55.add(char_literal152)

                # AST Rewrite
                # elements: 69, MODIFIERS
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
                # 155:30: -> ^( MODIFIERS 'const' )
                # GOC.g:155:33: ^( MODIFIERS 'const' )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_MODIFIERS.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_69.nextNode())

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
    # GOC.g:158:1: propertyElement : ( 'type' ':' (val= 'boolean' | val= 'integer' | val= 'double' | val= 'string' | val= 'pointer' | val= 'object' | val= 'enumeration' ) ';' -> ^( PROP_TYPE $val) | 'access' ':' (val= 'read-only' | val= 'initial-write' | val= 'read-write' ) ';' -> ^( PROP_ACCESS $val) | 'description' ':' STRING ';' -> ^( PROP_DESC STRING ) | 'gtype' ':' ID ';' -> ^( PROP_GTYPE ID ) | 'min' ':' STRING ';' -> ^( PROP_MIN STRING ) | 'max' ':' STRING ';' -> ^( PROP_MAX STRING ) | 'default' ':' STRING ';' -> ^( PROP_DEFAULT STRING ) | AUTO_CREATE ';' );
    def propertyElement(self, ):

        retval = self.propertyElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        val = None
        string_literal153 = None
        char_literal154 = None
        char_literal155 = None
        string_literal156 = None
        char_literal157 = None
        char_literal158 = None
        string_literal159 = None
        char_literal160 = None
        STRING161 = None
        char_literal162 = None
        string_literal163 = None
        char_literal164 = None
        ID165 = None
        char_literal166 = None
        string_literal167 = None
        char_literal168 = None
        STRING169 = None
        char_literal170 = None
        string_literal171 = None
        char_literal172 = None
        STRING173 = None
        char_literal174 = None
        string_literal175 = None
        char_literal176 = None
        STRING177 = None
        char_literal178 = None
        AUTO_CREATE179 = None
        char_literal180 = None

        val_tree = None
        string_literal153_tree = None
        char_literal154_tree = None
        char_literal155_tree = None
        string_literal156_tree = None
        char_literal157_tree = None
        char_literal158_tree = None
        string_literal159_tree = None
        char_literal160_tree = None
        STRING161_tree = None
        char_literal162_tree = None
        string_literal163_tree = None
        char_literal164_tree = None
        ID165_tree = None
        char_literal166_tree = None
        string_literal167_tree = None
        char_literal168_tree = None
        STRING169_tree = None
        char_literal170_tree = None
        string_literal171_tree = None
        char_literal172_tree = None
        STRING173_tree = None
        char_literal174_tree = None
        string_literal175_tree = None
        char_literal176_tree = None
        STRING177_tree = None
        char_literal178_tree = None
        AUTO_CREATE179_tree = None
        char_literal180_tree = None
        stream_79 = RewriteRuleTokenStream(self._adaptor, "token 79")
        stream_78 = RewriteRuleTokenStream(self._adaptor, "token 78")
        stream_77 = RewriteRuleTokenStream(self._adaptor, "token 77")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_GTYPE = RewriteRuleTokenStream(self._adaptor, "token GTYPE")
        stream_82 = RewriteRuleTokenStream(self._adaptor, "token 82")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_83 = RewriteRuleTokenStream(self._adaptor, "token 83")
        stream_70 = RewriteRuleTokenStream(self._adaptor, "token 70")
        stream_80 = RewriteRuleTokenStream(self._adaptor, "token 80")
        stream_71 = RewriteRuleTokenStream(self._adaptor, "token 71")
        stream_81 = RewriteRuleTokenStream(self._adaptor, "token 81")
        stream_72 = RewriteRuleTokenStream(self._adaptor, "token 72")
        stream_73 = RewriteRuleTokenStream(self._adaptor, "token 73")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_74 = RewriteRuleTokenStream(self._adaptor, "token 74")
        stream_84 = RewriteRuleTokenStream(self._adaptor, "token 84")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")
        stream_75 = RewriteRuleTokenStream(self._adaptor, "token 75")
        stream_TYPE = RewriteRuleTokenStream(self._adaptor, "token TYPE")
        stream_76 = RewriteRuleTokenStream(self._adaptor, "token 76")

        try:
            try:
                # GOC.g:159:5: ( 'type' ':' (val= 'boolean' | val= 'integer' | val= 'double' | val= 'string' | val= 'pointer' | val= 'object' | val= 'enumeration' ) ';' -> ^( PROP_TYPE $val) | 'access' ':' (val= 'read-only' | val= 'initial-write' | val= 'read-write' ) ';' -> ^( PROP_ACCESS $val) | 'description' ':' STRING ';' -> ^( PROP_DESC STRING ) | 'gtype' ':' ID ';' -> ^( PROP_GTYPE ID ) | 'min' ':' STRING ';' -> ^( PROP_MIN STRING ) | 'max' ':' STRING ';' -> ^( PROP_MAX STRING ) | 'default' ':' STRING ';' -> ^( PROP_DEFAULT STRING ) | AUTO_CREATE ';' )
                alt31 = 8
                LA31 = self.input.LA(1)
                if LA31 == TYPE:
                    alt31 = 1
                elif LA31 == 77:
                    alt31 = 2
                elif LA31 == 81:
                    alt31 = 3
                elif LA31 == GTYPE:
                    alt31 = 4
                elif LA31 == 82:
                    alt31 = 5
                elif LA31 == 83:
                    alt31 = 6
                elif LA31 == 84:
                    alt31 = 7
                elif LA31 == AUTO_CREATE:
                    alt31 = 8
                else:
                    nvae = NoViableAltException("", 31, 0, self.input)

                    raise nvae

                if alt31 == 1:
                    # GOC.g:159:9: 'type' ':' (val= 'boolean' | val= 'integer' | val= 'double' | val= 'string' | val= 'pointer' | val= 'object' | val= 'enumeration' ) ';'
                    pass 
                    string_literal153=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_propertyElement1254) 
                    stream_TYPE.add(string_literal153)
                    char_literal154=self.match(self.input, 60, self.FOLLOW_60_in_propertyElement1256) 
                    stream_60.add(char_literal154)
                    # GOC.g:159:20: (val= 'boolean' | val= 'integer' | val= 'double' | val= 'string' | val= 'pointer' | val= 'object' | val= 'enumeration' )
                    alt29 = 7
                    LA29 = self.input.LA(1)
                    if LA29 == 70:
                        alt29 = 1
                    elif LA29 == 71:
                        alt29 = 2
                    elif LA29 == 72:
                        alt29 = 3
                    elif LA29 == 73:
                        alt29 = 4
                    elif LA29 == 74:
                        alt29 = 5
                    elif LA29 == 75:
                        alt29 = 6
                    elif LA29 == 76:
                        alt29 = 7
                    else:
                        nvae = NoViableAltException("", 29, 0, self.input)

                        raise nvae

                    if alt29 == 1:
                        # GOC.g:159:21: val= 'boolean'
                        pass 
                        val=self.match(self.input, 70, self.FOLLOW_70_in_propertyElement1261) 
                        stream_70.add(val)


                    elif alt29 == 2:
                        # GOC.g:159:35: val= 'integer'
                        pass 
                        val=self.match(self.input, 71, self.FOLLOW_71_in_propertyElement1265) 
                        stream_71.add(val)


                    elif alt29 == 3:
                        # GOC.g:159:49: val= 'double'
                        pass 
                        val=self.match(self.input, 72, self.FOLLOW_72_in_propertyElement1269) 
                        stream_72.add(val)


                    elif alt29 == 4:
                        # GOC.g:160:5: val= 'string'
                        pass 
                        val=self.match(self.input, 73, self.FOLLOW_73_in_propertyElement1278) 
                        stream_73.add(val)


                    elif alt29 == 5:
                        # GOC.g:160:18: val= 'pointer'
                        pass 
                        val=self.match(self.input, 74, self.FOLLOW_74_in_propertyElement1282) 
                        stream_74.add(val)


                    elif alt29 == 6:
                        # GOC.g:160:32: val= 'object'
                        pass 
                        val=self.match(self.input, 75, self.FOLLOW_75_in_propertyElement1286) 
                        stream_75.add(val)


                    elif alt29 == 7:
                        # GOC.g:160:45: val= 'enumeration'
                        pass 
                        val=self.match(self.input, 76, self.FOLLOW_76_in_propertyElement1290) 
                        stream_76.add(val)



                    char_literal155=self.match(self.input, 55, self.FOLLOW_55_in_propertyElement1293) 
                    stream_55.add(char_literal155)

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
                    # 161:5: -> ^( PROP_TYPE $val)
                    # GOC.g:161:8: ^( PROP_TYPE $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_TYPE, "PROP_TYPE"), root_1)

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt31 == 2:
                    # GOC.g:162:9: 'access' ':' (val= 'read-only' | val= 'initial-write' | val= 'read-write' ) ';'
                    pass 
                    string_literal156=self.match(self.input, 77, self.FOLLOW_77_in_propertyElement1316) 
                    stream_77.add(string_literal156)
                    char_literal157=self.match(self.input, 60, self.FOLLOW_60_in_propertyElement1318) 
                    stream_60.add(char_literal157)
                    # GOC.g:162:22: (val= 'read-only' | val= 'initial-write' | val= 'read-write' )
                    alt30 = 3
                    LA30 = self.input.LA(1)
                    if LA30 == 78:
                        alt30 = 1
                    elif LA30 == 79:
                        alt30 = 2
                    elif LA30 == 80:
                        alt30 = 3
                    else:
                        nvae = NoViableAltException("", 30, 0, self.input)

                        raise nvae

                    if alt30 == 1:
                        # GOC.g:162:23: val= 'read-only'
                        pass 
                        val=self.match(self.input, 78, self.FOLLOW_78_in_propertyElement1323) 
                        stream_78.add(val)


                    elif alt30 == 2:
                        # GOC.g:162:39: val= 'initial-write'
                        pass 
                        val=self.match(self.input, 79, self.FOLLOW_79_in_propertyElement1327) 
                        stream_79.add(val)


                    elif alt30 == 3:
                        # GOC.g:162:59: val= 'read-write'
                        pass 
                        val=self.match(self.input, 80, self.FOLLOW_80_in_propertyElement1331) 
                        stream_80.add(val)



                    char_literal158=self.match(self.input, 55, self.FOLLOW_55_in_propertyElement1334) 
                    stream_55.add(char_literal158)

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
                    # 163:5: -> ^( PROP_ACCESS $val)
                    # GOC.g:163:8: ^( PROP_ACCESS $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_ACCESS, "PROP_ACCESS"), root_1)

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt31 == 3:
                    # GOC.g:164:9: 'description' ':' STRING ';'
                    pass 
                    string_literal159=self.match(self.input, 81, self.FOLLOW_81_in_propertyElement1357) 
                    stream_81.add(string_literal159)
                    char_literal160=self.match(self.input, 60, self.FOLLOW_60_in_propertyElement1359) 
                    stream_60.add(char_literal160)
                    STRING161=self.match(self.input, STRING, self.FOLLOW_STRING_in_propertyElement1361) 
                    stream_STRING.add(STRING161)
                    char_literal162=self.match(self.input, 55, self.FOLLOW_55_in_propertyElement1363) 
                    stream_55.add(char_literal162)

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
                    # 164:38: -> ^( PROP_DESC STRING )
                    # GOC.g:164:41: ^( PROP_DESC STRING )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_DESC, "PROP_DESC"), root_1)

                    self._adaptor.addChild(root_1, stream_STRING.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt31 == 4:
                    # GOC.g:165:9: 'gtype' ':' ID ';'
                    pass 
                    string_literal163=self.match(self.input, GTYPE, self.FOLLOW_GTYPE_in_propertyElement1381) 
                    stream_GTYPE.add(string_literal163)
                    char_literal164=self.match(self.input, 60, self.FOLLOW_60_in_propertyElement1383) 
                    stream_60.add(char_literal164)
                    ID165=self.match(self.input, ID, self.FOLLOW_ID_in_propertyElement1385) 
                    stream_ID.add(ID165)
                    char_literal166=self.match(self.input, 55, self.FOLLOW_55_in_propertyElement1387) 
                    stream_55.add(char_literal166)

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
                    # 166:5: -> ^( PROP_GTYPE ID )
                    # GOC.g:166:8: ^( PROP_GTYPE ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_GTYPE, "PROP_GTYPE"), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt31 == 5:
                    # GOC.g:167:9: 'min' ':' STRING ';'
                    pass 
                    string_literal167=self.match(self.input, 82, self.FOLLOW_82_in_propertyElement1409) 
                    stream_82.add(string_literal167)
                    char_literal168=self.match(self.input, 60, self.FOLLOW_60_in_propertyElement1411) 
                    stream_60.add(char_literal168)
                    STRING169=self.match(self.input, STRING, self.FOLLOW_STRING_in_propertyElement1413) 
                    stream_STRING.add(STRING169)
                    char_literal170=self.match(self.input, 55, self.FOLLOW_55_in_propertyElement1415) 
                    stream_55.add(char_literal170)

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
                    # 167:30: -> ^( PROP_MIN STRING )
                    # GOC.g:167:33: ^( PROP_MIN STRING )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_MIN, "PROP_MIN"), root_1)

                    self._adaptor.addChild(root_1, stream_STRING.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt31 == 6:
                    # GOC.g:168:9: 'max' ':' STRING ';'
                    pass 
                    string_literal171=self.match(self.input, 83, self.FOLLOW_83_in_propertyElement1433) 
                    stream_83.add(string_literal171)
                    char_literal172=self.match(self.input, 60, self.FOLLOW_60_in_propertyElement1435) 
                    stream_60.add(char_literal172)
                    STRING173=self.match(self.input, STRING, self.FOLLOW_STRING_in_propertyElement1437) 
                    stream_STRING.add(STRING173)
                    char_literal174=self.match(self.input, 55, self.FOLLOW_55_in_propertyElement1439) 
                    stream_55.add(char_literal174)

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
                    # 168:30: -> ^( PROP_MAX STRING )
                    # GOC.g:168:33: ^( PROP_MAX STRING )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_MAX, "PROP_MAX"), root_1)

                    self._adaptor.addChild(root_1, stream_STRING.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt31 == 7:
                    # GOC.g:169:9: 'default' ':' STRING ';'
                    pass 
                    string_literal175=self.match(self.input, 84, self.FOLLOW_84_in_propertyElement1457) 
                    stream_84.add(string_literal175)
                    char_literal176=self.match(self.input, 60, self.FOLLOW_60_in_propertyElement1459) 
                    stream_60.add(char_literal176)
                    STRING177=self.match(self.input, STRING, self.FOLLOW_STRING_in_propertyElement1461) 
                    stream_STRING.add(STRING177)
                    char_literal178=self.match(self.input, 55, self.FOLLOW_55_in_propertyElement1463) 
                    stream_55.add(char_literal178)

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
                    # 169:34: -> ^( PROP_DEFAULT STRING )
                    # GOC.g:169:37: ^( PROP_DEFAULT STRING )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROP_DEFAULT, "PROP_DEFAULT"), root_1)

                    self._adaptor.addChild(root_1, stream_STRING.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt31 == 8:
                    # GOC.g:170:9: AUTO_CREATE ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    AUTO_CREATE179=self.match(self.input, AUTO_CREATE, self.FOLLOW_AUTO_CREATE_in_propertyElement1481)

                    AUTO_CREATE179_tree = self._adaptor.createWithPayload(AUTO_CREATE179)
                    root_0 = self._adaptor.becomeRoot(AUTO_CREATE179_tree, root_0)

                    char_literal180=self.match(self.input, 55, self.FOLLOW_55_in_propertyElement1484)

                    char_literal180_tree = self._adaptor.createWithPayload(char_literal180)
                    self._adaptor.addChild(root_0, char_literal180_tree)



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
    # GOC.g:173:1: signalElement : ( RESULT '{' 'type' ':' signalType ';' '}' -> ^( RESULT signalType ) | PARAMETER ID '{' 'type' ':' signalType ';' '}' -> ^( PARAMETER ID signalType ) );
    def signalElement(self, ):

        retval = self.signalElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RESULT181 = None
        char_literal182 = None
        string_literal183 = None
        char_literal184 = None
        char_literal186 = None
        char_literal187 = None
        PARAMETER188 = None
        ID189 = None
        char_literal190 = None
        string_literal191 = None
        char_literal192 = None
        char_literal194 = None
        char_literal195 = None
        signalType185 = None

        signalType193 = None


        RESULT181_tree = None
        char_literal182_tree = None
        string_literal183_tree = None
        char_literal184_tree = None
        char_literal186_tree = None
        char_literal187_tree = None
        PARAMETER188_tree = None
        ID189_tree = None
        char_literal190_tree = None
        string_literal191_tree = None
        char_literal192_tree = None
        char_literal194_tree = None
        char_literal195_tree = None
        stream_RESULT = RewriteRuleTokenStream(self._adaptor, "token RESULT")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_PARAMETER = RewriteRuleTokenStream(self._adaptor, "token PARAMETER")
        stream_TYPE = RewriteRuleTokenStream(self._adaptor, "token TYPE")
        stream_signalType = RewriteRuleSubtreeStream(self._adaptor, "rule signalType")
        try:
            try:
                # GOC.g:174:5: ( RESULT '{' 'type' ':' signalType ';' '}' -> ^( RESULT signalType ) | PARAMETER ID '{' 'type' ':' signalType ';' '}' -> ^( PARAMETER ID signalType ) )
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == RESULT) :
                    alt32 = 1
                elif (LA32_0 == PARAMETER) :
                    alt32 = 2
                else:
                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae

                if alt32 == 1:
                    # GOC.g:174:9: RESULT '{' 'type' ':' signalType ';' '}'
                    pass 
                    RESULT181=self.match(self.input, RESULT, self.FOLLOW_RESULT_in_signalElement1503) 
                    stream_RESULT.add(RESULT181)
                    char_literal182=self.match(self.input, 56, self.FOLLOW_56_in_signalElement1505) 
                    stream_56.add(char_literal182)
                    string_literal183=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_signalElement1507) 
                    stream_TYPE.add(string_literal183)
                    char_literal184=self.match(self.input, 60, self.FOLLOW_60_in_signalElement1509) 
                    stream_60.add(char_literal184)
                    self._state.following.append(self.FOLLOW_signalType_in_signalElement1511)
                    signalType185 = self.signalType()

                    self._state.following.pop()
                    stream_signalType.add(signalType185.tree)
                    char_literal186=self.match(self.input, 55, self.FOLLOW_55_in_signalElement1513) 
                    stream_55.add(char_literal186)
                    char_literal187=self.match(self.input, 57, self.FOLLOW_57_in_signalElement1515) 
                    stream_57.add(char_literal187)

                    # AST Rewrite
                    # elements: signalType, RESULT
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
                    # 174:50: -> ^( RESULT signalType )
                    # GOC.g:174:53: ^( RESULT signalType )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_RESULT.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_signalType.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt32 == 2:
                    # GOC.g:175:9: PARAMETER ID '{' 'type' ':' signalType ';' '}'
                    pass 
                    PARAMETER188=self.match(self.input, PARAMETER, self.FOLLOW_PARAMETER_in_signalElement1533) 
                    stream_PARAMETER.add(PARAMETER188)
                    ID189=self.match(self.input, ID, self.FOLLOW_ID_in_signalElement1535) 
                    stream_ID.add(ID189)
                    char_literal190=self.match(self.input, 56, self.FOLLOW_56_in_signalElement1537) 
                    stream_56.add(char_literal190)
                    string_literal191=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_signalElement1539) 
                    stream_TYPE.add(string_literal191)
                    char_literal192=self.match(self.input, 60, self.FOLLOW_60_in_signalElement1541) 
                    stream_60.add(char_literal192)
                    self._state.following.append(self.FOLLOW_signalType_in_signalElement1543)
                    signalType193 = self.signalType()

                    self._state.following.pop()
                    stream_signalType.add(signalType193.tree)
                    char_literal194=self.match(self.input, 55, self.FOLLOW_55_in_signalElement1545) 
                    stream_55.add(char_literal194)
                    char_literal195=self.match(self.input, 57, self.FOLLOW_57_in_signalElement1547) 
                    stream_57.add(char_literal195)

                    # AST Rewrite
                    # elements: ID, signalType, PARAMETER
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
                    # 175:56: -> ^( PARAMETER ID signalType )
                    # GOC.g:175:59: ^( PARAMETER ID signalType )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_PARAMETER.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())
                    self._adaptor.addChild(root_1, stream_signalType.nextTree())

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

    class signalType_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.signalType_return, self).__init__()

            self.tree = None




    # $ANTLR start "signalType"
    # GOC.g:178:1: signalType : ( 'null' | 'integer' | 'boolean' | 'float' | 'double' | 'string' | 'object' | 'enumeration' );
    def signalType(self, ):

        retval = self.signalType_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set196 = None

        set196_tree = None

        try:
            try:
                # GOC.g:179:5: ( 'null' | 'integer' | 'boolean' | 'float' | 'double' | 'string' | 'object' | 'enumeration' )
                # GOC.g:
                pass 
                root_0 = self._adaptor.nil()

                set196 = self.input.LT(1)
                if (70 <= self.input.LA(1) <= 73) or (75 <= self.input.LA(1) <= 76) or (85 <= self.input.LA(1) <= 86):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set196))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





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

    # $ANTLR end "signalType"

    class attributeElement_return(ParserRuleReturnScope):
        def __init__(self):
            super(GOCParser.attributeElement_return, self).__init__()

            self.tree = None




    # $ANTLR start "attributeElement"
    # GOC.g:189:1: attributeElement : ( SCOPE ':' (val= 'static' | val= 'instance' ) ';' -> ^( SCOPE $val) | VISIBILITY ':' (val= 'public' | val= 'protected' | val= 'private' ) ';' -> ^( VISIBILITY $val) );
    def attributeElement(self, ):

        retval = self.attributeElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        val = None
        SCOPE197 = None
        char_literal198 = None
        char_literal199 = None
        VISIBILITY200 = None
        char_literal201 = None
        char_literal202 = None

        val_tree = None
        SCOPE197_tree = None
        char_literal198_tree = None
        char_literal199_tree = None
        VISIBILITY200_tree = None
        char_literal201_tree = None
        char_literal202_tree = None
        stream_VISIBILITY = RewriteRuleTokenStream(self._adaptor, "token VISIBILITY")
        stream_SCOPE = RewriteRuleTokenStream(self._adaptor, "token SCOPE")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_64 = RewriteRuleTokenStream(self._adaptor, "token 64")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_63 = RewriteRuleTokenStream(self._adaptor, "token 63")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_61 = RewriteRuleTokenStream(self._adaptor, "token 61")

        try:
            try:
                # GOC.g:190:2: ( SCOPE ':' (val= 'static' | val= 'instance' ) ';' -> ^( SCOPE $val) | VISIBILITY ':' (val= 'public' | val= 'protected' | val= 'private' ) ';' -> ^( VISIBILITY $val) )
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == SCOPE) :
                    alt35 = 1
                elif (LA35_0 == VISIBILITY) :
                    alt35 = 2
                else:
                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae

                if alt35 == 1:
                    # GOC.g:190:4: SCOPE ':' (val= 'static' | val= 'instance' ) ';'
                    pass 
                    SCOPE197=self.match(self.input, SCOPE, self.FOLLOW_SCOPE_in_attributeElement1660) 
                    stream_SCOPE.add(SCOPE197)
                    char_literal198=self.match(self.input, 60, self.FOLLOW_60_in_attributeElement1662) 
                    stream_60.add(char_literal198)
                    # GOC.g:190:14: (val= 'static' | val= 'instance' )
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == 65) :
                        alt33 = 1
                    elif (LA33_0 == 64) :
                        alt33 = 2
                    else:
                        nvae = NoViableAltException("", 33, 0, self.input)

                        raise nvae

                    if alt33 == 1:
                        # GOC.g:190:15: val= 'static'
                        pass 
                        val=self.match(self.input, 65, self.FOLLOW_65_in_attributeElement1667) 
                        stream_65.add(val)


                    elif alt33 == 2:
                        # GOC.g:190:28: val= 'instance'
                        pass 
                        val=self.match(self.input, 64, self.FOLLOW_64_in_attributeElement1671) 
                        stream_64.add(val)



                    char_literal199=self.match(self.input, 55, self.FOLLOW_55_in_attributeElement1674) 
                    stream_55.add(char_literal199)

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
                    # 190:48: -> ^( SCOPE $val)
                    # GOC.g:190:51: ^( SCOPE $val)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_SCOPE.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_val.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt35 == 2:
                    # GOC.g:191:4: VISIBILITY ':' (val= 'public' | val= 'protected' | val= 'private' ) ';'
                    pass 
                    VISIBILITY200=self.match(self.input, VISIBILITY, self.FOLLOW_VISIBILITY_in_attributeElement1688) 
                    stream_VISIBILITY.add(VISIBILITY200)
                    char_literal201=self.match(self.input, 60, self.FOLLOW_60_in_attributeElement1690) 
                    stream_60.add(char_literal201)
                    # GOC.g:191:19: (val= 'public' | val= 'protected' | val= 'private' )
                    alt34 = 3
                    LA34 = self.input.LA(1)
                    if LA34 == 61:
                        alt34 = 1
                    elif LA34 == 62:
                        alt34 = 2
                    elif LA34 == 63:
                        alt34 = 3
                    else:
                        nvae = NoViableAltException("", 34, 0, self.input)

                        raise nvae

                    if alt34 == 1:
                        # GOC.g:191:20: val= 'public'
                        pass 
                        val=self.match(self.input, 61, self.FOLLOW_61_in_attributeElement1695) 
                        stream_61.add(val)


                    elif alt34 == 2:
                        # GOC.g:191:33: val= 'protected'
                        pass 
                        val=self.match(self.input, 62, self.FOLLOW_62_in_attributeElement1699) 
                        stream_62.add(val)


                    elif alt34 == 3:
                        # GOC.g:191:49: val= 'private'
                        pass 
                        val=self.match(self.input, 63, self.FOLLOW_63_in_attributeElement1703) 
                        stream_63.add(val)



                    char_literal202=self.match(self.input, 55, self.FOLLOW_55_in_attributeElement1706) 
                    stream_55.add(char_literal202)

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
                    # 191:68: -> ^( VISIBILITY $val)
                    # GOC.g:191:71: ^( VISIBILITY $val)
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
    # GOC.g:194:1: typeName : ( typePath -> ^( TYPE_NAME typePath ) | ( 'unsigned ' )? 'integer' -> ^( TYPE_NAME ( 'unsigned ' )? 'integer' ) | ( 'unsigned ' )? 'long' -> ^( TYPE_NAME ( 'unsigned ' )? 'long' ) | (val= 'boolean' | val= 'string' | val= 'float' | val= 'double' | val= 'pointer' ) -> ^( TYPE_NAME $val) );
    def typeName(self, ):

        retval = self.typeName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        val = None
        string_literal204 = None
        string_literal205 = None
        string_literal206 = None
        string_literal207 = None
        typePath203 = None


        val_tree = None
        string_literal204_tree = None
        string_literal205_tree = None
        string_literal206_tree = None
        string_literal207_tree = None
        stream_70 = RewriteRuleTokenStream(self._adaptor, "token 70")
        stream_71 = RewriteRuleTokenStream(self._adaptor, "token 71")
        stream_72 = RewriteRuleTokenStream(self._adaptor, "token 72")
        stream_73 = RewriteRuleTokenStream(self._adaptor, "token 73")
        stream_86 = RewriteRuleTokenStream(self._adaptor, "token 86")
        stream_74 = RewriteRuleTokenStream(self._adaptor, "token 74")
        stream_87 = RewriteRuleTokenStream(self._adaptor, "token 87")
        stream_88 = RewriteRuleTokenStream(self._adaptor, "token 88")
        stream_typePath = RewriteRuleSubtreeStream(self._adaptor, "rule typePath")
        try:
            try:
                # GOC.g:195:2: ( typePath -> ^( TYPE_NAME typePath ) | ( 'unsigned ' )? 'integer' -> ^( TYPE_NAME ( 'unsigned ' )? 'integer' ) | ( 'unsigned ' )? 'long' -> ^( TYPE_NAME ( 'unsigned ' )? 'long' ) | (val= 'boolean' | val= 'string' | val= 'float' | val= 'double' | val= 'pointer' ) -> ^( TYPE_NAME $val) )
                alt39 = 4
                LA39 = self.input.LA(1)
                if LA39 == ID or LA39 == 93:
                    alt39 = 1
                elif LA39 == 87:
                    LA39_2 = self.input.LA(2)

                    if (LA39_2 == 71) :
                        alt39 = 2
                    elif (LA39_2 == 88) :
                        alt39 = 3
                    else:
                        nvae = NoViableAltException("", 39, 2, self.input)

                        raise nvae

                elif LA39 == 71:
                    alt39 = 2
                elif LA39 == 88:
                    alt39 = 3
                elif LA39 == 70 or LA39 == 72 or LA39 == 73 or LA39 == 74 or LA39 == 86:
                    alt39 = 4
                else:
                    nvae = NoViableAltException("", 39, 0, self.input)

                    raise nvae

                if alt39 == 1:
                    # GOC.g:195:6: typePath
                    pass 
                    self._state.following.append(self.FOLLOW_typePath_in_typeName1728)
                    typePath203 = self.typePath()

                    self._state.following.pop()
                    stream_typePath.add(typePath203.tree)

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
                    # 195:15: -> ^( TYPE_NAME typePath )
                    # GOC.g:195:18: ^( TYPE_NAME typePath )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE_NAME, "TYPE_NAME"), root_1)

                    self._adaptor.addChild(root_1, stream_typePath.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt39 == 2:
                    # GOC.g:196:6: ( 'unsigned ' )? 'integer'
                    pass 
                    # GOC.g:196:6: ( 'unsigned ' )?
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == 87) :
                        alt36 = 1
                    if alt36 == 1:
                        # GOC.g:196:6: 'unsigned '
                        pass 
                        string_literal204=self.match(self.input, 87, self.FOLLOW_87_in_typeName1743) 
                        stream_87.add(string_literal204)



                    string_literal205=self.match(self.input, 71, self.FOLLOW_71_in_typeName1746) 
                    stream_71.add(string_literal205)

                    # AST Rewrite
                    # elements: 71, 87
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
                    # 196:29: -> ^( TYPE_NAME ( 'unsigned ' )? 'integer' )
                    # GOC.g:196:32: ^( TYPE_NAME ( 'unsigned ' )? 'integer' )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE_NAME, "TYPE_NAME"), root_1)

                    # GOC.g:196:44: ( 'unsigned ' )?
                    if stream_87.hasNext():
                        self._adaptor.addChild(root_1, stream_87.nextNode())


                    stream_87.reset();
                    self._adaptor.addChild(root_1, stream_71.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt39 == 3:
                    # GOC.g:197:6: ( 'unsigned ' )? 'long'
                    pass 
                    # GOC.g:197:6: ( 'unsigned ' )?
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == 87) :
                        alt37 = 1
                    if alt37 == 1:
                        # GOC.g:197:6: 'unsigned '
                        pass 
                        string_literal206=self.match(self.input, 87, self.FOLLOW_87_in_typeName1764) 
                        stream_87.add(string_literal206)



                    string_literal207=self.match(self.input, 88, self.FOLLOW_88_in_typeName1767) 
                    stream_88.add(string_literal207)

                    # AST Rewrite
                    # elements: 87, 88
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
                    # 197:26: -> ^( TYPE_NAME ( 'unsigned ' )? 'long' )
                    # GOC.g:197:29: ^( TYPE_NAME ( 'unsigned ' )? 'long' )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE_NAME, "TYPE_NAME"), root_1)

                    # GOC.g:197:41: ( 'unsigned ' )?
                    if stream_87.hasNext():
                        self._adaptor.addChild(root_1, stream_87.nextNode())


                    stream_87.reset();
                    self._adaptor.addChild(root_1, stream_88.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt39 == 4:
                    # GOC.g:198:4: (val= 'boolean' | val= 'string' | val= 'float' | val= 'double' | val= 'pointer' )
                    pass 
                    # GOC.g:198:4: (val= 'boolean' | val= 'string' | val= 'float' | val= 'double' | val= 'pointer' )
                    alt38 = 5
                    LA38 = self.input.LA(1)
                    if LA38 == 70:
                        alt38 = 1
                    elif LA38 == 73:
                        alt38 = 2
                    elif LA38 == 86:
                        alt38 = 3
                    elif LA38 == 72:
                        alt38 = 4
                    elif LA38 == 74:
                        alt38 = 5
                    else:
                        nvae = NoViableAltException("", 38, 0, self.input)

                        raise nvae

                    if alt38 == 1:
                        # GOC.g:198:5: val= 'boolean'
                        pass 
                        val=self.match(self.input, 70, self.FOLLOW_70_in_typeName1786) 
                        stream_70.add(val)


                    elif alt38 == 2:
                        # GOC.g:199:4: val= 'string'
                        pass 
                        val=self.match(self.input, 73, self.FOLLOW_73_in_typeName1793) 
                        stream_73.add(val)


                    elif alt38 == 3:
                        # GOC.g:200:4: val= 'float'
                        pass 
                        val=self.match(self.input, 86, self.FOLLOW_86_in_typeName1800) 
                        stream_86.add(val)


                    elif alt38 == 4:
                        # GOC.g:201:4: val= 'double'
                        pass 
                        val=self.match(self.input, 72, self.FOLLOW_72_in_typeName1807) 
                        stream_72.add(val)


                    elif alt38 == 5:
                        # GOC.g:202:6: val= 'pointer'
                        pass 
                        val=self.match(self.input, 74, self.FOLLOW_74_in_typeName1816) 
                        stream_74.add(val)




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
                    # 202:21: -> ^( TYPE_NAME $val)
                    # GOC.g:202:24: ^( TYPE_NAME $val)
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
    # GOC.g:205:1: typeArg : ( typeName | 'ref' '(' typeArg ')' -> ^( REF_TO typeArg ) | 'list' '(' typeArg ')' -> ^( LIST_OF typeArg ) );
    def typeArg(self, ):

        retval = self.typeArg_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal209 = None
        char_literal210 = None
        char_literal212 = None
        string_literal213 = None
        char_literal214 = None
        char_literal216 = None
        typeName208 = None

        typeArg211 = None

        typeArg215 = None


        string_literal209_tree = None
        char_literal210_tree = None
        char_literal212_tree = None
        string_literal213_tree = None
        char_literal214_tree = None
        char_literal216_tree = None
        stream_92 = RewriteRuleTokenStream(self._adaptor, "token 92")
        stream_91 = RewriteRuleTokenStream(self._adaptor, "token 91")
        stream_90 = RewriteRuleTokenStream(self._adaptor, "token 90")
        stream_89 = RewriteRuleTokenStream(self._adaptor, "token 89")
        stream_typeArg = RewriteRuleSubtreeStream(self._adaptor, "rule typeArg")
        try:
            try:
                # GOC.g:206:5: ( typeName | 'ref' '(' typeArg ')' -> ^( REF_TO typeArg ) | 'list' '(' typeArg ')' -> ^( LIST_OF typeArg ) )
                alt40 = 3
                LA40 = self.input.LA(1)
                if LA40 == ID or LA40 == 70 or LA40 == 71 or LA40 == 72 or LA40 == 73 or LA40 == 74 or LA40 == 86 or LA40 == 87 or LA40 == 88 or LA40 == 93:
                    alt40 = 1
                elif LA40 == 89:
                    alt40 = 2
                elif LA40 == 92:
                    alt40 = 3
                else:
                    nvae = NoViableAltException("", 40, 0, self.input)

                    raise nvae

                if alt40 == 1:
                    # GOC.g:206:9: typeName
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_typeName_in_typeArg1842)
                    typeName208 = self.typeName()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, typeName208.tree)


                elif alt40 == 2:
                    # GOC.g:207:9: 'ref' '(' typeArg ')'
                    pass 
                    string_literal209=self.match(self.input, 89, self.FOLLOW_89_in_typeArg1852) 
                    stream_89.add(string_literal209)
                    char_literal210=self.match(self.input, 90, self.FOLLOW_90_in_typeArg1854) 
                    stream_90.add(char_literal210)
                    self._state.following.append(self.FOLLOW_typeArg_in_typeArg1856)
                    typeArg211 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg211.tree)
                    char_literal212=self.match(self.input, 91, self.FOLLOW_91_in_typeArg1858) 
                    stream_91.add(char_literal212)

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
                    # 207:31: -> ^( REF_TO typeArg )
                    # GOC.g:207:34: ^( REF_TO typeArg )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(REF_TO, "REF_TO"), root_1)

                    self._adaptor.addChild(root_1, stream_typeArg.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt40 == 3:
                    # GOC.g:208:9: 'list' '(' typeArg ')'
                    pass 
                    string_literal213=self.match(self.input, 92, self.FOLLOW_92_in_typeArg1876) 
                    stream_92.add(string_literal213)
                    char_literal214=self.match(self.input, 90, self.FOLLOW_90_in_typeArg1878) 
                    stream_90.add(char_literal214)
                    self._state.following.append(self.FOLLOW_typeArg_in_typeArg1880)
                    typeArg215 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg215.tree)
                    char_literal216=self.match(self.input, 91, self.FOLLOW_91_in_typeArg1882) 
                    stream_91.add(char_literal216)

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
                    # 208:32: -> ^( LIST_OF typeArg )
                    # GOC.g:208:35: ^( LIST_OF typeArg )
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
    # GOC.g:211:1: typePath : ( '::' ID '::' )? ( ID '::' )* ID ;
    def typePath(self, ):

        retval = self.typePath_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal217 = None
        ID218 = None
        string_literal219 = None
        ID220 = None
        string_literal221 = None
        ID222 = None

        string_literal217_tree = None
        ID218_tree = None
        string_literal219_tree = None
        ID220_tree = None
        string_literal221_tree = None
        ID222_tree = None

        try:
            try:
                # GOC.g:212:5: ( ( '::' ID '::' )? ( ID '::' )* ID )
                # GOC.g:212:9: ( '::' ID '::' )? ( ID '::' )* ID
                pass 
                root_0 = self._adaptor.nil()

                # GOC.g:212:9: ( '::' ID '::' )?
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if (LA41_0 == 93) :
                    alt41 = 1
                if alt41 == 1:
                    # GOC.g:212:10: '::' ID '::'
                    pass 
                    string_literal217=self.match(self.input, 93, self.FOLLOW_93_in_typePath1910)

                    string_literal217_tree = self._adaptor.createWithPayload(string_literal217)
                    self._adaptor.addChild(root_0, string_literal217_tree)

                    ID218=self.match(self.input, ID, self.FOLLOW_ID_in_typePath1912)

                    ID218_tree = self._adaptor.createWithPayload(ID218)
                    self._adaptor.addChild(root_0, ID218_tree)

                    string_literal219=self.match(self.input, 93, self.FOLLOW_93_in_typePath1914)

                    string_literal219_tree = self._adaptor.createWithPayload(string_literal219)
                    self._adaptor.addChild(root_0, string_literal219_tree)




                # GOC.g:212:24: ( ID '::' )*
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 == ID) :
                        LA42_1 = self.input.LA(2)

                        if (LA42_1 == 93) :
                            alt42 = 1




                    if alt42 == 1:
                        # GOC.g:212:25: ID '::'
                        pass 
                        ID220=self.match(self.input, ID, self.FOLLOW_ID_in_typePath1918)

                        ID220_tree = self._adaptor.createWithPayload(ID220)
                        self._adaptor.addChild(root_0, ID220_tree)

                        string_literal221=self.match(self.input, 93, self.FOLLOW_93_in_typePath1920)

                        string_literal221_tree = self._adaptor.createWithPayload(string_literal221)
                        self._adaptor.addChild(root_0, string_literal221_tree)



                    else:
                        break #loop42
                ID222=self.match(self.input, ID, self.FOLLOW_ID_in_typePath1924)

                ID222_tree = self._adaptor.createWithPayload(ID222)
                self._adaptor.addChild(root_0, ID222_tree)




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
    # GOC.g:333:1: signalID : part1= ID ( '-' part2+= ID )* -> ^( SIGNAL_ID $part1 ( $part2)* ) ;
    def signalID(self, ):

        retval = self.signalID_return()
        retval.start = self.input.LT(1)

        root_0 = None

        part1 = None
        char_literal223 = None
        part2 = None
        list_part2 = None

        part1_tree = None
        char_literal223_tree = None
        part2_tree = None
        stream_94 = RewriteRuleTokenStream(self._adaptor, "token 94")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # GOC.g:334:5: (part1= ID ( '-' part2+= ID )* -> ^( SIGNAL_ID $part1 ( $part2)* ) )
                # GOC.g:334:9: part1= ID ( '-' part2+= ID )*
                pass 
                part1=self.match(self.input, ID, self.FOLLOW_ID_in_signalID2489) 
                stream_ID.add(part1)
                # GOC.g:334:18: ( '-' part2+= ID )*
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if (LA43_0 == 94) :
                        alt43 = 1


                    if alt43 == 1:
                        # GOC.g:334:19: '-' part2+= ID
                        pass 
                        char_literal223=self.match(self.input, 94, self.FOLLOW_94_in_signalID2492) 
                        stream_94.add(char_literal223)
                        part2=self.match(self.input, ID, self.FOLLOW_ID_in_signalID2496) 
                        stream_ID.add(part2)
                        if list_part2 is None:
                            list_part2 = []
                        list_part2.append(part2)



                    else:
                        break #loop43

                # AST Rewrite
                # elements: part2, part1
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
                # 334:35: -> ^( SIGNAL_ID $part1 ( $part2)* )
                # GOC.g:334:38: ^( SIGNAL_ID $part1 ( $part2)* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(SIGNAL_ID, "SIGNAL_ID"), root_1)

                self._adaptor.addChild(root_1, stream_part1.nextNode())
                # GOC.g:334:57: ( $part2)*
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


 

    FOLLOW_stmt_in_defFile143 = frozenset([1, 21, 22, 23, 24, 26, 27, 49, 54])
    FOLLOW_classDef_in_stmt165 = frozenset([1])
    FOLLOW_intfDef_in_stmt170 = frozenset([1])
    FOLLOW_errorDomainDef_in_stmt177 = frozenset([1])
    FOLLOW_enumDef_in_stmt184 = frozenset([1])
    FOLLOW_flagsDef_in_stmt191 = frozenset([1])
    FOLLOW_packageDef_in_stmt196 = frozenset([1])
    FOLLOW_typeDecl_in_stmt203 = frozenset([1])
    FOLLOW_includeStmt_in_stmt210 = frozenset([1])
    FOLLOW_54_in_includeStmt226 = frozenset([19])
    FOLLOW_STRING_in_includeStmt230 = frozenset([55])
    FOLLOW_55_in_includeStmt232 = frozenset([1])
    FOLLOW_PACKAGE_in_packageDef255 = frozenset([20])
    FOLLOW_ID_in_packageDef257 = frozenset([56])
    FOLLOW_56_in_packageDef259 = frozenset([21, 22, 27, 49, 57])
    FOLLOW_packageElement_in_packageDef261 = frozenset([21, 22, 27, 49, 57])
    FOLLOW_57_in_packageDef264 = frozenset([1])
    FOLLOW_packageDef_in_packageElement289 = frozenset([1])
    FOLLOW_classDef_in_packageElement294 = frozenset([1])
    FOLLOW_intfDef_in_packageElement299 = frozenset([1])
    FOLLOW_typeDecl_in_packageElement306 = frozenset([1])
    FOLLOW_GOBJECT_in_classDef317 = frozenset([20])
    FOLLOW_ID_in_classDef321 = frozenset([55, 56])
    FOLLOW_56_in_classDef324 = frozenset([28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 57])
    FOLLOW_classMember_in_classDef326 = frozenset([28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 57])
    FOLLOW_57_in_classDef329 = frozenset([1])
    FOLLOW_55_in_classDef331 = frozenset([1])
    FOLLOW_GINTERFACE_in_intfDef358 = frozenset([20])
    FOLLOW_ID_in_intfDef362 = frozenset([55, 56])
    FOLLOW_56_in_intfDef365 = frozenset([33, 38, 57])
    FOLLOW_intfMember_in_intfDef367 = frozenset([33, 38, 57])
    FOLLOW_57_in_intfDef370 = frozenset([1])
    FOLLOW_55_in_intfDef372 = frozenset([1])
    FOLLOW_ERROR_DOMAIN_in_errorDomainDef403 = frozenset([20])
    FOLLOW_ID_in_errorDomainDef405 = frozenset([56])
    FOLLOW_56_in_errorDomainDef407 = frozenset([58])
    FOLLOW_errorDomainElement_in_errorDomainDef409 = frozenset([57, 58])
    FOLLOW_57_in_errorDomainDef412 = frozenset([1])
    FOLLOW_58_in_errorDomainElement447 = frozenset([20])
    FOLLOW_ID_in_errorDomainElement449 = frozenset([55])
    FOLLOW_55_in_errorDomainElement451 = frozenset([1])
    FOLLOW_ENUMERATION_in_enumDef476 = frozenset([20])
    FOLLOW_ID_in_enumDef478 = frozenset([56])
    FOLLOW_56_in_enumDef480 = frozenset([58])
    FOLLOW_enumElement_in_enumDef482 = frozenset([57, 58])
    FOLLOW_57_in_enumDef485 = frozenset([1])
    FOLLOW_58_in_enumElement520 = frozenset([20])
    FOLLOW_ID_in_enumElement522 = frozenset([55, 56])
    FOLLOW_55_in_enumElement525 = frozenset([1])
    FOLLOW_56_in_enumElement527 = frozenset([59])
    FOLLOW_59_in_enumElement529 = frozenset([60])
    FOLLOW_60_in_enumElement531 = frozenset([25])
    FOLLOW_INT_in_enumElement533 = frozenset([55])
    FOLLOW_55_in_enumElement535 = frozenset([57])
    FOLLOW_57_in_enumElement537 = frozenset([1])
    FOLLOW_FLAGS_in_flagsDef573 = frozenset([20])
    FOLLOW_ID_in_flagsDef575 = frozenset([56])
    FOLLOW_56_in_flagsDef577 = frozenset([58])
    FOLLOW_flagsElement_in_flagsDef579 = frozenset([57, 58])
    FOLLOW_57_in_flagsDef582 = frozenset([1])
    FOLLOW_58_in_flagsElement617 = frozenset([20])
    FOLLOW_ID_in_flagsElement619 = frozenset([55])
    FOLLOW_55_in_flagsElement621 = frozenset([1])
    FOLLOW_GTYPE_in_typeDecl646 = frozenset([20])
    FOLLOW_ID_in_typeDecl648 = frozenset([55])
    FOLLOW_55_in_typeDecl650 = frozenset([1])
    FOLLOW_SUPER_in_classMember681 = frozenset([20, 70, 71, 72, 73, 74, 86, 87, 88, 93])
    FOLLOW_typeName_in_classMember683 = frozenset([55])
    FOLLOW_55_in_classMember685 = frozenset([1])
    FOLLOW_ABSTRACT_in_classMember701 = frozenset([55])
    FOLLOW_55_in_classMember704 = frozenset([1])
    FOLLOW_PREFIX_in_classMember711 = frozenset([20])
    FOLLOW_ID_in_classMember713 = frozenset([55])
    FOLLOW_55_in_classMember715 = frozenset([1])
    FOLLOW_IMPLEMENTS_in_classMember728 = frozenset([20, 70, 71, 72, 73, 74, 86, 87, 88, 93])
    FOLLOW_typeName_in_classMember730 = frozenset([55])
    FOLLOW_55_in_classMember732 = frozenset([1])
    FOLLOW_CONSTRUCTOR_in_classMember752 = frozenset([56])
    FOLLOW_56_in_classMember754 = frozenset([43, 57])
    FOLLOW_constructorElement_in_classMember756 = frozenset([43, 57])
    FOLLOW_57_in_classMember759 = frozenset([1])
    FOLLOW_METHOD_in_classMember787 = frozenset([20])
    FOLLOW_ID_in_classMember789 = frozenset([56])
    FOLLOW_56_in_classMember791 = frozenset([39, 40, 41, 42, 43, 57])
    FOLLOW_methodElement_in_classMember793 = frozenset([39, 40, 41, 42, 43, 57])
    FOLLOW_57_in_classMember796 = frozenset([1])
    FOLLOW_OVERRIDE_in_classMember813 = frozenset([20])
    FOLLOW_ID_in_classMember815 = frozenset([55])
    FOLLOW_55_in_classMember817 = frozenset([1])
    FOLLOW_ATTRIBUTE_in_classMember830 = frozenset([20])
    FOLLOW_ID_in_classMember832 = frozenset([56])
    FOLLOW_56_in_classMember834 = frozenset([36])
    FOLLOW_TYPE_in_classMember836 = frozenset([60])
    FOLLOW_60_in_classMember838 = frozenset([20, 70, 71, 72, 73, 74, 86, 87, 88, 89, 92, 93])
    FOLLOW_typeArg_in_classMember840 = frozenset([55])
    FOLLOW_55_in_classMember842 = frozenset([40, 41, 57])
    FOLLOW_attributeElement_in_classMember844 = frozenset([40, 41, 57])
    FOLLOW_57_in_classMember847 = frozenset([1])
    FOLLOW_PROPERTY_in_classMember866 = frozenset([20])
    FOLLOW_ID_in_classMember868 = frozenset([56])
    FOLLOW_56_in_classMember870 = frozenset([27, 36, 45, 77, 81, 82, 83, 84])
    FOLLOW_propertyElement_in_classMember872 = frozenset([27, 36, 45, 57, 77, 81, 82, 83, 84])
    FOLLOW_57_in_classMember875 = frozenset([1])
    FOLLOW_SIGNAL_in_classMember891 = frozenset([20])
    FOLLOW_signalID_in_classMember893 = frozenset([56])
    FOLLOW_56_in_classMember895 = frozenset([39, 43, 57])
    FOLLOW_signalElement_in_classMember897 = frozenset([39, 43, 57])
    FOLLOW_57_in_classMember900 = frozenset([1])
    FOLLOW_METHOD_in_intfMember923 = frozenset([20])
    FOLLOW_ID_in_intfMember925 = frozenset([56])
    FOLLOW_56_in_intfMember927 = frozenset([39, 40, 41, 42, 43, 57])
    FOLLOW_methodElement_in_intfMember929 = frozenset([39, 40, 41, 42, 43, 57])
    FOLLOW_57_in_intfMember932 = frozenset([1])
    FOLLOW_SIGNAL_in_intfMember953 = frozenset([20])
    FOLLOW_signalID_in_intfMember955 = frozenset([56])
    FOLLOW_56_in_intfMember957 = frozenset([39, 43, 57])
    FOLLOW_signalElement_in_intfMember959 = frozenset([39, 43, 57])
    FOLLOW_57_in_intfMember962 = frozenset([1])
    FOLLOW_RESULT_in_resultDef985 = frozenset([56])
    FOLLOW_56_in_resultDef987 = frozenset([36])
    FOLLOW_TYPE_in_resultDef989 = frozenset([60])
    FOLLOW_60_in_resultDef991 = frozenset([20, 70, 71, 72, 73, 74, 86, 87, 88, 89, 92, 93])
    FOLLOW_typeArg_in_resultDef993 = frozenset([55])
    FOLLOW_55_in_resultDef995 = frozenset([44, 57])
    FOLLOW_modifiers_in_resultDef997 = frozenset([57])
    FOLLOW_57_in_resultDef1000 = frozenset([1])
    FOLLOW_constructorElement_in_methodElement1023 = frozenset([1])
    FOLLOW_resultDef_in_methodElement1028 = frozenset([1])
    FOLLOW_VISIBILITY_in_methodElement1033 = frozenset([60])
    FOLLOW_60_in_methodElement1035 = frozenset([61, 62, 63])
    FOLLOW_61_in_methodElement1040 = frozenset([55])
    FOLLOW_62_in_methodElement1044 = frozenset([55])
    FOLLOW_63_in_methodElement1048 = frozenset([55])
    FOLLOW_55_in_methodElement1051 = frozenset([1])
    FOLLOW_SCOPE_in_methodElement1066 = frozenset([60])
    FOLLOW_60_in_methodElement1068 = frozenset([64, 65])
    FOLLOW_64_in_methodElement1073 = frozenset([55])
    FOLLOW_65_in_methodElement1077 = frozenset([55])
    FOLLOW_55_in_methodElement1080 = frozenset([1])
    FOLLOW_INHERITANCE_in_methodElement1096 = frozenset([60])
    FOLLOW_60_in_methodElement1098 = frozenset([29, 66, 67])
    FOLLOW_66_in_methodElement1103 = frozenset([55])
    FOLLOW_67_in_methodElement1107 = frozenset([55])
    FOLLOW_ABSTRACT_in_methodElement1111 = frozenset([55])
    FOLLOW_55_in_methodElement1114 = frozenset([1])
    FOLLOW_PARAMETER_in_constructorElement1136 = frozenset([20])
    FOLLOW_ID_in_constructorElement1138 = frozenset([56])
    FOLLOW_56_in_constructorElement1140 = frozenset([36])
    FOLLOW_TYPE_in_constructorElement1142 = frozenset([60])
    FOLLOW_60_in_constructorElement1144 = frozenset([20, 70, 71, 72, 73, 74, 86, 87, 88, 89, 92, 93])
    FOLLOW_typeArg_in_constructorElement1146 = frozenset([55])
    FOLLOW_55_in_constructorElement1148 = frozenset([44, 57, 68])
    FOLLOW_parameterElement_in_constructorElement1150 = frozenset([57])
    FOLLOW_57_in_constructorElement1153 = frozenset([1])
    FOLLOW_modifiers_in_parameterElement1183 = frozenset([1])
    FOLLOW_68_in_parameterElement1196 = frozenset([60])
    FOLLOW_60_in_parameterElement1198 = frozenset([20])
    FOLLOW_ID_in_parameterElement1200 = frozenset([55])
    FOLLOW_55_in_parameterElement1202 = frozenset([1])
    FOLLOW_MODIFIERS_in_modifiers1224 = frozenset([60])
    FOLLOW_60_in_modifiers1226 = frozenset([69])
    FOLLOW_69_in_modifiers1228 = frozenset([55])
    FOLLOW_55_in_modifiers1230 = frozenset([1])
    FOLLOW_TYPE_in_propertyElement1254 = frozenset([60])
    FOLLOW_60_in_propertyElement1256 = frozenset([70, 71, 72, 73, 74, 75, 76])
    FOLLOW_70_in_propertyElement1261 = frozenset([55])
    FOLLOW_71_in_propertyElement1265 = frozenset([55])
    FOLLOW_72_in_propertyElement1269 = frozenset([55])
    FOLLOW_73_in_propertyElement1278 = frozenset([55])
    FOLLOW_74_in_propertyElement1282 = frozenset([55])
    FOLLOW_75_in_propertyElement1286 = frozenset([55])
    FOLLOW_76_in_propertyElement1290 = frozenset([55])
    FOLLOW_55_in_propertyElement1293 = frozenset([1])
    FOLLOW_77_in_propertyElement1316 = frozenset([60])
    FOLLOW_60_in_propertyElement1318 = frozenset([78, 79, 80])
    FOLLOW_78_in_propertyElement1323 = frozenset([55])
    FOLLOW_79_in_propertyElement1327 = frozenset([55])
    FOLLOW_80_in_propertyElement1331 = frozenset([55])
    FOLLOW_55_in_propertyElement1334 = frozenset([1])
    FOLLOW_81_in_propertyElement1357 = frozenset([60])
    FOLLOW_60_in_propertyElement1359 = frozenset([19])
    FOLLOW_STRING_in_propertyElement1361 = frozenset([55])
    FOLLOW_55_in_propertyElement1363 = frozenset([1])
    FOLLOW_GTYPE_in_propertyElement1381 = frozenset([60])
    FOLLOW_60_in_propertyElement1383 = frozenset([20])
    FOLLOW_ID_in_propertyElement1385 = frozenset([55])
    FOLLOW_55_in_propertyElement1387 = frozenset([1])
    FOLLOW_82_in_propertyElement1409 = frozenset([60])
    FOLLOW_60_in_propertyElement1411 = frozenset([19])
    FOLLOW_STRING_in_propertyElement1413 = frozenset([55])
    FOLLOW_55_in_propertyElement1415 = frozenset([1])
    FOLLOW_83_in_propertyElement1433 = frozenset([60])
    FOLLOW_60_in_propertyElement1435 = frozenset([19])
    FOLLOW_STRING_in_propertyElement1437 = frozenset([55])
    FOLLOW_55_in_propertyElement1439 = frozenset([1])
    FOLLOW_84_in_propertyElement1457 = frozenset([60])
    FOLLOW_60_in_propertyElement1459 = frozenset([19])
    FOLLOW_STRING_in_propertyElement1461 = frozenset([55])
    FOLLOW_55_in_propertyElement1463 = frozenset([1])
    FOLLOW_AUTO_CREATE_in_propertyElement1481 = frozenset([55])
    FOLLOW_55_in_propertyElement1484 = frozenset([1])
    FOLLOW_RESULT_in_signalElement1503 = frozenset([56])
    FOLLOW_56_in_signalElement1505 = frozenset([36])
    FOLLOW_TYPE_in_signalElement1507 = frozenset([60])
    FOLLOW_60_in_signalElement1509 = frozenset([70, 71, 72, 73, 75, 76, 85, 86])
    FOLLOW_signalType_in_signalElement1511 = frozenset([55])
    FOLLOW_55_in_signalElement1513 = frozenset([57])
    FOLLOW_57_in_signalElement1515 = frozenset([1])
    FOLLOW_PARAMETER_in_signalElement1533 = frozenset([20])
    FOLLOW_ID_in_signalElement1535 = frozenset([56])
    FOLLOW_56_in_signalElement1537 = frozenset([36])
    FOLLOW_TYPE_in_signalElement1539 = frozenset([60])
    FOLLOW_60_in_signalElement1541 = frozenset([70, 71, 72, 73, 75, 76, 85, 86])
    FOLLOW_signalType_in_signalElement1543 = frozenset([55])
    FOLLOW_55_in_signalElement1545 = frozenset([57])
    FOLLOW_57_in_signalElement1547 = frozenset([1])
    FOLLOW_set_in_signalType0 = frozenset([1])
    FOLLOW_SCOPE_in_attributeElement1660 = frozenset([60])
    FOLLOW_60_in_attributeElement1662 = frozenset([64, 65])
    FOLLOW_65_in_attributeElement1667 = frozenset([55])
    FOLLOW_64_in_attributeElement1671 = frozenset([55])
    FOLLOW_55_in_attributeElement1674 = frozenset([1])
    FOLLOW_VISIBILITY_in_attributeElement1688 = frozenset([60])
    FOLLOW_60_in_attributeElement1690 = frozenset([61, 62, 63])
    FOLLOW_61_in_attributeElement1695 = frozenset([55])
    FOLLOW_62_in_attributeElement1699 = frozenset([55])
    FOLLOW_63_in_attributeElement1703 = frozenset([55])
    FOLLOW_55_in_attributeElement1706 = frozenset([1])
    FOLLOW_typePath_in_typeName1728 = frozenset([1])
    FOLLOW_87_in_typeName1743 = frozenset([71])
    FOLLOW_71_in_typeName1746 = frozenset([1])
    FOLLOW_87_in_typeName1764 = frozenset([88])
    FOLLOW_88_in_typeName1767 = frozenset([1])
    FOLLOW_70_in_typeName1786 = frozenset([1])
    FOLLOW_73_in_typeName1793 = frozenset([1])
    FOLLOW_86_in_typeName1800 = frozenset([1])
    FOLLOW_72_in_typeName1807 = frozenset([1])
    FOLLOW_74_in_typeName1816 = frozenset([1])
    FOLLOW_typeName_in_typeArg1842 = frozenset([1])
    FOLLOW_89_in_typeArg1852 = frozenset([90])
    FOLLOW_90_in_typeArg1854 = frozenset([20, 70, 71, 72, 73, 74, 86, 87, 88, 89, 92, 93])
    FOLLOW_typeArg_in_typeArg1856 = frozenset([91])
    FOLLOW_91_in_typeArg1858 = frozenset([1])
    FOLLOW_92_in_typeArg1876 = frozenset([90])
    FOLLOW_90_in_typeArg1878 = frozenset([20, 70, 71, 72, 73, 74, 86, 87, 88, 89, 92, 93])
    FOLLOW_typeArg_in_typeArg1880 = frozenset([91])
    FOLLOW_91_in_typeArg1882 = frozenset([1])
    FOLLOW_93_in_typePath1910 = frozenset([20])
    FOLLOW_ID_in_typePath1912 = frozenset([93])
    FOLLOW_93_in_typePath1914 = frozenset([20])
    FOLLOW_ID_in_typePath1918 = frozenset([93])
    FOLLOW_93_in_typePath1920 = frozenset([20])
    FOLLOW_ID_in_typePath1924 = frozenset([1])
    FOLLOW_ID_in_signalID2489 = frozenset([1, 94])
    FOLLOW_94_in_signalID2492 = frozenset([20])
    FOLLOW_ID_in_signalID2496 = frozenset([1, 94])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("GOCLexer", GOCParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
