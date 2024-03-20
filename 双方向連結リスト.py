class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, data_list=None):
        self.head = None
        self.tail = None
        if data_list is not None:
            for data in data_list:
                self.append(data)

    def append_right(self, data):
        """
        リストの末尾に新しいノードを追加 O(1)
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        last_node = self.tail
        last_node.next = new_node
        new_node.prev = last_node
        self.tail = new_node

    def append_left(self, data):
        """
        リストの先頭に新しいノードを追加 O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_left(self, target_data, new_data):
        """target_dataの左に挿入 O(N)"""
        current = self.head
        while current:
            if current.data == target_data and current.prev:
                new_node = Node(new_data)
                new_node.prev = current.prev
                new_node.next = current
                current.prev.next = new_node
                current.prev = new_node
                return
            elif current.data == target_data and current == self.head:
                self.prepend(new_data)
                return
            current = current.next

    def insert_right(self, target_data, new_data):
        """target_dataの右に挿入 O(N)"""
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next

    def delete_node(self, target_data):
        """target_dataを削除 O(N)"""
        current = self.head
        while current:
            if current.data == target_data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev

                return
            current = current.next

    def __str__(self):
        """
        リストの内容を前から順に表示し、その結果を文字列として返す
        """
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        return "<DoublyLinkedList>" + "[" + ", ".join(elements) + "]"

    def __iter__(self):
        """
        リストを通じてイテレートするために使用
        listへの変換が出来るようになる
        """
        current = self.head
        while current:
            yield current.data
            current = current.next
