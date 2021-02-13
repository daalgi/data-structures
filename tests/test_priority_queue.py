import unittest
from priority_queue import PriorityQueue, parent_node_index


class Test(unittest.TestCase):

    def test_parent_node_index(self):
        i = 0
        p = parent_node_index(i)
        self.assertIsNone(p)

        i = 1
        p = parent_node_index(i)
        self.assertEqual(p, 0)

        i = 2
        p = parent_node_index(i)
        self.assertEqual(p, 0)

        i = 3
        p = parent_node_index(i)
        self.assertEqual(p, 1)

        i = 4
        p = parent_node_index(i)
        self.assertEqual(p, 1)

        i = 5
        p = parent_node_index(i)
        self.assertEqual(p, 2)
        
        i = 6
        p = parent_node_index(i)
        self.assertEqual(p, 2)

        i = 7
        p = parent_node_index(i)
        self.assertEqual(p, 3)

        i = 8
        p = parent_node_index(i)
        self.assertEqual(p, 3)

    def test_construction(self):
        p = PriorityQueue()
        self.assertIsInstance(p.array, list)
        self.assertIsInstance(p.hashtable, dict)
        self.assertIsInstance(p.size, int)
        self.assertEqual(p.size, 0)    

    def test_construction_with_inital_array(self):
        p = PriorityQueue([2, 3, 2, 7, 7, 13, 2, 11])
        self.assertIsInstance(p.array, list)
        self.assertIsInstance(p.hashtable, dict)
        self.assertIsInstance(p.size, int)
        self.assertEqual(p.size, 8)
        self.assertEqual(p.hashtable[2], [0, 2, 6])
        self.assertEqual(p.hashtable[7], [3, 4])
        self.assertEqual(p.hashtable[11], [7])
        self.assertEqual(p.hashtable[13], [5])
        self.assertEqual(p.hashtable[3], [1])

    def test_add(self):
        p = PriorityQueue()
        print('-' * 60)
        print('Verbose PriorityQueue add tests:')
        print('-' * 60)
        # p.add(10)
        p.add(10, verbose=True)
        self.assertEqual(p.size, 1)
        self.assertEqual(len(p.array), 1)
        self.assertEqual(p.array[0], 10)
        self.assertEqual(p.hashtable[10], [0])

        # p.add(11)
        p.add(11, verbose=True)
        self.assertEqual(p.size, 2)
        self.assertEqual(len(p.array), 2)
        self.assertEqual(p.array, [10, 11])
        self.assertEqual(p.hashtable[10], [0])
        self.assertEqual(p.hashtable[11], [1])

        # p.add(8)
        p.add(8, verbose=True)
        self.assertEqual(p.size, 3)
        self.assertEqual(p.array, [8, 11, 10])
        self.assertEqual(p.hashtable[8], [0])
        self.assertEqual(p.hashtable[10], [2])
        self.assertEqual(p.hashtable[11], [1])

        # p.add(1)
        p.add(1, verbose=True)
        self.assertEqual(p.size, 4)
        self.assertEqual(p.array, [1, 8, 10, 11])
        self.assertEqual(p.hashtable[1], [0])
        self.assertEqual(p.hashtable[8], [1])
        self.assertEqual(p.hashtable[10], [2])
        self.assertEqual(p.hashtable[11], [3])

        # p.add(1)
        p.add(1, verbose=True)
        self.assertEqual(p.size, 5)
        self.assertEqual(p.array, [1, 1, 10, 11, 8])
        self.assertEqual(p.hashtable[1], [0, 1])
        self.assertEqual(p.hashtable[10], [2])
        self.assertEqual(p.hashtable[11], [3])
        self.assertEqual(p.hashtable[8], [4])


    def test_add_with_initial_array(self):
        p = PriorityQueue([2, 7, 2, 11, 7, 13, 2])
        
        p.add(3)
        self.assertEqual(p.size, 8)
        self.assertEqual(p.array, [2, 3, 2, 7, 7, 13, 2, 11])
        self.assertEqual(p.hashtable[2], [0, 2, 6])
        self.assertEqual(p.hashtable[11], [7])
        self.assertEqual(p.hashtable[13], [5])
        self.assertEqual(p.hashtable[3], [1])
        # Note: p.hashtable[7] not necessarily sorted
        self.assertEqual(p.hashtable[7], [4, 3])
        self.assertIn(3, p.hashtable[7])
        self.assertIn(4, p.hashtable[7])

    def test_add_with_initial_array_example(self):
        p = PriorityQueue([5, 6, 12, 8, 7, 14, 19, 13, 12, 11])
        
        p.add(1)
        self.assertEqual(p.array, [1, 5, 12, 8, 6, 14, 19, 13, 12, 11, 7])

        p.add(13)
        self.assertEqual(p.array, [1, 5, 12, 8, 6, 13, 19, 13, 12, 11, 7, 14])
        
        p.add(4)
        self.assertEqual(p.array, [1, 5, 4, 8, 6, 12, 19, 13, 12, 11, 7, 14, 13])

        p.add(0)
        self.assertEqual(p.array, [0, 5, 1, 8, 6, 12, 4, 13, 12, 11, 7, 14, 13, 19])

        p.add(10)
        self.assertEqual(p.array, [0, 5, 1, 8, 6, 12, 4, 13, 12, 11, 7, 14, 13, 19, 10])
        