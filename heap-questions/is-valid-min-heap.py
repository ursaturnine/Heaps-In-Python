"""Check whether a list has a valid min heap

Given: Heap and the array representation

Check the properties to verify the heap

"""

def is_min_heap(heap):

    # there is no need to check the leaf nodes
    num_of_items = (len(heap) -2 ) // 2 + 1


    for i in range(num_of_items):

        # check heap properties
        # parent must be smaller than children

        if heap[i] > heap[2 * i + 1] or heap[i] > heap[2 * i + 2]:
            return False

    return True
        

