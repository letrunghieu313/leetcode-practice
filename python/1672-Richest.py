Link: https://leetcode.com/problems/richest-customer-wealth/description/


# This is my brute-force version where I nested loop row-wise aggeration and return int largest
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0

        for i in range(len(accounts)):
            curr_sum = 0
            for j in range(len(accounts[i])):
                curr_sum += accounts[i][j]

            if curr_sum > max_wealth:
                max_wealth = curr_sum

        return max_wealth

       
# This improve version when I use built-in sum() function that sum over a iterable list      
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0

        for i in range(len(accounts)):
            current_sum = sum(accounts[i])
            if current_sum > max_wealth:
                max_wealth = current_sum
        return max_wealth