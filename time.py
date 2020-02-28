import time


while True:
  with open("files/vegetable.txt") as file:
     print(file.read())
     time.sleep(2)