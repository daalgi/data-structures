import unittest
from hashtable import HashTable


class Test(unittest.TestCase):

    def test_construction(self):
        h = HashTable()
        self.assertIsInstance(h.arr, list)

    def test_add_get_delete(self):
        h = HashTable()
        h.add('September 2013', 888)
        self.assertEqual(h.size, 1)
        self.assertEqual(h['September 2013'], 888)
        self.assertEqual(h.get('September 2013'), 888)
        self.assertEqual(h['September 2014'], None)
        self.assertEqual(h['September 2015'], None)

        h['September 2014'] = 8888
        self.assertEqual(h.size, 2)
        self.assertEqual(h['September 2014'], 8888)
        self.assertEqual(h.get('September 2014'), 8888)
        self.assertEqual(h['September 2015'], None)
        self.assertEqual(h.get('September 2015'), None)

        h.remove('September 2014')
        self.assertEqual(h.size, 1)
        self.assertEqual(h['September 2013'], 888)
        self.assertEqual(h.get('September 2013'), 888)
        self.assertEqual(h['September 2014'], None)
        self.assertEqual(h['September 2015'], None)

        h.remove('September 2013')
        self.assertEqual(h.size, 0)
        self.assertEqual(h['September 2013'], None)
        self.assertEqual(h.get('September 2013'), None)
        self.assertEqual(h['September 2014'], None)
        self.assertEqual(h['September 2015'], None)  
    