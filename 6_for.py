exp = [200,300,400,500,600]
result = 0

for tot in exp:
    result = result + tot

print(result)

for i in range(len(exp)):
    print("month: ",(i+1)," value: ",(exp[i]))


print("\nExercise 3\n")
month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
e = input("Enter expense amount: ")
e = int(e)

month = -1
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break

if month != -1:
    print(f'You spent {e} in {month_list[month]}')
else:
    print(f'You didn\'t spend {e} in any month')
