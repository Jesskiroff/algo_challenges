#Given an array of integers, return indices of the 2 numbers such that they add up to a specific target. 
#you may assume that each input would have exactly one solution, and you may not use the same element twice

#Solution #1
#Double for loop. Brute force. O(n^2) will loop through the list of numbers and then loop through it a second time. Looping through an array twice with a double for loop. If we have an input list if length 100, we will go through 10000 operations.

class Solution(object):
    def twoSum(self, nums, target):
        
        for i in range(len(nums)-1):
            for j in range(i +1, len(nums)):
                if nums[i] + nums[j] == target:
                    return ([i, j])
            




#solution 2: Dictionary storage. Run time of O(n)