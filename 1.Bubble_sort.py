def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range (0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = input("Enter element seperated by space : ").split()
arr = [float (num) if '.' in num else int(num) for num in arr]


bubble_sort(arr)


print("sorted array is :", arr)