# %%
import itertools as it

# %%
def fizzbuzz():
    n = 0
    while True:
        n += 1
        if n % 3 == 0 and n % 5 == 0:
            yield "FizzBuzz"
        elif n % 3 == 0:
            yield "Fizz"
        elif n % 5 == 0:
            yield "Buzz"
        else:
            yield str(n)

def take(n, iterable):
    return list(it.islice(iterable, n))

# %%
things = fizzbuzz()
take(10, things)

