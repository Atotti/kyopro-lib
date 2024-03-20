class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedDictList:
    """
    重複不可
    検索・挿入・削除 O(1)
    """

    def __init__(self, data_list=None):
        self.head = None
        self.tail = None
        self.nodes_dict = {}
        if data_list:
            for data in data_list:
                self.append_right(data)

    def append_right(self, data):
        """
        リストの末尾に新しいノードを追加 O(1)
        """
        if data in self.nodes_dict:
            raise ValueError("同じデータを持つノードが既に存在します。")
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            last = self.tail
            last.next = new_node
            new_node.prev = last
            self.tail = new_node
        self.nodes_dict[data] = new_node  # 辞書を更新

    def append_left(self, data):
        """
        リストの先頭に新しいノードを追加 O(1)
        """
        if data in self.nodes_dict:
            raise ValueError("同じデータを持つノードが既に存在します。")
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node
        self.nodes_dict[data] = new_node  # 辞書を更新

    def search(self, data):
        """
        指定されたデータを持つノードをO(1)で検索します。
        ノードが見つかればそのノードを返し、見つからなければNoneを返します。
        """
        return self.nodes_dict.get(data, None)

    def insert_left(self, target_data, new_data):
        """target_dataの左に挿入 O(1)"""
        if new_data in self.nodes_dict:
            raise ValueError("同じデータを持つノードが既に存在します: {}".format(new_data))
        target_node = self.search(target_data)
        if target_node is None:
            raise ValueError("対象のデータがリストに存在しません: {}".format(target_data))
        new_node = Node(new_data)
        self.nodes_dict[new_data] = new_node
        if target_node.prev:
            new_node.prev = target_node.prev
            target_node.prev.next = new_node
        else:
            self.head = new_node
        new_node.next = target_node
        target_node.prev = new_node

    def insert_right(self, target_data, new_data):
        """target_dataの右に挿入 O(1)"""
        if new_data in self.nodes_dict:
            raise ValueError("同じデータを持つノードが既に存在します: {}".format(new_data))
        target_node = self.search(target_data)
        if target_node is None:
            raise ValueError("対象のデータがリストに存在しません: {}".format(target_data))
        new_node = Node(new_data)
        self.nodes_dict[new_data] = new_node
        new_node.prev = target_node
        if target_node.next:
            new_node.next = target_node.next
            target_node.next.prev = new_node
        else:
            self.tail = new_node
        target_node.next = new_node

    def delete(self, target_data):
        """target_dataを削除 O(1)"""
        target_node = self.search(target_data)
        if target_node is None:
            raise ValueError(f"削除するデータがリストに存在しません: {target_data}")

        # 対象ノードの前後のノードを接続します
        if target_node.prev:
            target_node.prev.next = target_node.next
        else:
            # 削除するノードが先頭の場合は、headを更新します
            self.head = target_node.next

        if target_node.next:
            target_node.next.prev = target_node.prev

        # 辞書からも削除します
        del self.nodes_dict[target_data]

    def __str__(self):
        """
        リストの内容を前から順に表示し、その結果を文字列として返す
        """
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        return "<DoublyLinkedDictList>" + "[" + ", ".join(elements) + "]"

    def __iter__(self):
        """
        リストを通じてイテレートするために使用
        listへの変換が出来るようになる
        """
        current = self.head
        while current:
            yield current.data
            current = current.next


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    DLDL = DoublyLinkedDictList(A)

    Q = int(input())
    for i in range(Q):
        q, *xy = input().split()
        if q == "1":
            x, y = int(xy[0]), int(xy[1])
            DLDL.insert_right(x, y)
        else:
            x = int(xy[0])
            DLDL.delete(x)

    print(*list(DLDL))
