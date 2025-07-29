# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.fnal_art.packages.fnal_github_package.package import *


class Phlex(CMakePackage, FnalGithubPackage):
    """Parallel, hierarchical, and layered execution of data-processing algorithms"""

    git = "https://github.com/framework-r-d/phlex.git"
    version_patterns = []

    maintainers("knoepfel")

    license("Apache-2.0")

    version("develop", branch="main", get_full_repo=True)

    cxxstd_variant("20", "23", default="20", sticky=True)

    variant("form", default=False, description="Build with experimental FORM integration")

    depends_on("cxx", type="build")

    depends_on("boost@1.75.0: +json+program_options+stacktrace")
    depends_on("fmt@:9")
    depends_on("jsonnet")
    depends_on("spdlog")
    depends_on("tbb")
    depends_on("catch2", type=("build", "test"))

    with when("+form"):
        # Put depends_on() calls specific to FORM here
        pass


    def cmake_args(self):
        define = self.define
        define_from_variant = self.define_from_variant
        return [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define_from_variant("PHLEX_USE_FORM", "form")
        ]
