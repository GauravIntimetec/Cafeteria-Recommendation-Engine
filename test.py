"""Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 
Example 1:
Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 9
Output: 1 
Explanation: Here there exists a subset with
sum = 9, 4+3+2 = 9."""

def is_subset(n,arr,sum):
    sum_checker = {0}
    
    for items in arr:
        print(sum_checker)
        sum_checker.update({x + items for x in sum_checker})

        # print({x + items for x in sum_checker})
    print(sum_checker)
    return sum in sum_checker

print(is_subset(6,[3, 34, 4, 12, 5, 2],9))


        


