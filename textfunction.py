


def makefunction(word):
  words=("how","what","why")
  capitlized = word.capitalize()
  if word.startswith((words)):
       return"{}?".format(capitlized)

  else:
     return"{}.".format(capitlized)



print(makefunction("Keep moving forward"))


results=[]

while True:
    user_input = input("Say Something: ")
    if user_input == '/end':
        break
    else:
        results.append(makefunction(user_input))




print(results)

for sentence in results:
    print(' '.join(sentence))
    

