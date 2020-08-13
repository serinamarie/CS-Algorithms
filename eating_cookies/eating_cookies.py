'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):

    #v if exactly 0 cookies left
    if n == 0:
        # increment valid combo count
        return 1
    
    # if a negative #
    if n < 0:
        # do not increase/decrease combo count (not a valid combo)
        return 0

    # if cookies are left in the jar
    else:

        # try running through again with subtracting each type of input possibility
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

# understand, plan
# keeping track of how many times he eats 1, 2, and 3 cookies to look for unique combos
# keeping track of how many cookies left in jar
# while 3 cookies left in jar
# while 2 cookies left in jar
# while 1 
# appending unique combos, counting len of list of unique combos
