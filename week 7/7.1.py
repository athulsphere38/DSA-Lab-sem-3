
MAX = 100
tree = [None] * MAX


def insert(value, index=0):
    if index >= MAX:
        print("Tree is full.")
        return

    if tree[index] is None:
        tree[index] = value
        print(value, "inserted.")
        return

    if value < tree[index]:
        insert(value, 2 * index + 1)
    else:
        insert(value, 2 * index + 2)


def inorder(index=0):
    if index >= MAX or tree[index] is None:
        return

    inorder(2 * index + 1)
    print(tree[index], end=" ")
    inorder(2 * index + 2)


def preorder(index=0):
    if index >= MAX or tree[index] is None:
        return

    print(tree[index], end=" ")
    preorder(2 * index + 1)
    preorder(2 * index + 2)


def postorder(index=0):
    if index >= MAX or tree[index] is None:
        return

    postorder(2 * index + 1)
    postorder(2 * index + 2)
    print(tree[index], end=" ")


def level_order():
    for i in range(MAX):
        if tree[i] is not None:
            print(tree[i], end=" ")


def search(value, index=0):
    if index >= MAX or tree[index] is None:
        return False

    if tree[index] == value:
        return True

    if value < tree[index]:
        return search(value, 2 * index + 1)
    else:
        return search(value, 2 * index + 2)


def count_nodes(index=0):
    if index >= MAX or tree[index] is None:
        return 0

    return (1 + count_nodes(2 * index + 1)
            + count_nodes(2 * index + 2))


def count_leaf_nodes(index=0):
    if index >= MAX or tree[index] is None:
        return 0

    left = 2 * index + 1
    right = 2 * index + 2

    if ((left >= MAX or tree[left] is None)
            and (right >= MAX or tree[right] is None)):
        return 1

    return count_leaf_nodes(left) + count_leaf_nodes(right)


def height(index=0):
    if index >= MAX or tree[index] is None:
        return 0

    left_height = height(2 * index + 1)
    right_height = height(2 * index + 2)

    return 1 + max(left_height, right_height)


def display():
    print("\nArray Representation:")

    for i in range(MAX):
        if tree[i] is not None:
            print("Index", i, ":", tree[i])


while True:
    print("\n===== BINARY TREE USING ARRAY =====")
    print("1. Insert")
    print("2. Inorder Traversal")
    print("3. Preorder Traversal")
    print("4. Postorder Traversal")
    print("5. Level Order Traversal")
    print("6. Search")
    print("7. Count Nodes")
    print("8. Count Leaf Nodes")
    print("9. Height")
    print("10. Display Array")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        insert(value)

    elif choice == 2:
        print("Inorder:", end=" ")
        inorder()
        print()

    elif choice == 3:
        print("Preorder:", end=" ")
        preorder()
        print()

    elif choice == 4:
        print("Postorder:", end=" ")
        postorder()
        print()

    elif choice == 5:
        print("Level Order:", end=" ")
        level_order()
        print()

    elif choice == 6:
        value = int(input("Enter value to search: "))

        if search(value):
            print("Value found.")
        else:
            print("Value not found.")

    elif choice == 7:
        print("Total nodes:", count_nodes())

    elif choice == 8:
        print("Leaf nodes:", count_leaf_nodes())

    elif choice == 9:
        print("Height:", height())

    elif choice == 10:
        display()

    elif choice == 11:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")
