import random
import getpass
from _pool import Room, Table, json, time, datetime, convert_time, closing
    
if __name__ == "__main__":

    print("#### Welcome to a Pool Room simulator ####")
    print("####    Enter 'view' to view tables   ####")
    print("####          Exit with 'q'           ####\n")

    while True:
        pswd = getpass.getpass("Password (hint: it's 'admin'):")
        if pswd == 'admin':
            break
    
    Room.init(12)

    load_state = False

    with open('state.json') as f:
        read = f.read()
        if read:
            load_state = True

    if load_state:
        old_state = json.loads(open("state.json","r").read())

        with open('time-left.txt') as f:
            timestr = f.read()[11:18]
            chours, cminutes, cseconds = (datetime.datetime.now().hour,datetime.datetime.now().minute,datetime.datetime.now().second)
            hours, minutes, seconds = timestr.split(":")
            hours, minutes, seconds = (int(hours),int(minutes),int(seconds))
            seconds_elapsed = 0
            if chours > hours:
                seconds_elapsed_while_gone = (chours - hours) * 3600
            if cminutes > minutes:
                seconds_elapsed += (cminutes - minutes) * 60
            else:
                seconds_elapsed -= (minutes - cminutes) * 60
            if cseconds > seconds:
                seconds_elapsed += cseconds - seconds
            else:
                seconds_elapsed -= seconds - cseconds

        for key in old_state:
            Room.tables[int(key) - 1].occupy()
            Room.tables[int(key) - 1].start -= round(old_state[key],2) - seconds_elapsed
            



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
                state = {}
                for table in Room.tables:
                    if table.occupied:
                        table_state_time = round(time.time() - table.start)
                        state[table.num] = table_state_time
                with open('state.json','w') as j:
                    json.dump(state,j)
                with open('time-left.txt','w') as f:
                    f.write(str(datetime.datetime.now()))
                break

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
