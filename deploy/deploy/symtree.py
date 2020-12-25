from pathlib import Path
from typing import Sequence

from deploy import toplevel, fileops


class Symtree(toplevel.Task):

    devenv_name = 'symtree'

    def __init__(
            self,
            source: Path, dest: Path,
            hide_files: bool = False, create_dirs: bool = False
    ):
        self.source = source
        self.dest = dest
        self.hide_files = hide_files
        self.create_dirs = create_dirs

    @classmethod
    def from_yaml(cls, entry: dict) -> object:
        return cls(
            source=Path(entry['source']).expanduser(),
            dest=Path(entry['dest']).expanduser(),
            hide_files=entry.get('hide_files', False),
            create_dirs=entry.get('create_dirs', False)
        )

    def compute_sources(self) -> Sequence[Path]:
        pass

    def compute_symlinks(self) -> Sequence[fileops.Symlink]:
        return (
            fileops.Symlink(
                source,
                self.dest,
                dir_dep=self.create_dirs,
                hidden=self.hide_files
            )
            for source in self.compute_sources()
        )

    def execution_plan(self):
        yield from (link.task for link in self.compute_symlinks())

    @property
    def task_name(self):
        return f'Symtree: {self.source} -> {self.dest}'

    @property
    def task(self):
        yield from self.execution_plan()
