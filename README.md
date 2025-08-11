# phlex-spack-recipes
Repository for Spack recipes for Phlex, and its related packages and dependencies.

To install phlex using [spack](https://spack.io/) on a new system, first install spack itself then add the [FNAL art spack repo](https://github.com/FNALssi/fnal_art), which is used in the phlex recipe. Add this repo. Create and activate a spack environment, then add phlex and install it. Skip steps as appropriate, e.g. if you already have spack installed.

For example, assuming bash (see [spack documentation](https://spack-tutorial.readthedocs.io/en/latest/index.html) for other shells), to install spack and add the necessary repos:

```
$ git clone --depth=2 https://github.com/spack/spack.git
$ . spack/share/spack/setup-env.sh
$ git clone https://github.com/FNALssi/fnal_art.git
$ spack repo add ./fnal_art/spack_repo/fnal_art
$ git clone https://github.com/Framework-R-D/phlex-spack-recipes.git
$ spack repo add ./phlex-spack-recipes/spack_repo/phlex/
```

Create an environment, after adding the repos:

```
$ spack env create PHLEXDEV
$ spack env activate PHLEXDEV
```

Finally, add and install phlex in the spack environment:

```
$ spack -e PHLEXDEV add phlex@develop
$ spack install phlex
```
