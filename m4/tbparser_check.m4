AC_DEFUN([GOC2_CHECK_FOR_TBPARSER],[

# GOC2_CHECK_FOR_TBPARSER(required_min_version, script_file)

	AC_MSG_CHECKING([for tbparser library >= $1])
	
	script_call="$2 $1"
	installed_version=`$PYTHON $script_call`
	case $? in
		0)
		AC_MSG_RESULT([yes])
		;;
		1)
		AC_MSG_RESULT([no])
		AC_MSG_ERROR([tbparser library version is too old ($installed_version)])
		;;
		2)
		AC_MSG_RESULT([no])
		AC_MSG_ERROR([tbparser library is needed for GObjectCreator])
		;;
	esac
	
])
