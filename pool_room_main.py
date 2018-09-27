import _pool_admin
import _pool
import json
import time

_pool_admin.run()

check = input("Close the room? (y/n)")

if check.lower().strip() == "y":
    for table in _pool.Room.tables:
        table.vacate()

    with open('daily-log.json','w') as j:
        json.dump(_pool.history,j,indent=2)

    email = input("Send daily log to email? (y/n)")
    if email.lower().strip() == "y":
        _pool_admin.send_mail()

    open('state.json','w').close()

else:
    state = {"end": time.time()}
    for table in _pool.Room.tables:
        if table.occupied:
            elapsed_seconds = round(time.time() - table.start_time)
            state[table.num] = elapsed_seconds
    with open('state.json','w') as j:
        json.dump(state,j,indent=2)