from collections import deque

"""
Solve https://leetcode.com/problems/leaf-similar-trees/?envType=study-plan-v2&envId=leetcode-75
without traversing the entire trees first, as requested by Snowflake interviewer.
"""
class Node:
    # Input array is a preorder traversal of tree
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeIterator:
    def __init__(self, vals): 
        self.root = Node(vals[0])
        self.path = []
        self.top = None

        q = deque([self.root])
        start, end = 1, len(vals)
        while start < end:
            node = q.popleft()
            if vals[start] != None:
                node.left = Node(vals[start])
                q.append(node.left)
            if vals[start+1] != None:
                node.right = Node(vals[start+1])
                q.append(node.right)
            start += 2

    def print(self):
        res = []
        q = deque([self.root])
        while q:
            node = q.popleft()
            if node is None:
                res.append(None)
            else:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
        print(res)

    def __dfs(self, node):
        # respect self.path
        if not node.left and not node.right:
            self.top = node
            return node
        self.path.append(node)
        if node.left:
            return self.__dfs(node.left)
        if node.right:
            return self.__dfs(node.right)
        
    def __next__(self):
        if not self.top:  # start traversing now
            self.top = self.__dfs(self.root)
        else:  # need to update self.top
            if not self.path: # nothing more left to traverse
                return None
            if self.path[-1].left == self.top and self.path[-1].right:
                self.top = self.__dfs(self.path[-1].right)
            else:
                # go back path
                while self.path:
                    temp = self.path.pop()
                    if not self.path:
                        return None
                    if temp == self.path[-1].left and self.path[-1].right:
                        self.top = self._dfs(self.path[-1].right)
                        if self.top:
                            break
        return self.top

    def __iter__(self):
        return self
    
# sort the leaves of tree 1 and tree 2.
def isLeafSimilar(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    iter1 = TreeIterator(t1)
    iter2 = TreeIterator(t2)
    iter1.print()
    iter2.print()
    a, b = next(iter1), next(iter2)
    while a and b:
        print('a, b', a.val, b.val)
        if a.val != b.val:
            return False
        a = next(iter1)
        b = next(iter2)
    print('At the end:', a is None, b is None)
    return(a is None and b is None)
        

t1 = [3, 5, 1]
t2 = [3, 5, 2, None, None, 1, None]
print(isLeafSimilar(t1, t2))  # False