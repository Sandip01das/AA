def selection_sort(arr):
    n = len(arr)
    for i in range (n-1):
        j=i
        for k in range (j+1 , n):
            if arr[k] < arr [j]:
                j=k
        if i!= j:
            arr[i],arr[j] = arr[j],arr[i]


arr = input("Enter element seperated by space : ").split()
arr = [float (num) if '.' in num else int(num) for num in arr]


selection_sort(arr)


print("sorted array is :", arr)