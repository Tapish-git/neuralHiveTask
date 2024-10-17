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
        ptr = 1
        
        while queue and ptr < len(input):
            current = queue.pop(0)
            while input[ptr] is not None:
                child = Node(input[ptr])
                current.children.append(child)
                queue.append(child)
                ptr += 1
            ptr += 1

        return root