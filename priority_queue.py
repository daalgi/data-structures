"""
PRIORITY QUEUE BY MEANS OF A BINARY HEAP
"""
from collections import defaultdict


OUTPUT_COLUMN_WIDTH = 30

def parent_node_index(i):
    """
    Returns the index of the parent node in a Binary Heap

    If index `i` is a left child node, 
    the parent is defined as (i - 1) // 2.
    
    If index `i` is a right child node, 
    the parent is defined as (i - 2) // 2.
    """
    if not i: 
        return None
    addend = 1 if i & 1 else 2
    return (i - addend) // 2


class PriorityQueue:
    def __init__(self, array: list = None):
        self.array = [] if not array else array
        self.hashtable = defaultdict(list)
        self.size = len(self.array)
        
        if array:
            for i, elem in enumerate(array):
                self.hashtable[elem].append(i)
        
    def add(self, element, verbose: bool = False):
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

    def _swap(self, i, j):
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