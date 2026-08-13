n = int(input("Enter number of elements: "))

a = list(map(int, input("Enter the elements: ").split()))

key = int(input("Enter the element to search: "))

found = False

for i in range(n):
    if a[i] == key:
        print("Element found at position", i + 1)
        found = True
        break

if not found:
    print("Element not found")
