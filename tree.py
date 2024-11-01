class TreeError(Exception):
    """Custom exception for errors in the Tree class."""
    pass

class Tree:
    """
    A class representing a general tree structure where each node has an element, a parent,
    and a list of children.

    Attributes
    ----------
    _root : Tree._Node
        The root node of the tree.

    Methods
    -------
    get_root()
        Returns the root node of the tree.
    add_child(element: int, parent: _Node)
        Adds a child node with the specified element to the given parent node.
    add_node(element: int, parent_element: int)
        Adds a new node to the tree under the specified parent element.
    find(element: int, node=None)
        Searches for a node with the specified element starting from a given node.
    """

    class _Node:
        """
        Represents a single node in the tree.

        Attributes
        ----------
        _element : int
            The value or identifier of the node.
        _parent : Tree._Node or None
            The parent of the node, or None if the node is the root.
        _children : list of Tree._Node
            List of child nodes connected to this node.

        Methods
        -------
        element
            Returns the element of the node.
        parent
            Returns the parent of the node.
        children
            Returns a list of child nodes.
        add_child(child)
            Adds a child node to this node.
        __repr__()
            Returns a string representation of the node.
        """

        def __init__(self, element: int, parent=None):
            """
            Initialize a node with an element and an optional parent.

            Parameters
            ----------
            element : int
                The value or identifier for the node.
            parent : Tree._Node, optional
                The parent node, if any (default is None).
            """
            self._element = element
            self._parent = parent
            self._children = []

        @property
        def element(self):
            """Return the element of the node."""
            return self._element

        @property
        def parent(self):
            """Return the parent node of this node."""
            return self._parent

        @property
        def children(self):
            """Return a list of child nodes for this node."""
            return self._children

        def add_child(self, child):
            """
            Add a child node to this node.

            Parameters
            ----------
            child : Tree._Node
                The child node to be added.

            Raises
            ------
            TreeError
                If the child is not an instance of Tree._Node.
            """
            if not isinstance(child, Tree._Node):
                raise TreeError("Only Tree._Node instances can be added as children.")
            self._children.append(child)

        def __repr__(self):
            """Return a string representation of the node."""
            return f"Node({self._element})"

    def __init__(self, root_element: int):
        """
        Initialize the tree with a root node.

        Parameters
        ----------
        root_element : int
            The value or identifier for the root node.
        """
        self._root = self._Node(root_element)

    def get_root(self):
        """
        Return the root node of the tree.

        Returns
        -------
        Tree._Node
            The root node of the tree.
        """
        return self._root

    def add_child(self, element: int, parent: _Node):
        """
        Add a child node with the specified element to the given parent node.

        Parameters
        ----------
        element : int
            The value or identifier for the new child node.
        parent : Tree._Node
            The parent node to which the new child will be added.

        Returns
        -------
        Tree._Node
            The newly created child node.

        Raises
        ------
        TreeError
            If the parent is not a valid Tree._Node instance.
        """
        if not isinstance(parent, Tree._Node):
            raise TreeError("Parent must be a valid Tree._Node.")
        new_node = self._Node(element, parent)
        parent.add_child(new_node)
        return new_node

    def add_node(self, element: int, parent_element: int):
        """
        Add a new node to the tree under the specified parent element.

        Parameters
        ----------
        element : int
            The value or identifier for the new node.
        parent_element : int
            The element of the parent node to which the new node will be added.

        Returns
        -------
        Tree._Node
            The newly created node.

        Raises
        ------
        TreeError
            If the parent element does not exist in the tree.
        """
        parent_node = self.find(parent_element)
        if parent_node is None:
            raise TreeError(f"Parent element {parent_element} does not exist in the tree.")
        return self.add_child(element, parent_node)

    def find(self, element: int, node=None):
        """
        Find a node with the specified element.

        Parameters
        ----------
        element : int
            The value or identifier of the node to find.
        node : Tree._Node, optional
            The starting node for the search (default is the root node).

        Returns
        -------
        Tree._Node or None
            The node with the specified element, or None if not found.
        """
        if node is None:
            node = self._root
        if node.element == element:
            return node
        for child in node.children:
            result = self.find(element, child)
            if result:
                return result
        return None
