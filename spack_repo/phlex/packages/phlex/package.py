# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.fnal_art.packages.fnal_github_package.package import *


class Phlex(CMakePackage, FnalGithubPackage):
    """Parallel, hierarchical, and layered execution of data-processing algorithms"""

    git = "https://github.com/framework-r-d/phlex"
    version_patterns = ["v0.1.0"]

    maintainers("knoepfel")

    license("Apache-2.0")

    # Development version
    version("develop", branch="main", get_full_repo=True)

    # Released versions
    version("0.1.0", sha256="b525540e7526f9cefe8537b06640917ece70f771af3270e6bb0aa2722d23d915")

    cxxstd_variant("20", "23", default="20", sticky=True)

    variant("form", default=True, description="Build with experimental FORM integration")

    depends_on("cxx", type="build")

    depends_on("boost@1.75.0: +json+program_options+stacktrace")
    depends_on("fmt@:9")
    depends_on("jsonnet")
    depends_on("spdlog")
    depends_on("tbb")
    depends_on("catch2", type=("build", "test"))

    depends_on("python@3.11:")
    depends_on("py-numpy@2:")
    depends_on("py-packaging", type="build") # Used to check (e.g.) numpy veresions in CMake

    with when("+form"):
        for std in (20, 23):
            depends_on(f"root +root7 cxxstd={std}", when=f"cxxstd={std}")


    @cmake_preset
    def cmake_args(self):
        return [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define_from_variant("PHLEX_USE_FORM", "form")
        ]

    def setup_run_environment(self, env):
        env.prepend_path("PHLEX_PLUGIN_PATH", self.prefix.lib)
