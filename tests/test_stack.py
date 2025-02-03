import unittest
"""Тесты с использованием unittest для модуля stack."""
from src.stack import Node, Stack

class NodeTest(unittest.TestCase):

    def test_init(self):
       node = Node(10, 2)
       self.assertEqual(node.data,10)
       self.assertEqual(node.next_node, 2)

class StackTest(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        stack.push('Hello Word!')
        self.assertEqual(stack.top.data,'Hello Word!')
        self.assertEqual(len(stack.top.data),11)

    def test_pop(self):
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()
        stack.push(10)
        stack.push(15)
        stack.push(30)
        self.assertEqual(stack.top.next_node.data,15)
        self.assertEqual(stack.top.next_node.next_node.data,10)

    def test_str_empty(self):
        self.assertEqual(str(Stack()), "")

    def test_str_not_empty(self):
        stack = Stack()
        stack.push(10)
        self.assertEqual(str(stack), "Not Empty")






