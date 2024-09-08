def insertion_sort(arr):
    n = len(arr)
    for j in range (1,n):
        key = arr[j]
        i=j-1
        while i>=0 and key < arr[i]:
            arr[i+1]=arr[i]
            i-=1
        arr[i+1]= key


arr = input("Enter element seperated by space : ").split()
arr = [float (num) if '.' in num else int(num) for num in arr]

insertion_sort(arr)


print("sorted array is :", arr)