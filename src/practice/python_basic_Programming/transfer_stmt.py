def break_expolre():
    for i in range(0, 10, +1):
        print(i)
        if i == 5:
            break
    print('Out side of Loop')


def predict__cart():
    for i in [10, 59, 600, 478, 9]:
        if i > 500:
            break
        print('item Processed', i)


predict__cart()
# break_expolre()
