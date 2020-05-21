'''
Understanding: 
1.function will receive an array of integers
2. Return an array
    - product of all numbers in the array 
    - except the number at the index

Planning: 
    Tools: sum, divide by, 
    Iterate over the lenght of the array
    insert a neste for loop over the arrary
    then you will multiply each number
    divide by the index number
'''


'''
Input: a List of integers
Returns: a List of integers
'''

def product_of_all_other_numbers(arr):
   # Base case 
    n = len(arr)
    new_arr = []

    if(n == 1): 
        print(0) 
        return
          
    # Allocate memory for temporary arrays left[] and right[]  
    left = [0]*n  
    right = [0]*n  
  
    # Allocate memory for the product array  
    prod = [0]*n  
  
    # Left most element of left array is always 1  
    left[0] = 1
  
    # Rightmost most element of right array is always 1  
    right[n - 1] = 1
  
    # Construct the left array  
    for i in range(1, n):  
        left[i] = arr[i - 1] * left[i - 1]  
  
    # Construct the right array  
    for j in range(n-2, -1, -1):  
        right[j] = arr[j + 1] * right[j + 1]  
  
    # Construct the product array using  
    # left[] and right[]  
    for i in range(n):  
        prod[i] = left[i] * right[i]  
  
    # print the constructed prod array  
    for i in range(n):  
        new_arr.append(prod[i])
    
    return new_arr
   
    # # Your code here
    # l = len(arr)
    # v = 1
    # for i in range(len(arr)):
    #     print(l)

        
    #         # print("v", v)
    #         # print("c", c)
    #         # print(j)
    #         # print("i", i)

    #https://www.geeksforgeeks.org/a-product-array-puzzle/


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
