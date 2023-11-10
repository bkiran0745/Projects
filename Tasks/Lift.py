import time

print('-----------------Lift Operations-----------------')
while True:
    g_floor = 0
    print(" 0. Ground Floor")
    print(" 1. First Floor")
    print(" 2. Second Floor")
    print(" 3. Third Floor")
    print(" 4. Fourth Floor")
    print(" 5. Fifth Floor \n")
    ch = int(input("Enter your Choice : "))
    print("Please wait for a moment...\n")

    while (ch <= 5):
        if (ch == 1):
            print()
            print("Moving to the first floor...\n")
            # g_floor += 1
            time.sleep(3)
            print("Arrived to First Floor...\n")
            g_floor = 1
            break
        elif ch == 2:
            print()
            print("Moving to second floor...\n")
            # g_floor += 2
            time.sleep(4)
            print("Arrived to Second Floor...\n")
            g_floor = 2
            break
        elif ch == 3:
            print()
            print("Moving to Third floor...\n")
            # g_floor += 3
            time.sleep(5)
            print("Arrived to Third Floor...\n")
            g_floor = 3
            break
        elif ch == 4:
            print()
            print("Moving to fourth floor...\n")
            # g_floor += 4
            time.sleep(6)
            print("Arrived to Fourth Floor...\n")
            g_floor = 4
            break
        elif ch == 5:
            print()
            print("Moving to fifth floor...\n")
            # g_floor += 5
            time.sleep(7)
            print("Arrived to Fifth Floor...\n")
            g_floor = 5
            break
        else:
            print("Invalid choice")
            # print("I wish you to reach higher than the size of the building, Please Enter in 0-5 \n")
            break
        