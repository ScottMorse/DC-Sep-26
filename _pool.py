import time
import datetime

start_time = round(time.time())

history = {}

def convert_time(seconds):
    if seconds < 60:
        timestr = f"{seconds} sec"
    elif seconds < 3600:
        timestr = f"{seconds // 60} minutes, {seconds % 60} seconds"
    else:
        hours = seconds // 3600
        minutes = (seconds - 3600 * hours) // 60
        seconds = seconds - 3600 * hours - 60 * minutes
        timestr = f"{hours} hours, {minutes} minutes, {seconds} seconds"
    return timestr

class Room:
    
    tables = []

    initialized = False

    @classmethod
    def init(self,num_tables,load_state):
        for i in range(num_tables):
            Room.tables.append(Table(i + 1))
        Room.initialized = True
    
    @classmethod
    def view(self):
        for table in Room.tables:
            if not Room.initialized:
                print("Room not initialized.")
                return
        for table in Room.tables:
            if table.occupied:
                table.elapsed_seconds = round(time.time() - table.start_time)
                status = f"Occupied ({convert_time(table.elapsed_seconds)})"
            else:
                status = "Vacant"
            print(table,status)

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
        self.start_time = round(time.time())
        self.start_date = datetime.datetime.now()
    
    def vacate(self):
        if not self._occupied:
            return
        self._occupied = False

        self.end_time = round(time.time())
        self.end_date = datetime.datetime.now().ctime()
        self.seconds_elapsed = self.end_time - self.start_time

        timestr = convert_time(self.seconds_elapsed)
        cost = "${:,.2f}".format(round(30 * self.seconds_elapsed / 3600,2))

        log = {"Table": self.num, "Start": str(self.start_date),"End": str(self.end_date), "Time": timestr, "Cost": cost}
        history[f'Table {self.num}:{self.end_date}'] = [log]
    
    def __repr__(self):
        return f"<Table {self.num}>"

now = datetime.datetime.now().strftime("%H:%M:%S")

print(isinstance(now,str))