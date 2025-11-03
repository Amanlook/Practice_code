

from typing import List


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_ll(self):

        node = self.head
        response_list = []
        while node:
            response_list.append(node.value)
            node = node.next
        # return response_list
        print(response_list)

    def middleOfLinkedList(self):

        slowptr = self.head
        fastptr = self.head

        while fastptr and fastptr.next:
            
            fastptr = fastptr.next.next
            slowptr = slowptr.next

        return slowptr.value



    def modifiedList(self, nums: List[int]):
        head = self.head

        curr = head

        while curr:
            
            if curr == head and curr.value in nums:
                head = head.next
                curr = head
                continue

            if curr.next and curr.next.value in nums:
                curr.next = curr.next.next
            else:
                curr = curr.next
            
        self.head = head

    def reverseOfLinkedList(self):

        curr = self.head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

            
            


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)


linked_list.print_ll()
print("-----------------------")
# print(linked_list.middleOfLinkedList())
linked_list.reverseOfLinkedList()
# print("-----------------------")
# linked_list.modifiedList([1,2,3])
print("-----------------------")
linked_list.print_ll()