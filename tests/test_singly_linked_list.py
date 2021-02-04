import unittest
from singly_linked_list import SinglyLinkedList, SinglyLinkedListNode


class Test(unittest.TestCase):

    def test_insert_at_head(self):
        l = SinglyLinkedList()

        l.insert_at_head(8)
        self.assertEqual(l.head.data, 8)
        self.assertEqual(l.tail.data, 8)

        l.insert_at_head(9)
        self.assertEqual(l.head.data, 9)
        self.assertEqual(l.tail.data, 8)

    def test_insert_at_tail(self):
        l = SinglyLinkedList()

        l.insert_at_tail(8)
        self.assertEqual(l.head.data, 8)
        self.assertEqual(l.tail.data, 8)

        l.insert_at_tail(9)
        self.assertEqual(l.head.next.data, 9)
        self.assertEqual(l.tail.data, 9)

    def test_insert_at_position(self):
        l = SinglyLinkedList()
        
        l.insert(8)
        self.assertEqual(l.head.data, 8)
        self.assertEqual(l.tail.data, 8)

        l.insert(9)
        self.assertEqual(l.head.data, 8)
        self.assertEqual(l.tail.data, 9)

        l.insert(10, position=0)
        self.assertEqual(l.head.data, 10)
        self.assertEqual(l.head.next.data, 8)
        self.assertEqual(l.tail.data, 9)

        l.insert(13, position=2)
        self.assertEqual(l.head.data, 10)
        self.assertEqual(l.head.next.data, 8)
        self.assertEqual(l.head.next.next.data, 13)
        self.assertEqual(l.tail.data, 9)

    def test_reverse(self):
        l = SinglyLinkedList()

        l.insert(8)
        l.insert(9)
        l.reverse()
        self.assertEqual(l.head.data, 9)
        self.assertEqual(l.head.next.data, 8)
        self.assertEqual(l.tail.data, 8)

    def test_reverse_one_element_list(self):
        l = SinglyLinkedList()

        l.insert(8)
        l.reverse()
        self.assertEqual(l.head.data, 8)
        self.assertIsNone(l.head.next)
        self.assertEqual(l.tail.data, 8)

    def test_reverse_one_element_list(self):
        l = SinglyLinkedList()

        l.reverse()
        self.assertIsNone(l.head)
        self.assertIsNone(l.tail)

    def test_is_equal(self):
        l = SinglyLinkedList()
        m = SinglyLinkedList()

        self.assertTrue(l.is_equal(m))
        self.assertTrue(m.is_equal(l))
        
        l.insert(8)
        self.assertFalse(l.is_equal(m))
        self.assertFalse(m.is_equal(l))

        m.insert(8)
        self.assertTrue(l.is_equal(m))
        self.assertTrue(m.is_equal(l))

        l.insert(13)
        m.insert(13)
        self.assertTrue(l.is_equal(m))
        self.assertTrue(m.is_equal(l))

        l.insert(8)
        m.insert(88)
        self.assertFalse(l.is_equal(m))
        self.assertFalse(m.is_equal(l))

    def test_get_node(self):
        l = SinglyLinkedList()
        l.insert(7)
        l.insert(8)
        l.insert(9)

        self.assertIsInstance(l.get_node(0), SinglyLinkedListNode)
        self.assertEqual(l.get_node(0).data, 7)
        self.assertIsInstance(l.get_node(1), SinglyLinkedListNode)
        self.assertEqual(l.get_node(1).data, 8)
        self.assertIsInstance(l.get_node(2), SinglyLinkedListNode)
        self.assertEqual(l.get_node(2).data, 9)

    def test_get_node_negative_index(self):
        l = SinglyLinkedList()
        l.insert(7)
        l.insert(8)
        l.insert(9)
        self.assertIsInstance(l.get_node(-1), SinglyLinkedListNode)
        self.assertEqual(l.get_node(-1).data, 9)
        self.assertIsInstance(l.get_node(-1), SinglyLinkedListNode)
        self.assertEqual(l.get_node(-2).data, 8)
        self.assertIsInstance(l.get_node(-1), SinglyLinkedListNode)
        self.assertEqual(l.get_node(-3).data, 7)