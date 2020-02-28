import time
import os
import pandas


while True:
    if os.path.exists("temps.today.csv"):
        data = pandas.read_csv("temps.today.csv")
        print(data.mean)
    else:
        print("File does not exit")
    time.sleep(10)