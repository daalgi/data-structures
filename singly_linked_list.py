class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data, position: int = -1):
        if position == -1:
            return self.insert_at_tail(data)
        elif position == 0 or not self.head:
            return self.insert_at_head(data)

        # Insert between head and tail
        node = SinglyLinkedListNode(data)
        curr = self.head
        while position > 1:
            curr = curr.next
            position -= 1
        next_node = curr.next
        curr.next = node
        node.next = next_node
        
        return self.head

    def insert_at_head(self, data):
        node = SinglyLinkedListNode(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

        return self.head

    def insert_at_tail(self, data):
        node = SinglyLinkedListNode(data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

        return self.head

    def reverse(self):
        # Return None if no node is defined
        if not self.head:
            return None

        # Make a list of the nodes
        nodes = []
        n = 0
        curr = self.head
        while curr:
            n += 1
            nodes.append(curr)
            curr = curr.next

        # Change the pointers of the nodes
        self.head = nodes[n-1]
        for i in range(n-1, 0, -1):
            nodes[i].next = nodes[i-1]
        nodes[0].next = None
        self.tail = nodes[0]

        return self.head

    def is_equal(self, other):
        # Check if the head is None on both SingleLinkedLists
        if not self.head:
            if not other.head:
                return True
            return False

        # Loop through the nodes in both lists
        curr = self.head
        comp = other.head
        while curr and comp:
            if curr.data != comp.data:
                return False
            curr = curr.next
            comp = comp.next

        # False if one of the last nodes is None while the other is not
        if (not curr and comp) or (curr and not comp):
            return False

        # After passing all the tests, returns True
        return True

    def get_node(self, index: int = 0):
        # A negative index indicates position from the tail
        #   index = -1, tail node
        if index < 0:
            return self.get_node_from_tail(index=-index-1)

        curr = self.head
        while index > 0:
            curr = curr.next
            if not curr:
                raise ValueError("")
            index -= 1
        return curr

    def get_node_from_tail(self, index: int = 0):
        nodes = []
        curr = self.head
        n = 0
        while curr:
            nodes.append(curr)
            curr = curr.next
            n += 1
        return nodes[n-1-index]

    def merge_sorted(self, other):
        #TODO
        pass

    def print(self):
        if not self.head:
            return print(None)

        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next