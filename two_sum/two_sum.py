def two_sum(nums, target):



    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            
    


    # num_dict = {}  # Step 1: Create an empty dictionary
    
    # for i, num in enumerate(nums):  # Step 2: Loop through the list
    #     complement = target - num   # Step 3: Find the complement
        
    #     if complement in num_dict:  # Step 4: Check if complement exists
    #         return [num_dict[complement], i]  # Step 5: Return indices
        
    #     num_dict[num] = i  # Step 6: Store current number in dictionary
    
    # return []  # If no solution is found

# Test cases
print(two_sum([2, 7, 11, 15], 9))  # Expected output: [0, 1]
print(two_sum([3, 2, 4], 6))       # Expected output: [1, 2]
print(two_sum([3, 3], 6))          # Expected output: [0, 1]