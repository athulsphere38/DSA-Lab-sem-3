
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for i in arr[:-1]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = list(map(int, input("Enter elements separated by spaces: ").split()))

arr = quick_sort(arr)

print("Sorted list:", arr)
