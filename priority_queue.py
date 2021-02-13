"""
PRIORITY QUEUE BY MEANS OF A BINARY HEAP
"""
from collections import defaultdict


OUTPUT_COLUMN_WIDTH = 30

def parent_node_index(i):
    """
    Returns the index of the parent node of a 
    given node (index `i`) in a Binary Heap

    If index `i` is a left child node, 
    the parent is defined as (i - 1) // 2.
    
    If index `i` is a right child node, 
    the parent is defined as (i - 2) // 2.
    """
    if not i: 
        return None
    addend = 1 if i & 1 else 2
    return (i - addend) // 2


def child_left_node_index(i):
    """
    Returns the index of the child left node of a 
    given node (index `i`) in a Binary Heap
    """
    return 2 * i + 1


def child_right_node_index(i):
    """
    Returns the index of the child right node of a 
    given node (index `i`) in a Binary Heap
    """
    return 2 * i + 2


class PriorityQueue:
    def __init__(self, array: list = None):
        self.array = [] if not array else array
        self.hashtable = defaultdict(list)
        self.size = len(self.array)
        
        if array:
            for i, elem in enumerate(array):
                self.hashtable[elem].append(i)
        
    def add(self, element, verbose: bool = False):
        """
        Adds an element (value)
        """
        # Add to bottom left
        self.array.append(element)
        self.size += 1
        self.hashtable[element].append(self.size - 1)
        # Verbose output variables
        out, len_prev = '', 0

        if verbose:
            out += f'Add element {element}\n'
            
        if self.size > 1:
            # Current node index `i` and its parent `p`
            i = self.size - 1            
            p = parent_node_index(i)

            if verbose:
                new_out, len_prev = self._verbose_swap_output(element, i, p)
                out += new_out
                
            # Check if the heap invariant is satisfied
            while element < self.array[p]:
                # Swap child-parent nodes
                self._swap(i, p)

                # Update indices
                i = p
                p = parent_node_index(i)

                if verbose:
                    new_out, len_prev = self._verbose_swap_output(element, i, p, len_prev)
                    out += new_out
                
                if i == 0:
                    break
        
        if verbose:            
            print(self._verbose_updated_array_mutable_output(out))

        return self

    def remove(self, element):
        """
        Searches an element (value) and removes the node
        """
        if element not in self.hashtable:
            print(f'Element {element} not in the PriorityQueue.')

        # Last index containing `element`
        index = self.hashtable[element][-1]

        # Last index in the PriorityQueue
        last = self.size - 1

        # Swap with last node
        if index < last:
            self._swap(index, last)

        # Remove new last node
        self.array.pop()
        self.hashtable[element].remove(last)
        self.size -= 1

        if index == last:
            return self

        current = self.array[index]

        # Compare to parent and child nodes and "bubble" up or down
        c = self._smallest_child_index(index)
        p = parent_node_index(index)

        if p is not None and current < self.array[p]:
            self._bubble_up(current, index, p)
        elif c and current > self.array[c]:
            self._bubble_down(current, index, c)
        
        return self

    def poll(self):
        """
        Removes the root node
        """
        return self.remove(self.array[0])

    def _swap(self, i, j):
        """
        Swaps nodes by indices, updating self.array and self.hashtable
        """
        # Elements value
        elem_i = self.array[i]
        elem_j = self.array[j]

        # Swap in array
        self.array[i], self.array[j] = self.array[j], self.array[i]
        
        # Swap in hashtable
        self.hashtable[elem_i].remove(i)
        self.hashtable[elem_i].append(j)
        self.hashtable[elem_j].remove(j)
        self.hashtable[elem_j].append(i)

    def _bubble_up(self, element, i: int, p: int):
        """
        Swaps nodes upwards until the heap invariance is satisfied
        """
        while p is not None and element < self.array[p]:
            self._swap(i, p)            
            if p == 0:
                break            
            i = p
            p = parent_node_index(i)

    def _bubble_down(self, element, i: int, c: int):
        """
        Swaps nodes downwards until the heap invariance is satisfied
        """
        while c < self.size and element > self.array[c]:
            self._swap(i, c)
            i = c
            c = self._smallest_child_index(i)
            if not c:
                break

    def _smallest_child_index(self, i: int):
        left = child_left_node_index(i)
        right = child_right_node_index(i)
        
        if left >= self.size:
            return None
        
        if right >= self.size:
            return left

        if self.array[left] <= self.array[right]:
            return left

        return right

    def _verbose_swap_output(self, element, i, p, len_prev: int = 0):
        # Concatenate with previous line
        # `len_prev` is the previous line length
        prev = ''
        if len_prev > 0:
            prev += ' ' * (OUTPUT_COLUMN_WIDTH * 2 - len_prev)
            prev += '--> Nodes swapped!\n'

        # New line
        line = f'Current node {i} = {element}'
        if i > 0:
            line += ' ' * (OUTPUT_COLUMN_WIDTH - len(line))
            line += f'Parent node  {p} = {self.array[p]}'
        if i == 0 or element >= self.array[p]:
            line += ' ' * (OUTPUT_COLUMN_WIDTH * 2 - len(line))
            line += '--> Heap invariant satisfied!\n'

        return prev + line, len(line)

    def _verbose_updated_array_mutable_output(self, out):
        if out[-1:] != '\n':
            out += '\n'
        out += f'>> Updated array: {str(self.array)}\n'
        return out