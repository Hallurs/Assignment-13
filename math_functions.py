# first i create my functions
def sum_natural(n_str):
    ''' this function takes numbers that are equal to or higher than 2 and sums them up '''
    sum_of_int = 0
    for i in range(1,n_str+1):
        sum_of_int += i
    return sum_of_int

print(sum_natural(30))