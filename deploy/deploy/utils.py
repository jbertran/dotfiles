import functools

from pathlib import Path
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


# def build_title(self, cmd: str, task):
#     return '{cmd: <{width}} {path}'.format(
#         cmd=self.name, width=constants.CMD_WIDTH,
#         path=build_relpath(Path(task.targets[0])),
#     )
