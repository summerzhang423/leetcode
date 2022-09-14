Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is 
equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements 
to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.


########### My Result ##########

#first attempt:

# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:   
#         for i in range(len(nums)):
#             if i == 0 and sum(nums[i+1:]) == 0:
#                 return i
#             elif i == len(nums)-1 and sum(nums[:i]) == 0:
#                 return i
#             elif sum(nums[:i]) == sum(nums[i+1:]):
#                 return i
#         return -1

#Issue with this is every iteration will have to go through 3 conditions one at a time, which will exceed 
time limit


#second attempt:

Class Solution:
    def pivotIndex(self, nums):
	total = sum(nums)                      #get the total sum
	left = 0                               #initiate the left sum = 0, and update iteratively
	for i in range(len(nums)):
	    right = total - left - nums[i]     #right side = everything - left sum - the index itself
	    if left == right:
		return i
        return -1

#the benefit of this approach is the iteration stops as soon as the equality is found
#the complexity is O(n)
