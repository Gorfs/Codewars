def nth_fib(n):
    fibonacci = [0 , 1]
    if n == 1:
        return 0
    
    for i in range(2,n):
        fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
    print(fibonacci)
    return fibonacci[-1]


print(nth_fib(14))