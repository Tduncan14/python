import time
import os

while True:
    if os.path.exists("files/vegetables.txt"):
     with open("files/vegetable.txt") as file:
         print(file.read())
    else:
        print('files doesnt exit')

    time.sleep(10)
    


