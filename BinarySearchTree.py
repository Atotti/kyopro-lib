# AOJ向けに書いたやつ
class Node:
    """
    Parms:
        key: int
            key
        left: Node
            左の子
        right: Node
            右の子
        parent: Node
            親
    """
    def __init__(self, key: int, left = None, right = None, parent = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
    def __str__(self):
        return self.key

class BinarySearchTree:
    """
    Parms:
        root: Node
            根
    """
    def __init__(self, root = None):
        self.root = root
    
    def insert(self, z: Node):
        """
        挿入 O(h)
        """
        x = self.root # Tの根
        y = None # xの親
        # 木を探索
        while x != None:
            y = x # 親を設定
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y

        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
    
    def find(self, k: int) -> Node:
        """
        探索 O(h)
        """
        node = self.root
        while node != None and node.key != k:
            #print(node.key, k)
            if node.key < k:
                node = node.right
            else:
                node = node.left
        return node
    
    def delete(self, k: int) -> None:
        """
        削除  O(h)
        """
        #print(k)
        k_node = self.find(k)
        if k_node == None:
            return 0
        if k_node.left == None and k_node.right == None:
            #print("0delete", k)
            parent = k_node.parent
            #print(parent.key)
            if parent.left == k_node:
                parent.left = None
            else:
                parent.right = None
        elif k_node.left == None and k_node.right != None:
            #print("1delete", k)
            parent = k_node.parent
            if parent.left == k_node:
                parent.left = k_node.right
                k_node.right.parent = parent
            else:
                parent.right = k_node.right
                k_node.right.parent = parent
        elif k_node.left != None and k_node.right == None:
            #print("2delete", k)
            parent = k_node.parent
            if parent.left == k_node:
                parent.left = k_node.left
                k_node.left.parent = parent
            else:
                parent.right = k_node.left
                k_node.left.parent = parent
        # z が子を２つ持つ場合、 z の次節点 y のキーを z のキーへコピーし、 y を削除する。 y の削除では 1. または 2. を適用する。ここで、 z の次節点とは、中間順巡回で z の次に得られる節点である。
        elif k_node.left != None and k_node.right != None:
            #print("3delete", k)
            next_node = self._search_next_node(k_node)
            self.delete(next_node.key)
            k_node.key = next_node.key
    
    def high(self, node: Node) -> int:
        """
        node の高さを計算
        """
    
    def depth(self, node: Node) -> int:
        """
        node の深さを計算
        """
    
    def max(self) -> Node:
        """
        最大値
        """
    
    def min(self) -> Node:
        """
        最小値
        """
    
    
    def _search_next_node(self, node: Node) -> Node:
        node = node.right
        while node.left != None:
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


if __name__=="__main__":
    BST = BinarySearchTree()
    n = int(input())
    for i in range(n):
        mei, *key = input().split()
        if key != []:
            key = int(key[0])
        if mei == "insert":
            BST.insert(Node(key))
        elif mei == "print":
            print("", *BST.print_inorder())
            print("", *BST.print_preorder())
        elif mei == "find":
            ans = BST.find(key)
            if ans == None:
                print("no")
            else:
                print("yes")
        elif mei == "delete":
            BST.delete(key)