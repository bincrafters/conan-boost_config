from conans import ConanFile, os
from conans.util.files import mkdir

class BoostConfigConan(ConanFile):
    name = "Boost.Config"
    version = "1.64.0"
    url = "https://github.com/bincrafters/conan-boost-config"
    source_url = "https://github.com/boostorg/config"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["config"]

    def source(self):
        for lib_short_name in self.lib_short_names:
            self.run("git clone --depth=50 --branch=boost-{0} https://github.com/boostorg/{1}.git"
                     .format(self.version, lib_short_name)) 

    def build(self):
        stage_lib_dir = os.path.join(self.build_folder,"stage","lib")
        mkdir(stage_lib_dir)
        with open(os.path.join(stage_lib_dir,"jamroot.jam"),"w") as f:
            f.write("""
project /boost/config ;
""")

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)
            checks_dir = os.path.join(lib_short_name, "checks")
            self.copy(pattern="*.jam", dst=os.path.join("lib","checks"), src=checks_dir)
            self.copy(pattern="*.cpp", dst=os.path.join("lib","checks"), src=checks_dir)
            self.copy(pattern="Jamfile*", dst=os.path.join("lib","checks"), src=checks_dir)
            
        self.copy(pattern="*", dst="lib", src="stage/lib")

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        self.user_info.lib_short_names = (",").join(self.lib_short_names)
        self.cpp_info.libs = self.collect_libs()
