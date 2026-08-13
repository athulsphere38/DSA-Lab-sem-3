def search_employee(ids, key, index=0):
    if index == len(ids):
        return -1

    if ids[index] == key:
        return index

    return search_employee(ids, key, index + 1)


ids = list(map(int, input("Enter employee IDs: ").split()))
key = int(input("Enter employee ID to search: "))

result = search_employee(ids, key)

if result != -1:
    print("Employee ID found at position", result + 1)
else:
    print("Employee ID not found")
