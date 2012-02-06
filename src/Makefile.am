dist_bin_SCRIPTS = \
bin/gobject_creator2.py \
bin/goc_strip_edit_section_comments

SUBDIRS = gobjcreator2

install-exec-hook:
	rm -f $(DESTDIR)$(bindir)/gobjcreator2
	ln -s $(DESTDIR)$(bindir)/gobject_creator2.py \
$(DESTDIR)$(bindir)/gobjcreator2
	chmod +x $(DESTDIR)$(bindir)/gobjcreator2

uninstall-hook:
	rm -f $(DESTDIR)/$(bindir)/gobjcreator2

