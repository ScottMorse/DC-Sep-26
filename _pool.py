import time
import datetime
import json
import os
import sys
import os
import smtplib

class Room:

    tables = []
    initialized = False

    @classmethod
    def init(self,num_tables,load_state):
        for i in range(num_tables):
            Room.tables.append(Table(i + 1))
        if not load_state:
            with open("table_history.json","w") as j:
                j.write("{\n\t")

        Room.initialized = True
    
    @classmethod
    def view(self):
        if not Room.initialized:
            print("Room not initialized. ( Room.init() )")
            return
        for table in Room.tables:
            if table._loaded:
                elapsed = round(time.time(),2) + abs(table.start)
            elif not table._loaded and table.occupied:
                elapsed = round(time.time()) - table.start
            print(table,f": Occupied ({convert_time(elapsed)})" if table.occupied else ": Vacant")
    
    @classmethod
    def close_room(self):
        check = input("Are you sure? (y/n)")
        if check.lower().strip() == "y":
            for i in range(len(Room.tables)):
                Room.tables[i].vacate()
            with open("table_history.json","ab") as j:
                j.seek(-3, os.SEEK_CUR)
                j.truncate()
                j.write('\n}'.encode())

def convert_time(seconds):
    if seconds < 60:
        timed = f"{seconds} sec"
    elif seconds < 3600:
        timed = f"{seconds // 60} minutes, {seconds % 60} seconds"
    else:
        hours = seconds // 3600
        minutes = (seconds - 3600 * hours) // 60
        seconds = seconds - 3600 * hours - 60 * minutes
        timed = f"{hours} hours, {minutes} minutes, {seconds} seconds"
    return timed

class Table:

    def __init__(self,num):
        self._occupied = False
        self._num = num
        self._loaded = False
    
    @property
    def occupied(self):
        return self._occupied
    
    @property
    def num(self):
        return self._num
    
    def occupy(self):
        self._occupied = True
        self.start = round(time.time())
        self.starting_time = datetime.datetime.now()

    
    def vacate(self):
        if not self._occupied:
            return
        self._occupied = False
        self.end = round(time.time())
        self.ending_time = datetime.datetime.now()
        self.seconds_elapsed = self.end - self.start
        timed = convert_time(self.seconds_elapsed)
        cost = "${:,.2f}".format(round(30 * self.seconds_elapsed / 3600,2))
        log = {"Table": self.num, "Start": str(self.starting_time),"End": str(self.ending_time), "Time": timed, "Cost": cost}

        with open('table_history.json',"a") as j:
            j.write(f'"Table {self.num}:{self.ending_time}": ')
        with open('table_history.json',"a") as j:
            json.dump(log,j)
        with open('table_history.json',"a") as j:
            j.write(",\n\t")

    
    def __repr__(self):
        return f"<Table {self.num}>"

def closing():
    Room.close_room()
    email_check = input("Send email of table sales? (y/n)")
    if email_check.lower().strip() == "y":
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login("scottthrowaway314@gmail.com","password314")
        with open("table_history.json") as f:
            read = f.read()
            server.sendmail("scottthrowaway314@gmail.com","scottmorseguitar@yahoo.com",read)
            server.quit()
    print("\n#### Goodbye! ####")