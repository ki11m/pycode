class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 在链表末尾添加元素
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # 在指定位置插入元素
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 0
            while current and count < position - 1:
                current = current.next
                count += 1
            if not current:
                raise IndexError("位置超出链表范围")
            new_node.next = current.next
            current.next = new_node

    # 删除指定元素
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    # 查找元素是否存在
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    # 打印链表元素
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# 示例用法
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.display()  # 输出: 1 -> 2 -> 3 -> None

    linked_list.insert(4, 1)
    linked_list.display()  # 输出: 1 -> 4 -> 2 -> 3 -> None

    linked_list.delete(2)
    linked_list.display()  # 输出: 1 -> 4 -> 3 -> None

    print(linked_list.search(4))  # 输出: True
    print(linked_list.search(5))  # 输出: False
