from conans import ConanFile, tools


class BoostConfigConan(ConanFile):
    name = "Boost.Config"
    version = "1.65.1"
    lib_short_names = ["config"]
    is_header_only = True

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost-config"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    short_paths = True
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"

    def package_id(self):
        if self.is_header_only:
            self.info.header_only()

    @property
    def env(self):
        try:
            with tools.pythonpath(super(self.__class__, self)):
                import boostgenerator  # pylint: disable=F0401
                boostgenerator.BoostConanFile(self)
        except:
            pass
        return super(self.__class__, self).env

    # END
