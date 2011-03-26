AUTOMAKE_OPTIONS = dist-bzip2
ACLOCAL_AMFLAGS = -I m4

SUBDIRS = data examples src

uninstall-hook:
	rm -rf $(DESTDIR)$(datadir)/$(PACKAGE)
