#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires
import os


base = python_requires("boost_base/2.0.0@bincrafters/testing")


class BoostConfigConan(base.BoostBaseConan):
    name = "boost_config"
    version = "1.70.0"

    def package(self):
        super(BoostConfigConan, self).package()
        checks_dir = os.path.join("config", "checks")
        self.copy(
            pattern="*.jam",
            dst=os.path.join("config", "lib", "checks"),
            src=checks_dir)
        self.copy(
            pattern="*.cpp",
            dst=os.path.join("config", "lib", "checks"),
            src=checks_dir)
        self.copy(
            pattern="Jamfile*",
            dst=os.path.join("config", "lib", "checks"),
            src=checks_dir)
