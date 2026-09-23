class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None
tail = None

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
    print("10. Display Head and Tail")
    print("11. Print Data from Tail to Head")
    print("12. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        n = int(input("Enter number of nodes: "))
        head = None
        tail = None

        for i in range(n):
            data = int(input("Enter data: "))
            new = Node(data)

            if head is None:
                head = new
                tail = new
                new.next = head
            else:
                tail.next = new
                tail = new
                tail.next = head

    elif ch == 2:
        data = int(input("Enter data: "))
        new = Node(data)

        if head is None:
            head = new
            tail = new
            new.next = head
        else:
            new.next = head
            head = new
            tail.next = head

    elif ch == 3:
        data = int(input("Enter data: "))
        new = Node(data)

        if head is None:
            head = new
            tail = new
            new.next = head
        else:
            tail.next = new
            tail = new
            tail.next = head

    elif ch == 4:
        data = int(input("Enter data: "))
        pos = int(input("Enter index: "))
        new = Node(data)

        if pos == 0:
            new.next = head
            head = new
            tail.next = head

        else:
            temp = head

            for i in range(pos - 1):
                if temp == tail:
                    break
                temp = temp.next

            if temp == tail and pos > 1:
                print("Invalid index")
            else:
                new.next = temp.next
                temp.next = new

                if temp == tail:
                    tail = new

    elif ch == 5:
        data = int(input("Enter value to delete: "))

        if head is None:
            print("List is empty")

        elif head.data == data:
            if head == tail:
                head = None
                tail = None
            else:
                head = head.next
                tail.next = head

        else:
            temp = head

            while temp.next != head and temp.next.data != data:
                temp = temp.next

            if temp.next == head:
                print("Value not found")
            else:
                if temp.next == tail:
                    tail = temp
                temp.next = temp.next.next
                tail.next = head

    elif ch == 6:
        if head is None:
            print("List is empty")

        elif head == tail:
            head = None
            tail = None

        else:
            head = head.next
            tail.next = head

    elif ch == 7:
        if head is None:
            print("List is empty")

        elif head == tail:
            head = None
            tail = None

        else:
            temp = head

            while temp.next != tail:
                temp = temp.next

            tail = temp
            tail.next = head

    elif ch == 8:
        count = 0

        if head is not None:
            temp = head

            while True:
                count += 1
                temp = temp.next

                if temp == head:
                    break

        print("Number of nodes:", count)

    elif ch == 9:
        if head is None:
            print("List is empty")
        else:
            temp = head

            while True:
                print(temp.data, end=" -> ")
                temp = temp.next

                if temp == head:
                    break

            print("(Head)")

    elif ch == 10:
        if head is None:
            print("List is empty")
        else:
            print("Head:", head.data)
            print("Tail:", tail.data)

    elif ch == 11:
        if head is None:
            print("List is empty")
        else:
            arr = []
            temp = head

            while True:
                arr.append(temp.data)
                temp = temp.next

                if temp == head:
                    break

            for i in range(len(arr) - 1, -1, -1):
                print(arr[i], end=" -> ")

            print("(Head)")

    elif ch == 12:
        print("Exited")
        break

    else:
        print("Invalid choice")
