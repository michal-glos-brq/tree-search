### README
This project demonstrates an LCA (Lowest common ancestor) and a minimal subtree search for specified nodes in the find option. The tree searched is built from 1 to SIZE and in the BFS manner. Node numbers could be shuffled to introduce stochasticity.

### How to run the script?
```
python script.py [-h] [-s SIZE] [--shuffle] [-f FIND [FIND ...]] [-d]
```

##### The arguments are:
 - -h, --help: Show help message and exit.
 - -s SIZE, --size SIZE: Number of nodes in the binary tree. The default is 42.
 - --shuffle: Shuffle the values in the binary tree. This will make the tree randomized, but less readable.
 - -f FIND [FIND ...]: The values of the nodes to find the lowest common ancestor. The default is 1, 2, and 3.
 - -d, --different: Set this flag to exclude the possibility of a node being its own ancestor. If not set, the lowest common ancestor could be one of the nodes being searched for.

##### Output
The script will output the following:
 - The whole binary tree.
 - The minimal subtree containing all nodes being searched for.
 - The lowest common ancestor of the nodes being searched for (if it exists).
The script will exit with an error message if the binary tree size is negative or zero. Similarly, if any of the nodes being searched for do not exist in the binary tree, the script will exit with an error message.
