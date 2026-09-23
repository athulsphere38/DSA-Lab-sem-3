stack = []
size = int(input("Enter stack size: "))

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        if len(stack) == size:
            print("Stack Overflow")
        else:
            data = int(input("Enter data: "))
            stack.append(data)

    elif ch == 2:
        if len(stack) == 0:
            print("Stack Underflow")
        else:
            print("Deleted:", stack.pop())

    elif ch == 3:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", stack[-1])

    elif ch == 4:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Stack:", stack)

    elif ch == 5:
        break

    else:
        print("Invalid choice")
