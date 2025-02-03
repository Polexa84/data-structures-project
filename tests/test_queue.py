import unittest
"""Тесты с использованием unittest для модуля queue."""
from src.queue import Node, Queue

class NodeTest(unittest.TestCase):

    def test_init(self):
       node = Node(10, "data5")
       self.assertEqual(node.data,10)
       self.assertEqual(node.next_node, "data5")


class StackTest(unittest.TestCase):
    def test_init(self):
        queue = Queue()
        self.assertEqual(queue.head, None)
        self.assertEqual(queue.tail, None)

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue("data5")
        self.assertEqual(queue.head.data, "data5")
        self.assertEqual(queue.tail.data, "data5")
        self.assertEqual(queue.head, queue.tail)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.head.data, 1)
        self.assertEqual(queue.tail.data, 3)
        self.assertEqual(queue.head.next_node.data, 2)


if __name__ == '__main__':
    unittest.main()




