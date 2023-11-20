class FoodOrderingApp:
    def __init__(self):
        self.menu = {
            '1': {'dish': 'Burger', 'price': 60.0},
            '2': {'dish': 'Pizza', 'price': 120.0},
            '3': {'dish': 'Pasta', 'price': 100.0},
            '4': {'dish': 'Fries', 'price': 80.0},
            '5': {'dish': 'Salad', 'price': 45.0},
            '6': {'dish': 'Sandwich', 'price': 75.0},
            '7': {'dish': 'Chicken Wings', 'price': 110.0},
            '8': {'dish': 'Milkshake', 'price': 90.0},
        }
        self.order = []

    def display_menu(self):
        print("Our Menu:")
        for item_id, item_info in self.menu.items():
            print(f"{item_id}. {item_info['dish']} - Rs {item_info['price']}")

    def place_order(self):
        self.display_menu()
        while True:
            choice = input("Enter the number of the dish you'd like to order (type 'q' to quit): ")
            if choice.lower() == 'q':
                break
            elif choice in self.menu:
                try:
                    quantity = int(input(f"How many {self.menu[choice]['dish']}s would you like? "))
                    if quantity <= 0:
                        print("Please enter a valid quantity.")
                        continue
                    self.order.append({
                        'item': self.menu[choice]['dish'],
                        'quantity': quantity,
                        'price': self.menu[choice]['price'] * quantity
                    })
                    print(f"{quantity} {self.menu[choice]['dish']}(s) added to your order.")
                except ValueError:
                    print("Invalid input. Please enter a valid quantity.")
            else:
                print("Invalid choice. Please try again.")

    def remove_item(self):
        if not self.order:
            print("Your order is currently empty.")
        else:
            self.display_receipt()
            item_to_remove = input("Enter the number of the item you'd like to remove: ")
            if item_to_remove.isdigit() and 1 <= int(item_to_remove) <= len(self.order):
                removed_item = self.order.pop(int(item_to_remove) - 1)
                print(f"{removed_item['quantity']} {removed_item['item']}(s) removed from your order.")
            else:
                print("Invalid choice. Please enter a valid item number.")

    def display_receipt(self):
        if not self.order:
            print("Your order is currently empty.")
        else:
            total_price = sum(item['price'] for item in self.order)
            print("Your order is confirmed!")
            for item_index, item in enumerate(self.order, start=1):
                print(f"{item_index}. {item['item']} x{item['quantity']} - Rs {item['price']:.2f}")
            tax_rate = 0.1  # Assuming 10% tax rate
            tax_amount = total_price * tax_rate
            grand_total = total_price + tax_amount
            print(f"\nTax (10%): Rs {tax_amount:.2f}")
            print(f"Grand Total: Rs {grand_total:.2f}")

    def start(self):
        print("Welcome to the AIML Food !")
        while True:
            print("\n1. Place an order\n2. Remove item from order\n3. View receipt\n4. Quit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.place_order()
            elif choice == '2':
                self.remove_item()
            elif choice == '3':
                self.display_receipt()
            elif choice == '4':
                print("Thank you for using the AS Food Ordering App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = FoodOrderingApp()
    app.start()

'''Output

Welcome to the AS Food Ordering App!

1. Place an order
2. Remove item from order
3. View receipt
4. Quit
Enter your choice: 7
Invalid choice. Please try again.

1. Place an order
2. Remove item from order
3. View receipt
4. Quit
Enter your choice: 1
Our Menu:
1. Burger - Rs 60.0
2. Pizza - Rs 120.0
3. Pasta - Rs 100.0
4. Fries - Rs 80.0
5. Salad - Rs 45.0
6. Sandwich - Rs 75.0
7. Chicken Wings - Rs 110.0
8. Milkshake - Rs 90.0
Enter the number of the dish you'd like to order (type 'q' to quit): 7
How many Chicken Wingss would you like? 8
8 Chicken Wings(s) added to your order.
Enter the number of the dish you'd like to order (type 'q' to quit): 8
How many Milkshakes would you like? 8
8 Milkshake(s) added to your order.
Enter the number of the dish you'd like to order (type 'q' to quit): q

1. Place an order
2. Remove item from order
3. View receipt
4. Quit
Enter your choice: 3
Your order is confirmed!
1. Chicken Wings x8 - Rs 880.00
2. Milkshake x8 - Rs 720.00

Tax (10%): Rs 160.00
Grand Total: Rs 1760.00

1. Place an order
2. Remove item from order
3. View receipt
4. Quit
Enter your choice: 2
Your order is confirmed!
1. Chicken Wings x8 - Rs 880.00
2. Milkshake x8 - Rs 720.00

Tax (10%): Rs 160.00
Grand Total: Rs 1760.00
Enter the number of the item you'd like to remove: 2
8 Milkshake(s) removed from your order.

1. Place an order
2. Remove item from order
3. View receipt
4. Quit
Enter your choice: 3
Your order is confirmed!
1. Chicken Wings x8 - Rs 880.00

Tax (10%): Rs 88.00
Grand Total: Rs 968.00

1. Place an order
2. Remove item from order
3. View receipt
4. Quit
Enter your choice: 4
Thank you for using the AS Food Ordering App. Goodbye!'''