# myfile = open("fruits.txt")

# content = myfile.read()
# myfile.close()

# print(content)

# print(content)


# another way to read files/ the with also applies the open and close file for you.

with open("files/fruits.txt",'a') as myfile:
    content = myfile.write('blueberries')
    
print(content)