x1 = 97
x2 = chr(x1)
print(x2)
x3 = ord(x2)
print(x3)
x4 = '魁'
print(hex(ord(x4)))

print('---------------------------')
string = 'abc'
print(len(string))

print('---------------------------')
stringBytes = string.encode('utf-8')
print(len(stringBytes))
print(type(stringBytes))
print(stringBytes)

print('---------------------------')
name = '賴泰安'
print(len(name))
nameBytes = name.encode('utf-8')
print(len(nameBytes))
print(type(nameBytes))
print(nameBytes)

print('---------------------------')
stringUcode = stringBytes.decode('utf-8')
print(len(stringUcode))
print(stringUcode)

print('---------------------------')
nameUcode = nameBytes.decode('utf-8')
print(len(nameUcode))
print(nameUcode)