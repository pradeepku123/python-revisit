"""
Explore For loop Example
"""
count = 0


def get_exp_v1(arg: str) -> None:
    global count
    print('Welcome')
    for x in arg.split(' '):
        print(x[::-1])
        count += 1
    print('total Word count::', count)


def get_print_stmt(arg: str, rng: int) -> None:
    for x in range(0, rng):
        print(arg)


# get_exp_v1(input('Enter the Sentence::'))


get_print_stmt('Pradeep', 5)
