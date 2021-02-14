class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for _ in range(self.MAX)]
        self.size = 0

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
        self.size += 1
    
    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def remove(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
        self.size -= 1

    def __setitem__(self, key, val):
        self.add(key, val)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.remove(key)