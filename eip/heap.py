import heapq

heap = [12,3,134,6,5,654,23,43,5,345,46,54]

heapq._heapify_max(heap)
largest = heapq.heappop(heap)
print largest
