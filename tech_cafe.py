print (" Wecome to Byte & Brew tech cafe, PLEASE ENTER YOUR ORDER")
total_bill= 0.00

menu_item = ["1. Coffee - $3.00", "2. Juice - $3.50", "3. Coke - $1.50", "4. Ice Latte - $4.50", "5. Complete order"]


while True:  
    menu_item = input("Enter your choice: ")
    if menu_item == "1":
        total_bill += 3.00
        print("You have ordered Coffee, your current balance is $",total_bill)
        print("would you like to add another item? (yes/no):")
        add_item = input().lower()
        if add_item == "yes":
            print("add item")
        
        if add_item == "no":
            print("Thank you for your order! Your total balance is $",total_bill)
            break

    elif menu_item == "2":
        total_bill += 3.50
        print("You have ordered Juice, your current balance is $",total_bill)
    elif menu_item == "3":
        total_bill += 1.50
        print("You have ordered Coke, your current balance is $",total_bill)
    elif menu_item == "4":
        total_bill += 4.50
        print("You have ordered Ice Latte, your current balance is $",total_bill)
    elif menu_item == "5":
        print("Thank you for your order! Your total balance is $",total_bill)
        break
    else:
        print("Invalid choice. Please try again.")

    if menu_item == input("would you like to add another item? (yes/no): "):
        if menu_item == yes:
            print("add item")



print(f"Your Total bill: ${total_bill:.2f}")
