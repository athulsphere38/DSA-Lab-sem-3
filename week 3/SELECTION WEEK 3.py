def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

a = []
while True:
    elem = input("Enter an element (or enter stop to finish):- ")
    if elem.lower() == "stop":
        break
    a.append(int(elem))

print("Original List:", a)
sorted_list = selection_sort(a)
print("Sorted List:  ", sorted_list)
