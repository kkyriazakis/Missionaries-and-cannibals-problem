class State:
    def __init__(self, miss_L, cann_L, boat, miss_R, cann_R):
        self.cann_L = cann_L
        self.cann_R = cann_R
        self.miss_L = miss_L
        self.miss_R = miss_R
        self.boat = boat
        self.parent = None

    def is_goal(self):
        if self.cann_L == 0 and self.miss_L == 0:
            return True
        else:
            return False

    def is_valid(self):
        if self.miss_L >= 0 and self.miss_R >= 0 and self.cann_L >= 0 and self.cann_R >= 0 \
                and (self.miss_L == 0 or self.miss_L >= self.cann_L) \
                and (self.miss_R == 0 or self.miss_R >= self.cann_R):
            return True
        else:
            return False


def successors(curr):
    children = []
    # if boat is on left side
    if curr.boat == 0:
        # ---- Two missionaries cross left to right ----
        new_state = State(curr.cann_L, curr.miss_L - 2, 1, curr.cann_R, curr.miss_R + 2)
        if new_state.is_valid():
            new_state.parent = curr
            children.append(new_state)

        # ---- Two cannibals cross left to right ----
        new_state = State(curr.cann_L - 2, curr.miss_L, 1, curr.cann_R + 2, curr.miss_R)
        if new_state.is_valid():
            new_state.parent = curr
            children.append(new_state)

        # ---- One missionary and one cannibal cross left to right ----
        new_state = State(curr.cann_L - 1, curr.miss_L - 1, 1, curr.cann_R + 1, curr.miss_R + 1)
        if new_state.is_valid():
            new_state.parent = curr
            children.append(new_state)

        # ---- One missionary crosses left to right ----
        new_state = State(curr.cann_L, curr.miss_L - 1, 1, curr.cann_R, curr.miss_R + 1)
        if new_state.is_valid():
            new_state.parent = curr
            children.append(new_state)

        # ---- One cannibal crosses left to right ----
        new_state = State(curr.cann_L - 1, curr.miss_L, 1, curr.cann_R + 1, curr.miss_R)
        if new_state.is_valid():
            new_state.parent = curr
            children.append(new_state)

    # if boat is on right side
    else:
        # Two missionaries cross right to left.
        new_state = State(curr.cann_L, curr.miss_L + 2, 0, curr.cann_R, curr.miss_R - 2)
        if new_state.is_valid():
            new_state.parent = curr
            children.append(new_state)

        # Two cannibals cross right to left.
        new_state = State(curr.cann_L + 2, curr.miss_L, 0, curr.cann_R - 2, curr.miss_R)
        if new_state.is_valid():
            new_state.parent = curr
            children.append(new_state)

        # One missionary and one cannibal cross right to left.
        new_state = State(curr.cann_L + 1, curr.miss_L + 1, 0, curr.cann_R - 1, curr.miss_R - 1)
        if new_state.is_valid():
            new_state.parent = curr
            children.append(new_state)

        # One missionary crosses right to left.
        new_state = State(curr.cann_L, curr.miss_L + 1, 0, curr.cann_R, curr.miss_R - 1)
        if new_state.is_valid():
            new_state.parent = curr
            children.append(new_state)

        # One cannibal crosses right to left.
        new_state = State(curr.cann_L + 1, curr.miss_L, 0, curr.cann_R - 1, curr.miss_R)
        if new_state.is_valid():
            new_state.parent = curr
            children.append(new_state)

    return children


def breadth_first_search(initial_state):
    if initial_state.is_goal():
        return initial_state
    frontier = list()
    explored = set()
    frontier.append(initial_state)

    while frontier:
        state = frontier.pop(0)
        if state.is_goal():
            return state
        explored.add(state)
        children = successors(state)
        for child in children:
            if (child not in explored) or (child not in frontier):
                frontier.append(child)
    return None


def print_solution(solution):
    path = [solution]
    parent = solution.parent
    while parent:
        path.append(parent)
        parent = parent.parent

    for t in range(len(path)):
        state = path[len(path) - t - 1]
        if state.boat == 0:
            loc = "left "
        else:
            loc = "right"
        print("(", state.miss_L, ",", state.cann_L, ",", loc, ",", state.miss_R, ",", state.cann_R, ")")


# ---------- MAIN ----------
initial_state = State(3, 3, 0, 0, 0)
solution = breadth_first_search(initial_state)
print("Missionaries and Cannibals solution:")
print("( missionaries left, cannibals left, boat location, missionaries right, cannibals right )")
print_solution(solution)
