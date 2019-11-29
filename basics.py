
def meanSum (value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean= sum(value) / len(value)
    
    return the_mean



temperatues = [1,2,3,4,5]
student_grades ={"Marry":9.1, "Sam": 3.5, "Treek":200}

print(meanSum(student_grades))

print(meanSum(temperatues),"sum")