#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.67])
AC_INIT([gobjcreator2], [1.3.5], [TBollmeier@web.de])
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE
AM_PATH_PYTHON

# Checks for programs.
AC_PROG_CC

AC_CHECK_PROG([GLIB_GENMARSHAL], [glib-genmarshal], [yes], [no])
if test $GLIB_GENMARSHAL = "no"; then
	AC_MSG_ERROR([glib-genmarshal is needed by GObjectCreator2])
fi

# Checks for libraries.

GOC2_CHECK_FOR_TBPARSER(
	[1.0.14],
	[$srcdir/m4/check_tbparser_version.py]
	)

# Checks for header files.

# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.

AC_CONFIG_FILES([
Makefile
examples/Makefile
src/Makefile
src/gobjcreator2/Makefile
])

AC_OUTPUT
