# Uses python3
import sys

def gcd_euler(a, b):
    if b == 0:
        return a
    a_p = a % b
    return gcd_euler(b, a_p)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
