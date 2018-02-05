import heapq

heap_min = []
heap_max = []
medians = []

with open('median.txt') as file:
    i = 1
    for line in file.readlines():
        x = int(line)

        if i == 1:
            medians.append(x)
            heapq.heappush(heap_max, x)
            i+=1
            continue

        if x > heap_max[0]:
            if len(heap_max) > len(heap_min):
                heapq.heappush(heap_min, -heapq.heappushpop(heap_max, x))
            else:
                heapq.heappush(heap_max, x)
        else:
            if len(heap_min) > len(heap_max):
                heapq.heappush(heap_max, -heapq.heappushpop(heap_min, -x))
            else:
                heapq.heappush(heap_min, -x)

        if i%2 == 0:
            if len(heap_min) < len(heap_max):
                medians.append(heap_max[0])
            else:
                medians.append(-heap_min[0])
        else:
            if len(heap_min) > len(heap_max):
                medians.append(-heap_min[0])
            else:
                medians.append(heap_max[0])
        i += 1

print(sum(medians)%10000)
