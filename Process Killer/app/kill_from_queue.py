from .app_state import state

def killer():
    while state.len_of_queue() > 0:
        print(f"removing : {state.remove_from_queue()} from head, {state.len_of_queue()} are left")

