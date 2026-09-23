class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


top = None

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        data = int(input("Enter data: "))
        new = Node(data)

        new.next = top
        top = new

    elif ch == 2:
        if top is None:
            print("Stack Underflow")
        else:
            print("Deleted:", top.data)
            top = top.next

    elif ch == 3:
        if top is None:
            print("Stack is empty")
        else:
            print("Top element:", top.data)

    elif ch == 4:
        if top is None:
            print("Stack is empty")
        else:
            temp = top
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    elif ch == 5:
        break

    else:
        print("Invalid choice")
