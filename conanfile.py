from conans import ConanFile, CMake

class App(ConanFile):
    name = "App"
    version = "1.0"

    settings = "os", "arch", "compiler", "build_type"

    generators = "cmake"

    scm = {"type": "git",
           "url": "https://github.com/conan-ci-cd-training/App.git",
           "revision": "auto"}

    def requirements(self):
        self.requires("libD/1.0@mycompany/stable")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("LICENSE", dst="licenses")
