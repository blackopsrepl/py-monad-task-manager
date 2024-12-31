from rich.table import Table
from rich.prompt import Prompt
from rich.console import Console

from typing import List

from task import Task


def print_all_tasks(tasks: List[Task], console: Console) -> None:
    """
    Renders all tasks in a styled table using the Rich library.
    If there are no tasks, prints a message indicating no tasks found.
    """
    if not tasks:
        return console.print("No tasks found.", style="bold red")

    # Draw Table
    table = Table(title="Task Management")

    # Draw Columns
    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Task", justify="left", style="magenta")
    table.add_column("Status", justify="center", style="bold green")
    table.add_column("Parent Task", justify="center", style="blue")

    for task in tasks:
        task_id = str(task[2])
        task_name = str(task[0])
        task_status = str(task[1])
        parent_task_id = str(task[3]) if task[3] is not None else "None"

        # Color code the status for better readability
        status_color = "yellow" if task_status == "Pending" else "green"

        # Add each task row to the table
        table.add_row(
            task_id,
            task_name,
            f"[{status_color}]{task_status}[/{status_color}]",
            parent_task_id,
        )

    console.print(table)


def ask_for_action() -> str:
    """
    Prompts the user to choose an action from the list of available actions.
    """
    return Prompt.ask(
        "\n[bold blue]Action[/bold blue]",
        choices=["add", "del", "done", "edit", "exit"],
        default="add",
    ).lower()


def ask_for_task_name(default: str) -> str:
    """
    Prompts the user to provide a task name.
    """
    return Prompt.ask("Task name", default=default)


def ask_for_task_id() -> int:
    """
    Prompts the user to input a task ID.
    """
    return int(Prompt.ask("Task ID", default="1", show_default=True))


def ask_for_parent_task_id() -> int:
    """
    Prompts the user to input a parent task ID. Default is set to 0 for no parent.
    """
    return int(Prompt.ask("Parent Task ID", default="0", show_default=True))


def ask_for_status() -> str:
    """
    Prompts the user to choose a new status for a task.
    """
    return Prompt.ask(
        f"New status", choices=["Pending", "Completed"], default="Pending"
    )
