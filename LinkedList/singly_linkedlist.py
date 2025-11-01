

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
        while node:
            print(node.value)
            node = node.next

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
            

        return head

        
            
            


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

linked_list.print_ll()
print("-----------------------")
linked_list.modifiedList([1,2,3])
print("-----------------------")
linked_list.print_ll()
