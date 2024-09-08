def qsort(arr, m, n):
    if m < n:
        key = arr[m]
        i = m
        j = n + 1
        while True:
            i += 1
            while i <= n and arr[i] < key:
                i += 1
            j -= 1
            while arr[j] > key:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        arr[m], arr[j] = arr[j], arr[m]
        qsort(arr, m, j - 1)
        qsort(arr, j + 1, n)



arr = input("Enter element seperated by space : ").split()
arr = [float (num) if '.' in num else int(num) for num in arr]

qsort(arr, 0, len(arr)-1)
print("Sorted array:", arr)