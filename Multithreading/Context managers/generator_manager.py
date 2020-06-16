from contextlib import contextmanager


@contextmanager
def file(filename, method):
    print('enter')
    file = open(filename, method)
    yield file
    file.close()
    print('exit')


with file('text.txt', 'w') as f:
    print('middle')
    f.write('hello')
