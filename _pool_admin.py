import _pool
import getpass
import sys
import time
import select
import os
import random
import smtplib
import json

def init():
    print("#### Welcome to the Pool Room ####")
    print("####     'Enter' to quit    ####\n")

    pswd = ' '
    while pswd != "admin":
        pswd = getpass.getpass("Password (hint: it's 'admin'): ")
        if pswd == '':
            sys.exit()

    _pool.Room.init(12,True)

    with open('state.json') as s:
        read = s.read()
    if read:
        load = json.load(open('state.json'))
        last_time = load["end"]
        for table_key in load:
            if table_key != "end":
                table = _pool.Room.tables[int(table_key) - 1]
                table.occupy()
                table.start_time -= load[table_key] - round(last_time - time.time())

def timeout_input(timeout, prompt="", timeout_value=None):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    ready, _, _ = select.select([sys.stdin], [], [], timeout)
    if ready:
        return sys.stdin.readline()
    else:
        sys.stdout.flush()
        return timeout_value

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("scottthrowaway314@gmail.com","password314")
    with open("daily-log.json") as f:
        read = f.read()
        server.sendmail("scottthrowaway314@gmail.com","scottmorseguitar@yahoo.com",read)
        server.quit()

def run():
    init()
    i = 0
    hello = None
    while i<10:

        os.system('cls' if os.name == 'nt' else 'clear')

        print("#### 'Enter' to quit ####\n")

        _pool.Room.view()

        for table in _pool.Room.tables:
            #randomizes whether state of any table will change
            rand = random.randint(0,50)
            if not rand:
                if table.occupied:
                    #gives steeper chance for table to vacate if occupied
                    rand2 = random.randint(0,50)
                    if not rand2:
                        table.vacate()
                else:
                    #table has 50% chance of becoming occupied
                    table.occupy()

        hello = timeout_input(1,prompt="\nEnter: ")
        if hello == '\n':
            break


