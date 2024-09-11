class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):

        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1
        return temp

    def prepend(self, value):

        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head

        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

        return temp

    def set_value(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True

        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        else:
            new_node = Node(value)
            before = self.get(index - 1)
            after = before.next

            new_node.prev = before
            new_node.next = after
            before.next = new_node
            after.prev = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        while temp is not None:
            temp.next, temp.prev = temp.prev, temp.next
            temp = temp.prev

        self.head, self.tail = self.tail, self.head

    # def reverse(self):
    #     head = self.head
    #     tail = self.tail
    #     current = self.head
    #     while current is not None:
    #         temp = current
    #         current = current.next
    #         temp.next = temp.prev
    #         temp.prev = current
    #
    #     self.head = tail
    #     self.tail = head

    def is_palindrome(self):
        if self.length <= 1:
            return True

        temp_head = self.head
        temp_tail = self.tail

        for _ in range(self.length // 2):
            if temp_head.value == temp_tail.value:
                temp_head = temp_head.next
                temp_tail = temp_tail.prev
            else:
                return False
        return True

    def swap_pairs(self):
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node

        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next

            previous_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            second_node.prev = previous_node
            first_node.prev = second_node

            if first_node.next:
                first_node.next.prev = first_node

            self.head = first_node.next
            previous_node = first_node

        self.head = dummy_node.next

        if self.head:
            self.head.prev = None

