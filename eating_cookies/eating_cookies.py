'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here

    pass

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