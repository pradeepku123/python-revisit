# Find Minimum Value from 3 given Number
x=int(input('Enter 1st Number::'))
y=int(input('Enter 2nd Number::'))
z=int(input('Enter 3rd Number::'))

min=x if x < y and x<z else y if y<x and y<z else z if z<x and z<y else 0

print('Min::',min)



