#!/usr/bin/python3
"""7. Singly linked list
"""


class Node:
    """This class creates Nodes for a linked link list

    Attributes:
        private attributes: data and new_node
        public attributes: check_data and check_next_node"""

    def __init__(self, data, next_node=None):
        self.check_data(data)
        self.check_next_node(next_node)
        self.__data = data
        self.__next_node = next_node

    def check_data(self, data):
        if type(data) is not int:
            raise TypeError("data must be an integer")

    def check_next_node(self, next_node):
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.check_data(data)
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        self.check_next_node(next_node)
        self.__next_node = next_node


class SinglyLinkedList:
    """Class of LinkedList link"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            if self.__head.data > value:
                aux = self.__head
                self.__head = Node(value)
                self.__head.next_node = aux
                return
            aux = self.__head
            while aux.next_node is not None:
                if aux.next_node.data > value:
                    break
                aux = aux.next_node
            aux2 = aux.next_node
            aux.next_node = Node(value)
            aux.next_node.next_node = aux2

    def __str__(self):
        aux = self.__head
        list_print = ""
        while aux is not None:
            if aux.next_node is None:
                list_print += str(aux.data)
            else:
                list_print += str(aux.data) + '\n'
            aux = aux.next_node
        return list_print
