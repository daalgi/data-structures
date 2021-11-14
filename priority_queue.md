# PRIORITY QUEUES (PQs)
[William Fiset tutorial](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsCLFSHm1nYb9daYf60lCcag)

PQ is an abstract data type that operates similar to a normal queue, except that each element has a certain priority. The priority of the elements in the PQ determine the order in which elements are removed.

PQ only supports comparable data.

A heap is a tree based data structure that satisfies the heap invariant: if A is a parent node of B, then A is ordered with respect to B for all nodes A, B in the heap.
- The nodes can contain more or less than two branches.
- They must not contain cycles.

## 1. WHEN IS A PQ USED?
- Dijkstra's shortest path algorithm.
- Anytime you need the dynamically fetch the 'next best' or 'next worst' element.
- Used in Huffman coding (which is often used for lossless data compression).
- Best First Search (BFS) algorithms such as A* use PQs to
continuously grab the next most promising node.
- Minimum spanning tree (MST) algorithms.

## 2. COMPLEXITY PQ WITH BINARY HEAP
- Binary heap construction: O(n)
- Polling: O(log(n))
- Peeking: O(1)
- Adding: O(log(n))
- Naive removing: O(n)
- Advanced removing with help of a hash table: O(log(n))
- Naive contains: O(n)
- Contains check with help of a hash table: O(1)

## 3. TURNING MIN PQ INTO MAX PQ
Since elements in a PQ are comparable, they implement some sort of comparable interface, which we can simply **negate** to achieve a Max heap.

## 4. ACCESSING CHILDREN IN A BINARY HEAP
Let `i` be the parent node index (zero based):
- Left child index: `2i + 1`
- Right child index: `2i + 2`

## 5. ADDING ELEMENTS TO A BINARY HEAP
PQ are usually implemented with heaps, since this gives them the best possible time complexity.

However, a PQ is not a heap, it's an abstract data type (ADT), hence heaps are not the only way to implement PQs. As an example, we could use an unsorted list, but this would not give us the best possible time complexity.

A binary heap is a binary tree that support the **heap invariant**. In a binary tree every node has exactly two children.

A **complete binary tree** is a tree in which at every level, except possible the last, is completely filled and all the nodes as far left as possible.

1. Insert value at the bottom row as far left possible (after the last index).
2. Bubble up the node (swapping the node with the parent up until the heap invariant is satisfied).

## 6. REMOVING ELEMENTS FROM A BINARY HEAP
In general in heaps we always want to remove the root value, the node of interest, the one withthe highest priority (the smalles or largest value). When we remove the root we call it **polling**.

### 6.1. POLLING
Removing the root we don't need to search for its index, it's always position 0.
1. Swap the root and the last node.
2. Remove the new last node (previous root).
3. Bubble down the new root (previous last node), swapping with the smalles of each child.

Polling takes O(log(n))

### 6.2. REMOVING A VALUE
1. Search for the value, starting at one and then doing a linear search.
2. Swap the value node with the last node.
3. Remove the new last node.
4. Now we are in violation of the heap invariant, so bubble up/down.

Removing a random node takes O(n).

### 6.3. REMOVING A VALUE WITH A HASHTABLE IN O(log(n))
Hashtable provides a constant time lookup and update for a mapping from a key (the node value) to a value (the index).

Multiple value problem: instead of mapping one value to one position, we will map one value to multiple positions. We can maintain a `set` or `tree set` of indexes for which a particular node value (key) maps to.
