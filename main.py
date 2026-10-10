while True:

    print("""STUDY PROGRESS TRACKER
1. Add a result
2. View all results
3. View subject average
4. Exit""")

    input_choice = input("Enter your choice (1-4): ")
    if input_choice == "1":
        print("Add a new result.")
    elif input_choice == "2":
        print("Displaying all results...")
    elif input_choice == "3":
        print("Calculating subject average...")
    elif input_choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
