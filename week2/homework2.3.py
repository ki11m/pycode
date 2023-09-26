def can_move(state):
    # 判断当前状态是否合法，不会导致狼吃羊或羊吃菜
    if state['wolf'] == state['sheep'] and state['farmer'] != state['wolf']:
        return False
    if state['sheep'] == state['cabbage'] and state['farmer'] != state['sheep']:
        return False
    return True

def is_goal(state):
    # 判断是否达到目标状态
    return state == {'farmer': 1, 'wolf': 1, 'sheep': 1, 'cabbage': 1}

def get_next_states(current_state):
    next_states = []
    farmer = current_state['farmer']
    for item in ['wolf', 'sheep', 'cabbage']:
        for direction in [1, -1]:
            new_state = current_state.copy()
            new_state['farmer'] += direction
            new_state[item] += direction
            if 0 <= new_state['farmer'] <= 1 and 0 <= new_state[item] <= 1 and can_move(new_state):
                next_states.append(new_state)
    return next_states

def find_solution():
    initial_state = {'farmer': 0, 'wolf': 0, 'sheep': 0, 'cabbage': 0}
    visited = set()
    stack = [(initial_state, [])]

    while stack:
        current_state, path = stack.pop()
        visited.add(tuple(current_state.items()))

        if is_goal(current_state):
            return path

        for next_state in get_next_states(current_state):
            if tuple(next_state.items()) not in visited:
                stack.append((next_state, path + [next_state]))

    return None

solution = find_solution()
if solution:
    for step, state in enumerate(solution):
        print(f"Step {step + 1}: {state}")
else:
    print("No solution found.")
