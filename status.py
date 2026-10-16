import time
import psutil
from pypresence import Presence

client_id = "1560370365946003497"

RPC = Presence(client_id)
RPC.connect()

active = False

try:
    while True:
        running = False
        for proc in psutil.process_iter(['name']):
            try:
                if proc.info['name'] and proc.info['name'].lower() == 'taskmgr.exe':
                    running = True
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        if running:
            if not active:
                RPC.update(
                    state="Using Task Manager",
                    details="Task Manager",
                    start=time.time()
                )
                active = True
        else:
            if active:
                RPC.clear()
                active = False

        time.sleep(3)

except KeyboardInterrupt:
    RPC.close()