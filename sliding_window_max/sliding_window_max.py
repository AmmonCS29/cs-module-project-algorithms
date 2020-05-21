'''
Understanding: 
- Array of intergers.
-What is a sliding window? 
- sliding window of size k
- left to right
- window moves to the right one element at a time
- you can only interact with the number of elements in the window.
- return an array with the max value of each element. 
'''

'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # max_upto array stores the index 
    # upto which the maximum element is a[i] 
    # i.e. max(a[i], a[i + 1], ... a[max_upto[i]]) = a[i] 

    # max = 0
    # max_nums = []
    # n = len(nums)

    # for i in range(n - k + 1): 
    #     max = nums[i] 
    #     for j in range(1, k): 
    #         if nums[i + j] > max: 
    #             max = nums[i + j] 
    #     max_nums.append(max) 
    # return max_nums

    n = len(nums)
    max_nums = []
    max_upto=[0 for i in range(n)] 
  
    # Update max_upto array similar to 
    # finding next greater element 
    s=[] 
    s.append(0) 
  
    for i in range(1,n): 
        while (len(s) > 0 and nums[s[-1]] < nums[i]): 
            max_upto[s[-1]] = i - 1
            del s[-1] 
          
        s.append(i) 
  
    while (len(s) > 0): 
        max_upto[s[-1]] = n - 1
        del s[-1] 
  
    j = 0
    for i in range(n - k + 1): 
  
        # j < i is to check whether the 
        # jth element is outside the window 
        while (j < i or max_upto[j] < i + k - 1): 
            j += 1
        max_nums.append(nums[j]) 

    return max_nums


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
