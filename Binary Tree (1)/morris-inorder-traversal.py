from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def morrisInOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    current = root

    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            # Find the in-order predecessor
            pre = current.left
            while pre.right and pre.right != current:
                pre = pre.right

            if not pre.right:
                # Establish the temporary link
                pre.right = current
                current = current.left
            else:
                # Revert the temporary link and visit the current node
                pre.right = None
                result.append(current.val)
                current = current.right

    return result
