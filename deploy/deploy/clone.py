import configparser

from pathlib import Path
from typing import Sequence


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
    def clone(self) -> Sequence[str]:
        action = ['git', 'clone', self.source_url]
        if self.dest is not None:
            action.append(self.dest)
        if self.branch:
            action.extend(['--branch', self.branch])
        return action

    def uptodate(self) -> bool:
        if not self.dest.is_dir:
            return False

        gitconfig = self.dest / '.git' / 'config'
        if not gitconfig.is_file():
            return False

        try:
            conf = configparser.ConfigParser()
            conf.read(str(gitconfig))
            gitconf_url = conf['remote "origin"']['url'].rstrip('.git')
            dodo_url = self.source_url.rstrip('.git')
            return gitconf_url == dodo_url
        except KeyError:
            return False

        return True

    @property
    def task(self):
        return {
            'name': self.source_url,
            'actions': [self.clone],
            'uptodate': [self.uptodate()]
        }
