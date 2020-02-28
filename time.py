import time
import os

while True:
  with open("files/vegetables.txt") as file:
     print(file.read())
     time.sleep(2)