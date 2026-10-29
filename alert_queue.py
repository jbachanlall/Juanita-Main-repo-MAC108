
alert_queue = []

while True:
    # Main Menu Options:
    print("1. Log New Alert")
    print("2. View Active Queue")
    print("3. Resolve Oldest Alert")
    print("4. Exit System")

    choice = input("Select option [1-4]: ")

    if choice == "1":
        # user enter threat 
        new_alert = input("Enter threat description: ")
        # Append to end of alert queue
        alert_queue.append(new_alert)
        
        print("Alert logged successfully!")

    elif choice == "2":
        print("--- Current Pending Alerts ---")
        for alert in alert_queue:
            print(alert)

    elif choice == "3":
        
        if len(alert_queue) > 0:
            
            resolved_threat = alert_queue.pop(0)
            
            print(f"Resolved and cleared: {resolved_threat}")
        else:
            print("This queue is empty. There are no alerts to resolve.")

    elif choice == "4":
        print("Exiting system...")
        break

    else:
        print("Invalid option. Please enter a number from 1 to 4.")
