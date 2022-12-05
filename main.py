import flights

f = flights.Flights('f.dat')




while True: 
    print("*** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU")
    print()
    print("1. Add flight\n")
    print("2. Print flight schedule\n")
    print("3. Set flight schedule filename\n")
    print("9. Exit the program\n")
    print()

    choice = int(input("Enter menu choice: ")) 
    print()

    if choice == 1: 
        org = input("Enter Origin: ")
        dest = input("Enter Destination: ")
        num = input("Enter Flight Number: ")
        dep = input("Enter departure time (HHMM):")
        arr = input("Enter arrival time (HHMM):")
        next_day = input("Is arrival next day (Y/N):")

        f.add_flight(org, dest, num, dep, arr, next_day)
        print()

    elif choice == 2:
        fts=f.get_flights()
        print("================== FLIGHT SCHEDULE ==================\n") 
        print("Origin Destination Number Departure  Arrival Duration\n")
        print("====== =========== ====== ========= ======== ========")
        for x in fts: 
            org = x[0]
            dest = x[1]
            num = x[2]
            dep = x[3]
            arr = x[4]
            dur = x[5]
            print(f'{org:7}{dest:12}{num:>6}{dep:>10}{arr:>9}{dur:>9}')
            print()

    elif choice == 3: 
        fn = input("Enter the filename: ")
        f = flights.Flights(fn)
        print()

    elif choice == 9: 
        break