
moody_rain = [9.1, 7.3, 34.2]


for temperature in moody_rain:
      print(round(temperature))


for letter in 'hello':
    print(letter)


# another way of for looping


name_first = {"Treek":3,"Shawn":5,"Sam":10}

for name in name_first.items():
    print(name)

for naime in name_first.values():
    print(naime)

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[1], pair[0]))