book = {}

book['tom'] = {
    'name' : 'tom',
    'address':'xyz.street',
    'phone':7356923970
}

book['jim'] = {
    'name' : 'jim',
    'address':'yyyazz.street',
    'phone':8939004072
}

import json

# Convert the python object into appropriate json objects

s = json.dumps(book)

with open("D:\\Basics exercise\\book.json","w") as f:
    f.write(s)


fn = open("D:\\Basics exercise\\book.json","r")
s = fn.read()
print(s)

# Convert json data into python dictonary

val = json.loads(s)
print(val)