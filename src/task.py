from typing import Callable, Tuple, List, Optional


# Define Task as a type alias (name, status, task_id, parent_task_id)
Task = Tuple[str, str, int, Optional[int]]

# Define State monad as a type alias
State = Callable[[List[Task]], Tuple[List[Task], any]]


def return_(value: any) -> State:
    """
    Returns a new state monad with a given value.
    This is used to provide a way to return a value without altering the task state.
    """

    def state_fn(state: List[Task]) -> Tuple[List[Task], any]:
        return state, value

    return state_fn


def bind(state_monad: State, func: Callable[[any], State]) -> State:
    """
    Binds the state monad to a function, and returns a new state monad with the updated state.
    This is the core monadic pattern used to chain state transitions.
    """
    return lambda state: func(state_monad(state)[1])(state_monad(state)[0])
