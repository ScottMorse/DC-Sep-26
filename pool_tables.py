import random
import getpass
from _pool import Room, Table, convert_time, closing
    
if __name__ == "__main__":

    print("#### Welcome to a Pool Room simulator ####")
    print("####    Enter 'view' to view tables   ####")
    print("####          Exit with 'q'           ####\n")

    while True:
        pswd = getpass.getpass("Password (hint: it's 'admin'):")
        if pswd == 'admin':
            break
    
    Room.init(12)

    print("\n#### Room initialized. Try viewing the tables ####")

    while True:

        user_input = input("\nEnter: ")

        if user_input == "close":
            closing()
            break

        if user_input == "q":
            check_close = input("Close the room as well? (y/n)")
            if check_close.lower().strip() == "y":
                closing()
                break
            else:


        if user_input == "view":
            for table in Room.tables:
                #randomizes whether state of any table will change
                rand = random.randint(0,4)
                if not rand:
                    if table.occupied:
                        #gives steeper chance for table to vacate if occupied
                        rand2 = random.randint(0,20)
                        if not rand2:
                            table.vacate()
                    else:
                        #table has 50% chance of becoming occupied
                        table.occupy()
            Room.view()
