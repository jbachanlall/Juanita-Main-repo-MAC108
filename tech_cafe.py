print (" Wecome to Byte & Brew tech cafe, PLEASE ENTER YOUR ORDER")
total_bill= 0.00
while True:
    print("1. Coffee - $3.00")
    print("2. Juice - $3.50")
    print("3. Coke - $1.50")
    print("4. Ice Latte - $4.50")
    print("5. Complete order")
    choice = input("Enter your choice: ")
    if choice == "1":
        total_bill += 3.00
        print("You have ordered Coffee, your current balance is $",total_bill)
    elif choice == "2":
        total_bill += 3.50
        print("You have ordered Juice, your current balance is $",total_bill)
    elif choice == "3":
        total_bill += 1.50
        print("You have ordered Coke, your current balance is $",total_bill)
    elif choice == "4":
        total_bill += 4.50
        print("You have ordered Ice Latte, your current balance is $",total_bill)
    elif choice == "5":
        print("Thank you for your order! Your total balance is $",total_bill)
        break
    else:
        print("Invalid choice. Please try again.")
print(f"total bill: ${total_bill}")
