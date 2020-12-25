"""
Top-level devenv.yaml processing and task spawning.
"""
import abc
import dodo1 as dodo


class Task:

    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

    @property
    @abc.abstractmethod
    def task(self):
        pass

    @property
    @abc.abstractmethod
    def task_name(self):
        pass


class TopLevelTask(Task):

    toplevel_task_dict = {}

    def __init__(self, name, contents):
        self.name = name
        self.contents = contents
        self.compute_children()

    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)
        devenv_name = getattr(cls, 'devenv_name', None)
        if devenv_name:
            cls.toplevel_task_dict[devenv_name] = cls

    @classmethod
    def get_by_name(cls, name):
        return cls.toplevel_task_dict[name]

    def advertise(self):
        task_func_name = f'task_{self.task_name}'
        setattr(dodo, task_func_name, lambda: self.task)

    def compute_children(self):
        self.subtasks = [
            TopLevelTask.get_by_name(task_name).from_yaml(task_contents)
            for task in self.contents
            for task_name, task_contents in task.items()
        ]
        self.task_deps = [task_name for task_name in self.subtasks]

    @property
    def task_name(self):
        return self.name

    @property
    def task(self):
        return {
            'basename': self.task_name,
            'actions': [],
            # 'task_dep': self.task_deps
        }
