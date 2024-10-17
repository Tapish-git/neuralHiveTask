## The problem was to create a graph using the input list and check which algorithm would be best.


# Input: root = [1,null,3,2,4,null,5,6]

# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

## Summary-

# I approached this tree problem using Breadth-First Search (BFS) with a queue data structure, which perfectly suits the level-order representation of the input list as seen in the graph.
# Queue is used to track nodes whose children need to be processed next, maintaining the correct parent-child relationships and level structure.
# By processing nodes in the order they appear and using the queue to manage the level traversal, we can build the tree while closely following the structure of the input list

