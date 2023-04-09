def fibonacci(n):
    print(n)
    if n == 0 or n == 1:
        print('.')
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    fibonacci(5)