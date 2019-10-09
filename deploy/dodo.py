"""
Deploy configuration.
"""
import os

from pathlib import Path

from deploy.targets import Clone, Mkdir, Symlink


DOIT_CONFIG = {
    'default_tasks': ['deploy'],
    'cleandep': True,
    'cleanforget': True
}


def task_deploy():
    return {
        'actions': None,
        'task_dep': [
            'mkdir',
            'clone',
            'homelink',
            'configlink'
        ]
    }


HOME_DIR = Path('~').expanduser()
DODO_DIR = Path(os.path.realpath(__file__)).parent
DOT_DIR = DODO_DIR.parent
CONFIG_DIR = DOT_DIR / 'config'


DIRECTORIES = [
    Mkdir(HOME_DIR/'git'/'work'),
    Mkdir(HOME_DIR/'git'/'perso'),
]


def task_mkdir():
    for directory in DIRECTORIES:
        yield directory.task


CLONES = [
    Clone(
        source_url='https://github.com/syl20bnr/spacemacs',
        dest=HOME_DIR/'.emacs.d',
        branch='master'
    ),
    Clone(
        source_url='https://github.com/jimeh/tmux-themepack',
        dest=HOME_DIR/'tmux-themepack',
        branch='master'
    ),
]


def task_clone():
    for clone in CLONES:
        yield clone.task


HOME_SOURCE = DOT_DIR / 'home'
HOMELINKS = [
    Symlink(source=dotfile, dest_dir=HOME_DIR, hidden=True)
    for dotfile in HOME_SOURCE.iterdir()
]


def task_homelink():
    for link in HOMELINKS:
        yield link.task


TARGET_CONFIG_DIR = HOME_DIR / '.config'
CONFIGLINKS = [
    Symlink(
        source=config_file,
        dest_dir=TARGET_CONFIG_DIR / source_dir.name,
        dir_dep=True
    )
    for source_dir in CONFIG_DIR.iterdir()
    for config_file in source_dir.iterdir()
]


def task_config_subdir():
    for subdir in CONFIG_DIR.iterdir():
        yield Mkdir(TARGET_CONFIG_DIR/subdir.name).task


def task_configlink():
    for link in CONFIGLINKS:
        yield link.task
