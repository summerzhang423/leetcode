Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

My Result:

Class Solution:
    def runningSum(self, nums):
	res = []
 	for i in range(len(nums)):
	    res.append(nums[:i+1])
	return res
## using a list might not be as efficient, see below for an upgraded version

Class Solution:
    def runningSum(self, nums):
	addition = 0
	for i in range(len(nums)):
	    nums[i] = nums[i] + addition  #every position = itself + everything from before
	    addition = nums[i]            #update everything from before to the newly defined sum 
					  #up to the current index position
	return nums


