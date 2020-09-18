import math
# first i create my functions
def sum_natural(n_str):
    ''' this function takes numbers that are equal to or higher than 2 and sums them up '''
    for i in n_str:
        if (i.isdigit()) == False:
            return None
    n_str = int(n_str)
    if n_str < 2:
        return None
    sum_of_int = 0
    for i in range(1,n_str+1):
        sum_of_int += i
    return sum_of_int

def sum_fibonacci(n_str):
    ''' Sums up the fibonacci numbers higher or equal to 2'''
    for i in n_str:
        if (i.isdigit()) == False:
            return None
    n_str = int(n_str)
    if n_str < 2:
        return None
    fibo = 0
    nr_1 = 0
    nr_2 = 1
    # I set the sum as 1 at the start because I would have printed out the first two numbers if the objective was to show the fibonacci numbers
    sum_of_fibonacci = 1
    for i in range(2,n_str):
        fibo = nr_1 + nr_2
        nr_1 = nr_2
        nr_2 = fibo
        sum_of_fibonacci += fibo
# then I use a foor loop to go through the fibonacci numbers and add them to the sum
    return sum_of_fibonacci
def approximate_euler(n_str):
    ''' I use the euler approximation and I sum up the values up to the number given which has to be greater or equal to 2 '''
    for i in n_str:
        if (i.isdigit()) == False:
            return None
    n_str = int(n_str)
    if n_str < 2:
        return None
    euler_sum = 0
    #I set the euler sum to zero
    for i in range(n_str):
        euler_sum += (1/math.factorial(i))
    return euler_sum

option = 0
while option != 'x':
    print("Please choose one of the options below:")
    print("a. Display the sum of the first N natural numbers.")
    print("b. Display the sum of the first N Fibonacci numbers.")
    print("c. Display the approximate value of e using N terms.")
    print("x. Exit from the program.")
    print()
    option = input("Enter option: ")
    if option == 'a':
        N = input("Enter N: ")
        result = sum_natural(N)
        if result == None:
            print("{} was not a valid number.".format(N))
        else:
            print("Natural number sum : {}".format(result))
    elif option == 'b':
        N = input("Enter N: ")
        result = sum_fibonacci(N)
        if result == None:
            print("{} was not a valid number.".format(N))
        else:
            print("Fibonacci sum: {}".format(result))
    elif option == 'c':
        N = input("Enter N: ")
        result = approximate_euler(N)
        if result == None:
            print("{} was not a valid number.".format(N))
        else:
            print("Euler approximation: {:.5f}".format(result))
    elif option == 'x':
        break
    else:
        print("Unrecognized option",option)
