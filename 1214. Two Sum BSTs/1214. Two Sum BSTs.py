"""
Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.



Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.


Constraints:

The number of nodes in each tree is in the range [1, 5000].
-10^9 <= Node.val, target <= 10^9


"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def inorder(root):
            if not root: return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        root1_set = set(inorder(root1))
        second_tree = inorder(root2)
        for node in second_tree:
            if target - node in root1_set:
                return True
        return False