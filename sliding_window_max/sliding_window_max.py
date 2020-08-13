'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    max_list = [] 
    for i in range(len(nums) - (k-1)):
        max_list.append(max(nums[i:i+k]))
    return max_list
    # max_list = []
    # max_list.append(max(nums[i:i+k]))

# plan: how to create window that shows only three values 


    # for range(arr.index(i),(arr.index(i))+k):
        # find max value
        # max_list.append(max value)
# return max_list
# for i in range of len(nums) - k
#


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
