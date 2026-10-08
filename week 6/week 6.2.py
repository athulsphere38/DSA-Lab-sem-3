MAX = 5
queue = [None] * MAX

front = -1
rear = -1

while True:
    print("\n--- CIRCULAR QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        # Check if queue is full
        if (rear + 1) % MAX == front:
            print("Circular Queue Overflow")

        else:
            value = int(input("Enter value: "))

            # First element
            if front == -1:
                front = 0
                rear = 0
            else:
                rear = (rear + 1) % MAX

            queue[rear] = value

            print(value, "inserted")

    elif choice == 2:

        # Check if queue is empty
        if front == -1:
            print("Circular Queue Underflow")

        else:
            print(queue[front], "deleted")
            queue[front] = None

            # Only one element was present
            if front == rear:
                front = -1
                rear = -1

            else:
                front = (front + 1) % MAX

    elif choice == 3:

        if front == -1:
            print("Circular Queue is empty")
        else:
            print("Front element =", queue[front])

    elif choice == 4:

        if front == -1:
            print("Circular Queue is empty")

        else:
            print("Queue elements:", end=" ")

            i = front

            while True:
                print(queue[i], end=" ")

                if i == rear:
                    break

                i = (i + 1) % MAX

            print()

    elif choice == 5:
        print("Program ended")
        break

    else:
        print("Invalid choice")
