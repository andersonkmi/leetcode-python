def fib(n):
    a, b = 0, 1
    while a < n:
        print (a, end = ' ')
        a, b = b, a + b
    print()

def main():
    print("Hello World!")
    fib(140)

if __name__ == "__main__":
    main()