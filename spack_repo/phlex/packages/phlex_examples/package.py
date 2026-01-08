# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *
from spack_repo.fnal_art.packages.fnal_github_package.package import *


class PhlexExamples(CMakePackage):
    """Examples that make use of the Phlex data-processing framework"""

    git = "https://github.com/Framework-R-D/phlex-examples"

    maintainers("knoepfel")

    license("Apache-2.0")

    # Development version
    version("develop", branch="main", get_full_repo=True)

    cxxstd_variant("20", "23", default="20", sticky=True)

    depends_on("cxx", type="build")
    depends_on("phlex")

    def cmake_args(self):
        return []

    def setup_run_environment(self, env):
        env.prepend_path("PHLEX_PLUGIN_PATH", self.prefix.lib)
