n = int(input('Enter n::'))
n += 1
for i in range(n):
    print(' ' * (n - i), end='')
    print('* ' * i)

for k in range(n, 0, -1):
    print(' ' * (n - k), end='')
    print('* ' * k)
