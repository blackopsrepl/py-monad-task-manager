from typing import Tuple, List, Optional

from task import Task, State

from utils import get_max_task_id, load_from_file


def create_task(
    name: str, status: str = "Pending", parent_task_id: Optional[int] = None
) -> Task:
    return (
        name,
        status,
        get_max_task_id(load_from_file("todos.pkl")) + 1,
        parent_task_id,
    )


def add_task(new_task: Task) -> State:
    def state_fn(state: List[Task]) -> Tuple[List[Task], None]:
        return state + [new_task], None

    return state_fn


def update_task(index: int, new_task: Task) -> State:
    def state_fn(state: List[Task]) -> Tuple[List[Task], None]:
        if 0 <= index < len(state):
            state[index] = new_task
        return state, None

    return state_fn


def delete_task(index: int) -> State:
    def state_fn(state: List[Task]) -> Tuple[List[Task], None]:
        if 0 <= index < len(state):
            state = state[:index] + state[index + 1 :]
        return state, None

    return state_fn


def toggle_task_status(index: int) -> State:
    def state_fn(state: List[Task]) -> Tuple[List[Task], None]:
        def toggle_status_for_task(task: Task) -> Task:
            name, status, task_id, parent_id = task
            new_status = "Completed" if status == "Pending" else "Pending"
            return (name, new_status, task_id, parent_id)

        if 0 <= index < len(state):
            state[index] = toggle_status_for_task(state[index])
        return state, None

    return state_fn
