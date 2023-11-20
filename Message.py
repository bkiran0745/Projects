Message = {}
def send(sender, receiver, message):
    if receiver not in Message:
        Message[receiver] = []
    Message[receiver].append((sender, message))
def view(user):
    if user in Message:
        print(f"Messages for {user}:")
        for sender, message in Message[user]:
            print(f"{sender}: {message}")
    else:
        print("No messages for this user.")
while True:
    print("1. Send Message")
    print("2. View Messages")
    print("3. Exit")
    e = input("Enter your choice: ")

    if e == "1":
        sender = input("Enter your name: ")
        receiver = input("Enter receiver's name: ")
        message = input("Enter your message: ")
        send(sender, receiver, message)
        print("Message sent!")

    elif e == "2":
        user = input("Enter your name to view messages: ")
        view(user)

    elif e == "3":
        print("Exiting the messaging system. Goodbye!")
        break
    else:
        print("Invalid choice.")
