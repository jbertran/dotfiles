import yaml

from deploy.toplevel import TopLevelTask


with open('devenv.yaml', 'r') as f:
    devenv_data = yaml.safe_load(f)

tlts = [
    TopLevelTask(name, contents) for name, contents in devenv_data.items()
]

for tlt in tlts:
    tlt.advertise()


def task_deploy():
    for tlt in tlts:
        print()
    return {
        'actions': [],
        'task_dep': [tlt.task_name for tlt in tlts]
    }
