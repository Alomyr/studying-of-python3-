import heapq

heap = []

for i in range(3):
    numero = int(input("Digite o {} numero: ".format(i + 1)))
    heapq.heappush(heap, numero)
print("O maior numero sera: {} e o menor numero sera: {}".format(heap[0], max(heap)))
