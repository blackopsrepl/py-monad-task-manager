from typing import Callable, Tuple, List, Optional


# Define Task as a type alias (name, status, task_id, parent_task_id)
Task = Tuple[str, str, int, Optional[int]]

# Define State monad as a type alias
State = Callable[[List[Task]], Tuple[List[Task], any]]


# Returns a new state monad with the given value
def return_(value: any) -> State:
    def state_fn(state: List[Task]) -> Tuple[List[Task], any]:
        return state, value

    return state_fn


# Binds the state monad to a function and returns a new monad with updated state
def bind(state_monad: State, func: Callable[[any], State]) -> State:
    return lambda state: func(state_monad(state)[1])(state_monad(state)[0])
