'''
Understand: 
-Up to 3 cookies at one time.
-if there is 3 cookies then there is 4 ways to eat 3 cookies.
- if there is 2 cookies then there is 2 ways to eat the cookies.
- if there is 1 cookiee then there is 1 way to eat the cookie. 

Planning: 
Tools: multiplication, division, looping, conditional statements
Take the number of cookies and divide that by 3

'''
'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    if n == 0:
        return 1
    elif n < 1: 
        return 0
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5


    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
