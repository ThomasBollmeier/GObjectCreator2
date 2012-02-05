dist_bin_SCRIPTS = bin/gobject_creator2.py

SUBDIRS = gobjcreator2

install-exec-hook:
	rm -f $(DESTDIR)$(bindir)/gobjcreator2
	ln -s $(DESTDIR)$(bindir)/gobject_creator2.py \
$(DESTDIR)$(bindir)/gobjcreator2
	chmod +x $(DESTDIR)$(bindir)/gobjcreator2

uninstall-hook:
	rm -f $(DESTDIR)/$(bindir)/gobjcreator2

