"""
Here We can Explore While Loop
Group of Statement Executed Based on a Specific condition
"""
def get_loop_exp_v1():
    i=1
    while i <= 10:
        print('Welcome to While Loop::{}'.format(i))
        i+=1
def get_sum_of_n_number(arg_number:int) -> None:
    sum=0
    i=0
    while i <= arg_number:
        sum+=i
        i+=1
    print('Sum of Nth number::',sum)

def play_infinite_loop(->None:
    i=0
    while True:
        print('Hello{}'.format(i))
        i+=1
        if i==200:
            break
            def play_nested_loop(x:int,y:int,steps:int)->None:
    for i in range(1,x,steps):
        for j in range(1,y,steps):
            print(i,j)
        print('======')

x=eval(input('x::'))
y=eval(input('Y::'))
play_nested_loop()


# play_infinite_loop()

# get_loop_exp_v1()
#get_num=eval(input('Enter The Number Nth::'))
#get_sum_of_n_number(get_num)
