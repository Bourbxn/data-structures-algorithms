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
    
    def insert(self, data: float) -> None:
        self.root = self.insert_h(self.root, data)
    
    def insert_h(self, root: Node, data: float) -> Node:
        if not root:
            self.root = Node(data)
            return self.root
        else:
            if root.data == data:
                return root
            if data < root.data:
                root.left = self.insert_h(root.left, data)
            else:
                root.right = self.insert_h(root.right, data)
        return root
    
    def min_data(self) -> float:
        return self.min_data_h(self.root)

    def min_data_h(self, root: Node) -> float:
        if not root:
            return
        if not root.left:
            return root.data
        return self.min_data_h(root.left)
    
    def max_data(self) -> float:
        return self.max_data_h(self.root)
    
    def max_data_h(self, root: Node) -> float:
        if not root:
            return
        if not root.right:
            return root.data
        return self.max_data_h(root.right)
    
    def print_preorder(self) -> None:
        self.print_preorder_h(self.root)
        print()
    
    def print_preorder_h(self, root: Node) -> None:
        if root:
            print(root, end=' ')
            self.print_preorder_h(root.left)
            self.print_preorder_h(root.right)
    
    def print_inorder(self) -> None:
        self.print_inorder_h(self.root)
        print()
    
    def print_inorder_h(self, root: Node) -> None:
        if root:
            self.print_inorder_h(root.left)
            print(root, end=' ')
            self.print_inorder_h(root.right)
    
    def print_postorder(self) -> None:
        self.print_postorder_h(self.root)
        print()

    def print_postorder_h(self, root: Node) -> None:
        if root:
            self.print_postorder_h(root.left)
            self.print_postorder_h(root.right)
            print(root, end=' ')
    
    def print_breadth(self) -> None:
        self.print_breadth_h(self.root)
        print()

    def print_breadth_h(self, root: Node, l: list = []) -> None:
        if root:
            print(root, end=' ')
            if root.left:
                l.append(root.left)
            if root.right:
                l.append(root.right)
            if len(l):
                self.print_breadth_h(l.pop(0), l)
    
    def print_tree(self) -> None:
        self.print_tree_h(self.root)
    
    def print_tree_h(self, root: Node, level: int = 0) -> None:
        if root != None:
            self.print_tree_h(root.right, level + 1)
            print('     ' * level, root)
            self.print_tree_h(root.left, level + 1)

def main():
    pass
    # tree = BinarySearchTree()
    # tree.insert(10)
    # tree.insert(20)
    # tree.insert(30)
    # tree.print_tree()
    # tree.print_inorder()
    # tree.print_preorder()
    # tree.print_postorder()
    # tree.print_breadth()
    # print(tree.min_data())
    # print(tree.max_data())

if __name__ == '__main__':
    main()
