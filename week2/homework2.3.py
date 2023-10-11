from collections import deque

def is_valid_state(state):
    # 检查状态是否合法，即没有狼吃羊或羊吃菜
    if state['wolf'] == state['sheep'] and state['farmer'] != state['wolf']:
        return False
    if state['sheep'] == state['cabbage'] and state['farmer'] != state['sheep']:
        return False
    return True

def is_goal_state(state, goal):
    return state == goal

def get_next_states(current_state):
    next_states = []
    farmer = current_state['farmer']
    opposites = {'farmer': 1, 'wolf': 1, 'sheep': 1, 'cabbage': 1}

    # 生成所有可能的下一个状态
    for item, opposite in opposites.items():
        if current_state['farmer'] == farmer:
            new_state = current_state.copy()
            new_state['farmer'] = opposite
            new_state[item] = opposite

            if is_valid_state(new_state):
                next_states.append(new_state)
    return next_states

def find_solution():
    start_state = {'farmer': 0, 'wolf': 0, 'sheep': 0, 'cabbage': 0}
    goal_state = {'farmer': 1, 'wolf': 1, 'sheep': 1, 'cabbage': 1}
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        current_state, path = queue.popleft()
        visited.add(tuple(current_state.items()))

        if is_goal_state(current_state, goal_state):
            return path

        for next_state in get_next_states(current_state):
            if tuple(next_state.items()) not in visited:
                queue.append((next_state, path + [next_state]))

    return None

solution = find_solution()

if solution:
    for step, state in enumerate(solution):
        print(f"Step {step + 1}: {state}")
else:
    print("No solution found.")
