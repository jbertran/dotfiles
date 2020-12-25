import functools

import dodo1 as dodo

from typing import Any, Callable, Optional, Type

from doit.exceptions import TaskError


def task_errors(*expected_exn: Type[Exception]) -> Callable[[Any], Any]:
    """Wrap a callable to create a resilient `doit` task

    This decorator wraps action functions in a try…except block that abstracts
    the exceptions raised by the underlying actions (docker API calls, file
    system actions…) and returns a result conforming to `doit`'s expectations
    in order to have `doit` manage the trace-back display:
     - None in case of successful task run
     - a TaskError instance in case of error
    """
    def wrapped_task(task_func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(task_func)
        def decorated_task(*args: Any, **kwargs: Any) -> Optional[TaskError]:
            try:
                task_func(*args, **kwargs)
            except expected_exn as err:
                return TaskError(err)
            return None
        return decorated_task
    return wrapped_task


def unpack_single_dict(data: dict) -> tuple:
    """Given a dict with a single key, unpack this dict."""
    if len(data) != 1:
        raise Exception(
            'Expected single key-value pair in package definition'
        )
    key = next(iter(data.keys()))
    return key, data[key]


def advertise_task(origin, task_name, task_func):
    task_func_name = f'task_{task_name}'
    current_attr = getattr(dodo, task_func_name, None)
    if current_attr is not None:
        raise Exception(
            f'Attempting to advertise task {task_func_name} from'
            f'{origin} but a task with the same name is already advertised'
        )
    setattr(dodo, task_func_name, task_func)
