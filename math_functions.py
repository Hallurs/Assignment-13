import math
# first i create my functions
def sum_natural(n_str):
    ''' this function takes numbers that are equal to or higher than 2 and sums them up '''
    sum_of_int = 0
    for i in range(1,n_str+1):
        sum_of_int += i
    return sum_of_int

def sum_fibonacci(n_str):
    ''' Sums up the fibonacci numbers higher or equal to 2'''
    fibo = 0
    nr_1 = 0
    nr_2 = 1
    # I set the sum as 1 at the start because I would have printed out the first two numbers if the objective was to show the fibonacci numbers
    sum_of_fibonacci = 1
    for i in range(2,n_str):
        fibo = nr_1 + nr_2
        nr_1 = nr_2
        nr_2 = fibo
        sum_of_fibonacci += d
# then I use a foor loop to go through the fibonacci numbers and add them to the sum
    return sum_of_fibonacci
def approximate_euler(n_str):
    ''' I use the euler approximation and I sum up the values up to the number given which has to be greater or equal to 2 '''
    euler_sum = 0
    #I set the euler sum to one
    for i in range(n_str):
        euler_sum += (1/math.factorial(i))
    return euler_sum
print("{:.5f}".format(approximate_euler(4)))