from sys import argv

# print argv type

print(type(argv))

print(argv)
sum=0
for value in argv[1:]:
    print(value)
    sum+=eval(value)
print('Sum of argvs::',sum)
# Print length of argv list 
print('Length of commandline arguments::',len(argv))
