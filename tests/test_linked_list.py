import unittest
"""Тесты с использованием unittest для модуля linked_list."""
from src.linked_list import Node, LinkedList

class NodeTest(unittest.TestCase):

    def test_init(self):
       node = Node("data6", "data5")
       self.assertEqual(node.data,"data6")
       self.assertEqual(node.next_node, "data5")

class StackTest(unittest.TestCase):
    def test_init(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

    def test_insert_beginning(self):
        linked_list = LinkedList()
        linked_list.insert_beginning({'id': 5})
        self.assertEqual(linked_list.head.data, {'id': 5})
        self.assertEqual(linked_list.tail.data, {'id': 5})
        self.assertEqual(linked_list.head, linked_list.tail)

    def test_dequeue(self):
        linked_list = LinkedList()
        linked_list.insert_beginning({'id': 1})
        self.assertEqual(linked_list.head.data, {'id': 1})
        linked_list.insert_at_end({'id': 2})
        self.assertEqual(linked_list.head.data, {'id': 1}, {'id': 2})
        linked_list.insert_at_end({'id': 3})
        self.assertEqual(str(linked_list)," {'id': 1} -> {'id': 2} -> {'id': 3} -> None")  # Проверяем весь список
        linked_list.insert_beginning({'id': 0})
        self.assertEqual(str(linked_list),
                        " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")  # Проверяем весь список