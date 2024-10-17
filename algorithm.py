from typing import List

class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class Solution:
    
    def createTree(self, input: List) -> Node:
        if not input:
            return None
        
        root = Node(input[0])
        queue = [root]
        
        while queue:
            current =  queue.pop(0)
            while input[0] is None:
                child = Node(input[1])
                current.children.append(child)
                queue.append(child)

        return root