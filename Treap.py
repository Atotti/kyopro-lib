import random


class Node:
    def __init__(self, key, priority=None, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.priority = priority


class Treap:
    def __init__(self):
        self.root = None
        self.priority_set = set()

    def right_rotate(self, t: Node) -> Node:
        """
        右回転
        """
        s = t.left
        t.left = s.right
        s.right = t
        if t == self.root:
            self.root = s
        return s

    def left_rotate(self, t: Node) -> Node:
        """
        左回転
        """
        s = t.right
        t.right = s.left
        s.left = t
        if t == self.root:
            self.root = s
        return s

    def insert(self, key: int, priority=None):
        if priority == None:
            priority = random.randint(0, 10**18)
            while priority in self.priority_set:
                priority = random.randint()
            self.priority_set.add(priority)
        if self.root == None:
            self.root = Node(key, priority=priority)
        else:
            self._insert(self.root, key, priority, self.root)
        # print(*Tr.print_inorder())

    def _insert(self, t: Node, key: int, priority: int, t_parent: Node):
        if t == None:
            t = Node(key, priority=priority, parent=t_parent)
            # print(t.key, t.parent.key)
            if t_parent.key > key:
                t_parent.left = t
            else:
                t_parent.right = t
            return t
        if key == t.key:
            return t

        if key < t.key:
            # print("ddd", key, t.key, key < t.key)
            # print(self._insert(t.left, key, priority, t_parent))
            t.left = self._insert(t.left, key, priority, t)
            if t.priority < t.left.priority:
                t = self.right_rotate(t)
        else:
            # print("siu", t.right, t.key)
            # print(self._insert(t.right, key, priority, t_parent))
            t.right = self._insert(t.right, key, priority, t)
            if t.priority < t.right.priority:
                t = self.left_rotate(t)
        # print("a", t.key, t_parent.key)
        return t

    def delete(self, t: Node, key: int):
        if t == None:
            return None
        if key < t.key:
            t.left = self.delete(t.left, key)
        elif key > t.key:
            t.right = self.delete(t.right, key)
        else:
            return self._delete(t, key)
        return t

    def _delete(self, t: Node, key):
        if t.left == None and t.right == None:
            return None
        elif t.left == None:
            t = self.left_rotate(t)
        elif t.right == None:
            t = self.right_rotate(t)
        else:
            if t.left.priority > t.right.priority:
                t = self.right_rotate(t)
            else:
                t = self.left_rotate(t)
        return self.delete(t, key)

    def find(self, k: int) -> Node:
        """
        探索 O(h)
        """
        node = self.root
        while node != None and node.key != k:
            if node.key < k:
                node = node.right
            else:
                node = node.left
        return node

    def inorder(self, left: Node, root: Node, right: Node) -> list:
        """
        先行順巡回 O(N)
        """
        if left != None and right != None:
            left = self.inorder(left.left, left, left.right)
            right = self.inorder(right.left, right, right.right)
            return left + [root] + right
        elif left != None and right == None:
            left = self.inorder(left.left, left, left.right)
            return left + [root]
        elif left == None and right != None:
            right = self.inorder(right.left, right, right.right)
            return [root] + right
        else:
            return [root]

    def print_inorder(self) -> list:
        # print(self.root)
        inorder_list = self.inorder(self.root.left, self.root, self.root.right)
        ans = []
        for node in inorder_list:
            ans.append(node.key)
        return ans

    def preorder(self, left: Node, root: Node, right: Node) -> list:
        """
        中間順巡回 O(N)
        """
        if left != None and right != None:
            left = self.preorder(left.left, left, left.right)
            right = self.preorder(right.left, right, right.right)
            return [root] + left + right
        elif left != None and right == None:
            left = self.preorder(left.left, left, left.right)
            return [root] + left
        elif left == None and right != None:
            right = self.preorder(right.left, right, right.right)
            return [root] + right
        else:
            return [root]

    def print_preorder(self) -> list:
        preorder_list = self.preorder(self.root.left, self.root, self.root.right)
        ans = []
        for node in preorder_list:
            ans.append(node.key)
        return ans

    def postorder(self, left: Node, root: Node, right: Node) -> list:
        """
        後行順巡回 O(N)
        """
        if left != None and right != None:
            left = self.postorder(left.left, left, left.right)
            right = self.postorder(right.left, right, right.right)
            return left + right + [root]
        elif left != None and right == None:
            left = self.postorder(left.left, left, left.right)
            return left + [root]
        elif left == None and right != None:
            right = self.postorder(right.left, right, right.right)
            return right + [root]
        else:
            return [root]

    def print_postorder(self) -> list:
        postorder_list = self.postorder(self.root.left, self.root, self.root.right)
        ans = []
        for node in postorder_list:
            ans.append(node.key)
        return ans


if __name__ == "__main__":
    Tr = Treap()
    n = int(input())
    for i in range(n):
        mei, *key = input().split()
        if mei == "insert":
            Tr.insert(int(key[0]), int(key[1]))
        elif mei == "print":
            print("", *Tr.print_inorder())
            print("", *Tr.print_preorder())
        elif mei == "find":
            ans = Tr.find(int(key[0]))
            if ans == None:
                print("no")
            else:
                print("yes")
        elif mei == "delete":
            Tr.delete(Tr.root, int(key[0]))
