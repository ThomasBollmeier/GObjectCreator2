goc2dir = $(pkgpythondir)
inputdir = $(goc2dir)/input
grammardir = $(inputdir)/grammar
metadefdir = $(goc2dir)/metadef
outputdir = $(goc2dir)/output

goc2_PYTHON = __init__.py

input_PYTHON = \
input/__init__.py \
input/goc_parser.py \
input/goc_recognizer.py \
input/goc_visitor.py \
input/reader.py

grammar_PYTHON = \
input/grammar/__init__.py \
input/grammar/attribute.py \
input/grammar/class_def.py \
input/grammar/enumeration_def.py \
input/grammar/error_domain_def.py \
input/grammar/flags_def.py \
input/grammar/goc_grammar.py \
input/grammar/include_stmt.py \
input/grammar/intf_def.py \
input/grammar/method.py \
input/grammar/misc_rules.py \
input/grammar/package_def.py \
input/grammar/property.py \
input/grammar/tokens.py \
input/grammar/type_decl.py \
input/grammar/type_name.py \
input/grammar/util.py

metadef_PYTHON = \
metadef/attribute.py \
metadef/clif.py \
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
output/file_name_manager.py \
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
