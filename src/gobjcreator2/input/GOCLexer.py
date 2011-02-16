# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 GOC.g 2011-02-16 09:13:37

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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
VISIBILITY=40
REF_TO=8
T__81=81
T__82=82
BOOLVALUE=48
T__83=83
GINTERFACE=22
INT=25
T__85=85
T__84=84
T__87=87
T__86=86
T__89=89
T__88=88
WS=47
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


class GOCLexer(Lexer):

    grammarFileName = "GOC.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(GOCLexer, self).__init__(input, state)


        self.dfa11 = self.DFA11(
            self, 11,
            eot = self.DFA11_eot,
            eof = self.DFA11_eof,
            min = self.DFA11_min,
            max = self.DFA11_max,
            accept = self.DFA11_accept,
            special = self.DFA11_special,
            transition = self.DFA11_transition
            )






    # $ANTLR start "T__54"
    def mT__54(self, ):

        try:
            _type = T__54
            _channel = DEFAULT_CHANNEL

            # GOC.g:7:7: ( 'include' )
            # GOC.g:7:9: 'include'
            pass 
            self.match("include")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__54"



    # $ANTLR start "T__55"
    def mT__55(self, ):

        try:
            _type = T__55
            _channel = DEFAULT_CHANNEL

            # GOC.g:8:7: ( ';' )
            # GOC.g:8:9: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__55"



    # $ANTLR start "T__56"
    def mT__56(self, ):

        try:
            _type = T__56
            _channel = DEFAULT_CHANNEL

            # GOC.g:9:7: ( '{' )
            # GOC.g:9:9: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__56"



    # $ANTLR start "T__57"
    def mT__57(self, ):

        try:
            _type = T__57
            _channel = DEFAULT_CHANNEL

            # GOC.g:10:7: ( '}' )
            # GOC.g:10:9: '}'
            pass 
            self.match(125)



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

            # GOC.g:11:7: ( 'code' )
            # GOC.g:11:9: 'code'
            pass 
            self.match("code")



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

            # GOC.g:12:7: ( 'value' )
            # GOC.g:12:9: 'value'
            pass 
            self.match("value")



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

            # GOC.g:13:7: ( ':' )
            # GOC.g:13:9: ':'
            pass 
            self.match(58)



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

            # GOC.g:14:7: ( 'public' )
            # GOC.g:14:9: 'public'
            pass 
            self.match("public")



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

            # GOC.g:15:7: ( 'protected' )
            # GOC.g:15:9: 'protected'
            pass 
            self.match("protected")



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

            # GOC.g:16:7: ( 'private' )
            # GOC.g:16:9: 'private'
            pass 
            self.match("private")



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

            # GOC.g:17:7: ( 'instance' )
            # GOC.g:17:9: 'instance'
            pass 
            self.match("instance")



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

            # GOC.g:18:7: ( 'static' )
            # GOC.g:18:9: 'static'
            pass 
            self.match("static")



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

            # GOC.g:19:7: ( 'final' )
            # GOC.g:19:9: 'final'
            pass 
            self.match("final")



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

            # GOC.g:20:7: ( 'virtual' )
            # GOC.g:20:9: 'virtual'
            pass 
            self.match("virtual")



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

            # GOC.g:21:7: ( 'bind_property' )
            # GOC.g:21:9: 'bind_property'
            pass 
            self.match("bind_property")



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

            # GOC.g:22:7: ( 'const' )
            # GOC.g:22:9: 'const'
            pass 
            self.match("const")



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

            # GOC.g:23:7: ( 'boolean' )
            # GOC.g:23:9: 'boolean'
            pass 
            self.match("boolean")



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

            # GOC.g:24:7: ( 'integer' )
            # GOC.g:24:9: 'integer'
            pass 
            self.match("integer")



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

            # GOC.g:25:7: ( 'double' )
            # GOC.g:25:9: 'double'
            pass 
            self.match("double")



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

            # GOC.g:26:7: ( 'string' )
            # GOC.g:26:9: 'string'
            pass 
            self.match("string")



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

            # GOC.g:27:7: ( 'pointer' )
            # GOC.g:27:9: 'pointer'
            pass 
            self.match("pointer")



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

            # GOC.g:28:7: ( 'object' )
            # GOC.g:28:9: 'object'
            pass 
            self.match("object")



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

            # GOC.g:29:7: ( 'enumeration' )
            # GOC.g:29:9: 'enumeration'
            pass 
            self.match("enumeration")



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

            # GOC.g:30:7: ( 'access' )
            # GOC.g:30:9: 'access'
            pass 
            self.match("access")



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

            # GOC.g:31:7: ( 'read-only' )
            # GOC.g:31:9: 'read-only'
            pass 
            self.match("read-only")



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

            # GOC.g:32:7: ( 'initial-write' )
            # GOC.g:32:9: 'initial-write'
            pass 
            self.match("initial-write")



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

            # GOC.g:33:7: ( 'read-write' )
            # GOC.g:33:9: 'read-write'
            pass 
            self.match("read-write")



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

            # GOC.g:34:7: ( 'description' )
            # GOC.g:34:9: 'description'
            pass 
            self.match("description")



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

            # GOC.g:35:7: ( 'min' )
            # GOC.g:35:9: 'min'
            pass 
            self.match("min")



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

            # GOC.g:36:7: ( 'max' )
            # GOC.g:36:9: 'max'
            pass 
            self.match("max")



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

            # GOC.g:37:7: ( 'default' )
            # GOC.g:37:9: 'default'
            pass 
            self.match("default")



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

            # GOC.g:38:7: ( 'null' )
            # GOC.g:38:9: 'null'
            pass 
            self.match("null")



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

            # GOC.g:39:7: ( 'float' )
            # GOC.g:39:9: 'float'
            pass 
            self.match("float")



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

            # GOC.g:40:7: ( 'unsigned ' )
            # GOC.g:40:9: 'unsigned '
            pass 
            self.match("unsigned ")



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

            # GOC.g:41:7: ( 'long' )
            # GOC.g:41:9: 'long'
            pass 
            self.match("long")



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

            # GOC.g:42:7: ( 'ref' )
            # GOC.g:42:9: 'ref'
            pass 
            self.match("ref")



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

            # GOC.g:43:7: ( '(' )
            # GOC.g:43:9: '('
            pass 
            self.match(40)



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

            # GOC.g:44:7: ( ')' )
            # GOC.g:44:9: ')'
            pass 
            self.match(41)



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

            # GOC.g:45:7: ( 'list' )
            # GOC.g:45:9: 'list'
            pass 
            self.match("list")



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

            # GOC.g:46:7: ( '::' )
            # GOC.g:46:9: '::'
            pass 
            self.match("::")



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

            # GOC.g:47:7: ( '-' )
            # GOC.g:47:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__94"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # GOC.g:216:5: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' | '/*' ( options {greedy=false; } : . )* '*/' )
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
                # GOC.g:216:9: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
                pass 
                self.match("//")
                # GOC.g:216:14: (~ ( '\\n' | '\\r' ) )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((0 <= LA1_0 <= 9) or (11 <= LA1_0 <= 12) or (14 <= LA1_0 <= 65535)) :
                        alt1 = 1


                    if alt1 == 1:
                        # GOC.g:216:14: ~ ( '\\n' | '\\r' )
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop1
                # GOC.g:216:28: ( '\\r' )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 13) :
                    alt2 = 1
                if alt2 == 1:
                    # GOC.g:216:28: '\\r'
                    pass 
                    self.match(13)



                self.match(10)
                #action start
                _channel=HIDDEN;
                #action end


            elif alt4 == 2:
                # GOC.g:217:9: '/*' ( options {greedy=false; } : . )* '*/'
                pass 
                self.match("/*")
                # GOC.g:217:14: ( options {greedy=false; } : . )*
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
                        # GOC.g:217:42: .
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

            # GOC.g:220:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # GOC.g:220:9: ( ' ' | '\\t' | '\\r' | '\\n' )
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

            # GOC.g:228:5: ( 'true' | 'false' )
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
                # GOC.g:228:9: 'true'
                pass 
                self.match("true")


            elif alt5 == 2:
                # GOC.g:229:9: 'false'
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

            # GOC.g:233:5: ( 'package' )
            # GOC.g:233:9: 'package'
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

            # GOC.g:237:2: ( 'gobject' )
            # GOC.g:237:4: 'gobject'
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

            # GOC.g:241:2: ( 'ginterface' )
            # GOC.g:241:4: 'ginterface'
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

            # GOC.g:245:5: ( 'gtype' )
            # GOC.g:245:9: 'gtype'
            pass 
            self.match("gtype")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GTYPE"



    # $ANTLR start "ERROR_DOMAIN"
    def mERROR_DOMAIN(self, ):

        try:
            _type = ERROR_DOMAIN
            _channel = DEFAULT_CHANNEL

            # GOC.g:249:5: ( 'gerror' )
            # GOC.g:249:9: 'gerror'
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

            # GOC.g:253:5: ( 'genum' )
            # GOC.g:253:9: 'genum'
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

            # GOC.g:257:5: ( 'gflags' )
            # GOC.g:257:9: 'gflags'
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

            # GOC.g:261:2: ( 'super' )
            # GOC.g:261:4: 'super'
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

            # GOC.g:265:5: ( 'prefix' )
            # GOC.g:265:9: 'prefix'
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

            # GOC.g:269:2: ( 'implements' )
            # GOC.g:269:4: 'implements'
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

            # GOC.g:273:2: ( 'constructor' )
            # GOC.g:273:4: 'constructor'
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

            # GOC.g:277:2: ( 'method' )
            # GOC.g:277:4: 'method'
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

            # GOC.g:281:2: ( 'override' )
            # GOC.g:281:4: 'override'
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

            # GOC.g:285:2: ( 'parameter' )
            # GOC.g:285:4: 'parameter'
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

            # GOC.g:289:2: ( 'attribute' )
            # GOC.g:289:4: 'attribute'
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

            # GOC.g:293:2: ( 'property' )
            # GOC.g:293:4: 'property'
            pass 
            self.match("property")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PROPERTY"



    # $ANTLR start "SIGNAL"
    def mSIGNAL(self, ):

        try:
            _type = SIGNAL
            _channel = DEFAULT_CHANNEL

            # GOC.g:297:2: ( 'signal' )
            # GOC.g:297:4: 'signal'
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

            # GOC.g:301:2: ( 'result' )
            # GOC.g:301:4: 'result'
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

            # GOC.g:304:5: ( 'type' )
            # GOC.g:304:7: 'type'
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

            # GOC.g:307:2: ( 'modifiers' )
            # GOC.g:307:4: 'modifiers'
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

            # GOC.g:311:2: ( 'scope' )
            # GOC.g:311:4: 'scope'
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

            # GOC.g:315:2: ( 'visibility' )
            # GOC.g:315:4: 'visibility'
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

            # GOC.g:319:2: ( 'inheritance' )
            # GOC.g:319:4: 'inheritance'
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

            # GOC.g:323:5: ( 'abstract' )
            # GOC.g:323:9: 'abstract'
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

            # GOC.g:327:5: ( 'auto_create' )
            # GOC.g:327:9: 'auto_create'
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

            # GOC.g:330:5: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )* )
            # GOC.g:330:7: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # GOC.g:330:31: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
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

            # GOC.g:338:5: ( '\"' ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )* '\"' )
            # GOC.g:338:8: '\"' ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )* '\"'
            pass 
            self.match(34)
            # GOC.g:338:12: ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )*
            while True: #loop7
                alt7 = 3
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 92) :
                    alt7 = 1
                elif ((0 <= LA7_0 <= 33) or (35 <= LA7_0 <= 91) or (93 <= LA7_0 <= 65535)) :
                    alt7 = 2


                if alt7 == 1:
                    # GOC.g:338:14: ESC_SEQ
                    pass 
                    self.mESC_SEQ()


                elif alt7 == 2:
                    # GOC.g:338:24: ~ ( '\\\\' | '\"' )
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

            # GOC.g:341:5: ( ( '1' .. '9' ) ( '0' .. '9' )* )
            # GOC.g:341:9: ( '1' .. '9' ) ( '0' .. '9' )*
            pass 
            # GOC.g:341:9: ( '1' .. '9' )
            # GOC.g:341:10: '1' .. '9'
            pass 
            self.matchRange(49, 57)



            # GOC.g:341:19: ( '0' .. '9' )*
            while True: #loop8
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if ((48 <= LA8_0 <= 57)) :
                    alt8 = 1


                if alt8 == 1:
                    # GOC.g:341:20: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    break #loop8



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INT"



    # $ANTLR start "HEX_DIGIT"
    def mHEX_DIGIT(self, ):

        try:
            # GOC.g:345:11: ( ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' ) )
            # GOC.g:345:13: ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )
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
            # GOC.g:349:5: ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | UNICODE_ESC | OCTAL_ESC )
            alt9 = 3
            LA9_0 = self.input.LA(1)

            if (LA9_0 == 92) :
                LA9 = self.input.LA(2)
                if LA9 == 34 or LA9 == 39 or LA9 == 92 or LA9 == 98 or LA9 == 102 or LA9 == 110 or LA9 == 114 or LA9 == 116:
                    alt9 = 1
                elif LA9 == 117:
                    alt9 = 2
                elif LA9 == 48 or LA9 == 49 or LA9 == 50 or LA9 == 51 or LA9 == 52 or LA9 == 53 or LA9 == 54 or LA9 == 55:
                    alt9 = 3
                else:
                    nvae = NoViableAltException("", 9, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 9, 0, self.input)

                raise nvae

            if alt9 == 1:
                # GOC.g:349:9: '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' )
                pass 
                self.match(92)
                if self.input.LA(1) == 34 or self.input.LA(1) == 39 or self.input.LA(1) == 92 or self.input.LA(1) == 98 or self.input.LA(1) == 102 or self.input.LA(1) == 110 or self.input.LA(1) == 114 or self.input.LA(1) == 116:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



            elif alt9 == 2:
                # GOC.g:350:9: UNICODE_ESC
                pass 
                self.mUNICODE_ESC()


            elif alt9 == 3:
                # GOC.g:351:9: OCTAL_ESC
                pass 
                self.mOCTAL_ESC()



        finally:

            pass

    # $ANTLR end "ESC_SEQ"



    # $ANTLR start "OCTAL_ESC"
    def mOCTAL_ESC(self, ):

        try:
            # GOC.g:356:5: ( '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) )
            alt10 = 3
            LA10_0 = self.input.LA(1)

            if (LA10_0 == 92) :
                LA10_1 = self.input.LA(2)

                if ((48 <= LA10_1 <= 51)) :
                    LA10_2 = self.input.LA(3)

                    if ((48 <= LA10_2 <= 55)) :
                        LA10_4 = self.input.LA(4)

                        if ((48 <= LA10_4 <= 55)) :
                            alt10 = 1
                        else:
                            alt10 = 2
                    else:
                        alt10 = 3
                elif ((52 <= LA10_1 <= 55)) :
                    LA10_3 = self.input.LA(3)

                    if ((48 <= LA10_3 <= 55)) :
                        alt10 = 2
                    else:
                        alt10 = 3
                else:
                    nvae = NoViableAltException("", 10, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 10, 0, self.input)

                raise nvae

            if alt10 == 1:
                # GOC.g:356:9: '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)
                # GOC.g:356:14: ( '0' .. '3' )
                # GOC.g:356:15: '0' .. '3'
                pass 
                self.matchRange(48, 51)



                # GOC.g:356:25: ( '0' .. '7' )
                # GOC.g:356:26: '0' .. '7'
                pass 
                self.matchRange(48, 55)



                # GOC.g:356:36: ( '0' .. '7' )
                # GOC.g:356:37: '0' .. '7'
                pass 
                self.matchRange(48, 55)





            elif alt10 == 2:
                # GOC.g:357:9: '\\\\' ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)
                # GOC.g:357:14: ( '0' .. '7' )
                # GOC.g:357:15: '0' .. '7'
                pass 
                self.matchRange(48, 55)



                # GOC.g:357:25: ( '0' .. '7' )
                # GOC.g:357:26: '0' .. '7'
                pass 
                self.matchRange(48, 55)





            elif alt10 == 3:
                # GOC.g:358:9: '\\\\' ( '0' .. '7' )
                pass 
                self.match(92)
                # GOC.g:358:14: ( '0' .. '7' )
                # GOC.g:358:15: '0' .. '7'
                pass 
                self.matchRange(48, 55)






        finally:

            pass

    # $ANTLR end "OCTAL_ESC"



    # $ANTLR start "UNICODE_ESC"
    def mUNICODE_ESC(self, ):

        try:
            # GOC.g:363:5: ( '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT )
            # GOC.g:363:9: '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
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
        # GOC.g:1:8: ( T__54 | T__55 | T__56 | T__57 | T__58 | T__59 | T__60 | T__61 | T__62 | T__63 | T__64 | T__65 | T__66 | T__67 | T__68 | T__69 | T__70 | T__71 | T__72 | T__73 | T__74 | T__75 | T__76 | T__77 | T__78 | T__79 | T__80 | T__81 | T__82 | T__83 | T__84 | T__85 | T__86 | T__87 | T__88 | T__89 | T__90 | T__91 | T__92 | T__93 | T__94 | COMMENT | WS | BOOLVALUE | PACKAGE | GOBJECT | GINTERFACE | GTYPE | ERROR_DOMAIN | ENUMERATION | FLAGS | SUPER | PREFIX | IMPLEMENTS | CONSTRUCTOR | METHOD | OVERRIDE | PARAMETER | ATTRIBUTE | PROPERTY | SIGNAL | RESULT | TYPE | MODIFIERS | SCOPE | VISIBILITY | INHERITANCE | ABSTRACT | AUTO_CREATE | ID | STRING | INT )
        alt11 = 72
        alt11 = self.dfa11.predict(self.input)
        if alt11 == 1:
            # GOC.g:1:10: T__54
            pass 
            self.mT__54()


        elif alt11 == 2:
            # GOC.g:1:16: T__55
            pass 
            self.mT__55()


        elif alt11 == 3:
            # GOC.g:1:22: T__56
            pass 
            self.mT__56()


        elif alt11 == 4:
            # GOC.g:1:28: T__57
            pass 
            self.mT__57()


        elif alt11 == 5:
            # GOC.g:1:34: T__58
            pass 
            self.mT__58()


        elif alt11 == 6:
            # GOC.g:1:40: T__59
            pass 
            self.mT__59()


        elif alt11 == 7:
            # GOC.g:1:46: T__60
            pass 
            self.mT__60()


        elif alt11 == 8:
            # GOC.g:1:52: T__61
            pass 
            self.mT__61()


        elif alt11 == 9:
            # GOC.g:1:58: T__62
            pass 
            self.mT__62()


        elif alt11 == 10:
            # GOC.g:1:64: T__63
            pass 
            self.mT__63()


        elif alt11 == 11:
            # GOC.g:1:70: T__64
            pass 
            self.mT__64()


        elif alt11 == 12:
            # GOC.g:1:76: T__65
            pass 
            self.mT__65()


        elif alt11 == 13:
            # GOC.g:1:82: T__66
            pass 
            self.mT__66()


        elif alt11 == 14:
            # GOC.g:1:88: T__67
            pass 
            self.mT__67()


        elif alt11 == 15:
            # GOC.g:1:94: T__68
            pass 
            self.mT__68()


        elif alt11 == 16:
            # GOC.g:1:100: T__69
            pass 
            self.mT__69()


        elif alt11 == 17:
            # GOC.g:1:106: T__70
            pass 
            self.mT__70()


        elif alt11 == 18:
            # GOC.g:1:112: T__71
            pass 
            self.mT__71()


        elif alt11 == 19:
            # GOC.g:1:118: T__72
            pass 
            self.mT__72()


        elif alt11 == 20:
            # GOC.g:1:124: T__73
            pass 
            self.mT__73()


        elif alt11 == 21:
            # GOC.g:1:130: T__74
            pass 
            self.mT__74()


        elif alt11 == 22:
            # GOC.g:1:136: T__75
            pass 
            self.mT__75()


        elif alt11 == 23:
            # GOC.g:1:142: T__76
            pass 
            self.mT__76()


        elif alt11 == 24:
            # GOC.g:1:148: T__77
            pass 
            self.mT__77()


        elif alt11 == 25:
            # GOC.g:1:154: T__78
            pass 
            self.mT__78()


        elif alt11 == 26:
            # GOC.g:1:160: T__79
            pass 
            self.mT__79()


        elif alt11 == 27:
            # GOC.g:1:166: T__80
            pass 
            self.mT__80()


        elif alt11 == 28:
            # GOC.g:1:172: T__81
            pass 
            self.mT__81()


        elif alt11 == 29:
            # GOC.g:1:178: T__82
            pass 
            self.mT__82()


        elif alt11 == 30:
            # GOC.g:1:184: T__83
            pass 
            self.mT__83()


        elif alt11 == 31:
            # GOC.g:1:190: T__84
            pass 
            self.mT__84()


        elif alt11 == 32:
            # GOC.g:1:196: T__85
            pass 
            self.mT__85()


        elif alt11 == 33:
            # GOC.g:1:202: T__86
            pass 
            self.mT__86()


        elif alt11 == 34:
            # GOC.g:1:208: T__87
            pass 
            self.mT__87()


        elif alt11 == 35:
            # GOC.g:1:214: T__88
            pass 
            self.mT__88()


        elif alt11 == 36:
            # GOC.g:1:220: T__89
            pass 
            self.mT__89()


        elif alt11 == 37:
            # GOC.g:1:226: T__90
            pass 
            self.mT__90()


        elif alt11 == 38:
            # GOC.g:1:232: T__91
            pass 
            self.mT__91()


        elif alt11 == 39:
            # GOC.g:1:238: T__92
            pass 
            self.mT__92()


        elif alt11 == 40:
            # GOC.g:1:244: T__93
            pass 
            self.mT__93()


        elif alt11 == 41:
            # GOC.g:1:250: T__94
            pass 
            self.mT__94()


        elif alt11 == 42:
            # GOC.g:1:256: COMMENT
            pass 
            self.mCOMMENT()


        elif alt11 == 43:
            # GOC.g:1:264: WS
            pass 
            self.mWS()


        elif alt11 == 44:
            # GOC.g:1:267: BOOLVALUE
            pass 
            self.mBOOLVALUE()


        elif alt11 == 45:
            # GOC.g:1:277: PACKAGE
            pass 
            self.mPACKAGE()


        elif alt11 == 46:
            # GOC.g:1:285: GOBJECT
            pass 
            self.mGOBJECT()


        elif alt11 == 47:
            # GOC.g:1:293: GINTERFACE
            pass 
            self.mGINTERFACE()


        elif alt11 == 48:
            # GOC.g:1:304: GTYPE
            pass 
            self.mGTYPE()


        elif alt11 == 49:
            # GOC.g:1:310: ERROR_DOMAIN
            pass 
            self.mERROR_DOMAIN()


        elif alt11 == 50:
            # GOC.g:1:323: ENUMERATION
            pass 
            self.mENUMERATION()


        elif alt11 == 51:
            # GOC.g:1:335: FLAGS
            pass 
            self.mFLAGS()


        elif alt11 == 52:
            # GOC.g:1:341: SUPER
            pass 
            self.mSUPER()


        elif alt11 == 53:
            # GOC.g:1:347: PREFIX
            pass 
            self.mPREFIX()


        elif alt11 == 54:
            # GOC.g:1:354: IMPLEMENTS
            pass 
            self.mIMPLEMENTS()


        elif alt11 == 55:
            # GOC.g:1:365: CONSTRUCTOR
            pass 
            self.mCONSTRUCTOR()


        elif alt11 == 56:
            # GOC.g:1:377: METHOD
            pass 
            self.mMETHOD()


        elif alt11 == 57:
            # GOC.g:1:384: OVERRIDE
            pass 
            self.mOVERRIDE()


        elif alt11 == 58:
            # GOC.g:1:393: PARAMETER
            pass 
            self.mPARAMETER()


        elif alt11 == 59:
            # GOC.g:1:403: ATTRIBUTE
            pass 
            self.mATTRIBUTE()


        elif alt11 == 60:
            # GOC.g:1:413: PROPERTY
            pass 
            self.mPROPERTY()


        elif alt11 == 61:
            # GOC.g:1:422: SIGNAL
            pass 
            self.mSIGNAL()


        elif alt11 == 62:
            # GOC.g:1:429: RESULT
            pass 
            self.mRESULT()


        elif alt11 == 63:
            # GOC.g:1:436: TYPE
            pass 
            self.mTYPE()


        elif alt11 == 64:
            # GOC.g:1:441: MODIFIERS
            pass 
            self.mMODIFIERS()


        elif alt11 == 65:
            # GOC.g:1:451: SCOPE
            pass 
            self.mSCOPE()


        elif alt11 == 66:
            # GOC.g:1:457: VISIBILITY
            pass 
            self.mVISIBILITY()


        elif alt11 == 67:
            # GOC.g:1:468: INHERITANCE
            pass 
            self.mINHERITANCE()


        elif alt11 == 68:
            # GOC.g:1:480: ABSTRACT
            pass 
            self.mABSTRACT()


        elif alt11 == 69:
            # GOC.g:1:489: AUTO_CREATE
            pass 
            self.mAUTO_CREATE()


        elif alt11 == 70:
            # GOC.g:1:501: ID
            pass 
            self.mID()


        elif alt11 == 71:
            # GOC.g:1:504: STRING
            pass 
            self.mSTRING()


        elif alt11 == 72:
            # GOC.g:1:511: INT
            pass 
            self.mINT()







    # lookup tables for DFA #11

    DFA11_eot = DFA.unpack(
        u"\1\uffff\1\34\3\uffff\2\34\1\45\15\34\5\uffff\2\34\3\uffff\5\34"
        u"\2\uffff\115\34\1\u00ad\1\34\1\u00af\1\u00b0\24\34\1\u00c5\41\34"
        u"\1\uffff\1\34\2\uffff\2\34\1\u00ea\1\34\1\u00ec\1\u00ed\1\u00ee"
        u"\1\u00ef\14\34\1\uffff\1\u00fd\1\u00fe\14\34\1\u010b\1\34\1\u010d"
        u"\1\u010e\1\u010f\1\u00ee\14\34\1\uffff\3\34\1\uffff\1\34\4\uffff"
        u"\2\34\1\u0124\1\34\1\u0126\10\34\2\uffff\2\34\1\u0131\3\34\1\u0135"
        u"\3\34\1\u0139\1\u013a\1\uffff\1\u013b\3\uffff\2\34\1\u013e\2\34"
        u"\1\u0141\2\34\1\u0144\3\34\2\uffff\1\u0148\1\u0149\4\34\1\uffff"
        u"\1\u014e\1\uffff\1\u014f\1\u0150\1\34\1\u0152\4\34\1\u0157\1\34"
        u"\1\uffff\2\34\1\u015b\1\uffff\1\u015c\1\u015d\1\34\3\uffff\1\34"
        u"\1\u0160\1\uffff\1\34\1\u0162\1\uffff\2\34\1\uffff\3\34\2\uffff"
        u"\2\34\1\u016a\1\34\3\uffff\1\u016c\2\uffff\3\34\1\uffff\2\34\1"
        u"\u0172\3\uffff\2\34\1\uffff\1\34\1\uffff\1\u0176\2\34\1\u0179\3"
        u"\34\1\uffff\1\34\1\uffff\4\34\1\u0182\1\uffff\1\u0183\2\34\1\uffff"
        u"\1\34\1\u0187\1\uffff\1\34\1\u0189\1\uffff\2\34\1\u018c\1\34\1"
        u"\u018e\2\uffff\3\34\1\uffff\1\34\1\uffff\1\u0193\1\u0194\1\uffff"
        u"\1\u0195\1\uffff\1\34\1\u0197\1\u0198\1\u0199\3\uffff\1\34\3\uffff"
        u"\1\u019b\1\uffff"
        )

    DFA11_eof = DFA.unpack(
        u"\u019c\uffff"
        )

    DFA11_min = DFA.unpack(
        u"\1\11\1\155\3\uffff\1\157\1\141\1\72\1\141\1\143\1\141\1\151\1"
        u"\145\1\142\1\156\1\142\1\145\1\141\1\165\1\156\1\151\5\uffff\1"
        u"\162\1\145\3\uffff\1\143\1\160\1\144\1\154\1\162\2\uffff\1\142"
        u"\1\145\1\151\1\143\1\141\1\160\1\147\1\157\1\156\1\157\1\154\1"
        u"\156\1\157\1\165\1\146\1\152\1\145\1\165\1\143\1\164\1\163\1\164"
        u"\1\141\1\156\1\170\1\164\1\144\1\154\1\163\1\156\1\163\1\165\1"
        u"\160\1\142\1\156\1\171\1\156\2\154\1\164\1\145\1\164\1\145\1\154"
        u"\1\145\1\163\1\165\1\164\1\151\1\154\1\160\1\166\1\146\1\156\1"
        u"\153\1\141\1\164\1\151\1\145\1\156\1\160\2\141\1\163\1\144\1\154"
        u"\1\142\1\143\1\141\1\145\1\162\1\155\1\145\1\162\1\164\1\157\1"
        u"\144\1\60\1\165\2\60\1\150\1\151\1\154\1\151\1\147\1\164\2\145"
        u"\1\152\1\164\1\160\1\162\1\165\1\141\1\165\1\141\1\147\1\151\1"
        u"\162\1\145\1\60\1\164\1\145\1\165\1\142\1\151\2\145\1\141\1\151"
        u"\1\164\1\141\1\155\1\151\1\156\1\162\1\141\1\145\1\154\1\164\1"
        u"\145\1\137\1\145\1\154\1\162\1\165\1\143\1\162\1\145\1\163\1\151"
        u"\1\162\1\137\1\55\1\uffff\1\154\2\uffff\1\157\1\146\1\60\1\147"
        u"\4\60\3\145\1\157\1\155\1\147\1\144\1\156\1\145\1\141\1\151\1\155"
        u"\1\uffff\2\60\1\141\1\151\2\143\1\162\1\164\1\170\1\145\1\147\1"
        u"\145\1\143\1\147\1\60\1\154\4\60\1\160\1\141\1\145\1\151\1\154"
        u"\1\164\1\151\1\162\1\163\1\142\1\141\1\143\1\157\1\164\1\144\1"
        u"\151\1\uffff\1\156\4\uffff\1\143\1\162\1\60\1\162\1\60\1\163\1"
        u"\145\1\143\1\162\1\154\1\164\1\145\1\165\2\uffff\2\154\1\60\2\164"
        u"\1\145\1\60\1\162\1\145\1\164\2\60\1\uffff\1\60\3\uffff\1\162\1"
        u"\156\1\60\1\160\1\164\1\60\1\144\1\141\1\60\1\165\1\143\1\162\2"
        u"\uffff\2\60\2\145\1\164\1\146\1\uffff\1\60\1\uffff\2\60\1\145\1"
        u"\60\1\55\1\141\1\156\1\143\1\60\1\151\1\uffff\1\145\1\171\1\60"
        u"\1\uffff\2\60\1\145\3\uffff\1\157\1\60\1\uffff\1\164\1\60\1\uffff"
        u"\1\145\1\164\1\uffff\2\164\1\145\2\uffff\1\162\1\144\1\60\1\141"
        u"\3\uffff\1\60\2\uffff\1\156\2\164\1\uffff\1\164\1\144\1\60\3\uffff"
        u"\1\162\1\160\1\uffff\1\151\1\uffff\1\60\1\151\1\145\1\60\1\141"
        u"\1\163\1\40\1\uffff\1\143\1\uffff\1\143\1\163\1\157\1\171\1\60"
        u"\1\uffff\1\60\1\145\1\157\1\uffff\1\157\1\60\1\uffff\1\164\1\60"
        u"\1\uffff\2\145\1\60\1\162\1\60\2\uffff\1\162\2\156\1\uffff\1\145"
        u"\1\uffff\2\60\1\uffff\1\60\1\uffff\1\164\3\60\3\uffff\1\171\3\uffff"
        u"\1\60\1\uffff"
        )

    DFA11_max = DFA.unpack(
        u"\1\175\1\156\3\uffff\1\157\1\151\1\72\2\165\1\154\2\157\1\166\1"
        u"\156\1\165\1\145\1\157\1\165\1\156\1\157\5\uffff\1\171\1\164\3"
        u"\uffff\1\164\1\160\1\156\1\154\1\163\2\uffff\1\142\1\157\1\151"
        u"\2\162\1\160\1\147\1\157\1\156\1\157\1\154\1\156\1\157\1\165\1"
        u"\163\1\152\1\145\1\165\1\143\1\164\1\163\1\164\1\163\1\156\1\170"
        u"\1\164\1\144\1\154\1\163\1\156\1\163\1\165\1\160\1\142\1\156\1"
        u"\171\1\162\2\154\1\164\1\145\1\164\1\145\1\154\1\145\1\163\1\165"
        u"\1\164\1\151\1\154\1\164\1\166\1\146\1\156\1\153\1\141\1\164\1"
        u"\151\1\145\1\156\1\160\2\141\1\163\1\144\1\154\1\142\1\143\1\141"
        u"\1\145\1\162\1\155\1\145\1\162\1\164\1\157\1\144\1\172\1\165\2"
        u"\172\1\150\1\151\1\154\1\151\1\147\1\164\2\145\1\152\1\164\1\160"
        u"\1\162\1\165\1\141\1\165\1\141\1\147\1\151\1\162\1\145\1\172\1"
        u"\164\1\145\1\165\1\142\1\151\2\145\1\141\1\151\1\164\1\141\1\155"
        u"\1\151\1\156\1\162\1\141\1\145\1\154\1\164\1\145\1\137\1\145\1"
        u"\154\1\162\1\165\1\143\1\162\1\145\1\163\1\151\1\162\1\137\1\55"
        u"\1\uffff\1\154\2\uffff\1\157\1\146\1\172\1\147\4\172\3\145\1\157"
        u"\1\155\1\147\1\144\1\156\1\145\1\141\1\151\1\155\1\uffff\2\172"
        u"\1\141\1\151\2\143\1\162\1\164\1\170\1\145\1\147\1\145\1\143\1"
        u"\147\1\172\1\154\4\172\1\160\1\141\1\145\1\151\1\154\1\164\1\151"
        u"\1\162\1\163\1\142\1\141\1\143\1\167\1\164\1\144\1\151\1\uffff"
        u"\1\156\4\uffff\1\143\1\162\1\172\1\162\1\172\1\163\1\145\1\143"
        u"\1\162\1\154\1\164\1\145\1\165\2\uffff\2\154\1\172\2\164\1\145"
        u"\1\172\1\162\1\145\1\164\2\172\1\uffff\1\172\3\uffff\1\162\1\156"
        u"\1\172\1\160\1\164\1\172\1\144\1\141\1\172\1\165\1\143\1\162\2"
        u"\uffff\2\172\2\145\1\164\1\146\1\uffff\1\172\1\uffff\2\172\1\145"
        u"\1\172\1\55\1\141\1\156\1\143\1\172\1\151\1\uffff\1\145\1\171\1"
        u"\172\1\uffff\2\172\1\145\3\uffff\1\157\1\172\1\uffff\1\164\1\172"
        u"\1\uffff\1\145\1\164\1\uffff\2\164\1\145\2\uffff\1\162\1\144\1"
        u"\172\1\141\3\uffff\1\172\2\uffff\1\156\2\164\1\uffff\1\164\1\144"
        u"\1\172\3\uffff\1\162\1\160\1\uffff\1\151\1\uffff\1\172\1\151\1"
        u"\145\1\172\1\141\1\163\1\40\1\uffff\1\143\1\uffff\1\143\1\163\1"
        u"\157\1\171\1\172\1\uffff\1\172\1\145\1\157\1\uffff\1\157\1\172"
        u"\1\uffff\1\164\1\172\1\uffff\2\145\1\172\1\162\1\172\2\uffff\1"
        u"\162\2\156\1\uffff\1\145\1\uffff\2\172\1\uffff\1\172\1\uffff\1"
        u"\164\3\172\3\uffff\1\171\3\uffff\1\172\1\uffff"
        )

    DFA11_accept = DFA.unpack(
        u"\2\uffff\1\2\1\3\1\4\20\uffff\1\45\1\46\1\51\1\52\1\53\2\uffff"
        u"\1\106\1\107\1\110\5\uffff\1\50\1\7\u0087\uffff\1\44\1\uffff\1"
        u"\35\1\36\24\uffff\1\5\44\uffff\1\40\1\uffff\1\43\1\47\1\54\1\77"
        u"\15\uffff\1\20\1\6\14\uffff\1\64\1\uffff\1\101\1\15\1\41\14\uffff"
        u"\1\31\1\33\6\uffff\1\60\1\uffff\1\62\12\uffff\1\10\3\uffff\1\65"
        u"\3\uffff\1\14\1\24\1\75\2\uffff\1\23\2\uffff\1\26\2\uffff\1\30"
        u"\3\uffff\1\76\1\70\4\uffff\1\61\1\63\1\1\1\uffff\1\22\1\32\3\uffff"
        u"\1\16\3\uffff\1\12\1\25\1\55\2\uffff\1\21\1\uffff\1\37\7\uffff"
        u"\1\56\1\uffff\1\13\5\uffff\1\74\3\uffff\1\71\2\uffff\1\104\2\uffff"
        u"\1\42\5\uffff\1\11\1\72\3\uffff\1\73\1\uffff\1\100\2\uffff\1\66"
        u"\1\uffff\1\102\4\uffff\1\57\1\103\1\67\1\uffff\1\34\1\27\1\105"
        u"\1\uffff\1\17"
        )

    DFA11_special = DFA.unpack(
        u"\u019c\uffff"
        )

            
    DFA11_transition = [
        DFA.unpack(u"\2\31\2\uffff\1\31\22\uffff\1\31\1\uffff\1\35\5\uffff"
        u"\1\25\1\26\3\uffff\1\27\1\uffff\1\30\1\uffff\11\36\1\7\1\2\5\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\1\17\1\13\1\5\1\14\1\16\1\12\1\33\1"
        u"\34\1\1\2\34\1\24\1\21\1\22\1\15\1\10\1\34\1\20\1\11\1\32\1\23"
        u"\1\6\4\34\1\3\1\uffff\1\4"),
        DFA.unpack(u"\1\40\1\37"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\41"),
        DFA.unpack(u"\1\42\7\uffff\1\43"),
        DFA.unpack(u"\1\44"),
        DFA.unpack(u"\1\51\15\uffff\1\50\2\uffff\1\47\2\uffff\1\46"),
        DFA.unpack(u"\1\55\5\uffff\1\54\12\uffff\1\52\1\53"),
        DFA.unpack(u"\1\60\7\uffff\1\56\2\uffff\1\57"),
        DFA.unpack(u"\1\61\5\uffff\1\62"),
        DFA.unpack(u"\1\64\11\uffff\1\63"),
        DFA.unpack(u"\1\65\23\uffff\1\66"),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u"\1\72\1\70\20\uffff\1\71\1\73"),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u"\1\76\3\uffff\1\77\3\uffff\1\75\5\uffff\1\100"),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\102"),
        DFA.unpack(u"\1\104\5\uffff\1\103"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\105\6\uffff\1\106"),
        DFA.unpack(u"\1\112\1\113\2\uffff\1\110\5\uffff\1\107\4\uffff\1"
        u"\111"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\114\4\uffff\1\120\1\117\11\uffff\1\115\1\116"),
        DFA.unpack(u"\1\121"),
        DFA.unpack(u"\1\122\11\uffff\1\123"),
        DFA.unpack(u"\1\124"),
        DFA.unpack(u"\1\125\1\126"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\127"),
        DFA.unpack(u"\1\132\3\uffff\1\131\5\uffff\1\130"),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u"\1\134\16\uffff\1\135"),
        DFA.unpack(u"\1\136\20\uffff\1\137"),
        DFA.unpack(u"\1\140"),
        DFA.unpack(u"\1\141"),
        DFA.unpack(u"\1\142"),
        DFA.unpack(u"\1\143"),
        DFA.unpack(u"\1\144"),
        DFA.unpack(u"\1\145"),
        DFA.unpack(u"\1\146"),
        DFA.unpack(u"\1\147"),
        DFA.unpack(u"\1\150"),
        DFA.unpack(u"\1\152\14\uffff\1\151"),
        DFA.unpack(u"\1\153"),
        DFA.unpack(u"\1\154"),
        DFA.unpack(u"\1\155"),
        DFA.unpack(u"\1\156"),
        DFA.unpack(u"\1\157"),
        DFA.unpack(u"\1\160"),
        DFA.unpack(u"\1\161"),
        DFA.unpack(u"\1\162\4\uffff\1\163\14\uffff\1\164"),
        DFA.unpack(u"\1\165"),
        DFA.unpack(u"\1\166"),
        DFA.unpack(u"\1\167"),
        DFA.unpack(u"\1\170"),
        DFA.unpack(u"\1\171"),
        DFA.unpack(u"\1\172"),
        DFA.unpack(u"\1\173"),
        DFA.unpack(u"\1\174"),
        DFA.unpack(u"\1\175"),
        DFA.unpack(u"\1\176"),
        DFA.unpack(u"\1\177"),
        DFA.unpack(u"\1\u0080"),
        DFA.unpack(u"\1\u0081"),
        DFA.unpack(u"\1\u0083\3\uffff\1\u0082"),
        DFA.unpack(u"\1\u0084"),
        DFA.unpack(u"\1\u0085"),
        DFA.unpack(u"\1\u0086"),
        DFA.unpack(u"\1\u0087"),
        DFA.unpack(u"\1\u0088"),
        DFA.unpack(u"\1\u0089"),
        DFA.unpack(u"\1\u008a"),
        DFA.unpack(u"\1\u008b"),
        DFA.unpack(u"\1\u008c"),
        DFA.unpack(u"\1\u008d"),
        DFA.unpack(u"\1\u008e"),
        DFA.unpack(u"\1\u008f"),
        DFA.unpack(u"\1\u0090"),
        DFA.unpack(u"\1\u0092\3\uffff\1\u0091"),
        DFA.unpack(u"\1\u0093"),
        DFA.unpack(u"\1\u0094"),
        DFA.unpack(u"\1\u0095"),
        DFA.unpack(u"\1\u0096"),
        DFA.unpack(u"\1\u0097"),
        DFA.unpack(u"\1\u0098"),
        DFA.unpack(u"\1\u0099"),
        DFA.unpack(u"\1\u009a"),
        DFA.unpack(u"\1\u009b"),
        DFA.unpack(u"\1\u009c"),
        DFA.unpack(u"\1\u009d"),
        DFA.unpack(u"\1\u009e"),
        DFA.unpack(u"\1\u009f"),
        DFA.unpack(u"\1\u00a0"),
        DFA.unpack(u"\1\u00a1"),
        DFA.unpack(u"\1\u00a2"),
        DFA.unpack(u"\1\u00a3"),
        DFA.unpack(u"\1\u00a4"),
        DFA.unpack(u"\1\u00a5"),
        DFA.unpack(u"\1\u00a6"),
        DFA.unpack(u"\1\u00a7"),
        DFA.unpack(u"\1\u00a8"),
        DFA.unpack(u"\1\u00a9"),
        DFA.unpack(u"\1\u00aa"),
        DFA.unpack(u"\1\u00ab"),
        DFA.unpack(u"\1\u00ac"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00ae"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00b1"),
        DFA.unpack(u"\1\u00b2"),
        DFA.unpack(u"\1\u00b3"),
        DFA.unpack(u"\1\u00b4"),
        DFA.unpack(u"\1\u00b5"),
        DFA.unpack(u"\1\u00b6"),
        DFA.unpack(u"\1\u00b7"),
        DFA.unpack(u"\1\u00b8"),
        DFA.unpack(u"\1\u00b9"),
        DFA.unpack(u"\1\u00ba"),
        DFA.unpack(u"\1\u00bb"),
        DFA.unpack(u"\1\u00bc"),
        DFA.unpack(u"\1\u00bd"),
        DFA.unpack(u"\1\u00be"),
        DFA.unpack(u"\1\u00bf"),
        DFA.unpack(u"\1\u00c0"),
        DFA.unpack(u"\1\u00c1"),
        DFA.unpack(u"\1\u00c2"),
        DFA.unpack(u"\1\u00c3"),
        DFA.unpack(u"\1\u00c4"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00c6"),
        DFA.unpack(u"\1\u00c7"),
        DFA.unpack(u"\1\u00c8"),
        DFA.unpack(u"\1\u00c9"),
        DFA.unpack(u"\1\u00ca"),
        DFA.unpack(u"\1\u00cb"),
        DFA.unpack(u"\1\u00cc"),
        DFA.unpack(u"\1\u00cd"),
        DFA.unpack(u"\1\u00ce"),
        DFA.unpack(u"\1\u00cf"),
        DFA.unpack(u"\1\u00d0"),
        DFA.unpack(u"\1\u00d1"),
        DFA.unpack(u"\1\u00d2"),
        DFA.unpack(u"\1\u00d3"),
        DFA.unpack(u"\1\u00d4"),
        DFA.unpack(u"\1\u00d5"),
        DFA.unpack(u"\1\u00d6"),
        DFA.unpack(u"\1\u00d7"),
        DFA.unpack(u"\1\u00d8"),
        DFA.unpack(u"\1\u00d9"),
        DFA.unpack(u"\1\u00da"),
        DFA.unpack(u"\1\u00db"),
        DFA.unpack(u"\1\u00dc"),
        DFA.unpack(u"\1\u00dd"),
        DFA.unpack(u"\1\u00de"),
        DFA.unpack(u"\1\u00df"),
        DFA.unpack(u"\1\u00e0"),
        DFA.unpack(u"\1\u00e1"),
        DFA.unpack(u"\1\u00e2"),
        DFA.unpack(u"\1\u00e3"),
        DFA.unpack(u"\1\u00e4"),
        DFA.unpack(u"\1\u00e5"),
        DFA.unpack(u"\1\u00e6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00e7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00e8"),
        DFA.unpack(u"\1\u00e9"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00eb"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00f0"),
        DFA.unpack(u"\1\u00f1"),
        DFA.unpack(u"\1\u00f2"),
        DFA.unpack(u"\1\u00f3"),
        DFA.unpack(u"\1\u00f4"),
        DFA.unpack(u"\1\u00f5"),
        DFA.unpack(u"\1\u00f6"),
        DFA.unpack(u"\1\u00f7"),
        DFA.unpack(u"\1\u00f8"),
        DFA.unpack(u"\1\u00f9"),
        DFA.unpack(u"\1\u00fa"),
        DFA.unpack(u"\1\u00fb"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\21\34\1\u00fc"
        u"\10\34"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00ff"),
        DFA.unpack(u"\1\u0100"),
        DFA.unpack(u"\1\u0101"),
        DFA.unpack(u"\1\u0102"),
        DFA.unpack(u"\1\u0103"),
        DFA.unpack(u"\1\u0104"),
        DFA.unpack(u"\1\u0105"),
        DFA.unpack(u"\1\u0106"),
        DFA.unpack(u"\1\u0107"),
        DFA.unpack(u"\1\u0108"),
        DFA.unpack(u"\1\u0109"),
        DFA.unpack(u"\1\u010a"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u010c"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u0110"),
        DFA.unpack(u"\1\u0111"),
        DFA.unpack(u"\1\u0112"),
        DFA.unpack(u"\1\u0113"),
        DFA.unpack(u"\1\u0114"),
        DFA.unpack(u"\1\u0115"),
        DFA.unpack(u"\1\u0116"),
        DFA.unpack(u"\1\u0117"),
        DFA.unpack(u"\1\u0118"),
        DFA.unpack(u"\1\u0119"),
        DFA.unpack(u"\1\u011a"),
        DFA.unpack(u"\1\u011b"),
        DFA.unpack(u"\1\u011c\7\uffff\1\u011d"),
        DFA.unpack(u"\1\u011e"),
        DFA.unpack(u"\1\u011f"),
        DFA.unpack(u"\1\u0120"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0121"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0122"),
        DFA.unpack(u"\1\u0123"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u0125"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u0127"),
        DFA.unpack(u"\1\u0128"),
        DFA.unpack(u"\1\u0129"),
        DFA.unpack(u"\1\u012a"),
        DFA.unpack(u"\1\u012b"),
        DFA.unpack(u"\1\u012c"),
        DFA.unpack(u"\1\u012d"),
        DFA.unpack(u"\1\u012e"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u012f"),
        DFA.unpack(u"\1\u0130"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u0132"),
        DFA.unpack(u"\1\u0133"),
        DFA.unpack(u"\1\u0134"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u0136"),
        DFA.unpack(u"\1\u0137"),
        DFA.unpack(u"\1\u0138"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u013c"),
        DFA.unpack(u"\1\u013d"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u013f"),
        DFA.unpack(u"\1\u0140"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u0142"),
        DFA.unpack(u"\1\u0143"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u0145"),
        DFA.unpack(u"\1\u0146"),
        DFA.unpack(u"\1\u0147"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u014a"),
        DFA.unpack(u"\1\u014b"),
        DFA.unpack(u"\1\u014c"),
        DFA.unpack(u"\1\u014d"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u0151"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u0153"),
        DFA.unpack(u"\1\u0154"),
        DFA.unpack(u"\1\u0155"),
        DFA.unpack(u"\1\u0156"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u0158"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0159"),
        DFA.unpack(u"\1\u015a"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u015e"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u015f"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0161"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0163"),
        DFA.unpack(u"\1\u0164"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0165"),
        DFA.unpack(u"\1\u0166"),
        DFA.unpack(u"\1\u0167"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0168"),
        DFA.unpack(u"\1\u0169"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u016b"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u016d"),
        DFA.unpack(u"\1\u016e"),
        DFA.unpack(u"\1\u016f"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0170"),
        DFA.unpack(u"\1\u0171"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0173"),
        DFA.unpack(u"\1\u0174"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0175"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u0177"),
        DFA.unpack(u"\1\u0178"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u017a"),
        DFA.unpack(u"\1\u017b"),
        DFA.unpack(u"\1\u017c"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u017d"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u017e"),
        DFA.unpack(u"\1\u017f"),
        DFA.unpack(u"\1\u0180"),
        DFA.unpack(u"\1\u0181"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u0184"),
        DFA.unpack(u"\1\u0185"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0186"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0188"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u018a"),
        DFA.unpack(u"\1\u018b"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u018d"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u018f"),
        DFA.unpack(u"\1\u0190"),
        DFA.unpack(u"\1\u0191"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0192"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0196"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u019a"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #11

    class DFA11(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(GOCLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
