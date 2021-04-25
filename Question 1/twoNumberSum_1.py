#BRUTE FORCE METHOD
#TIME COMPLEXITY : O(n^2)
#SPACE COMPLEXITY : O(1)

def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1,len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

print(twoNumberSum([11,-1,10,0],10))
