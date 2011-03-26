AC_DEFUN([GOC2_CHECK_FOR_ANTLR3],[

# GOC2_CHECK_FOR_ANTLR3(version)

	AC_MSG_CHECKING([for antlr3 python runtime])

	GOC2_ANTLR3_VERSION=`$PYTHON -c "import antlr3; print antlr3.__version__"`
	if test $? -eq 0 ; then
		if test $GOC2_ANTLR3_VERSION = $1 ; then
			AC_MSG_RESULT([yes])
		else
			AC_MSG_RESULT([no])
			AC_MSG_ERROR([antlr3 python runtime is needed in version $1])
		fi 
	else
		AC_MSG_RESULT([no])
		AC_MSG_ERROR([antlr3 python runtime is needed in version $1])
	fi

])
