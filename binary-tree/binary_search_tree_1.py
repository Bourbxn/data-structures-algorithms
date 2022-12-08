class Node:
    def __init__(self, data: float) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self) -> str:
        return str(self.data)

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, root: Node, data: float) -> Node:
        if not root:
            self.root = Node(data)
            return self.root
        else:
            if root.data == data:
                return root
            if data < root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
        return root
    
    def min_data(self, root: Node) -> float:
        if not root:
            return
        if not root.left:
            return root.data
        return self.min_data(root.left)
    
    def max_data(self, root: Node) -> float:
        if not root:
            return
        if not root.right:
            return root.data
        return self.max_data(root.right)
    
    def print_preorder(self, root: Node) -> None:
        if root:
            print(root, end=' ')
            self.print_preorder(root.left)
            self.print_preorder(root.right)
    
    def print_inorder(self, root: Node) -> None:
        if root:
            self.print_inorder(root.left)
            print(root, end=' ')
            self.print_inorder(root.right)
    
    def print_postorder(self, root: Node) -> None:
        if root:
            self.print_postorder(root.left)
            self.print_postorder(root.right)
            print(root, end=' ')
    
    def print_breadth(self, root: Node, l: list = []) -> None:
        if root:
            print(root, end=' ')
            if root.left:
                l.append(root.left)
            if root.right:
                l.append(root.right)
            if len(l):
                self.print_breadth(l.pop(0), l)
    
    def print_tree(self, root: Node, level: int = 0) -> None:
        if root != None:
            self.print_tree(root.right, level + 1)
            print('     ' * level, root)
            self.print_tree(root.left, level + 1)

def main():
    pass
    # tree = BinarySearchTree()
    # root = None
    # root = tree.insert(root, 20)
    # root = tree.insert(root, 10)
    # root = tree.insert(root, 30)
    # tree.print_tree(root)
    # tree.print_inorder(root) or print()
    # tree.print_preorder(root) or print()
    # tree.print_postorder(root) or print()
    # tree.print_breadth(root) or print()
    # print(tree.min_data(root))
    # print(tree.max_data(root))

if __name__ == '__main__':
    main()
