from conans import ConanFile, CMake

class App(ConanFile):
    name = "App"
    version = "0.0"

    settings = "os", "arch", "compiler", "build_type"

    generators = "cmake"

    scm = {"type": "git",
           "url": "auto",
           "revision": "auto"}

    exports_sources = "LICENSE" # to avoid build info bug

    def requirements(self):
        self.requires("libB/0.0@mycompany/stable")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("LICENSE", dst="licenses")
#####
####