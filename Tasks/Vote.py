# voting system in python

while True:
    print("Welcome to the Voting System")
    name = input("Enter your Name : ")
    age = int(input("Enter Your Age : "))
    if 18 <= age < 60:
        print("\n\tVOTING SYSTEM MENU \n" + "-" * 50)
        print("1. Register for vote")
        print("2. Cast your vote")
        print("3. View Result")
        print("4. Exit")
        choice = int(input("Enter your Choice (1/2/3/4): "))
        if choice == 1:
            global voter_list
            voters = []
            if 18 <= age < 60:
                voters.append([name,age])
                print("Registration Successful!")
                continue
            else:
                print("Invalid Entry, Please Enter a Valid Age between 18 and 59 years.")
                print("\n\tREGISTRATION MENU \n" + "-" * 24)
                continue
        elif choice == 2:
            candidates = ["A","B","C"]
            votes = [0]*len(candidates)
            print("\n\tCAST YOUR VOTE MENU \n" + "-"*24)
            print("Choose Candidate from below list:")
            for i in range(len(candidates)):
                print(f"{i+1}. {candidates[i]}")
                choice = int(input("Enter your Choice (1-3): "))
                candidate = candidates[choice - 1]
                votes[choice - 1] += 1
                print("Your vote has been recorded successfully!")
                print("\nDo you want to cast another vote? (y/n)")
                choice = str(input()).lower().strip()
                if choice == 'y':
                    break
        elif choice == 3:
            candidates = ["A","B","C"]
            votes = []
            print("\n\tRESULTS VIEWER MENU \n" + "-"*24)
            print("Name of the Candidate".ljust(20),"Number of Votes")
            for i in range(len(candidates)):
                print(f"{candidates[i].ljust(20)}{votes[i]}")
                print("\nEnd of Result")
        elif choice == 4:
            exit()
        else:
            print("Invalid Option! Try Again...")
            print("\n\tVOTING SYSTEM MENU \n" + "-" * 24)
            continue
    else:
        print("Invalid Entry, Please Enter a Valid Age between 18 and 59 years.")