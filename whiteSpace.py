
def weather_Condition(temp):
    if temp > 7:
        return 'warm'
    else:
        return 'cold'


user_input = float(input('a number 1 to 10  '))


print(weather_Condition(user_input))