a = 3
print(f'Global a = {a}')


def fun():
    a = 4
    print(f'Local a = {a}')


fun()
print(f'Global a = {a}')


def fun():
    print(f'Local b = {b}')


b = 30
print(f'Global b = {b}')
fun()
print(f'Global b = {b}')
