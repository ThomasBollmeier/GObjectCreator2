#
# Copyright 2011 Thomas Bollmeier
#
# This file is part of GObjectCreator2.
#
# GObjectCreator2 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GObjectCreator2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GObjectCreator2.  If not, see <http://www.gnu.org/licenses/>.
#

import gobjcreator2.output.util as util

class FileNameStyle:
	
	UNDERSCORE = 1
	HYPHEN = 2

def get_file_name_manager(style = FileNameStyle.UNDERSCORE):
	
	if style == FileNameStyle.UNDERSCORE:
		return _UnderScoreFileNames()
	elif style == FileNameStyle.HYPHEN:
		return _HyphenFileNames()
	else:
		raise UnknownFileNameStyle
	
class UnknownFileNameStyle(Exception):
	pass

class FileNameManager(object):
	
	def __init__(self):
		
		pass

	def get_header_name(self, obj):
		
		raise NotImplementedError
	
	def get_protected_header_name(self, obj):
		
		raise NotImplementedError

	def get_source_name(self, obj):
		
		raise NotImplementedError

	def get_marshaller_header_name(self, obj):
		
		raise NotImplementedError

	def get_marshaller_source_name(self, obj):
		
		raise NotImplementedError

class _UnderScoreFileNames(FileNameManager):
	
	def __init__(self):
		
		FileNameManager.__init__(self)
		
	def get_header_name(self, obj):
		
		return self._basename(obj) + ".h"
	
	def get_protected_header_name(self, obj):
		
		return self._basename(obj) + "_prot.h"

	def get_source_name(self, obj):
		
		return self._basename(obj) + ".c"

	def get_marshaller_header_name(self, obj):
		
		return self._basename(obj) + "_marshaller.h"

	def get_marshaller_source_name(self, obj):
		
		return self._basename(obj) + "_marshaller.c"

	def _basename(self, obj):
		
		res = util.camelcase_to_underscore(obj.name).lower()
		
		package = obj.package
		while package:
			if package.name:
				res = package.name.lower() + "_" + res
			package = package.package
			
		return res

class _HyphenFileNames(FileNameManager):
	
	def __init__(self):
		
		FileNameManager.__init__(self)
		
	def get_header_name(self, obj):
		
		return self._basename(obj) + ".h"
	
	def get_protected_header_name(self, obj):
		
		return self._basename(obj) + "-protected.h"

	def get_source_name(self, obj):
		
		return self._basename(obj) + ".c"

	def get_marshaller_header_name(self, obj):
		
		return self._basename(obj) + "-marshaller.h"

	def get_marshaller_source_name(self, obj):
		
		return self._basename(obj) + "-marshaller.c"

	def _basename(self, obj):
		
		res = util.camelcase_to_hyphen(obj.name).lower()
		
		package = obj.package
		while package:
			if package.name:
				res = package.name.lower() + "-" + res
			package = package.package
			
		return res
