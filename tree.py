class TreeError(Exception):
    """Custom exception for errors in the Tree class."""
    pass

class Tree:
    class _Node:
        def __init__(self, element: int, parent=None):
            self._element = element
            self._parent = parent
            self._children = []

        @property
        def element(self):
            return self._element

        @property
        def parent(self):
            return self._parent

        @property
        def children(self):
            return self._children

        def add_child(self, child):
            if not isinstance(child, Tree._Node):
                raise TreeError("Only Tree._Node instances can be added as children.")
            self._children.append(child)

        def __repr__(self):
            return f"Node({self._element})"

    def __init__(self, root_element: int):
        """Initialize the tree with a root node."""
        self._root = self._Node(root_element)

    def get_root(self):
        """Return the root node of the tree."""
        return self._root

    def add_child(self, element: int, parent: _Node):
        """Add a child node to the given parent node."""
        if not isinstance(parent, Tree._Node):
            raise TreeError("Parent must be a valid Tree._Node.")
        new_node = self._Node(element, parent)
        parent.add_child(new_node)
        return new_node

    def add_node(self, element: int, parent_element: int):
        """Add a new node to the tree under the specified parent element."""
        parent_node = self.find(parent_element)
        if parent_node is None:
            raise TreeError(f"Parent element {parent_element} does not exist in the tree.")
        return self.add_child(element, parent_node)

    def find(self, element: int, node=None):
        """Find a node with a given element."""
        if node is None:
            node = self._root
        if node.element == element:
            return node
        for child in node.children:
            result = self.find(element, child)
            if result:
                return result
        return None
