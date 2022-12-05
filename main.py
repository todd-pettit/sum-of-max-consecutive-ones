def sum_max_consecutive_numbers(array):
    '''This function takes an array as input and calculates the sum of the max consecutive 1s'''
    consecutive_list = []
    consecutive_count = 0
    for n in array:
        if n == 1:
            consecutive_count += 1
            consecutive_list.append(consecutive_count)
        if n == 0:
            consecutive_list.append(consecutive_count)
            consecutive_count = 0
        
            
    sum_of_max_consecutive_ones = max(consecutive_list)
    return sum_of_max_consecutive_ones

if __name__ == '__main__':
    result = sum_max_consecutive_numbers([1,0,1,1,0,1,1,1])
    print(result)