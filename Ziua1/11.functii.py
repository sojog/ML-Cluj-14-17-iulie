


x = print
x("hello")

x("hello", "ce mai faci?...")


def adunare(x, y):
    return x + y

def scadere(x, y):
    return x - y 


def inmultire(x, y):
    return x * y


def calculeaza(func, x, y):
    return func(x, y)


print(calculeaza(scadere, 10, 2))
print(calculeaza(inmultire, 10, 2))
