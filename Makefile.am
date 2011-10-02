AUTOMAKE_OPTIONS = dist-bzip2
ACLOCAL_AMFLAGS = -I m4

EXTRA_DIST = m4/check_tbparser_version.py

SUBDIRS = examples src

uninstall-hook:
	rm -rf $(DESTDIR)$(datadir)/$(PACKAGE)
