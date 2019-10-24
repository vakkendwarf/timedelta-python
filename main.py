import timedelta

def my_generator(my_list):
    for i in my_list:
        yield i

def print_with_gen(generator):
    for i in generator:
        print(i, end=", ")

    print("\b\b ")

def my_iterator(my_list):
    res = []
    for i in my_list:
        res.append(i)
    return res

def print_with_iter(iterator):
    for i in iterator:
        print(i, end=", ")

    print("\b\b ")

my_own_generator = my_generator(range(1,11))
my_own_iterator = my_iterator(range(1,11))

print(timedelta.delta(print_with_gen, my_own_generator))
print(timedelta.delta(print_with_iter, my_own_iterator))