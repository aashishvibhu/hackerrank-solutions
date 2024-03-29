#!/bin/python3

#Compare two linked lists

import os
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    currentNode_list1 = llist1
    currentNode_list2 = llist2
    while(True):
        if (currentNode_list1 != None and currentNode_list2 != None):
            if currentNode_list1.data == currentNode_list2.data:
                currentNode_list2 = currentNode_list2.next
                currentNode_list1 = currentNode_list1.next
            else:
                return 0
        elif currentNode_list1 != None or currentNode_list2 != None:
            return 0
        else:
            return 1

if __name__ == '__main__':
