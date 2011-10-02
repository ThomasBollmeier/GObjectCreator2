"""
Check whether installed version of TBParser
mets the requirements

Returns:
    0 -> everything fine
    1 -> installed version too old
    2 -> TBParser is not installed
"""
import sys
try:
    import tbparser
except ImportError:
    sys.exit(2)

class Version(object):
    
    @staticmethod
    def create(versionString):
        
        major, minor, patch = versionString.split('.')
        
        return Version(major, minor, patch)
    
    def __init__(self, major, minor, patch):
        
        self._major = major
        self._minor = minor
        self._patch = patch
        
    def __ge__(self, other):
        
        if self._major > other._major:
            return True
        elif self._major < other._major:
            return False
        elif self._minor > other._minor:
            return True
        elif self._minor < other._minor:
            return False
        elif self._patch >= other._patch:
            return True
        else:
            return False
        
##### Main #####

required_version = Version.create(sys.argv[1])
installed_version = Version.create(tbparser.PACKAGE_VERSION)

print tbparser.PACKAGE_VERSION

if installed_version >= required_version:
    sys.exit(0)
else:
    sys.exit(1)
