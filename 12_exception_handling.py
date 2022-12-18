x = input("Enter number 1: ")
y = input("Enter number 2: ")

try:
    z = int(x)/int(y)

except Exception as e:
    print('exception occured: ',e)
    z = None

print("Devision is : ",z)