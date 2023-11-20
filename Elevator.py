import time
op=0
while(True):
    count=op
    print("0.ground floor")
    print("1.first floor")
    print("2.second floor")
    print("3.third floor")
    print("4.fourth floor")
    print("5.fifth floor")
    print("6.Exit")
    c1=(input("Enter your choice(Enter range with in 0 to 5): "))
    try:
        c=int(c1)
    except:
        print("Plese Enter the numeric value")
        continue
    if(c==6):
        print("Have a good day.....  ")
        break
    if(c>5):
        print("-------------------------------------------\n")
        print("Rey Kanna Bondam Input Sariga Ivvu Ra Nana \n")
        print("-------------------------------------------\n")
        c=op
    op=c
    if(c<=5):
        if(count<=op):
            while(count!=c):
                print("entried to ",count,"Floor")
                count+=1
                time.sleep(1)
                print("entering to ",count,"Floor")
                time.sleep(1)
        else:
            op1=op+1
            #if (count>5):
                #count=op1
            while(count>=op1):
                    time.sleep(1)
                    print("entried to ",count," Floor")
                    count-=1
                    if(count!=op1):
                        print("entering to ",count,"Floor")
                    time.sleep(1)
    else:
        print("-------------------------------------------\n")
        print("Rey Kanna Bondam Input Sariga Ivvu Ra Nana \n")
        print("-------------------------------------------\n")
    if(count==c):        
        if(c1=='0'):   print(" Arrived to ground floor..\n")
        elif(c1=='1'): print(" Arrived to first floor..\n")
        elif(c1=='2'): print(" Arrived to second floor..\n")
        elif(c1=='3'): print(" Arrived to Third Floor..\n")
        elif(c1=='4'): print(" Arrived to fourth floor..")
        elif(c1=='5'): print(" Arrived to fifth floor..\n")
        