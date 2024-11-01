from collections import deque

def bfs(tree):
    """Perform a breadth-first search on the given tree."""
    root = tree.get_root()
    if root is None:
        return []

    queue = deque([root])
    visited = {root}
    traverse = []

    while queue:
        current = queue.popleft()
        traverse.append(current)
        for child in current.children:
            if child not in visited:
                queue.append(child)
                visited.add(child)

    return traverse
