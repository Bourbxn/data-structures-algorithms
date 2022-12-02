class Node:
    def __init__(self, data: float) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self) -> str:
        return str(self.data)

class AVLTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, data: int) -> None:
        self.root = self.insert_h(self.root, data)
    
    def insert_h(self, root: Node, data: float) -> Node:
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.insert_h(root.left, data)
        else:
            root.right = self.insert_h(root.right, data)
        root.height = 1 + max(self.get_height(root.left),
                           self.get_height(root.right))
        balance = self.get_balance(root)
        if balance > 1 and data < root.left.data:
            return self.right_rotate(root)
        if balance < -1 and data > root.right.data:
            return self.left_rotate(root)
        if balance > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
 
    def left_rotate(self, z: Node) -> Node:
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left),
                         self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                         self.get_height(y.right))
        return y
 
    def right_rotate(self, z: Node) -> Node:
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left),
                        self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                        self.get_height(y.right))
        return y
 
    def get_height(self, root: Node) -> int:
        if not root:
            return 0
        return root.height
 
    def get_balance(self, root: Node) -> int:
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
 
    
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
    # tree = AVLTree()
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