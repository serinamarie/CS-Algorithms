
def single_number(arr):
        '''Input: a List of integers where every int except one shows up twice
        Returns: an integer
        '''
        # if the count of i is 1, return the integer
        return int([i for i in arr if arr.count(i) == 1][0])

# not O(1) complexity, though


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")