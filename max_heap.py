# num of items you can store in 1D array representation of Heap
CAPACITY = 10

# max heap -root node will be the largest item
class Heap:
    def __init__(self):
        # num of items in the heap 
        self.heap_size = 0

        # underlying list data structure
        self.heap = [0] * CAPACITY
    
    def insert(self, item):

        # cannot insert anymore items
        if self.heap_size == CAPACITY:
            return
        
        # heap_size starts at 0
        self.heap[self.heap_size] = item

        self.heap_size += 1

        # check heap properties
        self.fix_up(self.heap_size - 1)

    # starts with node we've inserted up to the root node
    # we have to compare values to determine whether to make swap operations or not
    # O(logN)
    def fix_up(self, index ):

        parent_index = (index -1) //2

        # consider all items above until we hit the root node
        # if heap properties are violated, then swap the parent and child

        # parent node greater than child
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index] 
            self.fix_up(parent_index)
    
    # peek function
    def get_max(self):
        return self.heap[0]
    
    # return max and remove (root node)
    def poll(self):

        max_item = self.get_max()

        # swap root item with last item 
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        self.heap_size -= self.heap_size

        # "heapify"
        self.fix_down(0)

        return max_item
    
    # starting with root node downwards until heap properties are no longer violated
    # O(logN)
    def fix_down(self, index):

        left_index = 2 * index + 1
        right_index = 2 * index + 2

        # parent always > children in max heap
        largest_index = index

        if left_index < self.heap_size and self.heap[left_index] > self.heap[index]:
            largest_index = left_index

        # if right child is > left child then largest child is right child
        if right_index < self.heap_size and self.heap[right_index] > self.heap[index]:
            largest_index = right_index
        
        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.fix_down(largest_index)
        
    def heap_sort(self):
        
        # O(NlogN)
        for _ in range(self.heap_size):
            _max = self.poll()
            print(_max)


if __name__ == '__main__':

    heap = Heap()

    heap.insert(13)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(8)
    heap.insert(1)
    heap.insert(15)
    heap.insert(99)

    print(heap.heap)

    heap.heap_sort()

