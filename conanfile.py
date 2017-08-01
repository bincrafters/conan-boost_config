from conans import ConanFile, tools, os

class BoostConfigConan(ConanFile):
    name = "Boost.Config"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/config"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "config"

    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="", src=include_dir)
