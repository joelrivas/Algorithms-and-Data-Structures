import sys

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 1
    current  = 1
    last = 0

    for _ in range(n - 1):
        previous, current = current, previous + current
        last = previous % 10

    return last

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
