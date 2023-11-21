clients = {"name":"None", "company":"None","Investment":"None","InvestmentType":"None"}

name = input("Enter your Name : ")
company = input("Enter your Company : ")
investment = input("Enter your Investment : ")
investmentType = input("Enter the Type of Investment you want to do : ")

clients["name"] = name
# clients["name"] = input("Enter your Name : ")

clients["company"] = company
# clients["company"] = input("Enter your Company : ")

clients["Investment"] = investment
# clients["Investment"] = input("Enter the amount you asking for investment : ")

clients["InvestmentType"] = investmentType
# clients["InvestmentType"] = input("Enter the Type of Investment you want to do : ")

for key,value in clients.items():
    print(key," : ",value)
