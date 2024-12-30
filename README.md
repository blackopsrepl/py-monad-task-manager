# py-monad-task-manager

A minimal TUI task management tool built using Python, showcasing simplicity, efficiency, and the **Monad pattern** (because why not?) for managing application state.

## Features

- **Add Tasks**: Create new tasks with optional parent tasks
- **Delete Tasks**: Remove tasks by ID
- **Toggle Task Status**: Mark tasks as done or pending
- **Edit Tasks**: Update task names and statuses
- **Persistent Storage**: Save and load tasks from a file
- **Monadic State Management**: Use of a *State Monad* to manage application state (because we can)

## Installation

### Prerequisites

- Python 3.11
- `rich` library for console output formatting (`pip install rich`)

### Usage
Upon running `main.py`, you'll be greeted with a menu for managing your tasks.

```bash
[bold cyan]py-task-manager[/bold cyan]

┌────┬──────────────┬───────────┬────────────┐
│ ID │ Task          │ Status    │ Parent Task│
├────┼──────────────┼───────────┼────────────┤
│ 1  │ Buy groceries │ Pending   │ None       │
│ 2  │ Wash the car  │ Completed │ 1          │
└────┴──────────────┴───────────┴────────────┘

Action (add/del/done/edit/exit): add
Task name: Buy milk
Parent Task ID (0 for none): 1
Task added!
````

### The Monad Pattern

#### What is a Monad?

A **monad** is a **monoid** in the category of **endofunctors**... 😎

...let's try again:

A **monad** is an abstraction used in functional programming to handle computations in a consistent way. It is a design pattern that allows the chaining of operations while encapsulating side effects, such as state changes, I/O, or errors, in a controlled manner.

Monads can be thought of as a way to wrap values and apply functions to them, ensuring that computations are carried out in a predictable and controlled environment.

My personal understanding is: a **monad** is a data structure with
- a single, immutable value
- a **map/bind function** to map a function to that value
- a **return/flatten function** that returns the new state into a new monad each time

This enables **chaining** and **composition** of operations in a way that **preserves immutability** and **functional purity**—a "reverse" approach to a **class**, where state cannot be modified in-place, but transformations are applied functionally to produce new instances.

This "reverse symmetry" highlights the contrast:

- **Classes** modify their internal state, maintaining mutability and direct interaction through internal methods. They most of the time interact with a global state

- **Monads** reach similar outcomes to a class, but by wrapping values and mapping external immutable transformations, they have no side-effects: there is no global state

### Example:

- **Class**:
    - A `Box` class holds a value, and you can modify the value by calling methods like `setValue(newValue)`, which mutates the internal state of the `Box`.
- **Monad**:
    - A `BoxMonad` would hold a value in an immutable way. To transform the value, you would use a function like `map`, which applies an external function to the value and returns a new `BoxMonad`, with the new value.

#### The State Monad in This Project

In this application, we use the **State Monad** to manage the state of the task list. The State Monad provides a way to model the task management process as a series of transformations on the application's state, while keeping the state itself immutable.

Instead of directly modifying the state of the task list, we use the **`return_`** function to wrap the initial state into a monadic container, and the **`bind`** function to apply transformations to the state in a predictable way. Each time an operation is performed (such as adding, editing, or deleting tasks), it returns a new instance of the state, ensuring immutability and composability.

Key functions:

- **`return_`**: Wraps a value into a monadic container, making it part of the monadic computation chain.
- **`bind`**: Applies a function to the value inside the monad, returning a new monadic container with the transformed value.

By using the State Monad, we can handle task management operations in a way that ensures the state is updated immutably and computations are composed without side effects or unwanted interactions between operations.

### Project Structure

- **`main.py`**: The entry point of the application, where the task manager is initialized and the user interface is presented.
- **`task.py`**: Defines the `Task` class, which represents individual tasks with attributes like name, status, and parent task ID.
- **`task_manager.py`**: Contains the logic for managing tasks, including adding, editing, and deleting tasks, as well as updating their statuses.
- **`ui.py`**: Handles the console user interface, displaying tasks and accepting user input.
- **`utils.py`**: Contains utility functions for file handling, ID generation, and other helper tasks.
### License

This project is licensed under the MIT License. See the `LICENSE.md` file for more details.
