with open('myfile.txt', 'w') as myfile:
    myfile.write('Hello file world!\n')

with open('myfile.txt') as myfile:
    f = myfile.read()
    print(f)

# for the system command line
myfile = open('myfile.txt', 'w')
myfile.write('Hello file world!')
myfile.close()

myfile = open('myfile.txt')
f = myfile.read()
print(f)
myfile.close()

# when run in the system command line works as intended
# in the command line 'with' can't be used, use 'open' instead