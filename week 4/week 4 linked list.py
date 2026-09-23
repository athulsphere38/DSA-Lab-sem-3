class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None

while True:
    print("\n1. Create Linked List")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Insert at Specific Index")
    print("5. Delete by Value")
    print("6. Delete First Node")
    print("7. Delete Last Node")
    print("8. Count Nodes")
    print("9. Display")
    print("10. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        n = int(input("Enter number of nodes: "))
        head = None
        for i in range(n):
            data = int(input("Enter data: "))
            new = Node(data)
            if head is None:
                head = new
            else:
                temp = head
                while temp.next:
                    temp = temp.next
                temp.next = new

    elif ch == 2:
        data = int(input("Enter data: "))
        new = Node(data)
        new.next = head
        head = new

    elif ch == 3:
        data = int(input("Enter data: "))
        new = Node(data)

        if head is None:
            head = new
        else:
            temp = head
            while temp.next:
                temp = temp.next
            temp.next = new

    elif ch == 4:
        data = int(input("Enter data: "))
        pos = int(input("Enter index: "))

        new = Node(data)

        if pos == 0:
            new.next = head
            head = new
        else:
            temp = head
            for i in range(pos - 1):
                if temp is None:
                    break
                temp = temp.next

            if temp is None:
                print("Invalid index")
            else:
                new.next = temp.next
                temp.next = new

    elif ch == 5:
        data = int(input("Enter value to delete: "))

        if head is None:
            print("List is empty")
        elif head.data == data:
            head = head.next
        else:
            temp = head
            while temp.next and temp.next.data != data:
                temp = temp.next

            if temp.next is None:
                print("Value not found")
            else:
                temp.next = temp.next.next

    elif ch == 6:
        if head is None:
            print("List is empty")
        else:
            head = head.next

    elif ch == 7:
        if head is None:
            print("List is empty")
        elif head.next is None:
            head = None
        else:
            temp = head
            while temp.next.next:
                temp = temp.next
            temp.next = None

    elif ch == 8:
        count = 0
        temp = head

        while temp:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    elif ch == 9:
        if head is None:
            print("List is empty")
        else:
            temp = head
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

    elif ch == 10:
        print("Exited")
        break

    else:
        print("Invalid choice")
