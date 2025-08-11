# phlex-spack-recipes
Repository for Spack recipes for Phlex, and its related packages and dependencies.

To install phlex using [spack](https://spack.io/) on a new system:

1. install spack itself
2. add the [FNAL art spack repo](https://github.com/FNALssi/fnal_art), which is used in the `phlex` recipe
3. add this repo
4. create and activate a spack environment
5. add phlex and install it.

Skip steps as appropriate, e.g. if you already have spack installed.

### Example

Assuming bash (see [spack documentation](https://spack-tutorial.readthedocs.io/en/latest/index.html) for other shells), to install spack and add the necessary repos:

```console
$ git clone --depth=2 https://github.com/spack/spack.git
$ . spack/share/spack/setup-env.sh
$ spack repo add https://github.com/FNALssi/fnal_art.git
$ spack repo add https://github.com/Framework-R-D/phlex-spack-recipes.git
```

Create and activate an environment, after adding the repos:

```console
$ spack env activate --create PHLEXDEV
```

Finally, within the active environment, add and install `phlex` in the spack environment:

```console
$ spack add phlex@develop
$ spack install -j<N>
```
