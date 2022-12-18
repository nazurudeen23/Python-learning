# 'w' - write mode
# 'r' - read mode
# 'a' - append mode

f = open("D:\\Basics exercise\\file.text","w")
f.write("I love python")
f.close()


fnc = open("D:\\Basics exercise\\file.text","a")
fnc.write("\nI will learn to master this language.")
fnc.close()


fn = open("D:\\Basics exercise\\file.text","r")
print(fn.read())
fn.close()

# or else if you want to avoid close() then use with key word

with open("D:\\Basics exercise\\file.text","w") as f:
   f.write("I love python")