from collections import deque
from typing import List


# bfs approach - prefer this
class Solution:
    def distanceK(self, root, target, k):
        parent_node = self.findParentNode(root)
        visited = set()
        q = deque([[target]])
        d = 0
        res = []

        while q:
            neighbours = q.popleft()

            if d == k:
                res.extend(node.val for node in neighbours)
                break

            next_neighbours = []

            for node in neighbours:
                for child in (node.left, node.right, parent_node.get(node, None)):
                    if child and child not in visited:
                        next_neighbours.append(child)
                        visited.add(child)

                visited.add(node)

            q.append(next_neighbours)
            d += 1

        return res

    def findParentNode(self, root):
        if not root:
            return {}

        parent_map = {}
        queue = deque([root])

        while queue:
            node = queue.popleft()

            for child in (node.left, node.right):
                if child:
                    queue.append(child)
                    parent_map[child] = node

        return parent_map


# dfs approach
from typing import List


class Solution:
    def distanceK(self, root, target, k):
        parent_node = self.findParentNode(root)
        visited = set()
        res = []

        self.dfs(target, k, visited, parent_node, res)

        return res

    def dfs(self, node, k, visited, parent_node, res):
        if not node or node in visited:
            return

        visited.add(node)

        if k == 0:
            res.append(node.val)
            return

        for child in (node.left, node.right, parent_node.get(node, None)):
            self.dfs(child, k - 1, visited, parent_node, res)

    def findParentNode(self, root):
        if not root:
            return {}

        parent_map = {}
        self.buildParentMap(root, None, parent_map)

        return parent_map

    def buildParentMap(self, node, parent, parent_map):
        if not node:
            return

        parent_map[node] = parent

        self.buildParentMap(node.left, node, parent_map)
        self.buildParentMap(node.right, node, parent_map)
