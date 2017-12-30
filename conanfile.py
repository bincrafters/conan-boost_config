#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostConfigConan(ConanFile):
    name = "boost_config"
    version = "1.66.0"
    url = "https://github.com/bincrafters/conan-boost-config"
    
    lib_short_names = ["config"]
    is_header_only = True

    def package_id_additional(self):
        self.info.header_only()

    def package_additional(self):
        import os.path
        for lib_short_name in self.lib_short_names:
            checks_dir = os.path.join(lib_short_name, "checks")
            self.copy(pattern="*.jam", dst=os.path.join(lib_short_name, "lib","checks"), src=checks_dir)
            self.copy(pattern="*.cpp", dst=os.path.join(lib_short_name, "lib","checks"), src=checks_dir)
            self.copy(pattern="Jamfile*", dst=os.path.join(lib_short_name, "lib","checks"), src=checks_dir)

    requires = (
        "boost_package_tools/1.66.0@bincrafters/testing"
    )
    
    # BEGIN

    description = "Please visit http://www.boost.org/doc/libs/1_66_0"
    license = "BSL-1.0"
    short_paths = True
    build_requires = "boost_generator/1.66.0@bincrafters/testing"

    def package_id(self):
        getattr(self, "package_id_additional", lambda:None)()

    def source(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.source(self)
        getattr(self, "source_additional", lambda:None)()

    def build(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.build(self)
        getattr(self, "build_additional", lambda:None)()

    def package(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package(self)
        getattr(self, "package_additional", lambda:None)()

    def package_info(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package_info(self)
        getattr(self, "package_info_additional", lambda:None)()



    # END
