#! /usr/bin/env python3

import numpy as np
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--size", type=int, default=42, help="Number of nodes")
parser.add_argument("--shuffle", action="store_true", help="Shuffle tree values - randomized, but less readable")
parser.add_argument(
    "-f", "--find", nargs="+", type=int, default=[1, 2, 3], help="Find the closest common ancestor of nodes with values"
)
parser.add_argument(
    "-d",
    "--different",
    action="store_true",
    help="Node is not ancestor to itsefl. If not set, "
    "lowest common ancestor could be one of the nodes we searched for.",
)

args = parser.parse_args()

# Check if tree has natural size
assert 0 < args.size, "Please, the size of binary tree could not be negative or zero"

# Check if looking for existing nodes
assert all(
    map(lambda node_key: 0 <= node_key < args.size, args.find)
), f'Some of nodes {", ".join(map(str, args.find))} do not exist!'

TAB = "\t"


class Node:
    """Simple node of a binary tree (2 pointers to offspring)"""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def print(self, indent=0, prefix=""):
        """Create dictionary of the Node and it's children"""
        print(f"{TAB * indent}{prefix} {self.key}")
        if self.left:
            self.left.print(indent=(indent + 1), prefix="left")
        if self.right:
            self.right.print(indent=(indent + 1), prefix="right")

    def look_for_nodes(self, nodes):
        """
        When we already stumbled upon node in search, look for other values
        with the possibility of finding lowest common ancestor excluded

        @args:
            nodes:  A set of nodes we look for
        @returns:
            (_nodes, _node) :
                _nodes: Nodes it found (their's keys)
                _node:  Min. subtree containing all nodes (in recursive constructoion)
        """
        # Declare/Define return value
        _node = Node(self.key)
        _nodes = set()

        # Search left subtree
        if self.left:
            left_nodes, left_min_subtree = self.left.look_for_nodes(nodes)
            # If node found, proceed with min. subtree construction
            if left_min_subtree:
                _node.left = left_min_subtree
            # Add nodes it found in left subtree
            _nodes = _nodes.union(left_nodes)

        # Search right subtree
        if self.right:
            right_nodes, right_min_subtree = self.right.look_for_nodes(nodes)
            # If node found, proceed with min. subtree construction
            if right_min_subtree:
                _node.right = right_min_subtree
            # Add nodes it found in right subtree
            _nodes = _nodes.union(right_nodes)

        # Search self (Node), if in search, add it to the set of Nodes found
        if self.key in nodes:
            _nodes.add(self.key)

        # If any Node we look for found in either of self subtrees, add self into min. subtree
        return _nodes, _node if _nodes else None

    def lca(self, nodes, differ):
        """
        Look for lca i a minimal subtree containing nodes

        This method just works with the structure of minimal subtree and determines
        where is the lowest common ancestor
        """
        # If self is in search and differ set to True, we overshoot the search for LCA
        if self.key in nodes and differ:
            return None
        # Subtree node has 2 children or itself is in search
        if self.key in nodes or (self.left and self.right):
            return self

        # Subtree node has 1 children
        if self.right or self.left:
            child = self.right if self.right else self.left
            if child.key in nodes:
                return self
            else:
                return child.lca(nodes, differ)


# Values will always be None, it's just a test excercise
# Keys would not be sorted, otherwise the closest common ancestor could be calculated analytically
keys = np.arange(args.size)
if args.shuffle:
    np.random.shuffle(keys)

# Root node
root = Node(keys[0])
nodes = [root]

# Offspring nodes
for i, k in enumerate(keys[1:], 2):
    # New node
    new_node = Node(k)
    # This calculation works when indexing from 1 ..., subtract 1 then
    setattr(nodes[int(i / 2) - 1], "right" if i % 2 else "left", new_node)
    nodes.append(new_node)


# The whole tree
print("The whole tree:\n")
root.print()

# Find the nodes subtree
nodes_to_find = set(args.find)
_, min_subtree = root.look_for_nodes(nodes_to_find)

print("\n")
print("The minimal subtree containing all nodes we searched for")
min_subtree.print()

# Now really find the one lowest common ancestor
print("\n")


if min_subtree:
    lca = min_subtree.lca(args.find, args.different)
    if lca:
        print(f"LCA node key: {lca.key}")
    else:
        print(f"In given configuration, LCA does not exist!")
else:
    print("Mionimal subtree containing all nodes required does not exist!")
