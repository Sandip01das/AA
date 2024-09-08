def max_heapify(A, heap_size, i):
    l = 2 * i
    r = 2 * i + 1
    largest = i
    if l <= heap_size and A[l - 1] > A[i - 1]:
        largest = l
    if r <= heap_size and A[r - 1] > A[largest - 1]:
        largest = r
    if largest != i:
        A[i - 1], A[largest - 1] = A[largest - 1], A[i - 1]
        max_heapify(A, heap_size, largest)

def build_max_heap(A):
    heap_size = len(A)
    for i in range(heap_size // 2, 0, -1):
        max_heapify(A, heap_size, i)

def heap_sort(A):
    build_max_heap(A)
    heap_size = len(A)
    for i in range(heap_size, 1, -1):
        A[0], A[i - 1] = A[i - 1], A[0]
        heap_size -= 1
        max_heapify(A, heap_size, 1)

arr = input("Enter element seperated by space : ").split()
arr = [float (num) if '.' in num else int(num) for num in arr]

print("Original array:", arr)
heap_sort(arr)
print("Sorted array:", arr)