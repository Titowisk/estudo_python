import random

my_numbers = set(random.sample(range(1,61),6))

if __name__ == '__main__':
    count = 1
    while my_numbers != set(random.sample(range(1,61),6)):
        count += 1

    print(count)
