from conans import ConanFile


class BoostConfigConan(ConanFile):
    name = "Boost.Config"
    version = "1.65.1"
    lib_short_names = ["config"]
    is_header_only = True

    def package_after(self):
        import os.path
        for lib_short_name in self.lib_short_names:
            checks_dir = os.path.join(lib_short_name, "checks")
            self.copy(pattern="*.jam", dst=os.path.join(lib_short_name, "lib","checks"), src=checks_dir)
            self.copy(pattern="*.cpp", dst=os.path.join(lib_short_name, "lib","checks"), src=checks_dir)
            self.copy(pattern="Jamfile*", dst=os.path.join(lib_short_name, "lib","checks"), src=checks_dir)

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost-config"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1"
    license = "www.boost.org/users/license.html"
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"
    short_paths = True
    exports = "boostgenerator.py"

    def package_id(self):
        self.info.header_only()
        getattr(self, "package_id_after", lambda:None)()
    def source(self):
        self.call_patch("source")
    def build(self):
        self.call_patch("build")
    def package(self):
        self.call_patch("package")
    def package_info(self):
        self.call_patch("package_info")
    def call_patch(self, method, *args):
        if not hasattr(self, '__boost_conan_file__'):
            try:
                from conans import tools
                with tools.pythonpath(self):
                    import boostgenerator  # pylint: disable=F0401
                    boostgenerator.BoostConanFile(self)
            except Exception as e:
                self.output.error("Failed to import boostgenerator for: "+str(self)+" @ "+method.upper())
                raise e
        return getattr(self, method, lambda:None)(*args)
    @property
    def env(self):
        import os.path
        result = super(self.__class__, self).env
        result['PYTHONPATH'] = [os.path.dirname(__file__)] + result.get('PYTHONPATH',[])
        return result

    # END
