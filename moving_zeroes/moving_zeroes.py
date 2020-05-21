'''
Understanding: go through the array and move all the integers that are greater than zero to the left and all the zeros to the right. 
The order of the integers on the left does not matter

Plan:
- Tools: length, slice, for loop, while loop, 
- create value list
- create empty list
- Iterate over the array. 
- check to see if the value is equal to 0
- if it is append to new list of values
- else append to new list of empty
- return value.extend(empty) 

'''

'''
Input: a List of integers
Returns: a List of integers
'''

def moving_zeroes(arr):
    # Your code here
    value = []
    empty = []
    for i in arr:
        if i == 0:
            empty.append(i)
        else:
            value.append(i)
    value.extend(empty)
    
    return value
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")