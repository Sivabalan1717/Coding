# Sivabalan M, BE ECE, Day 16
# Problem: Convert a sorted array into a height-balanced Binary Search Tree.

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, arr):
        def create_tree(start, end):
            # No elements remain in this range.
            if start > end:
                return None

            # Choose the middle element as this subtree's root.
            mid = (start + end) // 2
            root = Node(arr[mid])

            # Recursively build the left and right subtrees.
            root.left = create_tree(start, mid - 1)
            root.right = create_tree(mid + 1, end)

            return root

        return create_tree(0, len(arr) - 1)


def inorder(root):
    """Return the tree values in sorted order (useful for checking)."""
    if root is None:
        return []
    return inorder(root.left) + [root.data] + inorder(root.right)


if __name__ == "__main__":
    arr = [1, 5, 9, 14, 23, 27]
    root = Solution().sortedArrayToBST(arr)
    print("Inorder traversal:", inorder(root))
