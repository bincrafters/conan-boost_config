#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires
import os


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostConfigConan(base.BoostBaseConan):
    name = "boost_config"
    version = "1.67.0"
    url = "https://github.com/bincrafters/conan-boost_config"
    lib_short_names = ["config"]
    header_only_libs = ["config"]

    def package_additional(self):
        for lib_short_name in self.lib_short_names:
            checks_dir = os.path.join(lib_short_name, "checks")
            self.copy(pattern="*.jam", dst=os.path.join(lib_short_name, "lib","checks"), src=checks_dir)
            self.copy(pattern="*.cpp", dst=os.path.join(lib_short_name, "lib","checks"), src=checks_dir)
            self.copy(pattern="Jamfile*", dst=os.path.join(lib_short_name, "lib","checks"), src=checks_dir)  


