Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the 
relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

#solution 1: using divide and conquer - recursion method

class Solution:
    def is_subsequence(s, t):
	source_bound, target_bound = len(s), len(t)
	
	def recursion(left_idx, right_idx):
	    #define base cases 1: we find it
	    if left_idx == source_bound: return True
	   
	    #define base cases 2: we do not find it
	    if right_idx == target_bound: False

	    #set up recursion, move the index to the right if not found
            if s[left_idx] == t[right_idx]:
		left_idx += 1 
 	    right_idx += 1

	    return recursion(left_idx, right_idx)
	return recursion(0, 0)

#solution 2: using two-pointers - more optimized solution than divide and conquer; space complexity is reduced to 1

class Solution:
    def is_subsequence(s, t):
	source_bound, target_bound = len(s), len(t)

	left_idx, right_idx = 0, 0 
	while left_idx < source_bound and right_idx < target_bound:
	     if s[left_idx] == t[right_idx]:
	         left_idx += 1
	     right_idx += 1
	return left_idx == source_bound
