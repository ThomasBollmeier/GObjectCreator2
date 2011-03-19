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


# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 GOC.g 2011-03-18 21:31:24

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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
GOBJECT=21
T__99=99
T__98=98
T__97=97
T__96=96
T__95=95
T__80=80
VISIBILITY=40
REF_TO=8
T__81=81
T__82=82
T__83=83
BOOLVALUE=51
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


class GOCLexer(Lexer):

    grammarFileName = "GOC.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(GOCLexer, self).__init__(input, state)


        self.dfa12 = self.DFA12(
            self, 12,
            eot = self.DFA12_eot,
            eof = self.DFA12_eof,
            min = self.DFA12_min,
            max = self.DFA12_max,
            accept = self.DFA12_accept,
            special = self.DFA12_special,
            transition = self.DFA12_transition
            )






    # $ANTLR start "T__57"
    def mT__57(self, ):

        try:
            _type = T__57
            _channel = DEFAULT_CHANNEL

            # GOC.g:7:7: ( 'include' )
            # GOC.g:7:9: 'include'
            pass 
            self.match("include")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__57"



    # $ANTLR start "T__58"
    def mT__58(self, ):

        try:
            _type = T__58
            _channel = DEFAULT_CHANNEL

            # GOC.g:8:7: ( '<' )
            # GOC.g:8:9: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__58"



    # $ANTLR start "T__59"
    def mT__59(self, ):

        try:
            _type = T__59
            _channel = DEFAULT_CHANNEL

            # GOC.g:9:7: ( '>' )
            # GOC.g:9:9: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__59"



    # $ANTLR start "T__60"
    def mT__60(self, ):

        try:
            _type = T__60
            _channel = DEFAULT_CHANNEL

            # GOC.g:10:7: ( '{' )
            # GOC.g:10:9: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__60"



    # $ANTLR start "T__61"
    def mT__61(self, ):

        try:
            _type = T__61
            _channel = DEFAULT_CHANNEL

            # GOC.g:11:7: ( '}' )
            # GOC.g:11:9: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__61"



    # $ANTLR start "T__62"
    def mT__62(self, ):

        try:
            _type = T__62
            _channel = DEFAULT_CHANNEL

            # GOC.g:12:7: ( ';' )
            # GOC.g:12:9: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__62"



    # $ANTLR start "T__63"
    def mT__63(self, ):

        try:
            _type = T__63
            _channel = DEFAULT_CHANNEL

            # GOC.g:13:7: ( 'code' )
            # GOC.g:13:9: 'code'
            pass 
            self.match("code")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__63"



    # $ANTLR start "T__64"
    def mT__64(self, ):

        try:
            _type = T__64
            _channel = DEFAULT_CHANNEL

            # GOC.g:14:7: ( 'value' )
            # GOC.g:14:9: 'value'
            pass 
            self.match("value")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__64"



    # $ANTLR start "T__65"
    def mT__65(self, ):

        try:
            _type = T__65
            _channel = DEFAULT_CHANNEL

            # GOC.g:15:7: ( ':' )
            # GOC.g:15:9: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__65"



    # $ANTLR start "T__66"
    def mT__66(self, ):

        try:
            _type = T__66
            _channel = DEFAULT_CHANNEL

            # GOC.g:16:7: ( 'public' )
            # GOC.g:16:9: 'public'
            pass 
            self.match("public")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__66"



    # $ANTLR start "T__67"
    def mT__67(self, ):

        try:
            _type = T__67
            _channel = DEFAULT_CHANNEL

            # GOC.g:17:7: ( 'protected' )
            # GOC.g:17:9: 'protected'
            pass 
            self.match("protected")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__67"



    # $ANTLR start "T__68"
    def mT__68(self, ):

        try:
            _type = T__68
            _channel = DEFAULT_CHANNEL

            # GOC.g:18:7: ( 'private' )
            # GOC.g:18:9: 'private'
            pass 
            self.match("private")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__68"



    # $ANTLR start "T__69"
    def mT__69(self, ):

        try:
            _type = T__69
            _channel = DEFAULT_CHANNEL

            # GOC.g:19:7: ( 'instance' )
            # GOC.g:19:9: 'instance'
            pass 
            self.match("instance")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__69"



    # $ANTLR start "T__70"
    def mT__70(self, ):

        try:
            _type = T__70
            _channel = DEFAULT_CHANNEL

            # GOC.g:20:7: ( 'static' )
            # GOC.g:20:9: 'static'
            pass 
            self.match("static")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__70"



    # $ANTLR start "T__71"
    def mT__71(self, ):

        try:
            _type = T__71
            _channel = DEFAULT_CHANNEL

            # GOC.g:21:7: ( 'final' )
            # GOC.g:21:9: 'final'
            pass 
            self.match("final")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__71"



    # $ANTLR start "T__72"
    def mT__72(self, ):

        try:
            _type = T__72
            _channel = DEFAULT_CHANNEL

            # GOC.g:22:7: ( 'virtual' )
            # GOC.g:22:9: 'virtual'
            pass 
            self.match("virtual")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__72"



    # $ANTLR start "T__73"
    def mT__73(self, ):

        try:
            _type = T__73
            _channel = DEFAULT_CHANNEL

            # GOC.g:23:7: ( 'bind_property' )
            # GOC.g:23:9: 'bind_property'
            pass 
            self.match("bind_property")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__73"



    # $ANTLR start "T__74"
    def mT__74(self, ):

        try:
            _type = T__74
            _channel = DEFAULT_CHANNEL

            # GOC.g:24:7: ( '.' )
            # GOC.g:24:9: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__74"



    # $ANTLR start "T__75"
    def mT__75(self, ):

        try:
            _type = T__75
            _channel = DEFAULT_CHANNEL

            # GOC.g:25:7: ( 'const' )
            # GOC.g:25:9: 'const'
            pass 
            self.match("const")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__75"



    # $ANTLR start "T__76"
    def mT__76(self, ):

        try:
            _type = T__76
            _channel = DEFAULT_CHANNEL

            # GOC.g:26:7: ( 'boolean' )
            # GOC.g:26:9: 'boolean'
            pass 
            self.match("boolean")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__76"



    # $ANTLR start "T__77"
    def mT__77(self, ):

        try:
            _type = T__77
            _channel = DEFAULT_CHANNEL

            # GOC.g:27:7: ( 'integer' )
            # GOC.g:27:9: 'integer'
            pass 
            self.match("integer")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__77"



    # $ANTLR start "T__78"
    def mT__78(self, ):

        try:
            _type = T__78
            _channel = DEFAULT_CHANNEL

            # GOC.g:28:7: ( 'float' )
            # GOC.g:28:9: 'float'
            pass 
            self.match("float")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__78"



    # $ANTLR start "T__79"
    def mT__79(self, ):

        try:
            _type = T__79
            _channel = DEFAULT_CHANNEL

            # GOC.g:29:7: ( 'double' )
            # GOC.g:29:9: 'double'
            pass 
            self.match("double")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__79"



    # $ANTLR start "T__80"
    def mT__80(self, ):

        try:
            _type = T__80
            _channel = DEFAULT_CHANNEL

            # GOC.g:30:7: ( 'string' )
            # GOC.g:30:9: 'string'
            pass 
            self.match("string")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__80"



    # $ANTLR start "T__81"
    def mT__81(self, ):

        try:
            _type = T__81
            _channel = DEFAULT_CHANNEL

            # GOC.g:31:7: ( 'pointer' )
            # GOC.g:31:9: 'pointer'
            pass 
            self.match("pointer")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__81"



    # $ANTLR start "T__82"
    def mT__82(self, ):

        try:
            _type = T__82
            _channel = DEFAULT_CHANNEL

            # GOC.g:32:7: ( 'object' )
            # GOC.g:32:9: 'object'
            pass 
            self.match("object")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__82"



    # $ANTLR start "T__83"
    def mT__83(self, ):

        try:
            _type = T__83
            _channel = DEFAULT_CHANNEL

            # GOC.g:33:7: ( 'enumeration' )
            # GOC.g:33:9: 'enumeration'
            pass 
            self.match("enumeration")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__83"



    # $ANTLR start "T__84"
    def mT__84(self, ):

        try:
            _type = T__84
            _channel = DEFAULT_CHANNEL

            # GOC.g:34:7: ( 'access' )
            # GOC.g:34:9: 'access'
            pass 
            self.match("access")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__84"



    # $ANTLR start "T__85"
    def mT__85(self, ):

        try:
            _type = T__85
            _channel = DEFAULT_CHANNEL

            # GOC.g:35:7: ( 'read-only' )
            # GOC.g:35:9: 'read-only'
            pass 
            self.match("read-only")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__85"



    # $ANTLR start "T__86"
    def mT__86(self, ):

        try:
            _type = T__86
            _channel = DEFAULT_CHANNEL

            # GOC.g:36:7: ( 'initial-write' )
            # GOC.g:36:9: 'initial-write'
            pass 
            self.match("initial-write")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__86"



    # $ANTLR start "T__87"
    def mT__87(self, ):

        try:
            _type = T__87
            _channel = DEFAULT_CHANNEL

            # GOC.g:37:7: ( 'read-write' )
            # GOC.g:37:9: 'read-write'
            pass 
            self.match("read-write")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__87"



    # $ANTLR start "T__88"
    def mT__88(self, ):

        try:
            _type = T__88
            _channel = DEFAULT_CHANNEL

            # GOC.g:38:7: ( 'description' )
            # GOC.g:38:9: 'description'
            pass 
            self.match("description")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__88"



    # $ANTLR start "T__89"
    def mT__89(self, ):

        try:
            _type = T__89
            _channel = DEFAULT_CHANNEL

            # GOC.g:39:7: ( '(' )
            # GOC.g:39:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__89"



    # $ANTLR start "T__90"
    def mT__90(self, ):

        try:
            _type = T__90
            _channel = DEFAULT_CHANNEL

            # GOC.g:40:7: ( ')' )
            # GOC.g:40:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__90"



    # $ANTLR start "T__91"
    def mT__91(self, ):

        try:
            _type = T__91
            _channel = DEFAULT_CHANNEL

            # GOC.g:41:7: ( 'min' )
            # GOC.g:41:9: 'min'
            pass 
            self.match("min")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__91"



    # $ANTLR start "T__92"
    def mT__92(self, ):

        try:
            _type = T__92
            _channel = DEFAULT_CHANNEL

            # GOC.g:42:7: ( 'max' )
            # GOC.g:42:9: 'max'
            pass 
            self.match("max")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__92"



    # $ANTLR start "T__93"
    def mT__93(self, ):

        try:
            _type = T__93
            _channel = DEFAULT_CHANNEL

            # GOC.g:43:7: ( 'default' )
            # GOC.g:43:9: 'default'
            pass 
            self.match("default")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__93"



    # $ANTLR start "T__94"
    def mT__94(self, ):

        try:
            _type = T__94
            _channel = DEFAULT_CHANNEL

            # GOC.g:44:7: ( 'unsigned ' )
            # GOC.g:44:9: 'unsigned '
            pass 
            self.match("unsigned ")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__94"



    # $ANTLR start "T__95"
    def mT__95(self, ):

        try:
            _type = T__95
            _channel = DEFAULT_CHANNEL

            # GOC.g:45:7: ( 'long' )
            # GOC.g:45:9: 'long'
            pass 
            self.match("long")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__95"



    # $ANTLR start "T__96"
    def mT__96(self, ):

        try:
            _type = T__96
            _channel = DEFAULT_CHANNEL

            # GOC.g:46:7: ( 'null' )
            # GOC.g:46:9: 'null'
            pass 
            self.match("null")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__96"



    # $ANTLR start "T__97"
    def mT__97(self, ):

        try:
            _type = T__97
            _channel = DEFAULT_CHANNEL

            # GOC.g:47:7: ( 'ref' )
            # GOC.g:47:9: 'ref'
            pass 
            self.match("ref")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__97"



    # $ANTLR start "T__98"
    def mT__98(self, ):

        try:
            _type = T__98
            _channel = DEFAULT_CHANNEL

            # GOC.g:48:7: ( 'list' )
            # GOC.g:48:9: 'list'
            pass 
            self.match("list")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__98"



    # $ANTLR start "T__99"
    def mT__99(self, ):

        try:
            _type = T__99
            _channel = DEFAULT_CHANNEL

            # GOC.g:49:7: ( '::' )
            # GOC.g:49:9: '::'
            pass 
            self.match("::")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__99"



    # $ANTLR start "T__100"
    def mT__100(self, ):

        try:
            _type = T__100
            _channel = DEFAULT_CHANNEL

            # GOC.g:50:8: ( '-' )
            # GOC.g:50:10: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__100"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # GOC.g:224:5: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' | '/*' ( options {greedy=false; } : . )* '*/' )
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 47) :
                LA4_1 = self.input.LA(2)

                if (LA4_1 == 47) :
                    alt4 = 1
                elif (LA4_1 == 42) :
                    alt4 = 2
                else:
                    nvae = NoViableAltException("", 4, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae

            if alt4 == 1:
                # GOC.g:224:9: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
                pass 
                self.match("//")
                # GOC.g:224:14: (~ ( '\\n' | '\\r' ) )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((0 <= LA1_0 <= 9) or (11 <= LA1_0 <= 12) or (14 <= LA1_0 <= 65535)) :
                        alt1 = 1


                    if alt1 == 1:
                        # GOC.g:224:14: ~ ( '\\n' | '\\r' )
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop1
                # GOC.g:224:28: ( '\\r' )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 13) :
                    alt2 = 1
                if alt2 == 1:
                    # GOC.g:224:28: '\\r'
                    pass 
                    self.match(13)



                self.match(10)
                #action start
                _channel=HIDDEN;
                #action end


            elif alt4 == 2:
                # GOC.g:225:9: '/*' ( options {greedy=false; } : . )* '*/'
                pass 
                self.match("/*")
                # GOC.g:225:14: ( options {greedy=false; } : . )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == 42) :
                        LA3_1 = self.input.LA(2)

                        if (LA3_1 == 47) :
                            alt3 = 2
                        elif ((0 <= LA3_1 <= 46) or (48 <= LA3_1 <= 65535)) :
                            alt3 = 1


                    elif ((0 <= LA3_0 <= 41) or (43 <= LA3_0 <= 65535)) :
                        alt3 = 1


                    if alt3 == 1:
                        # GOC.g:225:42: .
                        pass 
                        self.matchAny()


                    else:
                        break #loop3
                self.match("*/")
                #action start
                _channel=HIDDEN;
                #action end


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # GOC.g:228:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # GOC.g:228:9: ( ' ' | '\\t' | '\\r' | '\\n' )
            pass 
            if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "BOOLVALUE"
    def mBOOLVALUE(self, ):

        try:
            _type = BOOLVALUE
            _channel = DEFAULT_CHANNEL

            # GOC.g:236:5: ( 'true' | 'false' )
            alt5 = 2
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 116) :
                alt5 = 1
            elif (LA5_0 == 102) :
                alt5 = 2
            else:
                nvae = NoViableAltException("", 5, 0, self.input)

                raise nvae

            if alt5 == 1:
                # GOC.g:236:9: 'true'
                pass 
                self.match("true")


            elif alt5 == 2:
                # GOC.g:237:9: 'false'
                pass 
                self.match("false")


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BOOLVALUE"



    # $ANTLR start "PACKAGE"
    def mPACKAGE(self, ):

        try:
            _type = PACKAGE
            _channel = DEFAULT_CHANNEL

            # GOC.g:241:5: ( 'package' )
            # GOC.g:241:9: 'package'
            pass 
            self.match("package")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PACKAGE"



    # $ANTLR start "GOBJECT"
    def mGOBJECT(self, ):

        try:
            _type = GOBJECT
            _channel = DEFAULT_CHANNEL

            # GOC.g:245:2: ( 'gobject' )
            # GOC.g:245:4: 'gobject'
            pass 
            self.match("gobject")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GOBJECT"



    # $ANTLR start "GINTERFACE"
    def mGINTERFACE(self, ):

        try:
            _type = GINTERFACE
            _channel = DEFAULT_CHANNEL

            # GOC.g:249:2: ( 'ginterface' )
            # GOC.g:249:4: 'ginterface'
            pass 
            self.match("ginterface")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GINTERFACE"



    # $ANTLR start "GTYPE"
    def mGTYPE(self, ):

        try:
            _type = GTYPE
            _channel = DEFAULT_CHANNEL

            # GOC.g:253:5: ( 'gtype' )
            # GOC.g:253:9: 'gtype'
            pass 
            self.match("gtype")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GTYPE"



    # $ANTLR start "GTYPENAME"
    def mGTYPENAME(self, ):

        try:
            _type = GTYPENAME
            _channel = DEFAULT_CHANNEL

            # GOC.g:257:5: ( 'gtypename' )
            # GOC.g:257:9: 'gtypename'
            pass 
            self.match("gtypename")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GTYPENAME"



    # $ANTLR start "ERROR_DOMAIN"
    def mERROR_DOMAIN(self, ):

        try:
            _type = ERROR_DOMAIN
            _channel = DEFAULT_CHANNEL

            # GOC.g:261:5: ( 'gerror' )
            # GOC.g:261:9: 'gerror'
            pass 
            self.match("gerror")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ERROR_DOMAIN"



    # $ANTLR start "ENUMERATION"
    def mENUMERATION(self, ):

        try:
            _type = ENUMERATION
            _channel = DEFAULT_CHANNEL

            # GOC.g:265:5: ( 'genum' )
            # GOC.g:265:9: 'genum'
            pass 
            self.match("genum")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ENUMERATION"



    # $ANTLR start "FLAGS"
    def mFLAGS(self, ):

        try:
            _type = FLAGS
            _channel = DEFAULT_CHANNEL

            # GOC.g:269:5: ( 'gflags' )
            # GOC.g:269:9: 'gflags'
            pass 
            self.match("gflags")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FLAGS"



    # $ANTLR start "SUPER"
    def mSUPER(self, ):

        try:
            _type = SUPER
            _channel = DEFAULT_CHANNEL

            # GOC.g:273:2: ( 'super' )
            # GOC.g:273:4: 'super'
            pass 
            self.match("super")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SUPER"



    # $ANTLR start "PREFIX"
    def mPREFIX(self, ):

        try:
            _type = PREFIX
            _channel = DEFAULT_CHANNEL

            # GOC.g:277:5: ( 'prefix' )
            # GOC.g:277:9: 'prefix'
            pass 
            self.match("prefix")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PREFIX"



    # $ANTLR start "IMPLEMENTS"
    def mIMPLEMENTS(self, ):

        try:
            _type = IMPLEMENTS
            _channel = DEFAULT_CHANNEL

            # GOC.g:281:2: ( 'implements' )
            # GOC.g:281:4: 'implements'
            pass 
            self.match("implements")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IMPLEMENTS"



    # $ANTLR start "CONSTRUCTOR"
    def mCONSTRUCTOR(self, ):

        try:
            _type = CONSTRUCTOR
            _channel = DEFAULT_CHANNEL

            # GOC.g:285:2: ( 'constructor' )
            # GOC.g:285:4: 'constructor'
            pass 
            self.match("constructor")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CONSTRUCTOR"



    # $ANTLR start "METHOD"
    def mMETHOD(self, ):

        try:
            _type = METHOD
            _channel = DEFAULT_CHANNEL

            # GOC.g:289:2: ( 'method' )
            # GOC.g:289:4: 'method'
            pass 
            self.match("method")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "METHOD"



    # $ANTLR start "OVERRIDE"
    def mOVERRIDE(self, ):

        try:
            _type = OVERRIDE
            _channel = DEFAULT_CHANNEL

            # GOC.g:293:2: ( 'override' )
            # GOC.g:293:4: 'override'
            pass 
            self.match("override")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OVERRIDE"



    # $ANTLR start "PARAMETER"
    def mPARAMETER(self, ):

        try:
            _type = PARAMETER
            _channel = DEFAULT_CHANNEL

            # GOC.g:297:2: ( 'parameter' )
            # GOC.g:297:4: 'parameter'
            pass 
            self.match("parameter")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PARAMETER"



    # $ANTLR start "ATTRIBUTE"
    def mATTRIBUTE(self, ):

        try:
            _type = ATTRIBUTE
            _channel = DEFAULT_CHANNEL

            # GOC.g:301:2: ( 'attribute' )
            # GOC.g:301:4: 'attribute'
            pass 
            self.match("attribute")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ATTRIBUTE"



    # $ANTLR start "PROPERTY"
    def mPROPERTY(self, ):

        try:
            _type = PROPERTY
            _channel = DEFAULT_CHANNEL

            # GOC.g:305:2: ( 'property' )
            # GOC.g:305:4: 'property'
            pass 
            self.match("property")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PROPERTY"



    # $ANTLR start "INIT_PROPERTIES"
    def mINIT_PROPERTIES(self, ):

        try:
            _type = INIT_PROPERTIES
            _channel = DEFAULT_CHANNEL

            # GOC.g:309:5: ( 'init_properties' )
            # GOC.g:309:9: 'init_properties'
            pass 
            self.match("init_properties")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INIT_PROPERTIES"



    # $ANTLR start "SIGNAL"
    def mSIGNAL(self, ):

        try:
            _type = SIGNAL
            _channel = DEFAULT_CHANNEL

            # GOC.g:313:2: ( 'signal' )
            # GOC.g:313:4: 'signal'
            pass 
            self.match("signal")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SIGNAL"



    # $ANTLR start "RESULT"
    def mRESULT(self, ):

        try:
            _type = RESULT
            _channel = DEFAULT_CHANNEL

            # GOC.g:317:2: ( 'result' )
            # GOC.g:317:4: 'result'
            pass 
            self.match("result")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RESULT"



    # $ANTLR start "TYPE"
    def mTYPE(self, ):

        try:
            _type = TYPE
            _channel = DEFAULT_CHANNEL

            # GOC.g:320:5: ( 'type' )
            # GOC.g:320:7: 'type'
            pass 
            self.match("type")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TYPE"



    # $ANTLR start "MODIFIERS"
    def mMODIFIERS(self, ):

        try:
            _type = MODIFIERS
            _channel = DEFAULT_CHANNEL

            # GOC.g:323:2: ( 'modifiers' )
            # GOC.g:323:4: 'modifiers'
            pass 
            self.match("modifiers")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MODIFIERS"



    # $ANTLR start "SCOPE"
    def mSCOPE(self, ):

        try:
            _type = SCOPE
            _channel = DEFAULT_CHANNEL

            # GOC.g:327:2: ( 'scope' )
            # GOC.g:327:4: 'scope'
            pass 
            self.match("scope")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SCOPE"



    # $ANTLR start "VISIBILITY"
    def mVISIBILITY(self, ):

        try:
            _type = VISIBILITY
            _channel = DEFAULT_CHANNEL

            # GOC.g:331:2: ( 'visibility' )
            # GOC.g:331:4: 'visibility'
            pass 
            self.match("visibility")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VISIBILITY"



    # $ANTLR start "INHERITANCE"
    def mINHERITANCE(self, ):

        try:
            _type = INHERITANCE
            _channel = DEFAULT_CHANNEL

            # GOC.g:335:2: ( 'inheritance' )
            # GOC.g:335:4: 'inheritance'
            pass 
            self.match("inheritance")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INHERITANCE"



    # $ANTLR start "ABSTRACT"
    def mABSTRACT(self, ):

        try:
            _type = ABSTRACT
            _channel = DEFAULT_CHANNEL

            # GOC.g:339:5: ( 'abstract' )
            # GOC.g:339:9: 'abstract'
            pass 
            self.match("abstract")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ABSTRACT"



    # $ANTLR start "AUTO_CREATE"
    def mAUTO_CREATE(self, ):

        try:
            _type = AUTO_CREATE
            _channel = DEFAULT_CHANNEL

            # GOC.g:343:5: ( 'auto_create' )
            # GOC.g:343:9: 'auto_create'
            pass 
            self.match("auto_create")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AUTO_CREATE"



    # $ANTLR start "ID"
    def mID(self, ):

        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # GOC.g:346:5: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )* )
            # GOC.g:346:7: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # GOC.g:346:31: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((48 <= LA6_0 <= 57) or (65 <= LA6_0 <= 90) or LA6_0 == 95 or (97 <= LA6_0 <= 122)) :
                    alt6 = 1


                if alt6 == 1:
                    # GOC.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop6



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ID"



    # $ANTLR start "STRING"
    def mSTRING(self, ):

        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # GOC.g:354:5: ( '\"' ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )* '\"' )
            # GOC.g:354:8: '\"' ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )* '\"'
            pass 
            self.match(34)
            # GOC.g:354:12: ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )*
            while True: #loop7
                alt7 = 3
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 92) :
                    alt7 = 1
                elif ((0 <= LA7_0 <= 33) or (35 <= LA7_0 <= 91) or (93 <= LA7_0 <= 65535)) :
                    alt7 = 2


                if alt7 == 1:
                    # GOC.g:354:14: ESC_SEQ
                    pass 
                    self.mESC_SEQ()


                elif alt7 == 2:
                    # GOC.g:354:24: ~ ( '\\\\' | '\"' )
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop7
            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING"



    # $ANTLR start "INT"
    def mINT(self, ):

        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # GOC.g:357:5: ( ( '1' .. '9' ) ( '0' .. '9' )* )
            # GOC.g:357:9: ( '1' .. '9' ) ( '0' .. '9' )*
            pass 
            # GOC.g:357:9: ( '1' .. '9' )
            # GOC.g:357:10: '1' .. '9'
            pass 
            self.matchRange(49, 57)



            # GOC.g:357:19: ( '0' .. '9' )*
            while True: #loop8
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if ((48 <= LA8_0 <= 57)) :
                    alt8 = 1


                if alt8 == 1:
                    # GOC.g:357:20: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    break #loop8



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INT"



    # $ANTLR start "INCFILE_PATH"
    def mINCFILE_PATH(self, ):

        try:
            _type = INCFILE_PATH
            _channel = DEFAULT_CHANNEL

            # GOC.g:361:2: ( ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '.' | '/' )+ )
            # GOC.g:361:4: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '.' | '/' )+
            pass 
            # GOC.g:361:4: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '.' | '/' )+
            cnt9 = 0
            while True: #loop9
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if ((46 <= LA9_0 <= 57) or (65 <= LA9_0 <= 90) or LA9_0 == 95 or (97 <= LA9_0 <= 122)) :
                    alt9 = 1


                if alt9 == 1:
                    # GOC.g:
                    pass 
                    if (46 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt9 >= 1:
                        break #loop9

                    eee = EarlyExitException(9, self.input)
                    raise eee

                cnt9 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INCFILE_PATH"



    # $ANTLR start "HEX_DIGIT"
    def mHEX_DIGIT(self, ):

        try:
            # GOC.g:365:11: ( ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' ) )
            # GOC.g:365:13: ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "HEX_DIGIT"



    # $ANTLR start "ESC_SEQ"
    def mESC_SEQ(self, ):

        try:
            # GOC.g:369:5: ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | UNICODE_ESC | OCTAL_ESC )
            alt10 = 3
            LA10_0 = self.input.LA(1)

            if (LA10_0 == 92) :
                LA10 = self.input.LA(2)
                if LA10 == 34 or LA10 == 39 or LA10 == 92 or LA10 == 98 or LA10 == 102 or LA10 == 110 or LA10 == 114 or LA10 == 116:
                    alt10 = 1
                elif LA10 == 117:
                    alt10 = 2
                elif LA10 == 48 or LA10 == 49 or LA10 == 50 or LA10 == 51 or LA10 == 52 or LA10 == 53 or LA10 == 54 or LA10 == 55:
                    alt10 = 3
                else:
                    nvae = NoViableAltException("", 10, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 10, 0, self.input)

                raise nvae

            if alt10 == 1:
                # GOC.g:369:9: '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' )
                pass 
                self.match(92)
                if self.input.LA(1) == 34 or self.input.LA(1) == 39 or self.input.LA(1) == 92 or self.input.LA(1) == 98 or self.input.LA(1) == 102 or self.input.LA(1) == 110 or self.input.LA(1) == 114 or self.input.LA(1) == 116:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



            elif alt10 == 2:
                # GOC.g:370:9: UNICODE_ESC
                pass 
                self.mUNICODE_ESC()


            elif alt10 == 3:
                # GOC.g:371:9: OCTAL_ESC
                pass 
                self.mOCTAL_ESC()



        finally:

            pass

    # $ANTLR end "ESC_SEQ"



    # $ANTLR start "OCTAL_ESC"
    def mOCTAL_ESC(self, ):

        try:
            # GOC.g:376:5: ( '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) )
            alt11 = 3
            LA11_0 = self.input.LA(1)

            if (LA11_0 == 92) :
                LA11_1 = self.input.LA(2)

                if ((48 <= LA11_1 <= 51)) :
                    LA11_2 = self.input.LA(3)

                    if ((48 <= LA11_2 <= 55)) :
                        LA11_4 = self.input.LA(4)

                        if ((48 <= LA11_4 <= 55)) :
                            alt11 = 1
                        else:
                            alt11 = 2
                    else:
                        alt11 = 3
                elif ((52 <= LA11_1 <= 55)) :
                    LA11_3 = self.input.LA(3)

                    if ((48 <= LA11_3 <= 55)) :
                        alt11 = 2
                    else:
                        alt11 = 3
                else:
                    nvae = NoViableAltException("", 11, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 11, 0, self.input)

                raise nvae

            if alt11 == 1:
                # GOC.g:376:9: '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)
                # GOC.g:376:14: ( '0' .. '3' )
                # GOC.g:376:15: '0' .. '3'
                pass 
                self.matchRange(48, 51)



                # GOC.g:376:25: ( '0' .. '7' )
                # GOC.g:376:26: '0' .. '7'
                pass 
                self.matchRange(48, 55)



                # GOC.g:376:36: ( '0' .. '7' )
                # GOC.g:376:37: '0' .. '7'
                pass 
                self.matchRange(48, 55)





            elif alt11 == 2:
                # GOC.g:377:9: '\\\\' ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)
                # GOC.g:377:14: ( '0' .. '7' )
                # GOC.g:377:15: '0' .. '7'
                pass 
                self.matchRange(48, 55)



                # GOC.g:377:25: ( '0' .. '7' )
                # GOC.g:377:26: '0' .. '7'
                pass 
                self.matchRange(48, 55)





            elif alt11 == 3:
                # GOC.g:378:9: '\\\\' ( '0' .. '7' )
                pass 
                self.match(92)
                # GOC.g:378:14: ( '0' .. '7' )
                # GOC.g:378:15: '0' .. '7'
                pass 
                self.matchRange(48, 55)






        finally:

            pass

    # $ANTLR end "OCTAL_ESC"



    # $ANTLR start "UNICODE_ESC"
    def mUNICODE_ESC(self, ):

        try:
            # GOC.g:383:5: ( '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT )
            # GOC.g:383:9: '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
            pass 
            self.match(92)
            self.match(117)
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()




        finally:

            pass

    # $ANTLR end "UNICODE_ESC"



    def mTokens(self):
        # GOC.g:1:8: ( T__57 | T__58 | T__59 | T__60 | T__61 | T__62 | T__63 | T__64 | T__65 | T__66 | T__67 | T__68 | T__69 | T__70 | T__71 | T__72 | T__73 | T__74 | T__75 | T__76 | T__77 | T__78 | T__79 | T__80 | T__81 | T__82 | T__83 | T__84 | T__85 | T__86 | T__87 | T__88 | T__89 | T__90 | T__91 | T__92 | T__93 | T__94 | T__95 | T__96 | T__97 | T__98 | T__99 | T__100 | COMMENT | WS | BOOLVALUE | PACKAGE | GOBJECT | GINTERFACE | GTYPE | GTYPENAME | ERROR_DOMAIN | ENUMERATION | FLAGS | SUPER | PREFIX | IMPLEMENTS | CONSTRUCTOR | METHOD | OVERRIDE | PARAMETER | ATTRIBUTE | PROPERTY | INIT_PROPERTIES | SIGNAL | RESULT | TYPE | MODIFIERS | SCOPE | VISIBILITY | INHERITANCE | ABSTRACT | AUTO_CREATE | ID | STRING | INT | INCFILE_PATH )
        alt12 = 78
        alt12 = self.dfa12.predict(self.input)
        if alt12 == 1:
            # GOC.g:1:10: T__57
            pass 
            self.mT__57()


        elif alt12 == 2:
            # GOC.g:1:16: T__58
            pass 
            self.mT__58()


        elif alt12 == 3:
            # GOC.g:1:22: T__59
            pass 
            self.mT__59()


        elif alt12 == 4:
            # GOC.g:1:28: T__60
            pass 
            self.mT__60()


        elif alt12 == 5:
            # GOC.g:1:34: T__61
            pass 
            self.mT__61()


        elif alt12 == 6:
            # GOC.g:1:40: T__62
            pass 
            self.mT__62()


        elif alt12 == 7:
            # GOC.g:1:46: T__63
            pass 
            self.mT__63()


        elif alt12 == 8:
            # GOC.g:1:52: T__64
            pass 
            self.mT__64()


        elif alt12 == 9:
            # GOC.g:1:58: T__65
            pass 
            self.mT__65()


        elif alt12 == 10:
            # GOC.g:1:64: T__66
            pass 
            self.mT__66()


        elif alt12 == 11:
            # GOC.g:1:70: T__67
            pass 
            self.mT__67()


        elif alt12 == 12:
            # GOC.g:1:76: T__68
            pass 
            self.mT__68()


        elif alt12 == 13:
            # GOC.g:1:82: T__69
            pass 
            self.mT__69()


        elif alt12 == 14:
            # GOC.g:1:88: T__70
            pass 
            self.mT__70()


        elif alt12 == 15:
            # GOC.g:1:94: T__71
            pass 
            self.mT__71()


        elif alt12 == 16:
            # GOC.g:1:100: T__72
            pass 
            self.mT__72()


        elif alt12 == 17:
            # GOC.g:1:106: T__73
            pass 
            self.mT__73()


        elif alt12 == 18:
            # GOC.g:1:112: T__74
            pass 
            self.mT__74()


        elif alt12 == 19:
            # GOC.g:1:118: T__75
            pass 
            self.mT__75()


        elif alt12 == 20:
            # GOC.g:1:124: T__76
            pass 
            self.mT__76()


        elif alt12 == 21:
            # GOC.g:1:130: T__77
            pass 
            self.mT__77()


        elif alt12 == 22:
            # GOC.g:1:136: T__78
            pass 
            self.mT__78()


        elif alt12 == 23:
            # GOC.g:1:142: T__79
            pass 
            self.mT__79()


        elif alt12 == 24:
            # GOC.g:1:148: T__80
            pass 
            self.mT__80()


        elif alt12 == 25:
            # GOC.g:1:154: T__81
            pass 
            self.mT__81()


        elif alt12 == 26:
            # GOC.g:1:160: T__82
            pass 
            self.mT__82()


        elif alt12 == 27:
            # GOC.g:1:166: T__83
            pass 
            self.mT__83()


        elif alt12 == 28:
            # GOC.g:1:172: T__84
            pass 
            self.mT__84()


        elif alt12 == 29:
            # GOC.g:1:178: T__85
            pass 
            self.mT__85()


        elif alt12 == 30:
            # GOC.g:1:184: T__86
            pass 
            self.mT__86()


        elif alt12 == 31:
            # GOC.g:1:190: T__87
            pass 
            self.mT__87()


        elif alt12 == 32:
            # GOC.g:1:196: T__88
            pass 
            self.mT__88()


        elif alt12 == 33:
            # GOC.g:1:202: T__89
            pass 
            self.mT__89()


        elif alt12 == 34:
            # GOC.g:1:208: T__90
            pass 
            self.mT__90()


        elif alt12 == 35:
            # GOC.g:1:214: T__91
            pass 
            self.mT__91()


        elif alt12 == 36:
            # GOC.g:1:220: T__92
            pass 
            self.mT__92()


        elif alt12 == 37:
            # GOC.g:1:226: T__93
            pass 
            self.mT__93()


        elif alt12 == 38:
            # GOC.g:1:232: T__94
            pass 
            self.mT__94()


        elif alt12 == 39:
            # GOC.g:1:238: T__95
            pass 
            self.mT__95()


        elif alt12 == 40:
            # GOC.g:1:244: T__96
            pass 
            self.mT__96()


        elif alt12 == 41:
            # GOC.g:1:250: T__97
            pass 
            self.mT__97()


        elif alt12 == 42:
            # GOC.g:1:256: T__98
            pass 
            self.mT__98()


        elif alt12 == 43:
            # GOC.g:1:262: T__99
            pass 
            self.mT__99()


        elif alt12 == 44:
            # GOC.g:1:268: T__100
            pass 
            self.mT__100()


        elif alt12 == 45:
            # GOC.g:1:275: COMMENT
            pass 
            self.mCOMMENT()


        elif alt12 == 46:
            # GOC.g:1:283: WS
            pass 
            self.mWS()


        elif alt12 == 47:
            # GOC.g:1:286: BOOLVALUE
            pass 
            self.mBOOLVALUE()


        elif alt12 == 48:
            # GOC.g:1:296: PACKAGE
            pass 
            self.mPACKAGE()


        elif alt12 == 49:
            # GOC.g:1:304: GOBJECT
            pass 
            self.mGOBJECT()


        elif alt12 == 50:
            # GOC.g:1:312: GINTERFACE
            pass 
            self.mGINTERFACE()


        elif alt12 == 51:
            # GOC.g:1:323: GTYPE
            pass 
            self.mGTYPE()


        elif alt12 == 52:
            # GOC.g:1:329: GTYPENAME
            pass 
            self.mGTYPENAME()


        elif alt12 == 53:
            # GOC.g:1:339: ERROR_DOMAIN
            pass 
            self.mERROR_DOMAIN()


        elif alt12 == 54:
            # GOC.g:1:352: ENUMERATION
            pass 
            self.mENUMERATION()


        elif alt12 == 55:
            # GOC.g:1:364: FLAGS
            pass 
            self.mFLAGS()


        elif alt12 == 56:
            # GOC.g:1:370: SUPER
            pass 
            self.mSUPER()


        elif alt12 == 57:
            # GOC.g:1:376: PREFIX
            pass 
            self.mPREFIX()


        elif alt12 == 58:
            # GOC.g:1:383: IMPLEMENTS
            pass 
            self.mIMPLEMENTS()


        elif alt12 == 59:
            # GOC.g:1:394: CONSTRUCTOR
            pass 
            self.mCONSTRUCTOR()


        elif alt12 == 60:
            # GOC.g:1:406: METHOD
            pass 
            self.mMETHOD()


        elif alt12 == 61:
            # GOC.g:1:413: OVERRIDE
            pass 
            self.mOVERRIDE()


        elif alt12 == 62:
            # GOC.g:1:422: PARAMETER
            pass 
            self.mPARAMETER()


        elif alt12 == 63:
            # GOC.g:1:432: ATTRIBUTE
            pass 
            self.mATTRIBUTE()


        elif alt12 == 64:
            # GOC.g:1:442: PROPERTY
            pass 
            self.mPROPERTY()


        elif alt12 == 65:
            # GOC.g:1:451: INIT_PROPERTIES
            pass 
            self.mINIT_PROPERTIES()


        elif alt12 == 66:
            # GOC.g:1:467: SIGNAL
            pass 
            self.mSIGNAL()


        elif alt12 == 67:
            # GOC.g:1:474: RESULT
            pass 
            self.mRESULT()


        elif alt12 == 68:
            # GOC.g:1:481: TYPE
            pass 
            self.mTYPE()


        elif alt12 == 69:
            # GOC.g:1:486: MODIFIERS
            pass 
            self.mMODIFIERS()


        elif alt12 == 70:
            # GOC.g:1:496: SCOPE
            pass 
            self.mSCOPE()


        elif alt12 == 71:
            # GOC.g:1:502: VISIBILITY
            pass 
            self.mVISIBILITY()


        elif alt12 == 72:
            # GOC.g:1:513: INHERITANCE
            pass 
            self.mINHERITANCE()


        elif alt12 == 73:
            # GOC.g:1:525: ABSTRACT
            pass 
            self.mABSTRACT()


        elif alt12 == 74:
            # GOC.g:1:534: AUTO_CREATE
            pass 
            self.mAUTO_CREATE()


        elif alt12 == 75:
            # GOC.g:1:546: ID
            pass 
            self.mID()


        elif alt12 == 76:
            # GOC.g:1:549: STRING
            pass 
            self.mSTRING()


        elif alt12 == 77:
            # GOC.g:1:556: INT
            pass 
            self.mINT()


        elif alt12 == 78:
            # GOC.g:1:560: INCFILE_PATH
            pass 
            self.mINCFILE_PATH()







    # lookup tables for DFA #12

    DFA12_eot = DFA.unpack(
        u"\1\uffff\1\45\5\uffff\2\45\1\53\4\45\1\71\5\45\2\uffff\4\45\1\uffff"
        u"\1\42\1\uffff\3\45\1\uffff\1\125\1\uffff\2\45\1\uffff\4\45\2\uffff"
        u"\15\45\1\uffff\22\45\1\42\1\uffff\7\45\1\uffff\1\125\47\45\1\u00b9"
        u"\1\45\1\u00bb\1\u00bc\6\45\1\42\16\45\1\u00d2\41\45\1\uffff\1\45"
        u"\2\uffff\3\45\1\u00f8\1\u00f9\1\u00fa\1\u00fb\1\u00fc\15\45\1\uffff"
        u"\1\u010b\1\u010c\14\45\1\u0119\1\45\1\u011b\1\u011c\1\u011d\1\u00fb"
        u"\14\45\1\uffff\4\45\5\uffff\2\45\1\u0133\1\45\1\u0135\11\45\2\uffff"
        u"\2\45\1\u0141\3\45\1\u0145\3\45\1\u0149\1\u014a\1\uffff\1\u014b"
        u"\3\uffff\2\45\1\u014e\2\45\1\u0151\2\45\1\u0154\3\45\2\uffff\1"
        u"\u0158\1\u0159\5\45\1\uffff\1\u015f\1\uffff\1\u0160\1\u0161\1\45"
        u"\1\u0163\5\45\1\u0169\1\45\1\uffff\2\45\1\u016d\1\uffff\1\u016e"
        u"\1\u016f\1\45\3\uffff\1\45\1\u0172\1\uffff\1\45\1\u0174\1\uffff"
        u"\2\45\1\uffff\3\45\2\uffff\2\45\1\u017c\2\45\3\uffff\1\u017f\2"
        u"\uffff\4\45\1\uffff\2\45\1\u0186\3\uffff\2\45\1\uffff\1\45\1\uffff"
        u"\1\u018a\2\45\1\u018d\3\45\1\uffff\2\45\1\uffff\5\45\1\u0198\1"
        u"\uffff\1\u0199\2\45\1\uffff\1\45\1\u019d\1\uffff\1\45\1\u019f\1"
        u"\uffff\1\45\1\u01a1\2\45\1\u01a4\1\45\1\u01a6\2\uffff\3\45\1\uffff"
        u"\1\45\1\uffff\1\u01ab\1\uffff\1\45\1\u01ad\1\uffff\1\u01ae\1\uffff"
        u"\1\45\1\u01b0\1\u01b1\1\u01b2\1\uffff\1\45\2\uffff\1\45\3\uffff"
        u"\1\45\1\u01b6\1\45\1\uffff\1\u01b8\1\uffff"
        )

    DFA12_eof = DFA.unpack(
        u"\u01b9\uffff"
        )

    DFA12_min = DFA.unpack(
        u"\1\11\1\56\5\uffff\2\56\1\72\12\56\2\uffff\4\56\1\uffff\1\52\1"
        u"\uffff\3\56\1\uffff\1\56\1\uffff\2\56\1\uffff\4\56\2\uffff\15\56"
        u"\1\uffff\22\56\1\0\1\uffff\7\56\1\uffff\62\56\1\0\57\56\1\55\1"
        u"\uffff\1\56\2\uffff\25\56\1\uffff\40\56\1\157\4\56\5\uffff\16\56"
        u"\2\uffff\14\56\1\uffff\1\56\3\uffff\14\56\2\uffff\7\56\1\uffff"
        u"\1\56\1\uffff\4\56\1\55\6\56\1\uffff\3\56\1\uffff\3\56\3\uffff"
        u"\2\56\1\uffff\2\56\1\uffff\2\56\1\uffff\3\56\2\uffff\5\56\3\uffff"
        u"\1\56\2\uffff\4\56\1\uffff\3\56\3\uffff\2\56\1\uffff\1\56\1\uffff"
        u"\6\56\1\40\1\uffff\2\56\1\uffff\6\56\1\uffff\3\56\1\uffff\2\56"
        u"\1\uffff\2\56\1\uffff\7\56\2\uffff\3\56\1\uffff\1\56\1\uffff\1"
        u"\56\1\uffff\2\56\1\uffff\1\56\1\uffff\4\56\1\uffff\1\56\2\uffff"
        u"\1\56\3\uffff\3\56\1\uffff\1\56\1\uffff"
        )

    DFA12_max = DFA.unpack(
        u"\1\175\1\172\5\uffff\2\172\1\72\12\172\2\uffff\4\172\1\uffff\1"
        u"\57\1\uffff\3\172\1\uffff\1\172\1\uffff\2\172\1\uffff\4\172\2\uffff"
        u"\15\172\1\uffff\22\172\1\uffff\1\uffff\7\172\1\uffff\62\172\1\uffff"
        u"\60\172\1\uffff\1\172\2\uffff\25\172\1\uffff\40\172\1\167\4\172"
        u"\5\uffff\16\172\2\uffff\14\172\1\uffff\1\172\3\uffff\14\172\2\uffff"
        u"\7\172\1\uffff\1\172\1\uffff\13\172\1\uffff\3\172\1\uffff\3\172"
        u"\3\uffff\2\172\1\uffff\2\172\1\uffff\2\172\1\uffff\3\172\2\uffff"
        u"\5\172\3\uffff\1\172\2\uffff\4\172\1\uffff\3\172\3\uffff\2\172"
        u"\1\uffff\1\172\1\uffff\7\172\1\uffff\2\172\1\uffff\6\172\1\uffff"
        u"\3\172\1\uffff\2\172\1\uffff\2\172\1\uffff\7\172\2\uffff\3\172"
        u"\1\uffff\1\172\1\uffff\1\172\1\uffff\2\172\1\uffff\1\172\1\uffff"
        u"\4\172\1\uffff\1\172\2\uffff\1\172\3\uffff\3\172\1\uffff\1\172"
        u"\1\uffff"
        )

    DFA12_accept = DFA.unpack(
        u"\2\uffff\1\2\1\3\1\4\1\5\1\6\15\uffff\1\41\1\42\4\uffff\1\54\1"
        u"\uffff\1\56\3\uffff\1\114\1\uffff\1\116\2\uffff\1\113\4\uffff\1"
        u"\53\1\11\15\uffff\1\22\23\uffff\1\55\7\uffff\1\115\143\uffff\1"
        u"\51\1\uffff\1\43\1\44\25\uffff\1\7\45\uffff\1\47\1\52\1\50\1\57"
        u"\1\104\16\uffff\1\23\1\10\14\uffff\1\70\1\uffff\1\106\1\17\1\26"
        u"\14\uffff\1\35\1\37\7\uffff\1\63\1\uffff\1\66\13\uffff\1\12\3\uffff"
        u"\1\71\3\uffff\1\16\1\30\1\102\2\uffff\1\27\2\uffff\1\32\2\uffff"
        u"\1\34\3\uffff\1\103\1\74\5\uffff\1\65\1\67\1\1\1\uffff\1\25\1\36"
        u"\4\uffff\1\20\3\uffff\1\14\1\31\1\60\2\uffff\1\24\1\uffff\1\45"
        u"\7\uffff\1\61\2\uffff\1\15\6\uffff\1\100\3\uffff\1\75\2\uffff\1"
        u"\111\2\uffff\1\46\7\uffff\1\13\1\76\3\uffff\1\77\1\uffff\1\105"
        u"\1\uffff\1\64\2\uffff\1\72\1\uffff\1\107\4\uffff\1\62\1\uffff\1"
        u"\110\1\73\1\uffff\1\40\1\33\1\112\3\uffff\1\21\1\uffff\1\101"
        )

    DFA12_special = DFA.unpack(
        u"\114\uffff\1\1\73\uffff\1\0\u0130\uffff"
        )

            
    DFA12_transition = [
        DFA.unpack(u"\2\34\2\uffff\1\34\22\uffff\1\34\1\uffff\1\40\5\uffff"
        u"\1\24\1\25\3\uffff\1\32\1\16\1\33\1\42\11\41\1\11\1\6\1\2\1\uffff"
        u"\1\3\2\uffff\32\37\4\uffff\1\37\1\uffff\1\22\1\15\1\7\1\17\1\21"
        u"\1\14\1\36\1\37\1\1\2\37\1\30\1\26\1\31\1\20\1\12\1\37\1\23\1\13"
        u"\1\35\1\27\1\10\4\37\1\4\1\uffff\1\5"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\14\46"
        u"\1\44\1\43\14\46"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\16\46"
        u"\1\47\13\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\50"
        u"\7\46\1\51\21\46"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\57"
        u"\15\46\1\56\2\46\1\55\2\46\1\54\5\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\2\46"
        u"\1\63\5\46\1\62\12\46\1\60\1\61\5\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\66"
        u"\7\46\1\64\2\46\1\65\16\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\67\5\46\1\70\13\46"),
        DFA.unpack(u"\14\42\7\uffff\32\42\4\uffff\1\42\1\uffff\32\42"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\73\11\46\1\72\13\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\46"
        u"\1\74\23\46\1\75\4\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\76\14\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\46"
        u"\1\101\1\77\20\46\1\100\1\102\5\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\103\25\46"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\105"
        u"\3\46\1\106\3\46\1\104\5\46\1\107\13\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\110\14\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\112\5\46\1\111\13\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\24\46"
        u"\1\113\5\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\115\4\uffff\1\114"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\116\6\46\1\117\1\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\123\1\124\2\46\1\121\5\46\1\120\4\46\1\122\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\126\7\uffff\32\42\4\uffff\1\42\1\uffff\32"
        u"\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\2\46"
        u"\1\127\4\46\1\133\1\132\11\46\1\130\1\131\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\17\46"
        u"\1\134\12\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\3\46"
        u"\1\135\11\46\1\136\14\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\13\46"
        u"\1\137\16\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\140\1\141\7\46"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\46"
        u"\1\142\30\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\145\3\46\1\144\5\46\1\143\13\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\146\21\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\2\46"
        u"\1\147\16\46\1\150\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\151"
        u"\20\46\1\152\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\17\46"
        u"\1\153\12\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\6\46"
        u"\1\154\23\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\16\46"
        u"\1\155\13\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\156\14\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\16\46"
        u"\1\157\13\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\13\46"
        u"\1\160\16\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\161\14\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\16\46"
        u"\1\162\13\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\24\46"
        u"\1\163\5\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\5\46"
        u"\1\165\14\46\1\164\7\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\11\46"
        u"\1\166\20\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\167\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\24\46"
        u"\1\170\5\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\2\46"
        u"\1\171\27\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\172\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\22\46"
        u"\1\173\7\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\174\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\175"
        u"\4\46\1\176\14\46\1\177\7\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\u0080\14\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\27\46"
        u"\1\u0081\2\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u0082\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\3\46"
        u"\1\u0083\26\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\22\46"
        u"\1\u0084\7\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\u0085\14\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\22\46"
        u"\1\u0086\7\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\13\46"
        u"\1\u0087\16\46"),
        DFA.unpack(u"\56\115\14\u0088\7\115\32\u0088\4\115\1\u0088\1\115"
        u"\32\u0088\uff85\115"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\24\46"
        u"\1\u0089\5\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\17\46"
        u"\1\u008a\12\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\46"
        u"\1\u008b\30\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\u008c\14\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\30\46"
        u"\1\u008d\1\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\u008f\3\46\1\u008e\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\13\46"
        u"\1\u0090\16\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\126\7\uffff\32\42\4\uffff\1\42\1\uffff\32"
        u"\42"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\13\46"
        u"\1\u0091\16\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u0092\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u0093\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u0094\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u0095\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\13\46"
        u"\1\u0096\16\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u0097\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\22\46"
        u"\1\u0098\7\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\24\46"
        u"\1\u0099\5\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u009a\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\u009b\21\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\13\46"
        u"\1\u009c\16\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\17\46"
        u"\1\u009e\3\46\1\u009d\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\25\46"
        u"\1\u009f\4\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\5\46"
        u"\1\u00a0\24\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\u00a1\14\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\12\46"
        u"\1\u00a2\17\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\u00a3"
        u"\31\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u00a4\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\u00a5\21\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u00a6\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\u00a7\14\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\17\46"
        u"\1\u00a8\12\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\u00a9"
        u"\31\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\u00aa"
        u"\31\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\22\46"
        u"\1\u00ab\7\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\3\46"
        u"\1\u00ac\26\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\13\46"
        u"\1\u00ad\16\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\46"
        u"\1\u00ae\30\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\2\46"
        u"\1\u00af\27\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\u00b0"
        u"\31\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u00b1\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u00b2\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\14\46"
        u"\1\u00b3\15\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u00b4\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u00b5\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u00b6\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\16\46"
        u"\1\u00b7\13\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\3\46"
        u"\1\u00b8\26\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\24\46"
        u"\1\u00ba\5\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\7\46"
        u"\1\u00bd\22\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\u00be\21\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\u00bf\21\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\6\46"
        u"\1\u00c0\23\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u00c1\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\13\46"
        u"\1\u00c2\16\46"),
        DFA.unpack(u"\56\115\14\u0088\7\115\32\u0088\4\115\1\u0088\1\115"
        u"\32\u0088\uff85\115"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u00c3\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u00c4\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\11\46"
        u"\1\u00c5\20\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u00c6\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\17\46"
        u"\1\u00c7\12\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u00c8\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\24\46"
        u"\1\u00c9\5\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\u00ca"
        u"\31\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\24\46"
        u"\1\u00cb\5\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\u00cc"
        u"\31\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\6\46"
        u"\1\u00cd\23\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\u00cf\1\uffff\10"
        u"\46\1\u00ce\21\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u00d0\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u00d1\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u00d3\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u00d4\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\24\46"
        u"\1\u00d5\5\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\46"
        u"\1\u00d6\30\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\u00d7\21\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u00d8\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u00d9\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\u00da"
        u"\31\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\u00db\21\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u00dc\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\u00dd"
        u"\31\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\14\46"
        u"\1\u00de\15\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\u00df\21\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\u00e0\14\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u00e1\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\u00e2"
        u"\31\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u00e3\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\13\46"
        u"\1\u00e4\16\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u00e5\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u00e6\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\u00e7\1\uffff\32"
        u"\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u00e8\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\13\46"
        u"\1\u00e9\16\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u00ea\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\24\46"
        u"\1\u00eb\5\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\2\46"
        u"\1\u00ec\27\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u00ed\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u00ee\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\22\46"
        u"\1\u00ef\7\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\u00f0\21\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u00f1\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\u00f2\1\uffff\32"
        u"\46"),
        DFA.unpack(u"\1\u00f3\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff"
        u"\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\13\46"
        u"\1\u00f4\16\46"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\16\46"
        u"\1\u00f5\13\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\5\46"
        u"\1\u00f6\24\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\6\46"
        u"\1\u00f7\23\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u00fd\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u00fe\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u00ff\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\16\46"
        u"\1\u0100\13\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\14\46"
        u"\1\u0101\15\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\6\46"
        u"\1\u0102\23\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\3\46"
        u"\1\u0103\26\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\u0104\14\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u0105\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\u0106"
        u"\31\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\17\46"
        u"\1\u0107\12\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\u0108\21\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\14\46"
        u"\1\u0109\15\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u010a\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\u010d"
        u"\31\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\u010e\21\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\2\46"
        u"\1\u010f\27\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\2\46"
        u"\1\u0110\27\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u0111\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u0112\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\27\46"
        u"\1\u0113\2\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u0114\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\6\46"
        u"\1\u0115\23\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u0116\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\2\46"
        u"\1\u0117\27\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\6\46"
        u"\1\u0118\23\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\13\46"
        u"\1\u011a\16\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\17\46"
        u"\1\u011e\12\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\u011f"
        u"\31\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u0120\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\u0121\21\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\13\46"
        u"\1\u0122\16\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u0123\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\u0124\21\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u0125\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\22\46"
        u"\1\u0126\7\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\46"
        u"\1\u0127\30\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\u0128"
        u"\31\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\2\46"
        u"\1\u0129\27\46"),
        DFA.unpack(u"\1\u012a\7\uffff\1\u012b"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u012c\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\3\46"
        u"\1\u012d\26\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\u012e\21\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\u012f\14\46"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\2\46"
        u"\1\u0130\27\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u0131\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\u0132\14\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u0134\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\22\46"
        u"\1\u0136\7\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u0137\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\2\46"
        u"\1\u0138\27\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u0139\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\13\46"
        u"\1\u013a\16\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u013b\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u013c\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u013d\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\24\46"
        u"\1\u013e\5\46"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\13\46"
        u"\1\u013f\16\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\13\46"
        u"\1\u0140\16\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u0142\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u0143\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u0144\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u0146\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u0147\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u0148\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u014c\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\u014d\14\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\17\46"
        u"\1\u014f\12\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u0150\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\3\46"
        u"\1\u0152\26\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\u0153"
        u"\31\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\24\46"
        u"\1\u0155\5\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\2\46"
        u"\1\u0156\27\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u0157\10\46"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u015a\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u015b\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u015c\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\5\46"
        u"\1\u015d\24\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\u015e"
        u"\31\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u0162\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\1\u0164\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff"
        u"\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\16\46"
        u"\1\u0165\13\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\u0166"
        u"\31\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\u0167\14\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\2\46"
        u"\1\u0168\27\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\u016a\21\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u016b\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\30\46"
        u"\1\u016c\1\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u0170\25\46"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\16\46"
        u"\1\u0171\13\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u0173\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u0175\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u0176\6\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u0177\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u0178\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u0179\25\46"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u017a\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\3\46"
        u"\1\u017b\26\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\u017d"
        u"\31\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\14\46"
        u"\1\u017e\15\46"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\17\46"
        u"\1\u0180\12\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\u0181\14\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u0182\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u0183\6\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u0184\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\3\46"
        u"\1\u0185\26\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u0187\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\17\46"
        u"\1\u0188\12\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\u0189\21\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\u018b\21\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u018c\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\1\u018e"
        u"\31\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\22\46"
        u"\1\u018f\7\46"),
        DFA.unpack(u"\1\u0190\15\uffff\2\42\12\46\7\uffff\32\46\4\uffff"
        u"\1\46\1\uffff\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\2\46"
        u"\1\u0191\27\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u0192\25\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u0193\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\2\46"
        u"\1\u0194\27\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\22\46"
        u"\1\u0195\7\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\16\46"
        u"\1\u0196\13\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\30\46"
        u"\1\u0197\1\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u019a\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\16\46"
        u"\1\u019b\13\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\16\46"
        u"\1\u019c\13\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u019e\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u01a0\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u01a2\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u01a3\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u01a5\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\21\46"
        u"\1\u01a7\10\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\u01a8\14\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\15\46"
        u"\1\u01a9\14\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u01aa\25\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u01ac\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\23\46"
        u"\1\u01af\6\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\10\46"
        u"\1\u01b3\21\46"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\30\46"
        u"\1\u01b4\1\46"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\4\46"
        u"\1\u01b5\25\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\22\46"
        u"\1\u01b7\7\46"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\42\12\46\7\uffff\32\46\4\uffff\1\46\1\uffff\32\46"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #12

    class DFA12(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA12_136 = input.LA(1)

                s = -1
                if ((46 <= LA12_136 <= 57) or (65 <= LA12_136 <= 90) or LA12_136 == 95 or (97 <= LA12_136 <= 122)):
                    s = 136

                elif ((0 <= LA12_136 <= 45) or (58 <= LA12_136 <= 64) or (91 <= LA12_136 <= 94) or LA12_136 == 96 or (123 <= LA12_136 <= 65535)):
                    s = 77

                else:
                    s = 34

                if s >= 0:
                    return s
            elif s == 1: 
                LA12_76 = input.LA(1)

                s = -1
                if ((46 <= LA12_76 <= 57) or (65 <= LA12_76 <= 90) or LA12_76 == 95 or (97 <= LA12_76 <= 122)):
                    s = 136

                elif ((0 <= LA12_76 <= 45) or (58 <= LA12_76 <= 64) or (91 <= LA12_76 <= 94) or LA12_76 == 96 or (123 <= LA12_76 <= 65535)):
                    s = 77

                else:
                    s = 34

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 12, _s, input)
            self_.error(nvae)
            raise nvae
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(GOCLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
