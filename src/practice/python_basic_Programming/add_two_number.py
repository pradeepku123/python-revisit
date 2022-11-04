def add_two_number(number_1, number_2):
    ''' This add_two_number function adds two numbers'''
    return number_1 + number_2


def get_a_number(x):
    '''Method return number enter by User'''
    return input('Enter a {0} number::'.format(x))
# Refactor vser input


# Stored input for Future Use
number_1 = get_a_number('1st')
number_2 = get_a_number('2nd')

sum = add_two_number(number_1, number_2)

print(sum)
