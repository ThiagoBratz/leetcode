# LeetCode 2236 - Root Equals Sum of Children
# Conceitos: árvores binárias, acesso a atributos e comparação (==)

class Solution:
    def checkTree(self, root: TreeNode | None) -> bool:
        resultado = root.val == root.left.val + root.right.val
        return resultado