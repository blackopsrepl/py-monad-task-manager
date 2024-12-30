from typing import List

import os, pickle

from task import Task


def get_max_task_id(tasks: List[Task]) -> int:
    return max(task[2] for task in tasks) if tasks else 0


def search_row_by_id(tasks: List[Task], task_id: int) -> int:
    left, right = 0, len(tasks) - 1

    while left <= right:
        mid = (left + right) // 2
        if tasks[mid][2] == task_id:
            return mid
        elif tasks[mid][2] < task_id:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def save_to_file(tasks: List[Task], filename) -> None:
    with open(filename, "wb") as file:
        pickle.dump(tasks, file)


def load_from_file(filename) -> List[Task]:
    global task_id_counter
    if os.path.exists(filename):
        with open(filename, "rb") as file:
            tasks = pickle.load(file)
            if tasks:
                task_id_counter = get_max_task_id(tasks)
            return tasks
    return []
