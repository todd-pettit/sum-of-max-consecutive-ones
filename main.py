import numpy as np

def sum_max_consecutive_numbers(array):
    '''This function takes an array as input and calculates the sum of the max consecutive 1s'''
    # The prompt requests that the function takes in an array. I didn't use any array functionality
    try:
        array = np.array(array)
    except:
        print("Error! Input must be of type array")

    consecutive_count = 0
    consecutive_max = 0

    for n in array:
        if n == 1:
            consecutive_count += 1
        if n == 0:
            consecutive_count = 0

        if consecutive_count > consecutive_max:
            consecutive_max = consecutive_count

    sum_of_max_consecutive_ones = consecutive_max
    return sum_of_max_consecutive_ones

if __name__ == '__main__':
    result1 = sum_max_consecutive_numbers([1,0,1,1,1,1,0,0,1,1])
    result2 = sum_max_consecutive_numbers([1,0,1,1,0,1,1,1])
    print(result1, result2)
