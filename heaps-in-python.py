import heapq

# constructs min heap -root node is smallest in tree

heap = [4,7,3,-2, 1, 0]


# transforms list structure into a min heap
heapq.heapify(heap)


# print(heap)



nums = [7,8,9,-3,-4,5]
num_heap = []

for value in nums:
    heapq.heappush(num_heap, value)

print(num_heap)


# takes out root node -min item for min heap
# will print ascending order
while num_heap:
    print(heapq.heappop(num_heap))
