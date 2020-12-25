from collections import defaultdict

import dodo1 as dodo
from deploy import utils


class PackageOrchestrator:
    """Collect packages from a package installation step."""

    devenv_name = 'packages'

    def __init__(self, contents: dict):
        self.contents = contents
        self.pkg_objs = {
            Package.from_yaml(entry) for entry in self.contents
        }

    def collect_groups(self) -> set:
        """Compute require-compatible package groups."""
        with_deps, without_deps = [], []
        # Magic boolean coercion to int
        for pkg in self.pkg_objs:
            (without_deps, with_deps)[pkg.has_deps].append(pkg)

        pkg_groups = [without_deps]
        while with_deps:
            next_dep_group = {
                pkg for pkg in with_deps if all(
                    any(req in group for group in pkg_groups)
                    for req in pkg.requires
                )
            }
            pkg_groups.append(next_dep_group)
            with_deps -= next_dep_group
        return pkg_groups

    def sort_group_by_type(self, package_set: set) -> dict:
        """Separate packages by type."""
        segregated_pkgs = defaultdict(list)
        for pkg in package_set:
            segregated_pkgs[pkg.pkg_source].append(pkg)
        return segregated_pkgs.values()

    def advertise_install_group(self):
        pass


class Package:
    """Base package class.

    This class regroups common package logic and provides a single point of
    entry to generate specific packages.
    """

    default_pkg_source = 'pacman'
    package_classes = {}

    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)
        cls.package_classes[cls.pkg_source] = cls

    def __init__(self, name: str, requires=[]):
        self.name = name
        self.requires = requires

    @property
    def has_deps(self):
        return bool(self.requires)

    def uptodate(self):
        return f'pacman -Q f{self.name}'

    @classmethod
    def from_yaml(cls, entry):
        if isinstance(entry, str):
            return cls.package_classes[cls.default_pkg_source].from_yaml(entry)
        if isinstance(entry, dict):
            pkg_source = entry.get('type')
            if pkg_source is None:
                raise Exception('Expected type in package dict definition')
            pkg_cls = cls.package_classes.get(pkg_source)
            if pkg_cls is None:
                raise Exception(f'Package type {pkg_source} not known')
            return pkg_cls.from_yaml(entry)


class PacmanPackage(Package):
    """A package from Pacman."""

    pkg_source = 'pacman'
    pkg_mgr_bin = 'pacman'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def from_yaml(cls, entry):
        if isinstance(entry, str):
            return cls(entry)
        pkg_name, pkg_data = utils.unpack_single_dict(entry)
        return cls(pkg_name, requires=pkg_data['require'])


class YayPackage(PacmanPackage):
    """A package from AUR, via the `yay` package manager."""

    pkg_source = 'yay'
    pkg_mgr_bin = 'yay'


class TarballPackage(Package):
    """A package contained in a tarball."""

    pkg_source = 'tarxz'

    def __init__(self, source, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.source = source

    @classmethod
    def from_yaml(cls, entry):
        pkg_name, pkg_data = utils.unpack_single_dict(entry)
        return cls(pkg_name, source=pkg_data['source'])


class GitPackage(Package):
    """A package built from git source."""

    pkg_source = 'git'

    def __init__(self, git_source, install, *args, **kwargs):
        super()
        self.git_source = git_source
        self.install = install

    @classmethod
    def from_yaml(cls, entry):
        name, pkg_data = utils.unpack_single_dict(entry)
        return cls(
            pkg_data['git_source'],
            pkg_data['install'],
            name,
            requires=pkg_data.get('require', [])
        )
