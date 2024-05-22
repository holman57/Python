# https://docs.python.org/3/library/subprocess.html
import subprocess as proc
from datetime import datetime
import random
import time


jobs = [
    {"id": 0, "priority": 1, "call": "prog.exe", "args": ["arg1", "arg2"], "state": "wait"},
    {"id": 1, "priority": 2, "call": "prog2.exe", "args": ["arg1"], "state": "wait"},
    {"id": 2, "priority": 1, "call": "prog.exe", "args": ["arg1"], "state": "wait"}
]

while True:
    if len(jobs) > 0:
        j = jobs.pop(0)
        jid, jp, jcall, jargs, jstate = j["id"], j["priority"], j["call"], j["args"], j["state"]
        proc.call((jcall, f"{jargs[0]}"))
    buffer = random.randint(1, 5)
    time.sleep(buffer)
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    print("date and time =", dt_string)

