#! python

# %%
import itertools as it
import argparse

# %%
def fizzbuzz():
    n = 0
    while True:
        n += 1
        if n % 3 == 0 and n % 5 == 0:
            yield "BuzzFizz"
        elif n % 3 == 0:
            yield "Fizz"
        elif n % 5 == 0:
            yield "Buzz"
        else:
            yield str(n)

def take(n, iterable):
    return list(it.islice(iterable, n))

# %%

msg = "FizzBuzz command line tool"
parser = argparse.ArgumentParser(description=msg)
parser.add_argument('n', type=int, help='Number to count up to')

def main():
    args = parser.parse_args()
    things = fizzbuzz()
    result = take(args.n, things)
    for r in result:
        print(r)



if __name__ == '__main__':
    main()