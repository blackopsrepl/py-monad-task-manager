from rich.console import Console

from task import bind, return_

from task_manager import (
    create_task,
    add_task,
    delete_task,
    toggle_task_status,
    update_task,
)

from ui import (
    print_all_tasks,
    ask_for_action,
    ask_for_task_name,
    ask_for_task_id,
    ask_for_parent_task_id,
    ask_for_status,
)

from utils import load_from_file, save_to_file, search_row_by_id


def main():
    tasks = load_from_file("todos.pkl")
    console = Console()

    while True:
        console.print("[bold cyan]py-task-manager[/bold cyan]\n")

        print_all_tasks(tasks, console)

        action = ask_for_action()

        match action:
            case "add":
                new_task = create_task(
                    ask_for_task_name(f"Task {len(tasks) + 1}"),
                    "Pending",
                    ask_for_parent_task_id(),
                )
                tasks, _ = bind(add_task(new_task), lambda _: return_(tasks))(tasks)
                save_to_file(tasks, "todos.pkl")
                console.print(f"Task added!", style="bold green")

            case "del":
                task_row = search_row_by_id(tasks, ask_for_task_id())

                if 0 <= task_row < len(tasks):
                    tasks, _ = bind(delete_task(task_row), lambda _: return_(tasks))(
                        tasks
                    )
                    save_to_file(tasks, "todos.pkl")
                    console.print(f"Task deleted!", style="bold red")
                else:
                    console.print(f"[bold red]Invalid ID![/bold red]")

            case "done":
                task_row = search_row_by_id(tasks, ask_for_task_id())

                if 0 <= task_row < len(tasks):
                    tasks, _ = bind(
                        toggle_task_status(task_row), lambda _: return_(tasks)
                    )(tasks)
                    save_to_file(tasks, "todos.pkl")
                    console.print(f"Task marked as completed!", style="bold green")
                else:
                    console.print(f"[bold red]Invalid ID![/bold red]")

            case "edit":
                task_row = search_row_by_id(tasks, ask_for_task_id())

                if 0 <= task_row < len(tasks):
                    task = tasks[task_row]
                    new_name = ask_for_task_name(f"New name (current: {task[0]})")
                    new_status = ask_for_status()
                    updated_task = (new_name, new_status, task[2], task[3])
                    tasks, _ = bind(
                        update_task(task_row, updated_task), lambda _: return_(tasks)
                    )(tasks)
                    save_to_file(tasks, "todos.pkl")
                    console.print(f"Task updated!", style="bold yellow")
                else:
                    console.print(f"[bold red]Invalid ID![/bold red]")

            case "exit":
                console.print("Goodbye!", style="bold red")
                break


if __name__ == "__main__":
    main()
