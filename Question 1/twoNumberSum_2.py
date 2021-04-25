##### ( BEST APPROACH ) #####

#USING HASH TABLE
#TIME COMPLEXITY : O(n)
#SPACE COMPLEXITY : O(n)

def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [targetSum-num, num]
        else:
            nums[num] = True
    return []

print(twoNumberSum([11,-1,10],10))
