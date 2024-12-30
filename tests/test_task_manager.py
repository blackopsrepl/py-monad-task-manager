import pytest
from typing import List
from task import Task, State, bind, return_

from task_manager import add_task, update_task, delete_task, toggle_task_status


sample_task_data = [
    ("Task 1", "Pending", 1, 0),
    ("Task 2", "Completed", 2, 1),
    ("Task 3", "Pending", 3, 0),
    ("Task 4", "In Progress", 1, 2),
    ("Task 5", "Completed", 4, 3),
    ("Task 6", "Pending", 2, 0),
    ("Task 7", "In Progress", 3, 4),
    ("Task 8", "Completed", 5, 6),
    ("Task 9", "Pending", 1, 7),
    ("Task 10", "Completed", 2, 8),
    ("Task 11", "In Progress", 4, 9),
    ("Task 12", "Pending", 5, 10),
    ("Task 13", "Completed", 1, 11),
    ("Task 14", "In Progress", 3, 12),
    ("Task 15", "Pending", 2, 13),
    ("Task 16", "Completed", 4, 14),
    ("Task 17", "In Progress", 5, 15),
    ("Task 18", "Completed", 1, 16),
    ("Task 19", "Pending", 3, 17),
    ("Task 20", "Completed", 2, 18),
    ("Task 21", "Pending", 4, 19),
    ("Task 22", "In Progress", 5, 20),
    ("Task 23", "Completed", 1, 21),
    ("Task 24", "Pending", 3, 22),
    ("Task 25", "In Progress", 2, 23),
    ("Task 26", "Completed", 4, 24),
    ("Task 27", "Pending", 5, 25),
    ("Task 28", "Completed", 1, 26),
    ("Task 29", "In Progress", 2, 27),
    ("Task 30", "Pending", 3, 28),
]


def mock_load_from_file() -> List[Task]:
    global sample_task_data
    return sample_task_data


def mock_save_to_file(state: State) -> None:
    global sample_task_data
    sample_task_data = state


@pytest.fixture
def mock_dependencies(monkeypatch):
    monkeypatch.setattr("utils.load_from_file", mock_load_from_file)
    monkeypatch.setattr("utils.save_to_file", mock_save_to_file)


def test_add_task(mock_dependencies):
    global sample_task_data
    new_task = ("New Task", "Pending", 4, None)
    state, _ = bind(add_task(new_task), lambda _: return_(sample_task_data))(
        sample_task_data
    )
    assert len(state) == len(sample_task_data) + 1
    assert state[-1] == new_task


def test_update_task(mock_dependencies):
    updated_task = ("Updated Task", "Pending", 2, 1)
    update_fn = update_task(1, updated_task)
    state, _ = update_fn(sample_task_data)
    assert state[1] == updated_task


def test_delete_task(mock_dependencies):
    global sample_task_data
    state, _ = bind(delete_task(1), lambda _: return_(sample_task_data))(
        sample_task_data
    )
    assert sample_task_data[1] not in state


def test_toggle_task_status(mock_dependencies):
    toggle_fn = toggle_task_status(0)
    state, _ = toggle_fn(sample_task_data)
    assert state[0][1] == "Completed"
    toggle_fn = toggle_task_status(0)
    state, _ = toggle_fn(state)
    assert state[0][1] == "Pending"
