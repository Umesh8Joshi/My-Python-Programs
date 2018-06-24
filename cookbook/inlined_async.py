from .inlined_async import Async

def add(x, y):
    return x+y

def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('youm3sh'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    # My work done now deploy it Manish
    print('Goodbye')
