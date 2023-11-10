import time

print("--------------Password Generator-----------------")
counter = 0 
while True:
    createdPassword = input("Enter your Password of 8 character's To Create : \n")
    if(len(createdPassword)!=8):
        print("Password should be of 8 characters")
        break
    confirmPassword = input("Enter your Confirm Password : \n")
    password_length = len(createdPassword)

    if createdPassword == confirmPassword and password_length == 8:
        print("Password Matchhed Successfully...!🥳")
        
        while counter <= 5:
            password = input("Enter your Password:\n")
            if password_length == len(password) and password == createdPassword:
                print("Welcome to Home 🏠 || Login SuccessFull 🥳")
                break
            else:
                print("Incorrect Password ❌ , Please Enter again")
            counter += 1
            if counter == 5:
                print("You have entered wrong password for 5 times, Please try again after 30 seconds.")
                for i in range(30,0,-1):
                    print(i)
                    time.sleep(1)
        break
    else:
        print("Password Didn't Match ❌, Please Re-Enter your Password...")