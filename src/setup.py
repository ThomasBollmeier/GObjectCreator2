from distutils.core import setup

description = "Generation of source files in various languages"
description += " from meta definition files"

setup(
    name = "GObjectCreator2",
    version = "1.0.0-alpha",
    description = description,
    author = "Thomas Bollmeier",
    author_email = "TBollmeier@web.de",
    license = "GPLv3",
    packages = ["gobjcreator2", 
                "gobjcreator2/input",
                "gobjcreator2/metadef",
                "gobjcreator2/output"
                ],
    scripts = ["scripts/gobject_creator2.py"]
    )