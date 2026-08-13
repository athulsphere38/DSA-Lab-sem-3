def binary_search(a, key):
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == key:
            return mid
        elif a[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


a = list(map(int, input("Enter the elements: ").split()))
key = int(input("Enter the element to search: "))

if a == sorted(a):
    result = binary_search(a, key)

    if result != -1:
        print("Element found at position", result + 1)
    else:
        print("Element not found")
else:
    print("Array is unsorted. Binary search cannot be performed.")
