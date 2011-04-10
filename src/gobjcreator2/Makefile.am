goc2dir = $(pkgpythondir)
inputdir = $(goc2dir)/input
metadefdir = $(goc2dir)/metadef
outputdir = $(goc2dir)/output

goc2_PYTHON = __init__.py

input_PYTHON = \
input/GOCLexer.py \
input/GOCParser.py \
input/goc_recognizer.py \
input/GOC.tokens \
input/goc_tree_adaptor.py \
input/goc_visitor.py \
input/__init__.py \
input/reader.py

metadef_PYTHON = \
metadef/attribute.py \
metadef/constants.py \
metadef/constructor.py \
metadef/error_domain.py \
metadef/exceptions.py \
metadef/genum.py \
metadef/gflags.py \
metadef/ginterface.py \
metadef/gobject.py \
metadef/gtype.py \
metadef/__init__.py \
metadef/method_info.py \
metadef/method.py \
metadef/package.py \
metadef/parameter.py \
metadef/property.py \
metadef/signal.py \
metadef/types.py

output_PYTHON = \
output/annotations.py \
output/class_intf_writer.py \
output/error_domain_writer.py \
output/func_name_creator.py \
output/genum_writer.py \
output/gflags_writer.py \
output/ginterface_writer.py \
output/gobject_writer.py \
output/__init__.py \
output/marshaller_generator.py \
output/sections.py \
output/user_content.py \
output/util.py \
output/writer.py

uninstall-hook:
	rm -rf $(DESTDIR)$(goc2dir)
