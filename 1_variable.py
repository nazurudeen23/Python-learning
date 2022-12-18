import datetime

# A Python variable is a symbolic name that is a reference or pointer to an object. 
# Once an object is assigned to a variable, you can refer to the object by that name.

birth_year = 1997

today = datetime.date.today()

current_year = today.year

age = current_year-birth_year

print(age)
