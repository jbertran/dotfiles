import os

from pathlib import Path
from typing import Optional

from doit.exceptions import TaskError

from deploy import utils


class Mkdir:

    def __init__(self, dir_path: Path):
        self.dir_path = dir_path

    def task_name(self):
        return str(self.dir_path)

    def action(self):
        self.dir_path.mkdir(parents=True)

    @property
    def task(self):
        return {
            'name': self.dir_path,
            'actions': [self.action],
            'targets': [self.dir_path],
            'uptodate': [self.dir_path.is_dir()],
        }


class Symlink:
    """Create a symlink."""

    def __init__(
        self,
        source: Path,
        dest_dir: Path,
        dir_dep: bool = False,
        hidden: bool = False
    ):
        self.file_source = source
        if hidden and not source.name.startswith('.'):
            target_name = '.{}'.format(source.name)
        else:
            target_name = source.name
        self.file_dest = dest_dir / target_name
        self.dir_dep = dir_dep

    def uptodate(self):
        if not self.file_dest.is_symlink():
            return False
        sym_target = os.readlink(self.file_dest)
        return Path(sym_target) == self.file_source

    @property
    def task(self):
        if self.dir_dep:
            yield Mkdir(self.file_dest.parent).task
        yield {
            'actions': [self.link],
            'uptodate': [self.uptodate],
        }

    @utils.task_errors(IOError)
    def link(self) -> Optional[TaskError]:
        """Symlink operation"""
        # Poor man's link --force: remove target and link it
        try:
            os.unlink(self.file_dest)
        except FileNotFoundError:
            pass
        os.symlink(self.file_source, self.file_dest)
