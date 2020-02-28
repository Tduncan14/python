with open("files/fruits.txt","a") as myfile:
    myfile.write('\nChicken')


with open("files/fruits.txt") as myfile:
    content = myfile.read()
    print(content)