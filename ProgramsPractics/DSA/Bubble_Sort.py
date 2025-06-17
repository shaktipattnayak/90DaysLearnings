# Repeatedly swaps adjacent elements if they are in the wrong order.
arr = [64, 34, 25, 12, 22, 11, 90]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        print(f"for j in range(0, n-i-1)- meaning {n} - {i} - 1 is {n-i-1}")
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
print(bubble_sort(arr)) # Output: [11, 12, 22, 25, 34, 64, 90]