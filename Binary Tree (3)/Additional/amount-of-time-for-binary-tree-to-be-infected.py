# bfs - prefer this always, cause spreading/burning rate is same in every direction
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent_node = self.findParentNode(root)
        visited = set()
        start_node = self.findNode(root, start)
        time_taken = self.bfs(start_node, parent_node, visited)
        return time_taken

    def bfs(self, start_node, parent_node, visited):
        time_taken = 0
        queue = deque([(start_node, time_taken)])
        visited.add(start_node)
        while queue:
            current_node, time_taken = queue.popleft()

            for child in (
                current_node.left,
                current_node.right,
                parent_node.get(current_node, None),
            ):
                if child and child not in visited:
                    visited.add(child)
                    queue.append((child, time_taken + 1))

        return time_taken

    def findNode(self, node, val):
        if not node:
            return None
        if node.val == val:
            return node
        return self.findNode(node.left, val) or self.findNode(node.right, val)

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


# dfs -> don't prefer this
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent_node = self.findParentNode(root)
        visited = set()
        start_node = self.findNode(root, start)
        if len(parent_node) == 1:
            return 0
        time_taken = self.dfs(start_node, parent_node, visited)
        return time_taken - 1

    def dfs(self, node, parent_node, visited):
        if not node:
            return -1
        if node in visited:
            return 0

        visited.add(node)

        time_taken = 0
        for child in (node.left, node.right, parent_node.get(node, None)):
            time_taken = max(time_taken, 1 + self.dfs(child, parent_node, visited))
        return time_taken

    def findNode(self, node, val):
        if not node:
            return None
        if node.val == val:
            return node
        return self.findNode(node.left, val) or self.findNode(node.right, val)

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
