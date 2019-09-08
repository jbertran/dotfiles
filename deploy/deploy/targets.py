import configparser
import os

from pathlib import Path
from typing import Optional, Sequence

from doit.exceptions import TaskError

from . import utils


class Clone:

    def __init__(
        self,
        source_url: str,
        dest: Path = None,
        branch: str = ''
    ):
        self.source_url = source_url
        self.branch = branch
        self.dest = dest

    @property
    def clone(self):
        action = ['git', 'clone', self.source_url]
        if self.dest is not None:
            action.append(self.dest)
        if self.branch:
            action.extend(['--branch', self.branch])
        return action

    def uptodate(self):
        if not self.dest.is_dir:
            return False

        gitconfig = self.dest / '.git' / 'config'
        if not gitconfig.is_file():
            return False

        try:
            conf = configparser.ConfigParser()
            conf.read(str(gitconfig))
            return conf['remote "origin"']['url'] == self.source_url
        except KeyError:
            return False

    @property
    def task(self):
        return {
            'name': self.source_url,
            'actions': [self.clone],
            'uptodate': [self.uptodate()]
        }


class Mkdir:

    def __init__(self, dir_path: str):
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
        task_dict = {
            'name': str(self.file_source),
            'actions': [self.link],
            'uptodate': [self.uptodate],
        }
        if self.dir_dep:
            task_dict['task_dep'] = [
                'config_subdir:{}'.format(self.file_dest.parent)
            ]
        return task_dict

    @utils.task_errors(IOError)
    def link(self) -> Optional[TaskError]:
        """Symlink operation"""
        # Poor man's link --force: remove target and link it
        try:
            os.unlink(self.file_dest)
        except FileNotFoundError:
            pass
        os.symlink(self.file_source, self.file_dest)
