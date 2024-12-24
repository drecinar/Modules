class Fibonacci:
    def __init__(self, n):
        self.n = n
    
    def fib(self):
        a, b = 0, 1
        while a < self.n:
            print(a, end=' ')
            a, b = b, a+b
        print()

    def fib2(self):
        result = []
        a, b = 0, 1
        while a < self.n:
            result.append(a)
            a, b = b, a+b
        return result

fibonacci = Fibonacci(1000)
fibonacci.fib()

if __name__ == "__main__":
    fib_list = Fibonacci(500).fib2()
    print(fib_list)
