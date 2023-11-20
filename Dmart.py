print("-----------D-Mart----------")
poin=0
count = 0
overalllist=[]
overlistprize=[]
def Shopping():
    while(True):
        print("---------------------------")
        print("     1️⃣.Kitchen Item's 🍴")
        print("     2️⃣.Fashion 🥋")
        print("     3️⃣.Grooming 📱")
        print("     4️⃣.Exit  🙏🏻 ☞")
        print("---------------------------")
        def Kitchen():
            kilist=["kinves","Cutting Boards","spoons"]
            kiprlist=[1,0.5,0.6]
            while(True):
                print("---------------------------")
                print("         1️⃣.kinves 🔪")
                print("         2️⃣.Utensils 🍽️")
                print("         3️⃣.Spoons 🥄")
                print("---------------------------")
                x=int(input("Enter You'r Choice: "))
                if(x==1):
                    overalllist.append(kilist[0])
                    print("         Price:1₹")
                    a1=int(input("Enter the Number of Quantity:"))
                    print("     The price is :" ,(a1*1),"₹")
                    overlistprize.append((a1*kiprlist[0]))
                    #poin=poin+1
                    op1=input("Do you Want To Proceed Further Or No(y/n)")
                    if(op1=="n"):
                        print("     Thank You..!")
                        print("---------------------")
                        break
                elif(x==2):
                    overalllist.append(kilist[1])
                    print("price:100 ₹")
                    a2=int(input("Enter the Number of Quantity:"))
                    print("The price is :" ,(a2*0.5),"₹")
                    overlistprize.append((a1*kiprlist[1]))
                    op1=input("Do you Want To Proceed Further Or No(y/n)")
                    if(op1=="n"):
                        print("     Thank You..!")
                        print("---------------------")
                        break
                elif(x==3):
                    overalllist.append(kilist[2])
                    print("price:0.6$")
                    a3=int(input("Enter the Number of Quantity:"))
                    print("The price is :" ,(a3*0.6))
                    overlistprize.append((a1*kiprlist[2]))
                    op1=input("Do you Want To Proceed Further Or No(y/n)")
                    if(op1=="n"):
                        print("     Thank You..!")
                        print("---------------------")
                        break
                else:
                    print("please choose the right option. ")      
        def Fashion():
            while(True):
                print("---------------------------")
                print("     1.Shirt 👕")
                print("     2.Pant 👖")
                print("     3.Saree  🥻")
                print("---------------------------")
                y=int(input("Enter You'r Choice:"))
                if(y==1):
                    print(" Per Piece Price:3$")
                    a=int(input("Enter the Number of Quantity:"))
                    print("The price is :" ,(a*3))
                    op1=input("Do you Want To Proceed Further Or No(y/n)")
                    if(op1=="n"):
                        print("     Thank You..!")
                        print("---------------------")
                        break
                elif(y==2):
                    print("price:4$")
                    a=int(input("Enter the Number of Quantity:"))
                    print("The price is :" ,(a*4))
                    op1=input("Do you Want To Proceed Further Or No(y/n)")
                    if(op1=="n"):
                        print("     Thank You..!")
                        print("---------------------")
                        break
                    print("Thank You..!")
                    break
                elif(y==3):
                    print("price:6$")
                    a=int(input("Enter the Number of Quantity:"))
                    print("The price is :" ,(a*6))
                    op1=input("Do you Want To Proceed Further Or No(y/n)")
                    if(op1=="n"):
                        print("     Thank You..!")
                        print("---------------------")
                        break
                    print("Thank You..!")
                    break
                else:
                    print("please choose the right option. ")
            
        def Grooming():
            while(True):
                print("---------------------------")
                print("     1.Comb 🪮")
                print("     2.Face Cream 🧴")
                print("     3.Shampoo 🧴")
                print("---------------------------")
                z=int(input("Enter You'r Choice:"))
                if(z==1):
                    print("Price:0.6$")
                    print("Thank You..!")
                    break
                elif(z==2):
                    print("price:1$")
                    print("Thank You..!")
                    break
                elif(z==3):
                    print("price:1$")
                    print("Thank You..!")
                    break
                else:
                    print("please choose the right option. ")
        b=int(input("Enter you'r choice:"))
        if(b==1):
            Kitchen()
        elif(b==2):
            Fashion()
        elif(b==3):
            Grooming()
        elif(b==4):
            break
        else:
            print("please choose the right option. ")
def Verification():
    pass
def billing():
    z=0        
    for i in overalllist:
        print(i+"   ",overlistprize[z])
        z+=1
while (True):
    print("---------------------------")
    print("     1️⃣.Shopping 🛒")
    print("     2️⃣.Verification 🔍")
    print("     3️⃣.Billing 🧾")
    print("---------------------------")
    c=int(input("Enter you'r Choice: "))
    if(c == 1):
        count = 1
        Shopping()
    elif(c==2):
        if count == 0:
            print("Your cart is Empty, For Verification....")
            print("Please do Shopping First...!")
        else:
            Verification()
    elif(c==3):
        if count == 0:
            print("Your cart is Empty for, Billing...")
            print("Please do Shopping First...!")
        else:
            billing()
    else:
        print("Please choose the right option🧐")