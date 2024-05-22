# https://docs.python.org/3/library/subprocess.html
import subprocess as proc
import random
import time


queue = []

while True:
    arg1 = "description"
    proc.call(("prog.exe", f"{arg1}"))
    buffer = random.randint(1, 5)
    time.sleep(buffer)


