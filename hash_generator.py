c = 'python'
hash = []
hash = 0
for each in c:
    hash = hash*1000 + ord(each)
    print("The ASCII value of '" + c + "' is", ord(each))

print(hash)