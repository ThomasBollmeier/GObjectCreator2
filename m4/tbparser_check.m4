AC_DEFUN([GOC2_CHECK_FOR_TBPARSER],[

# GOC2_CHECK_FOR_TBPARSER()

	AC_MSG_CHECKING([for tbparser library])

	`$PYTHON -c "import tbparser" 2>/dev/null`
	if test $? -eq 0 ; then
		AC_MSG_RESULT([yes])
	else
		AC_MSG_RESULT([no])
		AC_MSG_ERROR([tbparser library is needed for GObjectCreator])
	fi

])
