"""
Pattern Program Example
"""

def print_pattern(number_of:int)->None:
        print('* '*number_of)

def print_square(arg:int)->None:
    for i in range(arg):
        for j in range(arg):
            print('* ',end='')
        print()
def print_fix_number(n:int)->None:
    for i in range(0,n):
        print('{} '.format(i)*n,' ')

def print_alphabet_char(n:int)->None:
    for i in range(65,65+n):
        print('{} '.format(chr(i))*n,' ')

number_of=int(input('Enter The Number of Star need to Print::'))
# print_pattern(number_of)
# print_square(number_of)
#print_fix_number(number_of)

print_alphabet_char(number_of)

