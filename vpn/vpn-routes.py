#!/usr/bin/env python3
# See https://developer.gnome.org/NetworkManager/stable/NetworkManager.html
import os
import sys

LOGFILE = '/var/log/vpn-out'

NM_PROFILE = os.environ.get('CONNECTION_ID')
if NM_PROFILE.lower() != 'scality':
    sys.exit(0)

import subprocess

NM_IFACE = sys.argv[1]
NM_ACTION = sys.argv[2]
if NM_ACTION != 'vpn-up':
    sys.exit(0)

PF9_NETWORK = [
    '10.100.0.0/16',
    '10.200.0.0/16',
]

SCAL_URLS = [
    'eve.devsca.com',
    'packages.scality.com',
    'ci.devsca.com'
]


def log_error(error: str):
    with open(LOGFILE, 'a') as f:
        print(error, file=f)


def resolve_domain(domain: str) -> str:
    out = subprocess.check_output(['getent', 'hosts', domain])
    out_lines = [line for line in out.decode().split('\n') if line]
    return out_lines[0].split()[0]


def add_route(route):
    cmd = ['ip', 'route', 'add', route, 'dev', NM_IFACE]
    try:
        out = subprocess.check_call(cmd)
    except subprocess.CalledProcessError:
        log_error(
            f'Error with adding route {route} on dev {NM_IFACE}: {cmd} failed'
        )
        return False
    return True


if __name__ == '__main__':
    try:
        scal_ips = [
            f'{resolve_domain(url)}' for url in SCAL_URLS
        ]

        route_action_res = True
        for ip in scal_ips + PF9_NETWORK:
            ret = add_route(ip)
            if not ret:
                route_action_res = False
    except Exception as exc:
        log_error(str(exc))
        route_action_res = False

    sys.exit(int(not route_action_res))
