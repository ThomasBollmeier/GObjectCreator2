#
# Copyright 2011 Thomas Bollmeier
#
# This file is part of GObjectCreator2.
#
# GObjectCreator2 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GObjectCreator2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GObjectCreator2.  If not, see <http://www.gnu.org/licenses/>.
#


# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 GOC.g 2011-03-18 21:31:23

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
PACKAGE=52
PREFIX=30
GTYPENAME=47
PROP_ACCESS=11
PROP_DEFAULT=16
GTYPE=27
OCTAL_ESC=56
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
COMMENT=49
T__99=99
GOBJECT=21
T__98=98
T__97=97
T__96=96
T__95=95
T__80=80
T__81=81
REF_TO=8
VISIBILITY=40
T__82=82
BOOLVALUE=51
T__83=83
GINTERFACE=22
INT=25
T__85=85
T__84=84
T__87=87
T__86=86
T__89=89
T__88=88
WS=50
T__71=71
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
MODIFIERS=46
T__57=57
T__58=58
ESC_SEQ=53
IMPLEMENTS=31
SCOPE=41
T__59=59
INCFILE_PATH=19
SIGNAL=38
TYPE_NAME=6
PROP_TYPE=10
AUTO_CREATE=48
ERROR_DOMAIN=23
PROP_MIN=14
INIT_PROPERTY=18
UNICODE_ESC=55
HEX_DIGIT=54
RESULT=39
T__100=100
ROOT=4
BIND_PROPERTY=17
PROP_MAX=15
OVERRIDE=34
PROP_GTYPE=13
METHOD=33
STRING=45

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ROOT", "INCLUDE", "TYPE_NAME", "SIGNAL_ID", "REF_TO", "LIST_OF", "PROP_TYPE", 
    "PROP_ACCESS", "PROP_DESC", "PROP_GTYPE", "PROP_MIN", "PROP_MAX", "PROP_DEFAULT", 
    "BIND_PROPERTY", "INIT_PROPERTY", "INCFILE_PATH", "ID", "GOBJECT", "GINTERFACE", 
    "ERROR_DOMAIN", "ENUMERATION", "INT", "FLAGS", "GTYPE", "SUPER", "ABSTRACT", 
    "PREFIX", "IMPLEMENTS", "CONSTRUCTOR", "METHOD", "OVERRIDE", "ATTRIBUTE", 
    "TYPE", "PROPERTY", "SIGNAL", "RESULT", "VISIBILITY", "SCOPE", "INHERITANCE", 
    "PARAMETER", "INIT_PROPERTIES", "STRING", "MODIFIERS", "GTYPENAME", 
    "AUTO_CREATE", "COMMENT", "WS", "BOOLVALUE", "PACKAGE", "ESC_SEQ", "HEX_DIGIT", 
    "UNICODE_ESC", "OCTAL_ESC", "'include'", "'<'", "'>'", "'{'", "'}'", 
    "';'", "'code'", "'value'", "':'", "'public'", "'protected'", "'private'", 
    "'instance'", "'static'", "'final'", "'virtual'", "'bind_property'", 
    "'.'", "'const'", "'boolean'", "'integer'", "'float'", "'double'", "'string'", 
    "'pointer'", "'object'", "'enumeration'", "'access'", "'read-only'", 
    "'initial-write'", "'read-write'", "'description'", "'('", "')'", "'min'", 
    "'max'", "'default'", "'unsigned '", "'long'", "'null'", "'ref'", "'list'", 
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

                    if ((GOBJECT <= LA1_0 <= ENUMERATION) or (FLAGS <= LA1_0 <= GTYPE) or LA1_0 == PACKAGE or LA1_0 == 57) :
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
                elif LA2 == 57:
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
    # GOC.g:41:1: includeStmt : 'include' '<' INCFILE_PATH '>' -> ^( INCLUDE INCFILE_PATH ) ;
    def includeStmt(self, ):

        retval = self.includeStmt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal10 = None
        char_literal11 = None
        INCFILE_PATH12 = None
        char_literal13 = None

        string_literal10_tree = None
        char_literal11_tree = None
        INCFILE_PATH12_tree = None
        char_literal13_tree = None
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_INCFILE_PATH = RewriteRuleTokenStream(self._adaptor, "token INCFILE_PATH")

        try:
            try:
                # GOC.g:42:5: ( 'include' '<' INCFILE_PATH '>' -> ^( INCLUDE INCFILE_PATH ) )
                # GOC.g:42:9: 'include' '<' INCFILE_PATH '>'
                pass 
                string_literal10=self.match(self.input, 57, self.FOLLOW_57_in_includeStmt226) 
                stream_57.add(string_literal10)
                char_literal11=self.match(self.input, 58, self.FOLLOW_58_in_includeStmt228) 
                stream_58.add(char_literal11)
                INCFILE_PATH12=self.match(self.input, INCFILE_PATH, self.FOLLOW_INCFILE_PATH_in_includeStmt230) 
                stream_INCFILE_PATH.add(INCFILE_PATH12)
                char_literal13=self.match(self.input, 59, self.FOLLOW_59_in_includeStmt232) 
                stream_59.add(char_literal13)

                # AST Rewrite
                # elements: INCFILE_PATH
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
                # 42:40: -> ^( INCLUDE INCFILE_PATH )
                # GOC.g:42:43: ^( INCLUDE INCFILE_PATH )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(INCLUDE, "INCLUDE"), root_1)

                self._adaptor.addChild(root_1, stream_INCFILE_PATH.nextNode())

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

        string_literal14 = None
        ID15 = None
        char_literal16 = None
        char_literal18 = None
        packageElement17 = None


        string_literal14_tree = None
        ID15_tree = None
        char_literal16_tree = None
        char_literal18_tree = None
        stream_PACKAGE = RewriteRuleTokenStream(self._adaptor, "token PACKAGE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_61 = RewriteRuleTokenStream(self._adaptor, "token 61")
        stream_packageElement = RewriteRuleSubtreeStream(self._adaptor, "rule packageElement")
        try:
            try:
                # GOC.g:46:2: ( 'package' ID '{' ( packageElement )* '}' -> ^( 'package' ID ( packageElement )* ) )
                # GOC.g:46:4: 'package' ID '{' ( packageElement )* '}'
                pass 
                string_literal14=self.match(self.input, PACKAGE, self.FOLLOW_PACKAGE_in_packageDef254) 
                stream_PACKAGE.add(string_literal14)
                ID15=self.match(self.input, ID, self.FOLLOW_ID_in_packageDef256) 
                stream_ID.add(ID15)
                char_literal16=self.match(self.input, 60, self.FOLLOW_60_in_packageDef258) 
                stream_60.add(char_literal16)
                # GOC.g:46:21: ( packageElement )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((GOBJECT <= LA3_0 <= ENUMERATION) or (FLAGS <= LA3_0 <= GTYPE) or LA3_0 == PACKAGE) :
                        alt3 = 1


                    if alt3 == 1:
                        # GOC.g:46:21: packageElement
                        pass 
                        self._state.following.append(self.FOLLOW_packageElement_in_packageDef260)
                        packageElement17 = self.packageElement()

                        self._state.following.pop()
                        stream_packageElement.add(packageElement17.tree)


                    else:
                        break #loop3
                char_literal18=self.match(self.input, 61, self.FOLLOW_61_in_packageDef263) 
                stream_61.add(char_literal18)

                # AST Rewrite
                # elements: packageElement, PACKAGE, ID
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

        packageDef19 = None

        classDef20 = None

        intfDef21 = None

        errorDomainDef22 = None

        enumDef23 = None

        flagsDef24 = None

        typeDecl25 = None



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

                    self._state.following.append(self.FOLLOW_packageDef_in_packageElement288)
                    packageDef19 = self.packageDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, packageDef19.tree)


                elif alt4 == 2:
                    # GOC.g:52:4: classDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_classDef_in_packageElement293)
                    classDef20 = self.classDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, classDef20.tree)


                elif alt4 == 3:
                    # GOC.g:53:4: intfDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_intfDef_in_packageElement298)
                    intfDef21 = self.intfDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, intfDef21.tree)


                elif alt4 == 4:
                    # GOC.g:54:6: errorDomainDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_errorDomainDef_in_packageElement305)
                    errorDomainDef22 = self.errorDomainDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, errorDomainDef22.tree)


                elif alt4 == 5:
                    # GOC.g:55:6: enumDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_enumDef_in_packageElement312)
                    enumDef23 = self.enumDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, enumDef23.tree)


                elif alt4 == 6:
                    # GOC.g:56:6: flagsDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_flagsDef_in_packageElement319)
                    flagsDef24 = self.flagsDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, flagsDef24.tree)


                elif alt4 == 7:
                    # GOC.g:57:6: typeDecl
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_typeDecl_in_packageElement326)
                    typeDecl25 = self.typeDecl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, typeDecl25.tree)


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
        GOBJECT26 = None
        char_literal27 = None
        char_literal29 = None
        char_literal30 = None
        classMember28 = None


        className_tree = None
        GOBJECT26_tree = None
        char_literal27_tree = None
        char_literal29_tree = None
        char_literal30_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_GOBJECT = RewriteRuleTokenStream(self._adaptor, "token GOBJECT")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_61 = RewriteRuleTokenStream(self._adaptor, "token 61")
        stream_classMember = RewriteRuleSubtreeStream(self._adaptor, "rule classMember")
        try:
            try:
                # GOC.g:61:2: ( GOBJECT className= ID ( '{' ( classMember )* '}' | ';' ) -> ^( GOBJECT $className ( classMember )* ) )
                # GOC.g:61:4: GOBJECT className= ID ( '{' ( classMember )* '}' | ';' )
                pass 
                GOBJECT26=self.match(self.input, GOBJECT, self.FOLLOW_GOBJECT_in_classDef337) 
                stream_GOBJECT.add(GOBJECT26)
                className=self.match(self.input, ID, self.FOLLOW_ID_in_classDef341) 
                stream_ID.add(className)
                # GOC.g:61:25: ( '{' ( classMember )* '}' | ';' )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 60) :
                    alt6 = 1
                elif (LA6_0 == 62) :
                    alt6 = 2
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # GOC.g:61:26: '{' ( classMember )* '}'
                    pass 
                    char_literal27=self.match(self.input, 60, self.FOLLOW_60_in_classDef344) 
                    stream_60.add(char_literal27)
                    # GOC.g:61:30: ( classMember )*
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if ((SUPER <= LA5_0 <= ATTRIBUTE) or (PROPERTY <= LA5_0 <= SIGNAL)) :
                            alt5 = 1


                        if alt5 == 1:
                            # GOC.g:61:30: classMember
                            pass 
                            self._state.following.append(self.FOLLOW_classMember_in_classDef346)
                            classMember28 = self.classMember()

                            self._state.following.pop()
                            stream_classMember.add(classMember28.tree)


                        else:
                            break #loop5
                    char_literal29=self.match(self.input, 61, self.FOLLOW_61_in_classDef349) 
                    stream_61.add(char_literal29)


                elif alt6 == 2:
                    # GOC.g:61:47: ';'
                    pass 
                    char_literal30=self.match(self.input, 62, self.FOLLOW_62_in_classDef351) 
                    stream_62.add(char_literal30)




                # AST Rewrite
                # elements: GOBJECT, classMember, className
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
        GINTERFACE31 = None
        char_literal32 = None
        char_literal34 = None
        char_literal35 = None
        intfMember33 = None


        intfName_tree = None
        GINTERFACE31_tree = None
        char_literal32_tree = None
        char_literal34_tree = None
        char_literal35_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_GINTERFACE = RewriteRuleTokenStream(self._adaptor, "token GINTERFACE")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_61 = RewriteRuleTokenStream(self._adaptor, "token 61")
        stream_intfMember = RewriteRuleSubtreeStream(self._adaptor, "rule intfMember")
        try:
            try:
                # GOC.g:66:2: ( GINTERFACE intfName= ID ( '{' ( intfMember )* '}' | ';' ) -> ^( GINTERFACE $intfName ( intfMember )* ) )
                # GOC.g:66:4: GINTERFACE intfName= ID ( '{' ( intfMember )* '}' | ';' )
                pass 
                GINTERFACE31=self.match(self.input, GINTERFACE, self.FOLLOW_GINTERFACE_in_intfDef378) 
                stream_GINTERFACE.add(GINTERFACE31)
                intfName=self.match(self.input, ID, self.FOLLOW_ID_in_intfDef382) 
                stream_ID.add(intfName)
                # GOC.g:66:27: ( '{' ( intfMember )* '}' | ';' )
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == 60) :
                    alt8 = 1
                elif (LA8_0 == 62) :
                    alt8 = 2
                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # GOC.g:66:28: '{' ( intfMember )* '}'
                    pass 
                    char_literal32=self.match(self.input, 60, self.FOLLOW_60_in_intfDef385) 
                    stream_60.add(char_literal32)
                    # GOC.g:66:32: ( intfMember )*
                    while True: #loop7
                        alt7 = 2
                        LA7_0 = self.input.LA(1)

                        if (LA7_0 == PREFIX or LA7_0 == METHOD or LA7_0 == SIGNAL) :
                            alt7 = 1


                        if alt7 == 1:
                            # GOC.g:66:32: intfMember
                            pass 
                            self._state.following.append(self.FOLLOW_intfMember_in_intfDef387)
                            intfMember33 = self.intfMember()

                            self._state.following.pop()
                            stream_intfMember.add(intfMember33.tree)


                        else:
                            break #loop7
                    char_literal34=self.match(self.input, 61, self.FOLLOW_61_in_intfDef390) 
                    stream_61.add(char_literal34)


                elif alt8 == 2:
                    # GOC.g:66:48: ';'
                    pass 
                    char_literal35=self.match(self.input, 62, self.FOLLOW_62_in_intfDef392) 
                    stream_62.add(char_literal35)




                # AST Rewrite
                # elements: intfMember, intfName, GINTERFACE
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

        ERROR_DOMAIN36 = None
        ID37 = None
        char_literal38 = None
        char_literal40 = None
        errorDomainElement39 = None


        ERROR_DOMAIN36_tree = None
        ID37_tree = None
        char_literal38_tree = None
        char_literal40_tree = None
        stream_ERROR_DOMAIN = RewriteRuleTokenStream(self._adaptor, "token ERROR_DOMAIN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_61 = RewriteRuleTokenStream(self._adaptor, "token 61")
        stream_errorDomainElement = RewriteRuleSubtreeStream(self._adaptor, "rule errorDomainElement")
        try:
            try:
                # GOC.g:71:5: ( ERROR_DOMAIN ID '{' ( errorDomainElement )+ '}' -> ^( ERROR_DOMAIN ID ( errorDomainElement )+ ) )
                # GOC.g:71:9: ERROR_DOMAIN ID '{' ( errorDomainElement )+ '}'
                pass 
                ERROR_DOMAIN36=self.match(self.input, ERROR_DOMAIN, self.FOLLOW_ERROR_DOMAIN_in_errorDomainDef423) 
                stream_ERROR_DOMAIN.add(ERROR_DOMAIN36)
                ID37=self.match(self.input, ID, self.FOLLOW_ID_in_errorDomainDef425) 
                stream_ID.add(ID37)
                char_literal38=self.match(self.input, 60, self.FOLLOW_60_in_errorDomainDef427) 
                stream_60.add(char_literal38)
                # GOC.g:71:29: ( errorDomainElement )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 63) :
                        alt9 = 1


                    if alt9 == 1:
                        # GOC.g:71:29: errorDomainElement
                        pass 
                        self._state.following.append(self.FOLLOW_errorDomainElement_in_errorDomainDef429)
                        errorDomainElement39 = self.errorDomainElement()

                        self._state.following.pop()
                        stream_errorDomainElement.add(errorDomainElement39.tree)


                    else:
                        if cnt9 >= 1:
                            break #loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1
                char_literal40=self.match(self.input, 61, self.FOLLOW_61_in_errorDomainDef432) 
                stream_61.add(char_literal40)

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

        string_literal41 = None
        ID42 = None
        char_literal43 = None

        string_literal41_tree = None
        ID42_tree = None
        char_literal43_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_63 = RewriteRuleTokenStream(self._adaptor, "token 63")

        try:
            try:
                # GOC.g:76:5: ( 'code' ID ';' -> ^( ID ) )
                # GOC.g:76:9: 'code' ID ';'
                pass 
                string_literal41=self.match(self.input, 63, self.FOLLOW_63_in_errorDomainElement467) 
                stream_63.add(string_literal41)
                ID42=self.match(self.input, ID, self.FOLLOW_ID_in_errorDomainElement469) 
                stream_ID.add(ID42)
                char_literal43=self.match(self.input, 62, self.FOLLOW_62_in_errorDomainElement471) 
                stream_62.add(char_literal43)

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

        ENUMERATION44 = None
        ID45 = None
        char_literal46 = None
        char_literal48 = None
        enumElement47 = None


        ENUMERATION44_tree = None
        ID45_tree = None
        char_literal46_tree = None
        char_literal48_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_ENUMERATION = RewriteRuleTokenStream(self._adaptor, "token ENUMERATION")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_61 = RewriteRuleTokenStream(self._adaptor, "token 61")
        stream_enumElement = RewriteRuleSubtreeStream(self._adaptor, "rule enumElement")
        try:
            try:
                # GOC.g:80:5: ( ENUMERATION ID '{' ( enumElement )+ '}' -> ^( ENUMERATION ID ( enumElement )+ ) )
                # GOC.g:80:9: ENUMERATION ID '{' ( enumElement )+ '}'
                pass 
                ENUMERATION44=self.match(self.input, ENUMERATION, self.FOLLOW_ENUMERATION_in_enumDef496) 
                stream_ENUMERATION.add(ENUMERATION44)
                ID45=self.match(self.input, ID, self.FOLLOW_ID_in_enumDef498) 
                stream_ID.add(ID45)
                char_literal46=self.match(self.input, 60, self.FOLLOW_60_in_enumDef500) 
                stream_60.add(char_literal46)
                # GOC.g:80:28: ( enumElement )+
                cnt10 = 0
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == 63) :
                        alt10 = 1


                    if alt10 == 1:
                        # GOC.g:80:28: enumElement
                        pass 
                        self._state.following.append(self.FOLLOW_enumElement_in_enumDef502)
                        enumElement47 = self.enumElement()

                        self._state.following.pop()
                        stream_enumElement.add(enumElement47.tree)


                    else:
                        if cnt10 >= 1:
                            break #loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1
                char_literal48=self.match(self.input, 61, self.FOLLOW_61_in_enumDef505) 
                stream_61.add(char_literal48)

                # AST Rewrite
                # elements: enumElement, ID, ENUMERATION
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

        string_literal49 = None
        ID50 = None
        char_literal51 = None
        char_literal52 = None
        string_literal53 = None
        char_literal54 = None
        INT55 = None
        char_literal56 = None
        char_literal57 = None

        string_literal49_tree = None
        ID50_tree = None
        char_literal51_tree = None
        char_literal52_tree = None
        string_literal53_tree = None
        char_literal54_tree = None
        INT55_tree = None
        char_literal56_tree = None
        char_literal57_tree = None
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_64 = RewriteRuleTokenStream(self._adaptor, "token 64")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_63 = RewriteRuleTokenStream(self._adaptor, "token 63")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_61 = RewriteRuleTokenStream(self._adaptor, "token 61")

        try:
            try:
                # GOC.g:85:5: ( 'code' ID ( ';' | '{' 'value' ':' INT ';' '}' ) -> ^( 'code' ID ( INT )? ) )
                # GOC.g:85:9: 'code' ID ( ';' | '{' 'value' ':' INT ';' '}' )
                pass 
                string_literal49=self.match(self.input, 63, self.FOLLOW_63_in_enumElement540) 
                stream_63.add(string_literal49)
                ID50=self.match(self.input, ID, self.FOLLOW_ID_in_enumElement542) 
                stream_ID.add(ID50)
                # GOC.g:85:19: ( ';' | '{' 'value' ':' INT ';' '}' )
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == 62) :
                    alt11 = 1
                elif (LA11_0 == 60) :
                    alt11 = 2
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # GOC.g:85:20: ';'
                    pass 
                    char_literal51=self.match(self.input, 62, self.FOLLOW_62_in_enumElement545) 
                    stream_62.add(char_literal51)


                elif alt11 == 2:
                    # GOC.g:85:24: '{' 'value' ':' INT ';' '}'
                    pass 
                    char_literal52=self.match(self.input, 60, self.FOLLOW_60_in_enumElement547) 
                    stream_60.add(char_literal52)
                    string_literal53=self.match(self.input, 64, self.FOLLOW_64_in_enumElement549) 
                    stream_64.add(string_literal53)
                    char_literal54=self.match(self.input, 65, self.FOLLOW_65_in_enumElement551) 
                    stream_65.add(char_literal54)
                    INT55=self.match(self.input, INT, self.FOLLOW_INT_in_enumElement553) 
                    stream_INT.add(INT55)
                    char_literal56=self.match(self.input, 62, self.FOLLOW_62_in_enumElement555) 
                    stream_62.add(char_literal56)
                    char_literal57=self.match(self.input, 61, self.FOLLOW_61_in_enumElement557) 
                    stream_61.add(char_literal57)




                # AST Rewrite
                # elements: ID, INT, 63
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
                root_1 = self._adaptor.becomeRoot(stream_63.nextNode(), root_1)

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

        FLAGS58 = None
        ID59 = None
        char_literal60 = None
        char_literal62 = None
        flagsElement61 = None


        FLAGS58_tree = None
        ID59_tree = None
        char_literal60_tree = None
        char_literal62_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_FLAGS = RewriteRuleTokenStream(self._adaptor, "token FLAGS")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_61 = RewriteRuleTokenStream(self._adaptor, "token 61")
        stream_flagsElement = RewriteRuleSubtreeStream(self._adaptor, "rule flagsElement")
        try:
            try:
                # GOC.g:90:5: ( FLAGS ID '{' ( flagsElement )+ '}' -> ^( FLAGS ID ( flagsElement )+ ) )
                # GOC.g:90:9: FLAGS ID '{' ( flagsElement )+ '}'
                pass 
                FLAGS58=self.match(self.input, FLAGS, self.FOLLOW_FLAGS_in_flagsDef593) 
                stream_FLAGS.add(FLAGS58)
                ID59=self.match(self.input, ID, self.FOLLOW_ID_in_flagsDef595) 
                stream_ID.add(ID59)
                char_literal60=self.match(self.input, 60, self.FOLLOW_60_in_flagsDef597) 
                stream_60.add(char_literal60)
                # GOC.g:90:22: ( flagsElement )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == 63) :
                        alt12 = 1


                    if alt12 == 1:
                        # GOC.g:90:22: flagsElement
                        pass 
                        self._state.following.append(self.FOLLOW_flagsElement_in_flagsDef599)
                        flagsElement61 = self.flagsElement()

                        self._state.following.pop()
                        stream_flagsElement.add(flagsElement61.tree)


                    else:
                        if cnt12 >= 1:
                            break #loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1
                char_literal62=self.match(self.input, 61, self.FOLLOW_61_in_flagsDef602) 
                stream_61.add(char_literal62)

                # AST Rewrite
                # elements: ID, FLAGS, flagsElement
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

        string_literal63 = None
        ID64 = None
        char_literal65 = None

        string_literal63_tree = None
        ID64_tree = None
        char_literal65_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_63 = RewriteRuleTokenStream(self._adaptor, "token 63")

        try:
            try:
                # GOC.g:95:5: ( 'code' ID ';' -> ^( ID ) )
                # GOC.g:95:9: 'code' ID ';'
                pass 
                string_literal63=self.match(self.input, 63, self.FOLLOW_63_in_flagsElement637) 
                stream_63.add(string_literal63)
                ID64=self.match(self.input, ID, self.FOLLOW_ID_in_flagsElement639) 
                stream_ID.add(ID64)
                char_literal65=self.match(self.input, 62, self.FOLLOW_62_in_flagsElement641) 
                stream_62.add(char_literal65)

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

        GTYPE66 = None
        ID67 = None
        char_literal68 = None

        GTYPE66_tree = None
        ID67_tree = None
        char_literal68_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_GTYPE = RewriteRuleTokenStream(self._adaptor, "token GTYPE")

        try:
            try:
                # GOC.g:99:5: ( GTYPE ID ';' -> ^( GTYPE ID ) )
                # GOC.g:99:9: GTYPE ID ';'
                pass 
                GTYPE66=self.match(self.input, GTYPE, self.FOLLOW_GTYPE_in_typeDecl666) 
                stream_GTYPE.add(GTYPE66)
                ID67=self.match(self.input, ID, self.FOLLOW_ID_in_typeDecl668) 
                stream_ID.add(ID67)
                char_literal68=self.match(self.input, 62, self.FOLLOW_62_in_typeDecl670) 
                stream_62.add(char_literal68)

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

        SUPER69 = None
        char_literal71 = None
        ABSTRACT72 = None
        char_literal73 = None
        PREFIX74 = None
        ID75 = None
        char_literal76 = None
        IMPLEMENTS77 = None
        char_literal79 = None
        CONSTRUCTOR80 = None
        char_literal81 = None
        char_literal83 = None
        METHOD84 = None
        ID85 = None
        char_literal86 = None
        char_literal88 = None
        OVERRIDE89 = None
        ID90 = None
        char_literal91 = None
        ATTRIBUTE92 = None
        ID93 = None
        char_literal94 = None
        TYPE95 = None
        char_literal96 = None
        char_literal98 = None
        char_literal100 = None
        PROPERTY101 = None
        ID102 = None
        char_literal103 = None
        char_literal105 = None
        SIGNAL106 = None
        char_literal108 = None
        char_literal110 = None
        typeName70 = None

        typeName78 = None

        constructorElement82 = None

        methodElement87 = None

        typeArg97 = None

        attributeElement99 = None

        propertyElement104 = None

        signalID107 = None

        signalElement109 = None


        SUPER69_tree = None
        char_literal71_tree = None
        ABSTRACT72_tree = None
        char_literal73_tree = None
        PREFIX74_tree = None
        ID75_tree = None
        char_literal76_tree = None
        IMPLEMENTS77_tree = None
        char_literal79_tree = None
        CONSTRUCTOR80_tree = None
        char_literal81_tree = None
        char_literal83_tree = None
        METHOD84_tree = None
        ID85_tree = None
        char_literal86_tree = None
        char_literal88_tree = None
        OVERRIDE89_tree = None
        ID90_tree = None
        char_literal91_tree = None
        ATTRIBUTE92_tree = None
        ID93_tree = None
        char_literal94_tree = None
        TYPE95_tree = None
        char_literal96_tree = None
        char_literal98_tree = None
        char_literal100_tree = None
        PROPERTY101_tree = None
        ID102_tree = None
        char_literal103_tree = None
        char_literal105_tree = None
        SIGNAL106_tree = None
        char_literal108_tree = None
        char_literal110_tree = None
        stream_PREFIX = RewriteRuleTokenStream(self._adaptor, "token PREFIX")
        stream_IMPLEMENTS = RewriteRuleTokenStream(self._adaptor, "token IMPLEMENTS")
        stream_PROPERTY = RewriteRuleTokenStream(self._adaptor, "token PROPERTY")
        stream_OVERRIDE = RewriteRuleTokenStream(self._adaptor, "token OVERRIDE")
        stream_SIGNAL = RewriteRuleTokenStream(self._adaptor, "token SIGNAL")
        stream_ATTRIBUTE = RewriteRuleTokenStream(self._adaptor, "token ATTRIBUTE")
        stream_SUPER = RewriteRuleTokenStream(self._adaptor, "token SUPER")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_CONSTRUCTOR = RewriteRuleTokenStream(self._adaptor, "token CONSTRUCTOR")
        stream_METHOD = RewriteRuleTokenStream(self._adaptor, "token METHOD")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_61 = RewriteRuleTokenStream(self._adaptor, "token 61")
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
                    SUPER69=self.match(self.input, SUPER, self.FOLLOW_SUPER_in_classMember701) 
                    stream_SUPER.add(SUPER69)
                    self._state.following.append(self.FOLLOW_typeName_in_classMember703)
                    typeName70 = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(typeName70.tree)
                    char_literal71=self.match(self.input, 62, self.FOLLOW_62_in_classMember705) 
                    stream_62.add(char_literal71)

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

                    ABSTRACT72=self.match(self.input, ABSTRACT, self.FOLLOW_ABSTRACT_in_classMember721)

                    ABSTRACT72_tree = self._adaptor.createWithPayload(ABSTRACT72)
                    root_0 = self._adaptor.becomeRoot(ABSTRACT72_tree, root_0)

                    char_literal73=self.match(self.input, 62, self.FOLLOW_62_in_classMember724)

                    char_literal73_tree = self._adaptor.createWithPayload(char_literal73)
                    self._adaptor.addChild(root_0, char_literal73_tree)



                elif alt18 == 3:
                    # GOC.g:112:6: PREFIX ID ';'
                    pass 
                    PREFIX74=self.match(self.input, PREFIX, self.FOLLOW_PREFIX_in_classMember731) 
                    stream_PREFIX.add(PREFIX74)
                    ID75=self.match(self.input, ID, self.FOLLOW_ID_in_classMember733) 
                    stream_ID.add(ID75)
                    char_literal76=self.match(self.input, 62, self.FOLLOW_62_in_classMember735) 
                    stream_62.add(char_literal76)

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
                    IMPLEMENTS77=self.match(self.input, IMPLEMENTS, self.FOLLOW_IMPLEMENTS_in_classMember748) 
                    stream_IMPLEMENTS.add(IMPLEMENTS77)
                    self._state.following.append(self.FOLLOW_typeName_in_classMember750)
                    typeName78 = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(typeName78.tree)
                    char_literal79=self.match(self.input, 62, self.FOLLOW_62_in_classMember752) 
                    stream_62.add(char_literal79)

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
                    CONSTRUCTOR80=self.match(self.input, CONSTRUCTOR, self.FOLLOW_CONSTRUCTOR_in_classMember772) 
                    stream_CONSTRUCTOR.add(CONSTRUCTOR80)
                    char_literal81=self.match(self.input, 60, self.FOLLOW_60_in_classMember774) 
                    stream_60.add(char_literal81)
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
                            self._state.following.append(self.FOLLOW_constructorElement_in_classMember776)
                            constructorElement82 = self.constructorElement()

                            self._state.following.pop()
                            stream_constructorElement.add(constructorElement82.tree)


                        else:
                            break #loop13
                    char_literal83=self.match(self.input, 61, self.FOLLOW_61_in_classMember779) 
                    stream_61.add(char_literal83)
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
                    METHOD84=self.match(self.input, METHOD, self.FOLLOW_METHOD_in_classMember807) 
                    stream_METHOD.add(METHOD84)
                    ID85=self.match(self.input, ID, self.FOLLOW_ID_in_classMember809) 
                    stream_ID.add(ID85)
                    char_literal86=self.match(self.input, 60, self.FOLLOW_60_in_classMember811) 
                    stream_60.add(char_literal86)
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
                            self._state.following.append(self.FOLLOW_methodElement_in_classMember813)
                            methodElement87 = self.methodElement()

                            self._state.following.pop()
                            stream_methodElement.add(methodElement87.tree)


                        else:
                            break #loop14
                    char_literal88=self.match(self.input, 61, self.FOLLOW_61_in_classMember816) 
                    stream_61.add(char_literal88)

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
                    OVERRIDE89=self.match(self.input, OVERRIDE, self.FOLLOW_OVERRIDE_in_classMember833) 
                    stream_OVERRIDE.add(OVERRIDE89)
                    ID90=self.match(self.input, ID, self.FOLLOW_ID_in_classMember835) 
                    stream_ID.add(ID90)
                    char_literal91=self.match(self.input, 62, self.FOLLOW_62_in_classMember837) 
                    stream_62.add(char_literal91)

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
                    ATTRIBUTE92=self.match(self.input, ATTRIBUTE, self.FOLLOW_ATTRIBUTE_in_classMember850) 
                    stream_ATTRIBUTE.add(ATTRIBUTE92)
                    ID93=self.match(self.input, ID, self.FOLLOW_ID_in_classMember852) 
                    stream_ID.add(ID93)
                    char_literal94=self.match(self.input, 60, self.FOLLOW_60_in_classMember854) 
                    stream_60.add(char_literal94)
                    TYPE95=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_classMember856) 
                    stream_TYPE.add(TYPE95)
                    char_literal96=self.match(self.input, 65, self.FOLLOW_65_in_classMember858) 
                    stream_65.add(char_literal96)
                    self._state.following.append(self.FOLLOW_typeArg_in_classMember860)
                    typeArg97 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg97.tree)
                    char_literal98=self.match(self.input, 62, self.FOLLOW_62_in_classMember862) 
                    stream_62.add(char_literal98)
                    # GOC.g:120:42: ( attributeElement )*
                    while True: #loop15
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if ((VISIBILITY <= LA15_0 <= SCOPE)) :
                            alt15 = 1


                        if alt15 == 1:
                            # GOC.g:120:42: attributeElement
                            pass 
                            self._state.following.append(self.FOLLOW_attributeElement_in_classMember864)
                            attributeElement99 = self.attributeElement()

                            self._state.following.pop()
                            stream_attributeElement.add(attributeElement99.tree)


                        else:
                            break #loop15
                    char_literal100=self.match(self.input, 61, self.FOLLOW_61_in_classMember867) 
                    stream_61.add(char_literal100)

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
                    PROPERTY101=self.match(self.input, PROPERTY, self.FOLLOW_PROPERTY_in_classMember886) 
                    stream_PROPERTY.add(PROPERTY101)
                    ID102=self.match(self.input, ID, self.FOLLOW_ID_in_classMember888) 
                    stream_ID.add(ID102)
                    char_literal103=self.match(self.input, 60, self.FOLLOW_60_in_classMember890) 
                    stream_60.add(char_literal103)
                    # GOC.g:122:20: ( propertyElement )+
                    cnt16 = 0
                    while True: #loop16
                        alt16 = 2
                        LA16_0 = self.input.LA(1)

                        if (LA16_0 == GTYPE or LA16_0 == TYPE or LA16_0 == AUTO_CREATE or LA16_0 == 84 or LA16_0 == 88 or (91 <= LA16_0 <= 93)) :
                            alt16 = 1


                        if alt16 == 1:
                            # GOC.g:122:20: propertyElement
                            pass 
                            self._state.following.append(self.FOLLOW_propertyElement_in_classMember892)
                            propertyElement104 = self.propertyElement()

                            self._state.following.pop()
                            stream_propertyElement.add(propertyElement104.tree)


                        else:
                            if cnt16 >= 1:
                                break #loop16

                            eee = EarlyExitException(16, self.input)
                            raise eee

                        cnt16 += 1
                    char_literal105=self.match(self.input, 61, self.FOLLOW_61_in_classMember895) 
                    stream_61.add(char_literal105)

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
                    SIGNAL106=self.match(self.input, SIGNAL, self.FOLLOW_SIGNAL_in_classMember911) 
                    stream_SIGNAL.add(SIGNAL106)
                    self._state.following.append(self.FOLLOW_signalID_in_classMember913)
                    signalID107 = self.signalID()

                    self._state.following.pop()
                    stream_signalID.add(signalID107.tree)
                    char_literal108=self.match(self.input, 60, self.FOLLOW_60_in_classMember915) 
                    stream_60.add(char_literal108)
                    # GOC.g:123:24: ( signalElement )*
                    while True: #loop17
                        alt17 = 2
                        LA17_0 = self.input.LA(1)

                        if (LA17_0 == RESULT or LA17_0 == PARAMETER) :
                            alt17 = 1


                        if alt17 == 1:
                            # GOC.g:123:24: signalElement
                            pass 
                            self._state.following.append(self.FOLLOW_signalElement_in_classMember917)
                            signalElement109 = self.signalElement()

                            self._state.following.pop()
                            stream_signalElement.add(signalElement109.tree)


                        else:
                            break #loop17
                    char_literal110=self.match(self.input, 61, self.FOLLOW_61_in_classMember920) 
                    stream_61.add(char_literal110)

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

        PREFIX111 = None
        ID112 = None
        char_literal113 = None
        METHOD114 = None
        ID115 = None
        char_literal116 = None
        char_literal118 = None
        SIGNAL119 = None
        char_literal121 = None
        char_literal123 = None
        methodElement117 = None

        signalID120 = None

        signalElement122 = None


        PREFIX111_tree = None
        ID112_tree = None
        char_literal113_tree = None
        METHOD114_tree = None
        ID115_tree = None
        char_literal116_tree = None
        char_literal118_tree = None
        SIGNAL119_tree = None
        char_literal121_tree = None
        char_literal123_tree = None
        stream_PREFIX = RewriteRuleTokenStream(self._adaptor, "token PREFIX")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_METHOD = RewriteRuleTokenStream(self._adaptor, "token METHOD")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_61 = RewriteRuleTokenStream(self._adaptor, "token 61")
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
                    PREFIX111=self.match(self.input, PREFIX, self.FOLLOW_PREFIX_in_intfMember943) 
                    stream_PREFIX.add(PREFIX111)
                    ID112=self.match(self.input, ID, self.FOLLOW_ID_in_intfMember945) 
                    stream_ID.add(ID112)
                    char_literal113=self.match(self.input, 62, self.FOLLOW_62_in_intfMember947) 
                    stream_62.add(char_literal113)

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
                    METHOD114=self.match(self.input, METHOD, self.FOLLOW_METHOD_in_intfMember962) 
                    stream_METHOD.add(METHOD114)
                    ID115=self.match(self.input, ID, self.FOLLOW_ID_in_intfMember964) 
                    stream_ID.add(ID115)
                    char_literal116=self.match(self.input, 60, self.FOLLOW_60_in_intfMember966) 
                    stream_60.add(char_literal116)
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
                            self._state.following.append(self.FOLLOW_methodElement_in_intfMember968)
                            methodElement117 = self.methodElement()

                            self._state.following.pop()
                            stream_methodElement.add(methodElement117.tree)


                        else:
                            break #loop19
                    char_literal118=self.match(self.input, 61, self.FOLLOW_61_in_intfMember971) 
                    stream_61.add(char_literal118)

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
                    SIGNAL119=self.match(self.input, SIGNAL, self.FOLLOW_SIGNAL_in_intfMember992) 
                    stream_SIGNAL.add(SIGNAL119)
                    self._state.following.append(self.FOLLOW_signalID_in_intfMember994)
                    signalID120 = self.signalID()

                    self._state.following.pop()
                    stream_signalID.add(signalID120.tree)
                    char_literal121=self.match(self.input, 60, self.FOLLOW_60_in_intfMember996) 
                    stream_60.add(char_literal121)
                    # GOC.g:129:29: ( signalElement )*
                    while True: #loop20
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if (LA20_0 == RESULT or LA20_0 == PARAMETER) :
                            alt20 = 1


                        if alt20 == 1:
                            # GOC.g:129:29: signalElement
                            pass 
                            self._state.following.append(self.FOLLOW_signalElement_in_intfMember998)
                            signalElement122 = self.signalElement()

                            self._state.following.pop()
                            stream_signalElement.add(signalElement122.tree)


                        else:
                            break #loop20
                    char_literal123=self.match(self.input, 61, self.FOLLOW_61_in_intfMember1001) 
                    stream_61.add(char_literal123)

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

        RESULT124 = None
        char_literal125 = None
        TYPE126 = None
        char_literal127 = None
        char_literal129 = None
        char_literal131 = None
        typeArg128 = None

        modifiers130 = None


        RESULT124_tree = None
        char_literal125_tree = None
        TYPE126_tree = None
        char_literal127_tree = None
        char_literal129_tree = None
        char_literal131_tree = None
        stream_RESULT = RewriteRuleTokenStream(self._adaptor, "token RESULT")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_61 = RewriteRuleTokenStream(self._adaptor, "token 61")
        stream_TYPE = RewriteRuleTokenStream(self._adaptor, "token TYPE")
        stream_typeArg = RewriteRuleSubtreeStream(self._adaptor, "rule typeArg")
        stream_modifiers = RewriteRuleSubtreeStream(self._adaptor, "rule modifiers")
        try:
            try:
                # GOC.g:133:2: ( RESULT '{' TYPE ':' typeArg ';' ( modifiers )? '}' -> ^( RESULT typeArg ( modifiers )? ) )
                # GOC.g:133:4: RESULT '{' TYPE ':' typeArg ';' ( modifiers )? '}'
                pass 
                RESULT124=self.match(self.input, RESULT, self.FOLLOW_RESULT_in_resultDef1024) 
                stream_RESULT.add(RESULT124)
                char_literal125=self.match(self.input, 60, self.FOLLOW_60_in_resultDef1026) 
                stream_60.add(char_literal125)
                TYPE126=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_resultDef1028) 
                stream_TYPE.add(TYPE126)
                char_literal127=self.match(self.input, 65, self.FOLLOW_65_in_resultDef1030) 
                stream_65.add(char_literal127)
                self._state.following.append(self.FOLLOW_typeArg_in_resultDef1032)
                typeArg128 = self.typeArg()

                self._state.following.pop()
                stream_typeArg.add(typeArg128.tree)
                char_literal129=self.match(self.input, 62, self.FOLLOW_62_in_resultDef1034) 
                stream_62.add(char_literal129)
                # GOC.g:133:36: ( modifiers )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == MODIFIERS) :
                    alt22 = 1
                if alt22 == 1:
                    # GOC.g:133:36: modifiers
                    pass 
                    self._state.following.append(self.FOLLOW_modifiers_in_resultDef1036)
                    modifiers130 = self.modifiers()

                    self._state.following.pop()
                    stream_modifiers.add(modifiers130.tree)



                char_literal131=self.match(self.input, 61, self.FOLLOW_61_in_resultDef1039) 
                stream_61.add(char_literal131)

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
        VISIBILITY134 = None
        char_literal135 = None
        char_literal136 = None
        SCOPE137 = None
        char_literal138 = None
        char_literal139 = None
        INHERITANCE140 = None
        char_literal141 = None
        char_literal142 = None
        constructorElement132 = None

        resultDef133 = None


        val_tree = None
        VISIBILITY134_tree = None
        char_literal135_tree = None
        char_literal136_tree = None
        SCOPE137_tree = None
        char_literal138_tree = None
        char_literal139_tree = None
        INHERITANCE140_tree = None
        char_literal141_tree = None
        char_literal142_tree = None
        stream_67 = RewriteRuleTokenStream(self._adaptor, "token 67")
        stream_66 = RewriteRuleTokenStream(self._adaptor, "token 66")
        stream_69 = RewriteRuleTokenStream(self._adaptor, "token 69")
        stream_68 = RewriteRuleTokenStream(self._adaptor, "token 68")
        stream_VISIBILITY = RewriteRuleTokenStream(self._adaptor, "token VISIBILITY")
        stream_SCOPE = RewriteRuleTokenStream(self._adaptor, "token SCOPE")
        stream_ABSTRACT = RewriteRuleTokenStream(self._adaptor, "token ABSTRACT")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_70 = RewriteRuleTokenStream(self._adaptor, "token 70")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_71 = RewriteRuleTokenStream(self._adaptor, "token 71")
        stream_72 = RewriteRuleTokenStream(self._adaptor, "token 72")
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

                    self._state.following.append(self.FOLLOW_constructorElement_in_methodElement1062)
                    constructorElement132 = self.constructorElement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, constructorElement132.tree)


                elif alt26 == 2:
                    # GOC.g:139:4: resultDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_resultDef_in_methodElement1067)
                    resultDef133 = self.resultDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, resultDef133.tree)


                elif alt26 == 3:
                    # GOC.g:140:4: VISIBILITY ':' (val= 'public' | val= 'protected' | val= 'private' ) ';'
                    pass 
                    VISIBILITY134=self.match(self.input, VISIBILITY, self.FOLLOW_VISIBILITY_in_methodElement1072) 
                    stream_VISIBILITY.add(VISIBILITY134)
                    char_literal135=self.match(self.input, 65, self.FOLLOW_65_in_methodElement1074) 
                    stream_65.add(char_literal135)
                    # GOC.g:140:19: (val= 'public' | val= 'protected' | val= 'private' )
                    alt23 = 3
                    LA23 = self.input.LA(1)
                    if LA23 == 66:
                        alt23 = 1
                    elif LA23 == 67:
                        alt23 = 2
                    elif LA23 == 68:
                        alt23 = 3
                    else:
                        nvae = NoViableAltException("", 23, 0, self.input)

                        raise nvae

                    if alt23 == 1:
                        # GOC.g:140:20: val= 'public'
                        pass 
                        val=self.match(self.input, 66, self.FOLLOW_66_in_methodElement1079) 
                        stream_66.add(val)


                    elif alt23 == 2:
                        # GOC.g:140:33: val= 'protected'
                        pass 
                        val=self.match(self.input, 67, self.FOLLOW_67_in_methodElement1083) 
                        stream_67.add(val)


                    elif alt23 == 3:
                        # GOC.g:140:49: val= 'private'
                        pass 
                        val=self.match(self.input, 68, self.FOLLOW_68_in_methodElement1087) 
                        stream_68.add(val)



                    char_literal136=self.match(self.input, 62, self.FOLLOW_62_in_methodElement1090) 
                    stream_62.add(char_literal136)

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
                    SCOPE137=self.match(self.input, SCOPE, self.FOLLOW_SCOPE_in_methodElement1105) 
                    stream_SCOPE.add(SCOPE137)
                    char_literal138=self.match(self.input, 65, self.FOLLOW_65_in_methodElement1107) 
                    stream_65.add(char_literal138)
                    # GOC.g:142:14: (val= 'instance' | val= 'static' )
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == 69) :
                        alt24 = 1
                    elif (LA24_0 == 70) :
                        alt24 = 2
                    else:
                        nvae = NoViableAltException("", 24, 0, self.input)

                        raise nvae

                    if alt24 == 1:
                        # GOC.g:142:15: val= 'instance'
                        pass 
                        val=self.match(self.input, 69, self.FOLLOW_69_in_methodElement1112) 
                        stream_69.add(val)


                    elif alt24 == 2:
                        # GOC.g:142:30: val= 'static'
                        pass 
                        val=self.match(self.input, 70, self.FOLLOW_70_in_methodElement1116) 
                        stream_70.add(val)



                    char_literal139=self.match(self.input, 62, self.FOLLOW_62_in_methodElement1119) 
                    stream_62.add(char_literal139)

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
                    INHERITANCE140=self.match(self.input, INHERITANCE, self.FOLLOW_INHERITANCE_in_methodElement1135) 
                    stream_INHERITANCE.add(INHERITANCE140)
                    char_literal141=self.match(self.input, 65, self.FOLLOW_65_in_methodElement1137) 
                    stream_65.add(char_literal141)
                    # GOC.g:144:21: (val= 'final' | val= 'virtual' | val= 'abstract' )
                    alt25 = 3
                    LA25 = self.input.LA(1)
                    if LA25 == 71:
                        alt25 = 1
                    elif LA25 == 72:
                        alt25 = 2
                    elif LA25 == ABSTRACT:
                        alt25 = 3
                    else:
                        nvae = NoViableAltException("", 25, 0, self.input)

                        raise nvae

                    if alt25 == 1:
                        # GOC.g:144:22: val= 'final'
                        pass 
                        val=self.match(self.input, 71, self.FOLLOW_71_in_methodElement1142) 
                        stream_71.add(val)


                    elif alt25 == 2:
                        # GOC.g:144:34: val= 'virtual'
                        pass 
                        val=self.match(self.input, 72, self.FOLLOW_72_in_methodElement1146) 
                        stream_72.add(val)


                    elif alt25 == 3:
                        # GOC.g:144:48: val= 'abstract'
                        pass 
                        val=self.match(self.input, ABSTRACT, self.FOLLOW_ABSTRACT_in_methodElement1150) 
                        stream_ABSTRACT.add(val)



                    char_literal142=self.match(self.input, 62, self.FOLLOW_62_in_methodElement1153) 
                    stream_62.add(char_literal142)

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

        PARAMETER143 = None
        ID144 = None
        char_literal145 = None
        string_literal146 = None
        char_literal147 = None
        char_literal149 = None
        char_literal151 = None
        INIT_PROPERTIES152 = None
        char_literal153 = None
        char_literal155 = None
        typeArg148 = None

        parameterElement150 = None

        init_prop154 = None


        PARAMETER143_tree = None
        ID144_tree = None
        char_literal145_tree = None
        string_literal146_tree = None
        char_literal147_tree = None
        char_literal149_tree = None
        char_literal151_tree = None
        INIT_PROPERTIES152_tree = None
        char_literal153_tree = None
        char_literal155_tree = None
        stream_INIT_PROPERTIES = RewriteRuleTokenStream(self._adaptor, "token INIT_PROPERTIES")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_61 = RewriteRuleTokenStream(self._adaptor, "token 61")
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
                    PARAMETER143=self.match(self.input, PARAMETER, self.FOLLOW_PARAMETER_in_constructorElement1175) 
                    stream_PARAMETER.add(PARAMETER143)
                    ID144=self.match(self.input, ID, self.FOLLOW_ID_in_constructorElement1177) 
                    stream_ID.add(ID144)
                    char_literal145=self.match(self.input, 60, self.FOLLOW_60_in_constructorElement1179) 
                    stream_60.add(char_literal145)
                    string_literal146=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_constructorElement1181) 
                    stream_TYPE.add(string_literal146)
                    char_literal147=self.match(self.input, 65, self.FOLLOW_65_in_constructorElement1183) 
                    stream_65.add(char_literal147)
                    self._state.following.append(self.FOLLOW_typeArg_in_constructorElement1185)
                    typeArg148 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg148.tree)
                    char_literal149=self.match(self.input, 62, self.FOLLOW_62_in_constructorElement1187) 
                    stream_62.add(char_literal149)
                    # GOC.g:149:44: ( parameterElement )?
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == MODIFIERS) :
                        alt27 = 1
                    elif (LA27_0 == 73) and ((self.classMember_stack[-1].with_constructor)):
                        alt27 = 1
                    if alt27 == 1:
                        # GOC.g:149:44: parameterElement
                        pass 
                        self._state.following.append(self.FOLLOW_parameterElement_in_constructorElement1189)
                        parameterElement150 = self.parameterElement()

                        self._state.following.pop()
                        stream_parameterElement.add(parameterElement150.tree)



                    char_literal151=self.match(self.input, 61, self.FOLLOW_61_in_constructorElement1192) 
                    stream_61.add(char_literal151)

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

                    INIT_PROPERTIES152=self.match(self.input, INIT_PROPERTIES, self.FOLLOW_INIT_PROPERTIES_in_constructorElement1217) 
                    stream_INIT_PROPERTIES.add(INIT_PROPERTIES152)
                    char_literal153=self.match(self.input, 60, self.FOLLOW_60_in_constructorElement1219) 
                    stream_60.add(char_literal153)
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
                            self._state.following.append(self.FOLLOW_init_prop_in_constructorElement1221)
                            init_prop154 = self.init_prop()

                            self._state.following.pop()
                            stream_init_prop.add(init_prop154.tree)


                        else:
                            if cnt28 >= 1:
                                break #loop28

                            eee = EarlyExitException(28, self.input)
                            raise eee

                        cnt28 += 1
                    char_literal155=self.match(self.input, 61, self.FOLLOW_61_in_constructorElement1224) 
                    stream_61.add(char_literal155)

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

        string_literal157 = None
        char_literal158 = None
        ID159 = None
        char_literal160 = None
        modifiers156 = None


        string_literal157_tree = None
        char_literal158_tree = None
        ID159_tree = None
        char_literal160_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_73 = RewriteRuleTokenStream(self._adaptor, "token 73")

        try:
            try:
                # GOC.g:156:5: ( modifiers | {...}? => 'bind_property' ':' ID ';' -> ^( BIND_PROPERTY ID ) )
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == MODIFIERS) :
                    alt30 = 1
                elif (LA30_0 == 73) and ((self.classMember_stack[-1].with_constructor)):
                    alt30 = 2
                else:
                    nvae = NoViableAltException("", 30, 0, self.input)

                    raise nvae

                if alt30 == 1:
                    # GOC.g:156:9: modifiers
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_modifiers_in_parameterElement1251)
                    modifiers156 = self.modifiers()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, modifiers156.tree)


                elif alt30 == 2:
                    # GOC.g:157:9: {...}? => 'bind_property' ':' ID ';'
                    pass 
                    if not ((self.classMember_stack[-1].with_constructor)):
                        raise FailedPredicateException(self.input, "parameterElement", "$classMember::with_constructor")

                    string_literal157=self.match(self.input, 73, self.FOLLOW_73_in_parameterElement1264) 
                    stream_73.add(string_literal157)
                    char_literal158=self.match(self.input, 65, self.FOLLOW_65_in_parameterElement1266) 
                    stream_65.add(char_literal158)
                    ID159=self.match(self.input, ID, self.FOLLOW_ID_in_parameterElement1268) 
                    stream_ID.add(ID159)
                    char_literal160=self.match(self.input, 62, self.FOLLOW_62_in_parameterElement1270) 
                    stream_62.add(char_literal160)

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
        char_literal161 = None
        char_literal162 = None
        char_literal163 = None
        char_literal164 = None
        char_literal165 = None
        enum = None


        name_tree = None
        value_tree = None
        code_tree = None
        char_literal161_tree = None
        char_literal162_tree = None
        char_literal163_tree = None
        char_literal164_tree = None
        char_literal165_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_74 = RewriteRuleTokenStream(self._adaptor, "token 74")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")
        stream_typeName = RewriteRuleSubtreeStream(self._adaptor, "rule typeName")
        try:
            try:
                # GOC.g:161:5: (name= ID ':' value= STRING ';' -> ^( INIT_PROPERTY $name $value) | name= ID ':' enum= typeName '.' code= ID ';' -> ^( INIT_PROPERTY $name $enum $code) )
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == ID) :
                    LA31_1 = self.input.LA(2)

                    if (LA31_1 == 65) :
                        LA31_2 = self.input.LA(3)

                        if (LA31_2 == STRING) :
                            alt31 = 1
                        elif (LA31_2 == ID or (76 <= LA31_2 <= 81) or (94 <= LA31_2 <= 96) or LA31_2 == 99) :
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
                    name=self.match(self.input, ID, self.FOLLOW_ID_in_init_prop1299) 
                    stream_ID.add(name)
                    char_literal161=self.match(self.input, 65, self.FOLLOW_65_in_init_prop1301) 
                    stream_65.add(char_literal161)
                    value=self.match(self.input, STRING, self.FOLLOW_STRING_in_init_prop1305) 
                    stream_STRING.add(value)
                    char_literal162=self.match(self.input, 62, self.FOLLOW_62_in_init_prop1307) 
                    stream_62.add(char_literal162)

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
                    name=self.match(self.input, ID, self.FOLLOW_ID_in_init_prop1336) 
                    stream_ID.add(name)
                    char_literal163=self.match(self.input, 65, self.FOLLOW_65_in_init_prop1338) 
                    stream_65.add(char_literal163)
                    self._state.following.append(self.FOLLOW_typeName_in_init_prop1342)
                    enum = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(enum.tree)
                    char_literal164=self.match(self.input, 74, self.FOLLOW_74_in_init_prop1344) 
                    stream_74.add(char_literal164)
                    code=self.match(self.input, ID, self.FOLLOW_ID_in_init_prop1348) 
                    stream_ID.add(code)
                    char_literal165=self.match(self.input, 62, self.FOLLOW_62_in_init_prop1350) 
                    stream_62.add(char_literal165)

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

        MODIFIERS166 = None
        char_literal167 = None
        string_literal168 = None
        char_literal169 = None

        MODIFIERS166_tree = None
        char_literal167_tree = None
        string_literal168_tree = None
        char_literal169_tree = None
        stream_MODIFIERS = RewriteRuleTokenStream(self._adaptor, "token MODIFIERS")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_75 = RewriteRuleTokenStream(self._adaptor, "token 75")

        try:
            try:
                # GOC.g:168:2: ( MODIFIERS ':' 'const' ';' -> ^( MODIFIERS 'const' ) )
                # GOC.g:168:4: MODIFIERS ':' 'const' ';'
                pass 
                MODIFIERS166=self.match(self.input, MODIFIERS, self.FOLLOW_MODIFIERS_in_modifiers1384) 
                stream_MODIFIERS.add(MODIFIERS166)
                char_literal167=self.match(self.input, 65, self.FOLLOW_65_in_modifiers1386) 
                stream_65.add(char_literal167)
                string_literal168=self.match(self.input, 75, self.FOLLOW_75_in_modifiers1388) 
                stream_75.add(string_literal168)
                char_literal169=self.match(self.input, 62, self.FOLLOW_62_in_modifiers1390) 
                stream_62.add(char_literal169)

                # AST Rewrite
                # elements: 75, MODIFIERS
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

                self._adaptor.addChild(root_1, stream_75.nextNode())

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
        string_literal170 = None
        char_literal171 = None
        char_literal172 = None
        string_literal173 = None
        char_literal174 = None
        char_literal175 = None
        string_literal176 = None
        char_literal177 = None
        STRING178 = None
        char_literal179 = None
        string_literal180 = None
        char_literal181 = None
        ID182 = None
        char_literal183 = None
        string_literal184 = None
        char_literal185 = None
        GTYPENAME186 = None
        char_literal187 = None
        char_literal189 = None
        char_literal190 = None
        string_literal191 = None
        char_literal192 = None
        STRING193 = None
        char_literal194 = None
        string_literal195 = None
        char_literal196 = None
        char_literal197 = None
        char_literal198 = None
        string_literal199 = None
        char_literal200 = None
        STRING201 = None
        char_literal202 = None
        string_literal203 = None
        char_literal204 = None
        char_literal205 = None
        char_literal206 = None
        string_literal207 = None
        char_literal208 = None
        STRING209 = None
        char_literal210 = None
        string_literal211 = None
        char_literal212 = None
        char_literal213 = None
        char_literal214 = None
        AUTO_CREATE215 = None
        char_literal216 = None
        enum = None

        typeName188 = None


        val_tree = None
        code_tree = None
        string_literal170_tree = None
        char_literal171_tree = None
        char_literal172_tree = None
        string_literal173_tree = None
        char_literal174_tree = None
        char_literal175_tree = None
        string_literal176_tree = None
        char_literal177_tree = None
        STRING178_tree = None
        char_literal179_tree = None
        string_literal180_tree = None
        char_literal181_tree = None
        ID182_tree = None
        char_literal183_tree = None
        string_literal184_tree = None
        char_literal185_tree = None
        GTYPENAME186_tree = None
        char_literal187_tree = None
        char_literal189_tree = None
        char_literal190_tree = None
        string_literal191_tree = None
        char_literal192_tree = None
        STRING193_tree = None
        char_literal194_tree = None
        string_literal195_tree = None
        char_literal196_tree = None
        char_literal197_tree = None
        char_literal198_tree = None
        string_literal199_tree = None
        char_literal200_tree = None
        STRING201_tree = None
        char_literal202_tree = None
        string_literal203_tree = None
        char_literal204_tree = None
        char_literal205_tree = None
        char_literal206_tree = None
        string_literal207_tree = None
        char_literal208_tree = None
        STRING209_tree = None
        char_literal210_tree = None
        string_literal211_tree = None
        char_literal212_tree = None
        char_literal213_tree = None
        char_literal214_tree = None
        AUTO_CREATE215_tree = None
        char_literal216_tree = None
        stream_79 = RewriteRuleTokenStream(self._adaptor, "token 79")
        stream_78 = RewriteRuleTokenStream(self._adaptor, "token 78")
        stream_77 = RewriteRuleTokenStream(self._adaptor, "token 77")
        stream_GTYPENAME = RewriteRuleTokenStream(self._adaptor, "token GTYPENAME")
        stream_GTYPE = RewriteRuleTokenStream(self._adaptor, "token GTYPE")
        stream_82 = RewriteRuleTokenStream(self._adaptor, "token 82")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_83 = RewriteRuleTokenStream(self._adaptor, "token 83")
        stream_80 = RewriteRuleTokenStream(self._adaptor, "token 80")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_81 = RewriteRuleTokenStream(self._adaptor, "token 81")
        stream_86 = RewriteRuleTokenStream(self._adaptor, "token 86")
        stream_87 = RewriteRuleTokenStream(self._adaptor, "token 87")
        stream_TYPE = RewriteRuleTokenStream(self._adaptor, "token TYPE")
        stream_84 = RewriteRuleTokenStream(self._adaptor, "token 84")
        stream_85 = RewriteRuleTokenStream(self._adaptor, "token 85")
        stream_93 = RewriteRuleTokenStream(self._adaptor, "token 93")
        stream_92 = RewriteRuleTokenStream(self._adaptor, "token 92")
        stream_91 = RewriteRuleTokenStream(self._adaptor, "token 91")
        stream_90 = RewriteRuleTokenStream(self._adaptor, "token 90")
        stream_74 = RewriteRuleTokenStream(self._adaptor, "token 74")
        stream_88 = RewriteRuleTokenStream(self._adaptor, "token 88")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")
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
                    string_literal170=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_propertyElement1414) 
                    stream_TYPE.add(string_literal170)
                    char_literal171=self.match(self.input, 65, self.FOLLOW_65_in_propertyElement1416) 
                    stream_65.add(char_literal171)
                    # GOC.g:172:20: (val= 'boolean' | val= 'integer' | val= 'float' | val= 'double' | val= 'string' | val= 'pointer' | val= 'object' | val= 'enumeration' )
                    alt32 = 8
                    LA32 = self.input.LA(1)
                    if LA32 == 76:
                        alt32 = 1
                    elif LA32 == 77:
                        alt32 = 2
                    elif LA32 == 78:
                        alt32 = 3
                    elif LA32 == 79:
                        alt32 = 4
                    elif LA32 == 80:
                        alt32 = 5
                    elif LA32 == 81:
                        alt32 = 6
                    elif LA32 == 82:
                        alt32 = 7
                    elif LA32 == 83:
                        alt32 = 8
                    else:
                        nvae = NoViableAltException("", 32, 0, self.input)

                        raise nvae

                    if alt32 == 1:
                        # GOC.g:172:21: val= 'boolean'
                        pass 
                        val=self.match(self.input, 76, self.FOLLOW_76_in_propertyElement1421) 
                        stream_76.add(val)


                    elif alt32 == 2:
                        # GOC.g:172:35: val= 'integer'
                        pass 
                        val=self.match(self.input, 77, self.FOLLOW_77_in_propertyElement1425) 
                        stream_77.add(val)


                    elif alt32 == 3:
                        # GOC.g:172:49: val= 'float'
                        pass 
                        val=self.match(self.input, 78, self.FOLLOW_78_in_propertyElement1429) 
                        stream_78.add(val)


                    elif alt32 == 4:
                        # GOC.g:172:61: val= 'double'
                        pass 
                        val=self.match(self.input, 79, self.FOLLOW_79_in_propertyElement1433) 
                        stream_79.add(val)


                    elif alt32 == 5:
                        # GOC.g:173:5: val= 'string'
                        pass 
                        val=self.match(self.input, 80, self.FOLLOW_80_in_propertyElement1442) 
                        stream_80.add(val)


                    elif alt32 == 6:
                        # GOC.g:173:18: val= 'pointer'
                        pass 
                        val=self.match(self.input, 81, self.FOLLOW_81_in_propertyElement1446) 
                        stream_81.add(val)


                    elif alt32 == 7:
                        # GOC.g:173:32: val= 'object'
                        pass 
                        val=self.match(self.input, 82, self.FOLLOW_82_in_propertyElement1450) 
                        stream_82.add(val)


                    elif alt32 == 8:
                        # GOC.g:173:45: val= 'enumeration'
                        pass 
                        val=self.match(self.input, 83, self.FOLLOW_83_in_propertyElement1454) 
                        stream_83.add(val)



                    char_literal172=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1457) 
                    stream_62.add(char_literal172)

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
                    string_literal173=self.match(self.input, 84, self.FOLLOW_84_in_propertyElement1481) 
                    stream_84.add(string_literal173)
                    char_literal174=self.match(self.input, 65, self.FOLLOW_65_in_propertyElement1483) 
                    stream_65.add(char_literal174)
                    # GOC.g:175:22: (val= 'read-only' | val= 'initial-write' | val= 'read-write' )
                    alt33 = 3
                    LA33 = self.input.LA(1)
                    if LA33 == 85:
                        alt33 = 1
                    elif LA33 == 86:
                        alt33 = 2
                    elif LA33 == 87:
                        alt33 = 3
                    else:
                        nvae = NoViableAltException("", 33, 0, self.input)

                        raise nvae

                    if alt33 == 1:
                        # GOC.g:175:23: val= 'read-only'
                        pass 
                        val=self.match(self.input, 85, self.FOLLOW_85_in_propertyElement1488) 
                        stream_85.add(val)


                    elif alt33 == 2:
                        # GOC.g:175:39: val= 'initial-write'
                        pass 
                        val=self.match(self.input, 86, self.FOLLOW_86_in_propertyElement1492) 
                        stream_86.add(val)


                    elif alt33 == 3:
                        # GOC.g:175:59: val= 'read-write'
                        pass 
                        val=self.match(self.input, 87, self.FOLLOW_87_in_propertyElement1496) 
                        stream_87.add(val)



                    char_literal175=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1499) 
                    stream_62.add(char_literal175)

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
                    string_literal176=self.match(self.input, 88, self.FOLLOW_88_in_propertyElement1523) 
                    stream_88.add(string_literal176)
                    char_literal177=self.match(self.input, 65, self.FOLLOW_65_in_propertyElement1525) 
                    stream_65.add(char_literal177)
                    STRING178=self.match(self.input, STRING, self.FOLLOW_STRING_in_propertyElement1527) 
                    stream_STRING.add(STRING178)
                    char_literal179=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1529) 
                    stream_62.add(char_literal179)

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
                    string_literal180=self.match(self.input, GTYPE, self.FOLLOW_GTYPE_in_propertyElement1547) 
                    stream_GTYPE.add(string_literal180)
                    char_literal181=self.match(self.input, 65, self.FOLLOW_65_in_propertyElement1549) 
                    stream_65.add(char_literal181)
                    ID182=self.match(self.input, ID, self.FOLLOW_ID_in_propertyElement1551) 
                    stream_ID.add(ID182)
                    char_literal183=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1553) 
                    stream_62.add(char_literal183)

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
                    string_literal184=self.match(self.input, GTYPE, self.FOLLOW_GTYPE_in_propertyElement1576) 
                    stream_GTYPE.add(string_literal184)
                    char_literal185=self.match(self.input, 65, self.FOLLOW_65_in_propertyElement1578) 
                    stream_65.add(char_literal185)
                    GTYPENAME186=self.match(self.input, GTYPENAME, self.FOLLOW_GTYPENAME_in_propertyElement1580) 
                    stream_GTYPENAME.add(GTYPENAME186)
                    char_literal187=self.match(self.input, 89, self.FOLLOW_89_in_propertyElement1582) 
                    stream_89.add(char_literal187)
                    self._state.following.append(self.FOLLOW_typeName_in_propertyElement1584)
                    typeName188 = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(typeName188.tree)
                    char_literal189=self.match(self.input, 90, self.FOLLOW_90_in_propertyElement1586) 
                    stream_90.add(char_literal189)
                    char_literal190=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1588) 
                    stream_62.add(char_literal190)

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
                    string_literal191=self.match(self.input, 91, self.FOLLOW_91_in_propertyElement1615) 
                    stream_91.add(string_literal191)
                    char_literal192=self.match(self.input, 65, self.FOLLOW_65_in_propertyElement1617) 
                    stream_65.add(char_literal192)
                    STRING193=self.match(self.input, STRING, self.FOLLOW_STRING_in_propertyElement1619) 
                    stream_STRING.add(STRING193)
                    char_literal194=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1621) 
                    stream_62.add(char_literal194)

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
                    string_literal195=self.match(self.input, 91, self.FOLLOW_91_in_propertyElement1637) 
                    stream_91.add(string_literal195)
                    char_literal196=self.match(self.input, 65, self.FOLLOW_65_in_propertyElement1639) 
                    stream_65.add(char_literal196)
                    self._state.following.append(self.FOLLOW_typeName_in_propertyElement1643)
                    enum = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(enum.tree)
                    char_literal197=self.match(self.input, 74, self.FOLLOW_74_in_propertyElement1645) 
                    stream_74.add(char_literal197)
                    code=self.match(self.input, ID, self.FOLLOW_ID_in_propertyElement1649) 
                    stream_ID.add(code)
                    char_literal198=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1651) 
                    stream_62.add(char_literal198)

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
                    string_literal199=self.match(self.input, 92, self.FOLLOW_92_in_propertyElement1673) 
                    stream_92.add(string_literal199)
                    char_literal200=self.match(self.input, 65, self.FOLLOW_65_in_propertyElement1675) 
                    stream_65.add(char_literal200)
                    STRING201=self.match(self.input, STRING, self.FOLLOW_STRING_in_propertyElement1677) 
                    stream_STRING.add(STRING201)
                    char_literal202=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1679) 
                    stream_62.add(char_literal202)

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
                    string_literal203=self.match(self.input, 92, self.FOLLOW_92_in_propertyElement1695) 
                    stream_92.add(string_literal203)
                    char_literal204=self.match(self.input, 65, self.FOLLOW_65_in_propertyElement1697) 
                    stream_65.add(char_literal204)
                    self._state.following.append(self.FOLLOW_typeName_in_propertyElement1701)
                    enum = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(enum.tree)
                    char_literal205=self.match(self.input, 74, self.FOLLOW_74_in_propertyElement1703) 
                    stream_74.add(char_literal205)
                    code=self.match(self.input, ID, self.FOLLOW_ID_in_propertyElement1707) 
                    stream_ID.add(code)
                    char_literal206=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1709) 
                    stream_62.add(char_literal206)

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
                    string_literal207=self.match(self.input, 93, self.FOLLOW_93_in_propertyElement1731) 
                    stream_93.add(string_literal207)
                    char_literal208=self.match(self.input, 65, self.FOLLOW_65_in_propertyElement1733) 
                    stream_65.add(char_literal208)
                    STRING209=self.match(self.input, STRING, self.FOLLOW_STRING_in_propertyElement1735) 
                    stream_STRING.add(STRING209)
                    char_literal210=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1737) 
                    stream_62.add(char_literal210)

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
                    string_literal211=self.match(self.input, 93, self.FOLLOW_93_in_propertyElement1753) 
                    stream_93.add(string_literal211)
                    char_literal212=self.match(self.input, 65, self.FOLLOW_65_in_propertyElement1755) 
                    stream_65.add(char_literal212)
                    self._state.following.append(self.FOLLOW_typeName_in_propertyElement1759)
                    enum = self.typeName()

                    self._state.following.pop()
                    stream_typeName.add(enum.tree)
                    char_literal213=self.match(self.input, 74, self.FOLLOW_74_in_propertyElement1761) 
                    stream_74.add(char_literal213)
                    code=self.match(self.input, ID, self.FOLLOW_ID_in_propertyElement1765) 
                    stream_ID.add(code)
                    char_literal214=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1767) 
                    stream_62.add(char_literal214)

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

                    AUTO_CREATE215=self.match(self.input, AUTO_CREATE, self.FOLLOW_AUTO_CREATE_in_propertyElement1789)

                    AUTO_CREATE215_tree = self._adaptor.createWithPayload(AUTO_CREATE215)
                    root_0 = self._adaptor.becomeRoot(AUTO_CREATE215_tree, root_0)

                    char_literal216=self.match(self.input, 62, self.FOLLOW_62_in_propertyElement1792)

                    char_literal216_tree = self._adaptor.createWithPayload(char_literal216)
                    self._adaptor.addChild(root_0, char_literal216_tree)



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

        RESULT217 = None
        char_literal218 = None
        string_literal219 = None
        char_literal220 = None
        char_literal222 = None
        char_literal223 = None
        PARAMETER224 = None
        ID225 = None
        char_literal226 = None
        string_literal227 = None
        char_literal228 = None
        char_literal230 = None
        char_literal231 = None
        typeArg221 = None

        typeArg229 = None


        RESULT217_tree = None
        char_literal218_tree = None
        string_literal219_tree = None
        char_literal220_tree = None
        char_literal222_tree = None
        char_literal223_tree = None
        PARAMETER224_tree = None
        ID225_tree = None
        char_literal226_tree = None
        string_literal227_tree = None
        char_literal228_tree = None
        char_literal230_tree = None
        char_literal231_tree = None
        stream_RESULT = RewriteRuleTokenStream(self._adaptor, "token RESULT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_61 = RewriteRuleTokenStream(self._adaptor, "token 61")
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
                    RESULT217=self.match(self.input, RESULT, self.FOLLOW_RESULT_in_signalElement1811) 
                    stream_RESULT.add(RESULT217)
                    char_literal218=self.match(self.input, 60, self.FOLLOW_60_in_signalElement1813) 
                    stream_60.add(char_literal218)
                    string_literal219=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_signalElement1815) 
                    stream_TYPE.add(string_literal219)
                    char_literal220=self.match(self.input, 65, self.FOLLOW_65_in_signalElement1817) 
                    stream_65.add(char_literal220)
                    self._state.following.append(self.FOLLOW_typeArg_in_signalElement1819)
                    typeArg221 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg221.tree)
                    char_literal222=self.match(self.input, 62, self.FOLLOW_62_in_signalElement1821) 
                    stream_62.add(char_literal222)
                    char_literal223=self.match(self.input, 61, self.FOLLOW_61_in_signalElement1823) 
                    stream_61.add(char_literal223)

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
                    PARAMETER224=self.match(self.input, PARAMETER, self.FOLLOW_PARAMETER_in_signalElement1841) 
                    stream_PARAMETER.add(PARAMETER224)
                    ID225=self.match(self.input, ID, self.FOLLOW_ID_in_signalElement1843) 
                    stream_ID.add(ID225)
                    char_literal226=self.match(self.input, 60, self.FOLLOW_60_in_signalElement1845) 
                    stream_60.add(char_literal226)
                    string_literal227=self.match(self.input, TYPE, self.FOLLOW_TYPE_in_signalElement1847) 
                    stream_TYPE.add(string_literal227)
                    char_literal228=self.match(self.input, 65, self.FOLLOW_65_in_signalElement1849) 
                    stream_65.add(char_literal228)
                    self._state.following.append(self.FOLLOW_typeArg_in_signalElement1851)
                    typeArg229 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg229.tree)
                    char_literal230=self.match(self.input, 62, self.FOLLOW_62_in_signalElement1853) 
                    stream_62.add(char_literal230)
                    char_literal231=self.match(self.input, 61, self.FOLLOW_61_in_signalElement1855) 
                    stream_61.add(char_literal231)

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
        SCOPE232 = None
        char_literal233 = None
        char_literal234 = None
        VISIBILITY235 = None
        char_literal236 = None
        char_literal237 = None

        val_tree = None
        SCOPE232_tree = None
        char_literal233_tree = None
        char_literal234_tree = None
        VISIBILITY235_tree = None
        char_literal236_tree = None
        char_literal237_tree = None
        stream_67 = RewriteRuleTokenStream(self._adaptor, "token 67")
        stream_66 = RewriteRuleTokenStream(self._adaptor, "token 66")
        stream_69 = RewriteRuleTokenStream(self._adaptor, "token 69")
        stream_68 = RewriteRuleTokenStream(self._adaptor, "token 68")
        stream_VISIBILITY = RewriteRuleTokenStream(self._adaptor, "token VISIBILITY")
        stream_SCOPE = RewriteRuleTokenStream(self._adaptor, "token SCOPE")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_70 = RewriteRuleTokenStream(self._adaptor, "token 70")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")

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
                    SCOPE232=self.match(self.input, SCOPE, self.FOLLOW_SCOPE_in_attributeElement1879) 
                    stream_SCOPE.add(SCOPE232)
                    char_literal233=self.match(self.input, 65, self.FOLLOW_65_in_attributeElement1881) 
                    stream_65.add(char_literal233)
                    # GOC.g:197:14: (val= 'static' | val= 'instance' )
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == 70) :
                        alt36 = 1
                    elif (LA36_0 == 69) :
                        alt36 = 2
                    else:
                        nvae = NoViableAltException("", 36, 0, self.input)

                        raise nvae

                    if alt36 == 1:
                        # GOC.g:197:15: val= 'static'
                        pass 
                        val=self.match(self.input, 70, self.FOLLOW_70_in_attributeElement1886) 
                        stream_70.add(val)


                    elif alt36 == 2:
                        # GOC.g:197:28: val= 'instance'
                        pass 
                        val=self.match(self.input, 69, self.FOLLOW_69_in_attributeElement1890) 
                        stream_69.add(val)



                    char_literal234=self.match(self.input, 62, self.FOLLOW_62_in_attributeElement1893) 
                    stream_62.add(char_literal234)

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
                    VISIBILITY235=self.match(self.input, VISIBILITY, self.FOLLOW_VISIBILITY_in_attributeElement1907) 
                    stream_VISIBILITY.add(VISIBILITY235)
                    char_literal236=self.match(self.input, 65, self.FOLLOW_65_in_attributeElement1909) 
                    stream_65.add(char_literal236)
                    # GOC.g:198:19: (val= 'public' | val= 'protected' | val= 'private' )
                    alt37 = 3
                    LA37 = self.input.LA(1)
                    if LA37 == 66:
                        alt37 = 1
                    elif LA37 == 67:
                        alt37 = 2
                    elif LA37 == 68:
                        alt37 = 3
                    else:
                        nvae = NoViableAltException("", 37, 0, self.input)

                        raise nvae

                    if alt37 == 1:
                        # GOC.g:198:20: val= 'public'
                        pass 
                        val=self.match(self.input, 66, self.FOLLOW_66_in_attributeElement1914) 
                        stream_66.add(val)


                    elif alt37 == 2:
                        # GOC.g:198:33: val= 'protected'
                        pass 
                        val=self.match(self.input, 67, self.FOLLOW_67_in_attributeElement1918) 
                        stream_67.add(val)


                    elif alt37 == 3:
                        # GOC.g:198:49: val= 'private'
                        pass 
                        val=self.match(self.input, 68, self.FOLLOW_68_in_attributeElement1922) 
                        stream_68.add(val)



                    char_literal237=self.match(self.input, 62, self.FOLLOW_62_in_attributeElement1925) 
                    stream_62.add(char_literal237)

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
        string_literal239 = None
        string_literal240 = None
        string_literal241 = None
        string_literal242 = None
        typePath238 = None


        val_tree = None
        string_literal239_tree = None
        string_literal240_tree = None
        string_literal241_tree = None
        string_literal242_tree = None
        stream_79 = RewriteRuleTokenStream(self._adaptor, "token 79")
        stream_96 = RewriteRuleTokenStream(self._adaptor, "token 96")
        stream_78 = RewriteRuleTokenStream(self._adaptor, "token 78")
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_77 = RewriteRuleTokenStream(self._adaptor, "token 77")
        stream_94 = RewriteRuleTokenStream(self._adaptor, "token 94")
        stream_80 = RewriteRuleTokenStream(self._adaptor, "token 80")
        stream_81 = RewriteRuleTokenStream(self._adaptor, "token 81")
        stream_76 = RewriteRuleTokenStream(self._adaptor, "token 76")
        stream_typePath = RewriteRuleSubtreeStream(self._adaptor, "rule typePath")
        try:
            try:
                # GOC.g:202:2: ( typePath -> ^( TYPE_NAME typePath ) | ( 'unsigned ' )? 'integer' -> ^( TYPE_NAME ( 'unsigned ' )? 'integer' ) | ( 'unsigned ' )? 'long' -> ^( TYPE_NAME ( 'unsigned ' )? 'long' ) | (val= 'null' | val= 'boolean' | val= 'string' | val= 'float' | val= 'double' | val= 'pointer' ) -> ^( TYPE_NAME $val) )
                alt42 = 4
                LA42 = self.input.LA(1)
                if LA42 == ID or LA42 == 99:
                    alt42 = 1
                elif LA42 == 94:
                    LA42_2 = self.input.LA(2)

                    if (LA42_2 == 77) :
                        alt42 = 2
                    elif (LA42_2 == 95) :
                        alt42 = 3
                    else:
                        nvae = NoViableAltException("", 42, 2, self.input)

                        raise nvae

                elif LA42 == 77:
                    alt42 = 2
                elif LA42 == 95:
                    alt42 = 3
                elif LA42 == 76 or LA42 == 78 or LA42 == 79 or LA42 == 80 or LA42 == 81 or LA42 == 96:
                    alt42 = 4
                else:
                    nvae = NoViableAltException("", 42, 0, self.input)

                    raise nvae

                if alt42 == 1:
                    # GOC.g:202:6: typePath
                    pass 
                    self._state.following.append(self.FOLLOW_typePath_in_typeName1947)
                    typePath238 = self.typePath()

                    self._state.following.pop()
                    stream_typePath.add(typePath238.tree)

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

                    if (LA39_0 == 94) :
                        alt39 = 1
                    if alt39 == 1:
                        # GOC.g:203:6: 'unsigned '
                        pass 
                        string_literal239=self.match(self.input, 94, self.FOLLOW_94_in_typeName1962) 
                        stream_94.add(string_literal239)



                    string_literal240=self.match(self.input, 77, self.FOLLOW_77_in_typeName1965) 
                    stream_77.add(string_literal240)

                    # AST Rewrite
                    # elements: 94, 77
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
                    if stream_94.hasNext():
                        self._adaptor.addChild(root_1, stream_94.nextNode())


                    stream_94.reset();
                    self._adaptor.addChild(root_1, stream_77.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt42 == 3:
                    # GOC.g:204:6: ( 'unsigned ' )? 'long'
                    pass 
                    # GOC.g:204:6: ( 'unsigned ' )?
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == 94) :
                        alt40 = 1
                    if alt40 == 1:
                        # GOC.g:204:6: 'unsigned '
                        pass 
                        string_literal241=self.match(self.input, 94, self.FOLLOW_94_in_typeName1983) 
                        stream_94.add(string_literal241)



                    string_literal242=self.match(self.input, 95, self.FOLLOW_95_in_typeName1986) 
                    stream_95.add(string_literal242)

                    # AST Rewrite
                    # elements: 95, 94
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
                    if stream_94.hasNext():
                        self._adaptor.addChild(root_1, stream_94.nextNode())


                    stream_94.reset();
                    self._adaptor.addChild(root_1, stream_95.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt42 == 4:
                    # GOC.g:205:4: (val= 'null' | val= 'boolean' | val= 'string' | val= 'float' | val= 'double' | val= 'pointer' )
                    pass 
                    # GOC.g:205:4: (val= 'null' | val= 'boolean' | val= 'string' | val= 'float' | val= 'double' | val= 'pointer' )
                    alt41 = 6
                    LA41 = self.input.LA(1)
                    if LA41 == 96:
                        alt41 = 1
                    elif LA41 == 76:
                        alt41 = 2
                    elif LA41 == 80:
                        alt41 = 3
                    elif LA41 == 78:
                        alt41 = 4
                    elif LA41 == 79:
                        alt41 = 5
                    elif LA41 == 81:
                        alt41 = 6
                    else:
                        nvae = NoViableAltException("", 41, 0, self.input)

                        raise nvae

                    if alt41 == 1:
                        # GOC.g:205:5: val= 'null'
                        pass 
                        val=self.match(self.input, 96, self.FOLLOW_96_in_typeName2005) 
                        stream_96.add(val)


                    elif alt41 == 2:
                        # GOC.g:206:6: val= 'boolean'
                        pass 
                        val=self.match(self.input, 76, self.FOLLOW_76_in_typeName2014) 
                        stream_76.add(val)


                    elif alt41 == 3:
                        # GOC.g:207:4: val= 'string'
                        pass 
                        val=self.match(self.input, 80, self.FOLLOW_80_in_typeName2021) 
                        stream_80.add(val)


                    elif alt41 == 4:
                        # GOC.g:208:4: val= 'float'
                        pass 
                        val=self.match(self.input, 78, self.FOLLOW_78_in_typeName2028) 
                        stream_78.add(val)


                    elif alt41 == 5:
                        # GOC.g:209:4: val= 'double'
                        pass 
                        val=self.match(self.input, 79, self.FOLLOW_79_in_typeName2035) 
                        stream_79.add(val)


                    elif alt41 == 6:
                        # GOC.g:210:6: val= 'pointer'
                        pass 
                        val=self.match(self.input, 81, self.FOLLOW_81_in_typeName2044) 
                        stream_81.add(val)




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

        string_literal244 = None
        char_literal245 = None
        char_literal247 = None
        string_literal248 = None
        char_literal249 = None
        char_literal251 = None
        typeName243 = None

        typeArg246 = None

        typeArg250 = None


        string_literal244_tree = None
        char_literal245_tree = None
        char_literal247_tree = None
        string_literal248_tree = None
        char_literal249_tree = None
        char_literal251_tree = None
        stream_98 = RewriteRuleTokenStream(self._adaptor, "token 98")
        stream_97 = RewriteRuleTokenStream(self._adaptor, "token 97")
        stream_90 = RewriteRuleTokenStream(self._adaptor, "token 90")
        stream_89 = RewriteRuleTokenStream(self._adaptor, "token 89")
        stream_typeArg = RewriteRuleSubtreeStream(self._adaptor, "rule typeArg")
        try:
            try:
                # GOC.g:214:5: ( typeName | 'ref' '(' typeArg ')' -> ^( REF_TO typeArg ) | 'list' '(' typeArg ')' -> ^( LIST_OF typeArg ) )
                alt43 = 3
                LA43 = self.input.LA(1)
                if LA43 == ID or LA43 == 76 or LA43 == 77 or LA43 == 78 or LA43 == 79 or LA43 == 80 or LA43 == 81 or LA43 == 94 or LA43 == 95 or LA43 == 96 or LA43 == 99:
                    alt43 = 1
                elif LA43 == 97:
                    alt43 = 2
                elif LA43 == 98:
                    alt43 = 3
                else:
                    nvae = NoViableAltException("", 43, 0, self.input)

                    raise nvae

                if alt43 == 1:
                    # GOC.g:214:9: typeName
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_typeName_in_typeArg2070)
                    typeName243 = self.typeName()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, typeName243.tree)


                elif alt43 == 2:
                    # GOC.g:215:9: 'ref' '(' typeArg ')'
                    pass 
                    string_literal244=self.match(self.input, 97, self.FOLLOW_97_in_typeArg2080) 
                    stream_97.add(string_literal244)
                    char_literal245=self.match(self.input, 89, self.FOLLOW_89_in_typeArg2082) 
                    stream_89.add(char_literal245)
                    self._state.following.append(self.FOLLOW_typeArg_in_typeArg2084)
                    typeArg246 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg246.tree)
                    char_literal247=self.match(self.input, 90, self.FOLLOW_90_in_typeArg2086) 
                    stream_90.add(char_literal247)

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
                    string_literal248=self.match(self.input, 98, self.FOLLOW_98_in_typeArg2104) 
                    stream_98.add(string_literal248)
                    char_literal249=self.match(self.input, 89, self.FOLLOW_89_in_typeArg2106) 
                    stream_89.add(char_literal249)
                    self._state.following.append(self.FOLLOW_typeArg_in_typeArg2108)
                    typeArg250 = self.typeArg()

                    self._state.following.pop()
                    stream_typeArg.add(typeArg250.tree)
                    char_literal251=self.match(self.input, 90, self.FOLLOW_90_in_typeArg2110) 
                    stream_90.add(char_literal251)

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

        string_literal252 = None
        ID253 = None
        string_literal254 = None
        ID255 = None
        string_literal256 = None
        ID257 = None

        string_literal252_tree = None
        ID253_tree = None
        string_literal254_tree = None
        ID255_tree = None
        string_literal256_tree = None
        ID257_tree = None

        try:
            try:
                # GOC.g:220:5: ( ( '::' ID '::' )? ( ID '::' )* ID )
                # GOC.g:220:9: ( '::' ID '::' )? ( ID '::' )* ID
                pass 
                root_0 = self._adaptor.nil()

                # GOC.g:220:9: ( '::' ID '::' )?
                alt44 = 2
                LA44_0 = self.input.LA(1)

                if (LA44_0 == 99) :
                    alt44 = 1
                if alt44 == 1:
                    # GOC.g:220:10: '::' ID '::'
                    pass 
                    string_literal252=self.match(self.input, 99, self.FOLLOW_99_in_typePath2138)

                    string_literal252_tree = self._adaptor.createWithPayload(string_literal252)
                    self._adaptor.addChild(root_0, string_literal252_tree)

                    ID253=self.match(self.input, ID, self.FOLLOW_ID_in_typePath2140)

                    ID253_tree = self._adaptor.createWithPayload(ID253)
                    self._adaptor.addChild(root_0, ID253_tree)

                    string_literal254=self.match(self.input, 99, self.FOLLOW_99_in_typePath2142)

                    string_literal254_tree = self._adaptor.createWithPayload(string_literal254)
                    self._adaptor.addChild(root_0, string_literal254_tree)




                # GOC.g:220:24: ( ID '::' )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == ID) :
                        LA45_1 = self.input.LA(2)

                        if (LA45_1 == 99) :
                            alt45 = 1




                    if alt45 == 1:
                        # GOC.g:220:25: ID '::'
                        pass 
                        ID255=self.match(self.input, ID, self.FOLLOW_ID_in_typePath2146)

                        ID255_tree = self._adaptor.createWithPayload(ID255)
                        self._adaptor.addChild(root_0, ID255_tree)

                        string_literal256=self.match(self.input, 99, self.FOLLOW_99_in_typePath2148)

                        string_literal256_tree = self._adaptor.createWithPayload(string_literal256)
                        self._adaptor.addChild(root_0, string_literal256_tree)



                    else:
                        break #loop45
                ID257=self.match(self.input, ID, self.FOLLOW_ID_in_typePath2152)

                ID257_tree = self._adaptor.createWithPayload(ID257)
                self._adaptor.addChild(root_0, ID257_tree)




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
        char_literal258 = None
        part2 = None
        list_part2 = None

        part1_tree = None
        char_literal258_tree = None
        part2_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_100 = RewriteRuleTokenStream(self._adaptor, "token 100")

        try:
            try:
                # GOC.g:350:5: (part1= ID ( '-' part2+= ID )* -> ^( SIGNAL_ID $part1 ( $part2)* ) )
                # GOC.g:350:9: part1= ID ( '-' part2+= ID )*
                pass 
                part1=self.match(self.input, ID, self.FOLLOW_ID_in_signalID2755) 
                stream_ID.add(part1)
                # GOC.g:350:18: ( '-' part2+= ID )*
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == 100) :
                        alt46 = 1


                    if alt46 == 1:
                        # GOC.g:350:19: '-' part2+= ID
                        pass 
                        char_literal258=self.match(self.input, 100, self.FOLLOW_100_in_signalID2758) 
                        stream_100.add(char_literal258)
                        part2=self.match(self.input, ID, self.FOLLOW_ID_in_signalID2762) 
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
        u"\1\33\3\uffff\4\101\1\uffff\4\24\10\uffff"
        )

    DFA34_max = DFA.unpack(
        u"\1\135\3\uffff\4\101\1\uffff\1\57\3\143\10\uffff"
        )

    DFA34_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\4\uffff\1\14\4\uffff\1\4\1\5\1\6\1\7\1\10"
        u"\1\11\1\12\1\13"
        )

    DFA34_special = DFA.unpack(
        u"\25\uffff"
        )

            
    DFA34_transition = [
        DFA.unpack(u"\1\4\10\uffff\1\1\13\uffff\1\10\43\uffff\1\2\3\uffff"
        u"\1\3\2\uffff\1\5\1\6\1\7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\11"),
        DFA.unpack(u"\1\12"),
        DFA.unpack(u"\1\13"),
        DFA.unpack(u"\1\14"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\15\32\uffff\1\16"),
        DFA.unpack(u"\1\20\30\uffff\1\17\36\uffff\6\20\14\uffff\3\20\2\uffff"
        u"\1\20"),
        DFA.unpack(u"\1\22\30\uffff\1\21\36\uffff\6\22\14\uffff\3\22\2\uffff"
        u"\1\22"),
        DFA.unpack(u"\1\24\30\uffff\1\23\36\uffff\6\24\14\uffff\3\24\2\uffff"
        u"\1\24"),
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


 

    FOLLOW_stmt_in_defFile143 = frozenset([1, 21, 22, 23, 24, 26, 27, 52, 57])
    FOLLOW_classDef_in_stmt165 = frozenset([1])
    FOLLOW_intfDef_in_stmt170 = frozenset([1])
    FOLLOW_errorDomainDef_in_stmt177 = frozenset([1])
    FOLLOW_enumDef_in_stmt184 = frozenset([1])
    FOLLOW_flagsDef_in_stmt191 = frozenset([1])
    FOLLOW_packageDef_in_stmt196 = frozenset([1])
    FOLLOW_typeDecl_in_stmt203 = frozenset([1])
    FOLLOW_includeStmt_in_stmt210 = frozenset([1])
    FOLLOW_57_in_includeStmt226 = frozenset([58])
    FOLLOW_58_in_includeStmt228 = frozenset([19])
    FOLLOW_INCFILE_PATH_in_includeStmt230 = frozenset([59])
    FOLLOW_59_in_includeStmt232 = frozenset([1])
    FOLLOW_PACKAGE_in_packageDef254 = frozenset([20])
    FOLLOW_ID_in_packageDef256 = frozenset([60])
    FOLLOW_60_in_packageDef258 = frozenset([21, 22, 23, 24, 26, 27, 52, 61])
    FOLLOW_packageElement_in_packageDef260 = frozenset([21, 22, 23, 24, 26, 27, 52, 61])
    FOLLOW_61_in_packageDef263 = frozenset([1])
    FOLLOW_packageDef_in_packageElement288 = frozenset([1])
    FOLLOW_classDef_in_packageElement293 = frozenset([1])
    FOLLOW_intfDef_in_packageElement298 = frozenset([1])
    FOLLOW_errorDomainDef_in_packageElement305 = frozenset([1])
    FOLLOW_enumDef_in_packageElement312 = frozenset([1])
    FOLLOW_flagsDef_in_packageElement319 = frozenset([1])
    FOLLOW_typeDecl_in_packageElement326 = frozenset([1])
    FOLLOW_GOBJECT_in_classDef337 = frozenset([20])
    FOLLOW_ID_in_classDef341 = frozenset([60, 62])
    FOLLOW_60_in_classDef344 = frozenset([28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 61])
    FOLLOW_classMember_in_classDef346 = frozenset([28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 61])
    FOLLOW_61_in_classDef349 = frozenset([1])
    FOLLOW_62_in_classDef351 = frozenset([1])
    FOLLOW_GINTERFACE_in_intfDef378 = frozenset([20])
    FOLLOW_ID_in_intfDef382 = frozenset([60, 62])
    FOLLOW_60_in_intfDef385 = frozenset([30, 33, 38, 61])
    FOLLOW_intfMember_in_intfDef387 = frozenset([30, 33, 38, 61])
    FOLLOW_61_in_intfDef390 = frozenset([1])
    FOLLOW_62_in_intfDef392 = frozenset([1])
    FOLLOW_ERROR_DOMAIN_in_errorDomainDef423 = frozenset([20])
    FOLLOW_ID_in_errorDomainDef425 = frozenset([60])
    FOLLOW_60_in_errorDomainDef427 = frozenset([63])
    FOLLOW_errorDomainElement_in_errorDomainDef429 = frozenset([61, 63])
    FOLLOW_61_in_errorDomainDef432 = frozenset([1])
    FOLLOW_63_in_errorDomainElement467 = frozenset([20])
    FOLLOW_ID_in_errorDomainElement469 = frozenset([62])
    FOLLOW_62_in_errorDomainElement471 = frozenset([1])
    FOLLOW_ENUMERATION_in_enumDef496 = frozenset([20])
    FOLLOW_ID_in_enumDef498 = frozenset([60])
    FOLLOW_60_in_enumDef500 = frozenset([63])
    FOLLOW_enumElement_in_enumDef502 = frozenset([61, 63])
    FOLLOW_61_in_enumDef505 = frozenset([1])
    FOLLOW_63_in_enumElement540 = frozenset([20])
    FOLLOW_ID_in_enumElement542 = frozenset([60, 62])
    FOLLOW_62_in_enumElement545 = frozenset([1])
    FOLLOW_60_in_enumElement547 = frozenset([64])
    FOLLOW_64_in_enumElement549 = frozenset([65])
    FOLLOW_65_in_enumElement551 = frozenset([25])
    FOLLOW_INT_in_enumElement553 = frozenset([62])
    FOLLOW_62_in_enumElement555 = frozenset([61])
    FOLLOW_61_in_enumElement557 = frozenset([1])
    FOLLOW_FLAGS_in_flagsDef593 = frozenset([20])
    FOLLOW_ID_in_flagsDef595 = frozenset([60])
    FOLLOW_60_in_flagsDef597 = frozenset([63])
    FOLLOW_flagsElement_in_flagsDef599 = frozenset([61, 63])
    FOLLOW_61_in_flagsDef602 = frozenset([1])
    FOLLOW_63_in_flagsElement637 = frozenset([20])
    FOLLOW_ID_in_flagsElement639 = frozenset([62])
    FOLLOW_62_in_flagsElement641 = frozenset([1])
    FOLLOW_GTYPE_in_typeDecl666 = frozenset([20])
    FOLLOW_ID_in_typeDecl668 = frozenset([62])
    FOLLOW_62_in_typeDecl670 = frozenset([1])
    FOLLOW_SUPER_in_classMember701 = frozenset([20, 76, 77, 78, 79, 80, 81, 94, 95, 96, 99])
    FOLLOW_typeName_in_classMember703 = frozenset([62])
    FOLLOW_62_in_classMember705 = frozenset([1])
    FOLLOW_ABSTRACT_in_classMember721 = frozenset([62])
    FOLLOW_62_in_classMember724 = frozenset([1])
    FOLLOW_PREFIX_in_classMember731 = frozenset([20])
    FOLLOW_ID_in_classMember733 = frozenset([62])
    FOLLOW_62_in_classMember735 = frozenset([1])
    FOLLOW_IMPLEMENTS_in_classMember748 = frozenset([20, 76, 77, 78, 79, 80, 81, 94, 95, 96, 99])
    FOLLOW_typeName_in_classMember750 = frozenset([62])
    FOLLOW_62_in_classMember752 = frozenset([1])
    FOLLOW_CONSTRUCTOR_in_classMember772 = frozenset([60])
    FOLLOW_60_in_classMember774 = frozenset([43, 44, 61])
    FOLLOW_constructorElement_in_classMember776 = frozenset([43, 44, 61])
    FOLLOW_61_in_classMember779 = frozenset([1])
    FOLLOW_METHOD_in_classMember807 = frozenset([20])
    FOLLOW_ID_in_classMember809 = frozenset([60])
    FOLLOW_60_in_classMember811 = frozenset([39, 40, 41, 42, 43, 44, 61])
    FOLLOW_methodElement_in_classMember813 = frozenset([39, 40, 41, 42, 43, 44, 61])
    FOLLOW_61_in_classMember816 = frozenset([1])
    FOLLOW_OVERRIDE_in_classMember833 = frozenset([20])
    FOLLOW_ID_in_classMember835 = frozenset([62])
    FOLLOW_62_in_classMember837 = frozenset([1])
    FOLLOW_ATTRIBUTE_in_classMember850 = frozenset([20])
    FOLLOW_ID_in_classMember852 = frozenset([60])
    FOLLOW_60_in_classMember854 = frozenset([36])
    FOLLOW_TYPE_in_classMember856 = frozenset([65])
    FOLLOW_65_in_classMember858 = frozenset([20, 76, 77, 78, 79, 80, 81, 94, 95, 96, 97, 98, 99])
    FOLLOW_typeArg_in_classMember860 = frozenset([62])
    FOLLOW_62_in_classMember862 = frozenset([40, 41, 61])
    FOLLOW_attributeElement_in_classMember864 = frozenset([40, 41, 61])
    FOLLOW_61_in_classMember867 = frozenset([1])
    FOLLOW_PROPERTY_in_classMember886 = frozenset([20])
    FOLLOW_ID_in_classMember888 = frozenset([60])
    FOLLOW_60_in_classMember890 = frozenset([27, 36, 48, 84, 88, 91, 92, 93])
    FOLLOW_propertyElement_in_classMember892 = frozenset([27, 36, 48, 61, 84, 88, 91, 92, 93])
    FOLLOW_61_in_classMember895 = frozenset([1])
    FOLLOW_SIGNAL_in_classMember911 = frozenset([20])
    FOLLOW_signalID_in_classMember913 = frozenset([60])
    FOLLOW_60_in_classMember915 = frozenset([39, 43, 61])
    FOLLOW_signalElement_in_classMember917 = frozenset([39, 43, 61])
    FOLLOW_61_in_classMember920 = frozenset([1])
    FOLLOW_PREFIX_in_intfMember943 = frozenset([20])
    FOLLOW_ID_in_intfMember945 = frozenset([62])
    FOLLOW_62_in_intfMember947 = frozenset([1])
    FOLLOW_METHOD_in_intfMember962 = frozenset([20])
    FOLLOW_ID_in_intfMember964 = frozenset([60])
    FOLLOW_60_in_intfMember966 = frozenset([39, 40, 41, 42, 43, 44, 61])
    FOLLOW_methodElement_in_intfMember968 = frozenset([39, 40, 41, 42, 43, 44, 61])
    FOLLOW_61_in_intfMember971 = frozenset([1])
    FOLLOW_SIGNAL_in_intfMember992 = frozenset([20])
    FOLLOW_signalID_in_intfMember994 = frozenset([60])
    FOLLOW_60_in_intfMember996 = frozenset([39, 43, 61])
    FOLLOW_signalElement_in_intfMember998 = frozenset([39, 43, 61])
    FOLLOW_61_in_intfMember1001 = frozenset([1])
    FOLLOW_RESULT_in_resultDef1024 = frozenset([60])
    FOLLOW_60_in_resultDef1026 = frozenset([36])
    FOLLOW_TYPE_in_resultDef1028 = frozenset([65])
    FOLLOW_65_in_resultDef1030 = frozenset([20, 76, 77, 78, 79, 80, 81, 94, 95, 96, 97, 98, 99])
    FOLLOW_typeArg_in_resultDef1032 = frozenset([62])
    FOLLOW_62_in_resultDef1034 = frozenset([46, 61])
    FOLLOW_modifiers_in_resultDef1036 = frozenset([61])
    FOLLOW_61_in_resultDef1039 = frozenset([1])
    FOLLOW_constructorElement_in_methodElement1062 = frozenset([1])
    FOLLOW_resultDef_in_methodElement1067 = frozenset([1])
    FOLLOW_VISIBILITY_in_methodElement1072 = frozenset([65])
    FOLLOW_65_in_methodElement1074 = frozenset([66, 67, 68])
    FOLLOW_66_in_methodElement1079 = frozenset([62])
    FOLLOW_67_in_methodElement1083 = frozenset([62])
    FOLLOW_68_in_methodElement1087 = frozenset([62])
    FOLLOW_62_in_methodElement1090 = frozenset([1])
    FOLLOW_SCOPE_in_methodElement1105 = frozenset([65])
    FOLLOW_65_in_methodElement1107 = frozenset([69, 70])
    FOLLOW_69_in_methodElement1112 = frozenset([62])
    FOLLOW_70_in_methodElement1116 = frozenset([62])
    FOLLOW_62_in_methodElement1119 = frozenset([1])
    FOLLOW_INHERITANCE_in_methodElement1135 = frozenset([65])
    FOLLOW_65_in_methodElement1137 = frozenset([29, 71, 72])
    FOLLOW_71_in_methodElement1142 = frozenset([62])
    FOLLOW_72_in_methodElement1146 = frozenset([62])
    FOLLOW_ABSTRACT_in_methodElement1150 = frozenset([62])
    FOLLOW_62_in_methodElement1153 = frozenset([1])
    FOLLOW_PARAMETER_in_constructorElement1175 = frozenset([20])
    FOLLOW_ID_in_constructorElement1177 = frozenset([60])
    FOLLOW_60_in_constructorElement1179 = frozenset([36])
    FOLLOW_TYPE_in_constructorElement1181 = frozenset([65])
    FOLLOW_65_in_constructorElement1183 = frozenset([20, 76, 77, 78, 79, 80, 81, 94, 95, 96, 97, 98, 99])
    FOLLOW_typeArg_in_constructorElement1185 = frozenset([62])
    FOLLOW_62_in_constructorElement1187 = frozenset([46, 61, 73])
    FOLLOW_parameterElement_in_constructorElement1189 = frozenset([61])
    FOLLOW_61_in_constructorElement1192 = frozenset([1])
    FOLLOW_INIT_PROPERTIES_in_constructorElement1217 = frozenset([60])
    FOLLOW_60_in_constructorElement1219 = frozenset([20])
    FOLLOW_init_prop_in_constructorElement1221 = frozenset([20, 61])
    FOLLOW_61_in_constructorElement1224 = frozenset([1])
    FOLLOW_modifiers_in_parameterElement1251 = frozenset([1])
    FOLLOW_73_in_parameterElement1264 = frozenset([65])
    FOLLOW_65_in_parameterElement1266 = frozenset([20])
    FOLLOW_ID_in_parameterElement1268 = frozenset([62])
    FOLLOW_62_in_parameterElement1270 = frozenset([1])
    FOLLOW_ID_in_init_prop1299 = frozenset([65])
    FOLLOW_65_in_init_prop1301 = frozenset([45])
    FOLLOW_STRING_in_init_prop1305 = frozenset([62])
    FOLLOW_62_in_init_prop1307 = frozenset([1])
    FOLLOW_ID_in_init_prop1336 = frozenset([65])
    FOLLOW_65_in_init_prop1338 = frozenset([20, 76, 77, 78, 79, 80, 81, 94, 95, 96, 99])
    FOLLOW_typeName_in_init_prop1342 = frozenset([74])
    FOLLOW_74_in_init_prop1344 = frozenset([20])
    FOLLOW_ID_in_init_prop1348 = frozenset([62])
    FOLLOW_62_in_init_prop1350 = frozenset([1])
    FOLLOW_MODIFIERS_in_modifiers1384 = frozenset([65])
    FOLLOW_65_in_modifiers1386 = frozenset([75])
    FOLLOW_75_in_modifiers1388 = frozenset([62])
    FOLLOW_62_in_modifiers1390 = frozenset([1])
    FOLLOW_TYPE_in_propertyElement1414 = frozenset([65])
    FOLLOW_65_in_propertyElement1416 = frozenset([76, 77, 78, 79, 80, 81, 82, 83])
    FOLLOW_76_in_propertyElement1421 = frozenset([62])
    FOLLOW_77_in_propertyElement1425 = frozenset([62])
    FOLLOW_78_in_propertyElement1429 = frozenset([62])
    FOLLOW_79_in_propertyElement1433 = frozenset([62])
    FOLLOW_80_in_propertyElement1442 = frozenset([62])
    FOLLOW_81_in_propertyElement1446 = frozenset([62])
    FOLLOW_82_in_propertyElement1450 = frozenset([62])
    FOLLOW_83_in_propertyElement1454 = frozenset([62])
    FOLLOW_62_in_propertyElement1457 = frozenset([1])
    FOLLOW_84_in_propertyElement1481 = frozenset([65])
    FOLLOW_65_in_propertyElement1483 = frozenset([85, 86, 87])
    FOLLOW_85_in_propertyElement1488 = frozenset([62])
    FOLLOW_86_in_propertyElement1492 = frozenset([62])
    FOLLOW_87_in_propertyElement1496 = frozenset([62])
    FOLLOW_62_in_propertyElement1499 = frozenset([1])
    FOLLOW_88_in_propertyElement1523 = frozenset([65])
    FOLLOW_65_in_propertyElement1525 = frozenset([45])
    FOLLOW_STRING_in_propertyElement1527 = frozenset([62])
    FOLLOW_62_in_propertyElement1529 = frozenset([1])
    FOLLOW_GTYPE_in_propertyElement1547 = frozenset([65])
    FOLLOW_65_in_propertyElement1549 = frozenset([20])
    FOLLOW_ID_in_propertyElement1551 = frozenset([62])
    FOLLOW_62_in_propertyElement1553 = frozenset([1])
    FOLLOW_GTYPE_in_propertyElement1576 = frozenset([65])
    FOLLOW_65_in_propertyElement1578 = frozenset([47])
    FOLLOW_GTYPENAME_in_propertyElement1580 = frozenset([89])
    FOLLOW_89_in_propertyElement1582 = frozenset([20, 76, 77, 78, 79, 80, 81, 94, 95, 96, 99])
    FOLLOW_typeName_in_propertyElement1584 = frozenset([90])
    FOLLOW_90_in_propertyElement1586 = frozenset([62])
    FOLLOW_62_in_propertyElement1588 = frozenset([1])
    FOLLOW_91_in_propertyElement1615 = frozenset([65])
    FOLLOW_65_in_propertyElement1617 = frozenset([45])
    FOLLOW_STRING_in_propertyElement1619 = frozenset([62])
    FOLLOW_62_in_propertyElement1621 = frozenset([1])
    FOLLOW_91_in_propertyElement1637 = frozenset([65])
    FOLLOW_65_in_propertyElement1639 = frozenset([20, 76, 77, 78, 79, 80, 81, 94, 95, 96, 99])
    FOLLOW_typeName_in_propertyElement1643 = frozenset([74])
    FOLLOW_74_in_propertyElement1645 = frozenset([20])
    FOLLOW_ID_in_propertyElement1649 = frozenset([62])
    FOLLOW_62_in_propertyElement1651 = frozenset([1])
    FOLLOW_92_in_propertyElement1673 = frozenset([65])
    FOLLOW_65_in_propertyElement1675 = frozenset([45])
    FOLLOW_STRING_in_propertyElement1677 = frozenset([62])
    FOLLOW_62_in_propertyElement1679 = frozenset([1])
    FOLLOW_92_in_propertyElement1695 = frozenset([65])
    FOLLOW_65_in_propertyElement1697 = frozenset([20, 76, 77, 78, 79, 80, 81, 94, 95, 96, 99])
    FOLLOW_typeName_in_propertyElement1701 = frozenset([74])
    FOLLOW_74_in_propertyElement1703 = frozenset([20])
    FOLLOW_ID_in_propertyElement1707 = frozenset([62])
    FOLLOW_62_in_propertyElement1709 = frozenset([1])
    FOLLOW_93_in_propertyElement1731 = frozenset([65])
    FOLLOW_65_in_propertyElement1733 = frozenset([45])
    FOLLOW_STRING_in_propertyElement1735 = frozenset([62])
    FOLLOW_62_in_propertyElement1737 = frozenset([1])
    FOLLOW_93_in_propertyElement1753 = frozenset([65])
    FOLLOW_65_in_propertyElement1755 = frozenset([20, 76, 77, 78, 79, 80, 81, 94, 95, 96, 99])
    FOLLOW_typeName_in_propertyElement1759 = frozenset([74])
    FOLLOW_74_in_propertyElement1761 = frozenset([20])
    FOLLOW_ID_in_propertyElement1765 = frozenset([62])
    FOLLOW_62_in_propertyElement1767 = frozenset([1])
    FOLLOW_AUTO_CREATE_in_propertyElement1789 = frozenset([62])
    FOLLOW_62_in_propertyElement1792 = frozenset([1])
    FOLLOW_RESULT_in_signalElement1811 = frozenset([60])
    FOLLOW_60_in_signalElement1813 = frozenset([36])
    FOLLOW_TYPE_in_signalElement1815 = frozenset([65])
    FOLLOW_65_in_signalElement1817 = frozenset([20, 76, 77, 78, 79, 80, 81, 94, 95, 96, 97, 98, 99])
    FOLLOW_typeArg_in_signalElement1819 = frozenset([62])
    FOLLOW_62_in_signalElement1821 = frozenset([61])
    FOLLOW_61_in_signalElement1823 = frozenset([1])
    FOLLOW_PARAMETER_in_signalElement1841 = frozenset([20])
    FOLLOW_ID_in_signalElement1843 = frozenset([60])
    FOLLOW_60_in_signalElement1845 = frozenset([36])
    FOLLOW_TYPE_in_signalElement1847 = frozenset([65])
    FOLLOW_65_in_signalElement1849 = frozenset([20, 76, 77, 78, 79, 80, 81, 94, 95, 96, 97, 98, 99])
    FOLLOW_typeArg_in_signalElement1851 = frozenset([62])
    FOLLOW_62_in_signalElement1853 = frozenset([61])
    FOLLOW_61_in_signalElement1855 = frozenset([1])
    FOLLOW_SCOPE_in_attributeElement1879 = frozenset([65])
    FOLLOW_65_in_attributeElement1881 = frozenset([69, 70])
    FOLLOW_70_in_attributeElement1886 = frozenset([62])
    FOLLOW_69_in_attributeElement1890 = frozenset([62])
    FOLLOW_62_in_attributeElement1893 = frozenset([1])
    FOLLOW_VISIBILITY_in_attributeElement1907 = frozenset([65])
    FOLLOW_65_in_attributeElement1909 = frozenset([66, 67, 68])
    FOLLOW_66_in_attributeElement1914 = frozenset([62])
    FOLLOW_67_in_attributeElement1918 = frozenset([62])
    FOLLOW_68_in_attributeElement1922 = frozenset([62])
    FOLLOW_62_in_attributeElement1925 = frozenset([1])
    FOLLOW_typePath_in_typeName1947 = frozenset([1])
    FOLLOW_94_in_typeName1962 = frozenset([77])
    FOLLOW_77_in_typeName1965 = frozenset([1])
    FOLLOW_94_in_typeName1983 = frozenset([95])
    FOLLOW_95_in_typeName1986 = frozenset([1])
    FOLLOW_96_in_typeName2005 = frozenset([1])
    FOLLOW_76_in_typeName2014 = frozenset([1])
    FOLLOW_80_in_typeName2021 = frozenset([1])
    FOLLOW_78_in_typeName2028 = frozenset([1])
    FOLLOW_79_in_typeName2035 = frozenset([1])
    FOLLOW_81_in_typeName2044 = frozenset([1])
    FOLLOW_typeName_in_typeArg2070 = frozenset([1])
    FOLLOW_97_in_typeArg2080 = frozenset([89])
    FOLLOW_89_in_typeArg2082 = frozenset([20, 76, 77, 78, 79, 80, 81, 94, 95, 96, 97, 98, 99])
    FOLLOW_typeArg_in_typeArg2084 = frozenset([90])
    FOLLOW_90_in_typeArg2086 = frozenset([1])
    FOLLOW_98_in_typeArg2104 = frozenset([89])
    FOLLOW_89_in_typeArg2106 = frozenset([20, 76, 77, 78, 79, 80, 81, 94, 95, 96, 97, 98, 99])
    FOLLOW_typeArg_in_typeArg2108 = frozenset([90])
    FOLLOW_90_in_typeArg2110 = frozenset([1])
    FOLLOW_99_in_typePath2138 = frozenset([20])
    FOLLOW_ID_in_typePath2140 = frozenset([99])
    FOLLOW_99_in_typePath2142 = frozenset([20])
    FOLLOW_ID_in_typePath2146 = frozenset([99])
    FOLLOW_99_in_typePath2148 = frozenset([20])
    FOLLOW_ID_in_typePath2152 = frozenset([1])
    FOLLOW_ID_in_signalID2755 = frozenset([1, 100])
    FOLLOW_100_in_signalID2758 = frozenset([20])
    FOLLOW_ID_in_signalID2762 = frozenset([1, 100])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("GOCLexer", GOCParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
