#! /usr/bin/env python

import json
import os
import typing
import subprocess

from pathlib import Path


DEFAULT_KEYLIST: str = '~/.config/keys/keylist.json'


def get_keys(data: dict) -> typing.Iterable[Path]:
    for directory, keyfiles in data.items():
        dir_path: Path = Path(directory).expanduser()
        for keyfile in keyfiles:
            yield dir_path / Path(keyfile)


def get_data() -> dict:
    keylist: Path = Path(os.getenv('KEYLIST') or DEFAULT_KEYLIST).expanduser()
    with open(keylist, 'r') as keylist_file:
        data = json.load(keylist_file)
    return data


def list_keys():
    return subprocess.run(['ssh-add', '-l'])


def add_key(keyfile: Path) -> subprocess.CompletedProcess:
    return subprocess.run(['ssh-add', str(keyfile)])


if __name__ == '__main__':
    print('Current keys:')
    list_keys()
    print('Add keys:')
    for key in get_keys(get_data()):
        add_key(key)
