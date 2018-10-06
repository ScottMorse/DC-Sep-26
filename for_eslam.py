class PoolTable:

    #When you make a new PoolTable instance, it ALWAYS needs table_number to create it
    def __init__(self,table_number):
        #All of these are what every NEW PoolTable instance gets:
        self.table_number = table_number # You need to give each table a table number
        self.occupied = False # All tables start as not occupied until people start playing
        self.time_started = None # No game has started on a new table
        self.time_ended = None # No game has ended on a new table

    def start_game(self,time_started):
        self.occupied = True # When you call this function on a PoolTable instace, it makes it occupied
        self.time_started = time_started # Saves the time the game started in self.time_started

    def end_game(self, time_ended):
        self.occupied = False # When the game ends, the occupied property goes back to False
        self.time_ended = time_ended # Saves the time the game ended in self.time_ended
    
    def __repr__(self):
        return f"<Table {self.table_number}>"

#creating 12 table objects in a list to make them easy to get.  Each one is an instance with a table_number (for the __init__)
#You could write these with a one-line for loop too:
#table_list = []
#[table_list.append(PoolTable(i)) for i in range(1,13)]
table_list = [
    PoolTable(1),
    PoolTable(2),
    PoolTable(3),
    PoolTable(4),
    PoolTable(5),
    PoolTable(6),
    PoolTable(7),
    PoolTable(8),
    PoolTable(9),
    PoolTable(10),
    PoolTable(11),
    PoolTable(12),
]


#just a general function for viewing the tables and their status, without needing a class
def view_tables():
    for table in table_list:
        print(table,"Occupied" if table.occupied else "Vacant")
        #table.occupied comes from self.occupied.  Each 'table' in table_list is a PoolTable object with an occupied property


#function to see a PoolTable instance's starting or ending time.  It needs the table_num to know which object to look at
def view_table_time(table_num):
    #finds the object from the list using the list index
    table = table_list[table_num - 1]
    
    if table.occupied:
        print(f"Game started at {table.time_started}")
    else:
        if table.time_ended == None:
            print("No games played for this table.")
        else:
            print(f"Game ended at {table.time_ended}")


#Instead of a PoolTableManager class, here is just the user input:

while True:

    print("""\nCommands:
    'view': view all tables
    'view table time': view a table's time
    'start game': start a table game
    'end game': end a table game
    'q': quit the program
    """)

    user_input = input("\nEnter a command: ")

    if user_input == "q":
        print("Goodbye")
        break
    
    elif user_input == 'view':
        view_tables() # This function just prints all the tables, doesn't need arguments

    elif user_input == 'view table time':
        user_input_stage_2 = input("Enter table number: ") #Needs to know which table
        view_table_time(int(user_input_stage_2)) #This function needs the table number from the user

    elif user_input == "start game":
        user_input_stage_2 = input("Enter table number: ")
        user_input_stage_3 = input("Enter time game started: ")
        list_index = int(user_input_stage_2) - 1 # converts the user string number into the index used for the list (needs to be 1 less for index)
        table = table_list[list_index] # finds the correct PoolTable instance from the list
        table.start_game(user_input_stage_3) # Uses the PoolTable instance's method start_game() to start the game, which needs the starting time.  
        #Try using command 'view' after
    
    elif user_input == "end game":
        #same as previous elif statement, just with the end_game() method instead of the start_game()
        user_input_stage_2 = input("Enter table number: ")
        user_input_stage_3 = input("Enter time game ended: ")
        list_index = int(user_input_stage_2) - 1
        table = table_list[list_index]
        table.end_game(user_input_stage_3)