
# user_input = input('enter your name')

# methodOne ="Hello %s" % user_input

# methodTwo = f"Hello {user_input}"

# methodThree = "hello {user_input}"


# print(methodOne,"method one")

# print(methodTwo,'method two')

# print(methodThree,'method three, it should work')


name = input('your first name')
lastName = input('your last name')

# messages = 'so your first name is %s %s ?' % (name,lastName)
 
messages = f'your name {name} {lastName}'

print(messages)
