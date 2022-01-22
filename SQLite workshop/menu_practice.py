# Nested menu


main_choice = None
while main_choice != "4":
    # Main Menu
    print("\nMain Menu")
    print("1 Option 1")
    print("2 Option 2")
    print("3 Option 3")
    print("4 Quit\n")
    main_choice = input("> ")

    if main_choice == "1":
        print("This is option 1 from the main menu")
    elif main_choice == "2":
        print("This is option 2 from the main menu")
    elif main_choice == "3":
        sub_choice_1 = None
        while sub_choice_1 != "3":
            print("\nSub Menu 1")
            print("1 Option 1")
            print("2 Option 2")
            print("3 Quit\n")
            sub_choice_1 = input("> ")

            if sub_choice_1 == "1":
                print("This is option 1 from sub menu 1")
            elif sub_choice_1 == "2":
                print("This is option 2 from sub menu 1")
        print("Exited out of Sub menu 1")
        continue     

print("End of program")