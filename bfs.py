from collections import deque


def bfs(root):
    """
    Perform a breadth-first search (BFS) traversal on a tree starting from the given root node.

    Parameters
    ----------
    root : Node
        The starting node for the BFS traversal.

    Returns
    -------
    list
        A list of nodes representing the order of traversal in BFS.

    Notes
    -----
    - This implementation uses a queue to maintain the BFS order and a set to track visited nodes,
      ensuring each node is processed only once.
    - Each node is expected to be a unique object, allowing it to be tracked using a set.

    """

    # Base case: if the root is None, return an empty list
    if root is None:
        return []

    # Initialize a queue with the root node for BFS
    queue = deque([root])

    # Initialize a set to track visited nodes, starting with the root
    visited = {root}

    # List to store the order of traversal
    traversed = []

    # While there are nodes to process in the queue
    while queue:
        # Remove the node from the front of the queue
        current = queue.popleft()
        # Append the current node to the traversal list
        traversed.append(current)

        # Process each child of the current node
        for child in current.children:
            # If the child hasn't been visited, add it to the queue and mark as visited
            if child not in visited:
                queue.append(child)
                visited.add(child)

    # Return the list of nodes in BFS order
    return traversed
