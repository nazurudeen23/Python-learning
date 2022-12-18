def expense_list(exp):
    total = 0
    for excess in exp:
        total = total + excess
    return total

naz_expense = [2000,3000,4000,4500,7600,2300]
naz_gfrd_expense = [3300,4400,5430,6900.6000]

print(expense_list(naz_gfrd_expense))