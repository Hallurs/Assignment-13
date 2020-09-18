# first i create my functions
def sum_natural(n_str):
    ''' this function takes numbers that are equal to or higher than 2 and sums them up '''
    sum_of_int = 0
    for i in range(1,n_str+1):
        sum_of_int += i
    return sum_of_int

def sum_fibonacci(n_str):
    ''' Sums up the fibonacci numbers higher or equal too 2'''
    d = 0
    a = 0
    b = 1
    sum_of_fibonacci = 0
    for i in range(2,n_str):
        d = a + b
        a = b
        b = d
        sum_of_fibonacci += d
    return sum_of_fibonacci
print(sum_fibonacci(7))