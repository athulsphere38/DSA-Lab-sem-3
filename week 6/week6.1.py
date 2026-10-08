MAX = 5
queue = []

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(queue) == MAX:
            print("Queue Overflow")
        else:
            value = int(input("Enter value: "))
            queue.append(value)
            print(value, "inserted")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue Underflow")
        else:
            value = queue.pop(0)
            print(value, "deleted")

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Front element =", queue[0])

    elif choice == 4:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Queue elements:", queue)

    elif choice == 5:
        print("Program ended")
        break

    else:
        print("Invalid choice")
