customer_details = []
def t_movie():
    
    print("which movie do you want to watch?")
    print("1: Javan")
    print("2: KGF")
    print("3: Leo")
    print("4: Back")
    movie = int(input("Choose your movie(from 1 to 4): "))
    if movie == 4:
        center()
        exit
    if movie in[1,2,3]:
        theater()
    else:
        print("Wrong choice. Please choose the correct option.")   

def theater():
    while(1):
        print("Which class do you want to watch the movie?")
        print("1: Platinum ------> 400RS")
        print("2: Gold     ------> 250RS")
        print("3: Recliner ------> 600RS")
        print("4. Quit")
        a = int(input("Choose your class(from 1 to 3): "))
        if a in [1, 2, 3]:
            Ticket(a)
        elif(a == 4):
            break
        else:
            print("Wrong choice. Please choose the correct option.")
        

def Ticket(a):
    ticket = int(input("Number of tickets do you want?: "))
    if(a == 1):
        total_amount = ticket * 400
    elif(a == 2):
        total_amount = ticket * 250
    else:
        total_amount = ticket * 600
    timing(a, total_amount, ticket)

def timing(a, total_amount, ticket):
    print(f"Your total amount is {total_amount} rs. \n\n\tEnjoy the movie!")
    theater()

def time(total_amount):
    print("Enter your details... ")
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")
    customer_details.append({
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Total Amount": total_amount
    })
    display_customer_details(customer_details)

def timing(a, total_amount, ticket):
    print("Select your time:")
    print("1: Morning show - 10.00-1.00")
    print("2: Afternoon show - 1.10-4.10")
    print("3: Evening show - 4.20-7.20")
    print("4: Night show - 7.30-10.30")
    Time = int(input("Choose your option: "))
    if Time in [1, 2, 3, 4]:
        while(ticket != 0):
            time(total_amount)
            ticket -= 1
        if(ticket == 0):
            print(f"Total Amount: {total_amount} Rs")
            print("Booking successful..! enjoy the movie")
    else:
        print("Wrong choice. Please choose the correct option.")
        timing(a, total_amount)

def movie(theater):
    if theater in [1, 2, 3]:
        t_movie()
    elif theater == 4:
        exit
    else:
        print("Wrong choice")
        movie(theater)

def center():
    print("Which theater do you wish to see the movie?")
    print("1: Inox")
    print("2: Icon")
    print("3: PVP")
    print("4: Back")
    a = int(input("Choose your option: "))
    movie(a)

def city():
    print("Hi, welcome to movie ticket booking:")
    print("Where do you want to watch the movie?")
    print("1: Bangalore")
    print("2: Hyderabad")
    print("3: Chennai")
    place = int(input("Choose your option: "))
    if place in [1, 2, 3]:
        center()
    else:
        print("Wrong choice please choose the correct option")

def display_customer_details(details):
    print("\nCustomer Billing Details:")
    for i, customer in enumerate(details):
        print(f"Customer {i + 1}:")
        print(f"Name: {customer['Name']}")
        print(f"Email: {customer['Email']}")
        print(f"Phone: {customer['Phone']}")

city()