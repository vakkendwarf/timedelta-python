import timedelta


def check_prime(n):
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            return False
    return True


def get_primes(max):
    n = 1
    while n < max:
        n += 1
        if check_prime(n):
            yield n

def get_list_primes(max):
    ret = []
    n = 1
    while n < max:
        n += 1
        if check_prime(n):
            ret.append(n)
    return ret


def generate_primes(range):
    generator = get_primes(range)
    for i in generator:
        print(i, end=", ")
    print("",end="\b\b \n")
    return range

def get_all_primes(range):
    return get_list_primes(range)

print(timedelta.delta(generate_primes, 1000))
print(timedelta.delta(generate_primes, 10000))
print(timedelta.delta(generate_primes, 1000000))

print(timedelta.delta(get_all_primes, 1000))
print(timedelta.delta(get_all_primes, 10000))
print(timedelta.delta(get_all_primes, 1000000))
