def dfs(root):
    """
    Perform a depth-first search (DFS) traversal on a tree starting from the given root node.

    Parameters
    ----------
    root : Node
        The starting node of the DFS traversal.

    Returns
    -------
    list
        A list of nodes representing the order of traversal in DFS.

    Notes
    -----
    - This implementation uses recursion to traverse the tree or graph.
    - Each node is expected to be a unique object, allowing it to be tracked using a set.
    """

    # Base case: if the root is None, return an empty list
    if root is None:
        return []

    # Initialize a set to track visited nodes (local to this function call)
    visited = {root}

    # Initialize the traversal list with the root node
    traversed = [root]

    # Recursively visit each child node if it has not been visited
    for child in root.children:
        if child not in visited:
            traversed.extend(dfs(child))

    # Return the traversal order for all nodes from this root node
    return traversed
