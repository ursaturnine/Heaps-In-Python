"""Transform a max heap to a min heap

Only consider internal nodes in a reversed order
-Leaf nodes don't have children, so heap properties do not have to be checked


"""

class HeapTransformer:
    def __init__(self, heap):
        self.heap = heap
    
    def transform(self):

        # start with last internal node, stop at 0, decrement (reverse)
        for i in range((len(self.heap) -2) // 2, -1, -1):
            self.fix_down(i)
    
    def fix_down(self, index):

        heap_size = len(self.heap)

        index_left = 2 * index + 1
        index_right = 2 * index + 2

        # in a max heap, the parent is always greater than the parent
        index_smallest = index

        # looking for the min (parent or left node)
        if index_left < heap_size and self.heap[index_left] < self.heap[index]:
            index_smallest = index_left
        
        # looking for min (left or right child)
        if index_right < heap_size and self.heap[index_right] < self.heap[index_smallest]:
            index_smallest = index_right
        
        if index != index_smallest:
            self.heap[index], self.heap[index_smallest] = self.heap[index_smallest], self.heap[index]
            self.fix_down(index_smallest)

    




if __name__ == '__main__':

    n = [210, 100, 23, 2, 5]
    heap_transform = HeapTransformer(n)
    heap_transform.transform()
    print(heap_transform.heap)


