print("Robot Movement Control")
print("1. Forward  2. Backward  3. Left  4. Right  5. Stop")

choice = input("Enter choice (1-5): ")

if choice == '1':
    print("Robot Moving Forward")
elif choice == '2':
    print("Robot Moving Backward")
elif choice == '3':
    print("Robot Turning Left")
elif choice == '4':
    print("Robot Turning Right")
elif choice == '5':
    print("Robot Stopped")
else:
    print("Invalid Choice")
