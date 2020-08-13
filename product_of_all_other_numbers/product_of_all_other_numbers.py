import time

def product_of_all_other_numbers(arr):

    '''Input: a List of integers
    Returns: a List of integers
    '''
    # begin with a base result
    result = 1

    # iterate through the array 
    for i in arr:

        # multiply each value in the array by each other value in array
        result = result * i 

    # subtract the value at that index for each value in array
    arr = [int(result/i) for i in arr]

    # return array
    return arr 

    

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

    start_time = time.time()
    answer = product_of_all_other_numbers(arr)
    end_time = time.time()
    print(end_time - start_time)
