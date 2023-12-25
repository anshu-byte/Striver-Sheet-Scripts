class Solution:
    def __init__(self):
        self.ancestors = {}

    def _populate_ancestors(self, node):
        if node:
            if node.left:
                self.ancestors[node.left] = node
                self._populate_ancestors(node.left)
            if node.right:
                self.ancestors[node.right] = node
                self._populate_ancestors(node.right)

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        self._populate_ancestors(root)
        ancestors_p = set()

        # Traverse up from node p to root and add all ancestors to a set
        while p:
            ancestors_p.add(p)
            p = self.ancestors.get(p)

        # Traverse up from node q to root and return the first ancestor that is also an ancestor of p
        while q not in ancestors_p:
            q = self.ancestors.get(q)

        return q
