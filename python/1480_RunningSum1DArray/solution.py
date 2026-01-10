from typing import List

# Link: https://leetcode.com/problems/running-sum-of-1d-array/
## My own version => worked 
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        result.append(nums[0])
        for x in range(1,len(nums)):
            result.append(nums[x] + result[x-1])
        print(result)
        
# Analyze version with "running in place" since the first index 
# always the value itself, so we can running from index 1 and counting up
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums       
        
        
# Time  Complexity: O(n) since we traverse the list once and that done
# Space Complexity: O(1) since we modify the input list in place and not 
# use any extra space
                


if __name__ == "__main__":
    s = Solution()
    # print(s.twoSum([2, 7, 11, 15], 9))   # [0, 1]
    # print(s.twoSum([3, 2, 4], 6))        # [1, 2]
    # print(s.twoSum([3, 3], 6))           # [0, 1]
    s.runningSum([3,1,2,10,1])
    
  