grammar GOC;

options {
	language = Python;
	output = AST;
}

tokens {
    ROOT;
    INCLUDE;
    TYPE_NAME;
    SIGNAL_ID;
    REF_TO;
    LIST_OF;
    PROP_TYPE;
    PROP_ACCESS;
    PROP_DESC;
    PROP_GTYPE;
    PROP_MIN;
    PROP_MAX;
    PROP_DEFAULT;
    BIND_PROPERTY;
    INIT_PROPERTY;
}

defFile
	:	 stmt* -> ^(ROOT stmt*)
	;
	
stmt
	:	classDef
	|	intfDef
	|   errorDomainDef
	|   enumDef
	|   flagsDef
	|	packageDef
	|   typeDecl
	|   includeStmt
	;

includeStmt
    :   'include' filename=STRING ';' -> ^(INCLUDE $filename)
    ;

packageDef
	:	'package' ID '{' packageElement* '}'
	-> 	^('package' ID packageElement*)
	;
	
packageElement
	:	packageDef
	|	classDef
	|	intfDef
	|   errorDomainDef
	|   enumDef
	|   flagsDef
	|   typeDecl
	;

classDef
	:	GOBJECT className=ID ('{' classMember* '}'|';') 
	-> ^(GOBJECT $className classMember*)
	;
	
intfDef
	:	GINTERFACE intfName=ID ('{' intfMember* '}'|';') 
	-> ^(GINTERFACE $intfName intfMember*)
	;

errorDomainDef
    :   ERROR_DOMAIN ID '{' errorDomainElement+ '}'
    ->  ^(ERROR_DOMAIN ID errorDomainElement+)
    ;

errorDomainElement
    :   'code' ID ';' -> ^(ID)
    ;

enumDef
    :   ENUMERATION ID '{' enumElement+ '}'
    ->  ^(ENUMERATION ID enumElement+)
    ;

enumElement
    :   'code' ID (';'|'{' 'value' ':' INT ';' '}')
    ->  ^('code' ID INT?)
    ;

flagsDef
    :   FLAGS ID '{' flagsElement+ '}'
    ->  ^(FLAGS ID flagsElement+)
    ;

flagsElement
    :   'code' ID ';' -> ^(ID)
    ;

typeDecl
    :   GTYPE ID ';' -> ^(GTYPE ID)
    ;

classMember
scope {
    with_constructor;
}
@init {
    $classMember::with_constructor = False
}
	:	SUPER typeName ';'
	-> ^(SUPER typeName)
	|   ABSTRACT^ ';'
	|   PREFIX ID ';' -> ^(PREFIX ID)
	|	IMPLEMENTS typeName ';' -> ^(IMPLEMENTS typeName)
	|	{ $classMember::with_constructor = True }
	    CONSTRUCTOR '{' constructorElement* '}'
	    { $classMember::with_constructor = False }
	    -> ^(CONSTRUCTOR constructorElement*)
	|  	METHOD ID '{' methodElement* '}' -> ^(METHOD ID methodElement*)
	| 	OVERRIDE ID ';' -> ^(OVERRIDE ID)
	|	ATTRIBUTE ID '{' TYPE ':' typeArg ';' attributeElement* '}'
	-> ^(ATTRIBUTE ID typeArg attributeElement*)
	|	PROPERTY ID '{' propertyElement+ '}' -> ^(PROPERTY ID propertyElement+)
	|	SIGNAL signalID '{' signalElement* '}' -> ^(SIGNAL signalID signalElement*)
	;
	
intfMember
	:	PREFIX ID ';' -> ^(PREFIX ID)
	|   METHOD ID '{' methodElement* '}' -> ^(METHOD ID methodElement*)
    |   SIGNAL signalID '{' signalElement* '}' -> ^(SIGNAL signalID signalElement*)
	;
	
resultDef
	:	RESULT '{' TYPE ':' typeArg ';' modifiers? '}'
	-> ^(RESULT typeArg modifiers?)
	;

methodElement
	:	constructorElement
	|	resultDef
	|	VISIBILITY ':' (val='public'|val='protected'|val='private') ';'
	-> ^(VISIBILITY $val)
	|	SCOPE ':' (val='instance'|val='static') ';'
	-> ^(SCOPE $val)
	| 	INHERITANCE ':' (val='final'|val='virtual'|val='abstract') ';'
	-> ^(INHERITANCE $val)
	;
	
constructorElement
	:	PARAMETER ID '{' 'type' ':' typeArg ';' parameterElement? '}'
	->  ^(PARAMETER ID typeArg parameterElement?)
	|   {$classMember::with_constructor}?=> INIT_PROPERTIES '{' init_prop+ '}'
	->  ^(INIT_PROPERTIES init_prop+)
	;

parameterElement
    :   modifiers
    |   {$classMember::with_constructor}?=> 'bind_property' ':' ID ';' -> ^(BIND_PROPERTY ID)
    ;

init_prop
    :   name=ID ':' value=STRING ';'
    ->  ^(INIT_PROPERTY $name $value)
    |   name=ID ':' enum=typeName '.' code=ID ';'
    ->  ^(INIT_PROPERTY $name $enum $code)
    ;

modifiers
	:	MODIFIERS ':' 'const' ';' -> ^(MODIFIERS 'const')
	;

propertyElement
    :   'type' ':' (val='boolean'|val='integer'|val='float'|val='double'|
    val='string'|val='pointer'|val='object'|val='enumeration') ';'
    ->  ^(PROP_TYPE $val)
    |   'access' ':' (val='read-only'|val='initial-write'|val='read-write') ';'
    ->  ^(PROP_ACCESS $val)
    |   'description' ':' STRING ';' -> ^(PROP_DESC STRING)
    |   'gtype' ':' ID ';'
    ->  ^(PROP_GTYPE ID)
    |   'gtype' ':' GTYPENAME '(' typeName ')' ';'
    ->  ^(PROP_GTYPE ^(GTYPENAME typeName))
    |   'min' ':' STRING ';' -> ^(PROP_MIN STRING)
    |   'max' ':' STRING ';' -> ^(PROP_MAX STRING)
    |   'default' ':' STRING ';' -> ^(PROP_DEFAULT STRING)
    |   AUTO_CREATE^ ';'
    ;

signalElement
    :   RESULT '{' 'type' ':' signalType ';' '}' -> ^(RESULT signalType)
    |   PARAMETER ID '{' 'type' ':' signalType ';' '}' -> ^(PARAMETER ID signalType)
    ;

signalType
    :   'null'
    |   'integer'
    |   'boolean'
    |   'float'
    |   'double'
    |   'string'
    |   'pointer'
    |   'object'
    |   'enumeration'
    ;

attributeElement
	:	SCOPE ':' (val='static'|val='instance') ';' -> ^(SCOPE $val)
	|	VISIBILITY ':' (val='public'|val='protected'|val='private') ';' -> ^(VISIBILITY $val)
	;

typeName
	:   typePath -> ^(TYPE_NAME typePath)
	|   'unsigned '? 'integer' -> ^(TYPE_NAME 'unsigned '? 'integer')
	|   'unsigned '? 'long' -> ^(TYPE_NAME 'unsigned '? 'long')
	|	(val='boolean'
	|	val='string'
	|	val='float'
	|	val='double'
	|   val='pointer') -> ^(TYPE_NAME $val)
	;

typeArg
    :   typeName
    |   'ref' '(' typeArg ')' -> ^(REF_TO typeArg)
    |   'list' '(' typeArg ')' -> ^(LIST_OF typeArg)
    ;

typePath
    :   ('::' ID '::')?(ID '::')* ID
    ;

COMMENT
    :   '//' ~('\n'|'\r')* '\r'? '\n' {$channel=HIDDEN;}
    |   '/*' ( options {greedy=false;} : . )* '*/' {$channel=HIDDEN;}
    ;

WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) {$channel=HIDDEN;}
    ;

BOOLVALUE
    :   'true'
    |   'false'
    ;

PACKAGE
    :   'package'
    ;

GOBJECT
	:	'gobject'
	;
	
GINTERFACE
	:	'ginterface'
	;

GTYPE
    :   'gtype'
    ;

GTYPENAME
    :   'gtypename'
    ;

ERROR_DOMAIN
    :   'gerror'
    ;

ENUMERATION
    :   'genum'
    ;

FLAGS
    :   'gflags'
    ;
	
SUPER
	:	'super'
	;

PREFIX
    :   'prefix'
    ;

IMPLEMENTS
	:	'implements'
	;
	
CONSTRUCTOR
	:	'constructor'
	;
	
METHOD
	:	'method'
	;
	
OVERRIDE
	:	'override'
	;
	
PARAMETER
	:	'parameter'
	;

ATTRIBUTE
	:	'attribute'
	;

PROPERTY
	:	'property'
	;

INIT_PROPERTIES
    :   'init_properties'
    ;
	
SIGNAL
	:	'signal'
	;
	
RESULT
	:	'result'
	;

TYPE:	'type';

MODIFIERS
	:	'modifiers'
	;

SCOPE
	:	'scope'
	;
	
VISIBILITY
	:	'visibility'
	;

INHERITANCE
	:	'inheritance'
	;

ABSTRACT
    :   'abstract'
    ;

AUTO_CREATE
    :   'auto_create'
    ;

ID  :	('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*
    ;

signalID
    :   part1=ID ('-' part2+=ID)* -> ^(SIGNAL_ID $part1 $part2*)
    ;

STRING
    :  '"' ( ESC_SEQ | ~('\\'|'"') )* '"'
    ;

INT :   ('1'..'9')('0'..'9')*
    ;

fragment
HEX_DIGIT : ('0'..'9'|'a'..'f'|'A'..'F') ;

fragment
ESC_SEQ
    :   '\\' ('b'|'t'|'n'|'f'|'r'|'\"'|'\''|'\\')
    |   UNICODE_ESC
    |   OCTAL_ESC
    ;

fragment
OCTAL_ESC
    :   '\\' ('0'..'3') ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7')
    ;

fragment
UNICODE_ESC
    :   '\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
    ;
