def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [arr[p + i] for i in range(n1)]
    R = [arr[q + j + 1] for j in range(n2)]

    L.append(float('inf'))  
    R.append(float('inf'))  

    i = j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

arr = input("Enter element seperated by space : ").split()
arr = [float (num) if '.' in num else int(num) for num in arr]

print("Original array:", arr)
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)