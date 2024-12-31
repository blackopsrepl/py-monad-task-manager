from typing import Tuple, List, Optional

from task import Task, State

from utils import get_max_task_id, load_from_file


def create_task(
    name: str, status: str = "Pending", parent_task_id: Optional[int] = None
) -> Task:
    """
    Creates a new task with the provided name, status, and optional parent task ID.
    Generates a new task ID based on the current tasks in the file.
    """
    return (
        name,
        status,
        get_max_task_id(load_from_file("todos.pkl")) + 1,
        parent_task_id,
    )


def add_task(new_task: Task) -> State:
    """
    Returns a function that adds a new task to the task list (state).
    The returned function can be bound to a state monad and updates the state with the new task.
    """

    def state_fn(state: List[Task]) -> Tuple[List[Task], None]:
        return state + [new_task], None

    return state_fn


def update_task(index: int, new_task: Task) -> State:
    """
    Returns a function that updates a task in the list at the given index with a new task.
    """

    def state_fn(state: List[Task]) -> Tuple[List[Task], None]:
        if 0 <= index < len(state):
            state = state[:index] + [new_task] + state[index + 1 :]
        return state, None

    return state_fn


def delete_task(index: int) -> State:
    """
    Returns a function that deletes a task from the task list at the given index.
    """

    def state_fn(state: List[Task]) -> Tuple[List[Task], None]:
        if 0 <= index < len(state):
            state = state[:index] + state[index + 1 :]
        return state, None

    return state_fn


def toggle_task_status(index: int) -> State:
    """
    Returns a function that toggles the status of a task at the given index.
    The status is toggled between "Pending" and "Completed".
    """

    def state_fn(state: List[Task]) -> Tuple[List[Task], None]:
        def toggle_status_for_task(task: Task) -> Task:
            name, status, task_id, parent_id = task
            new_status = "Completed" if status == "Pending" else "Pending"
            return (name, new_status, task_id, parent_id)

        if 0 <= index < len(state):
            state = (
                state[:index]
                + [toggle_status_for_task(state[index])]
                + state[index + 1 :]
            )
        return state, None

    return state_fn
