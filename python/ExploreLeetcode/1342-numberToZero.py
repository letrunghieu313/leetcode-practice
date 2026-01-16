# Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        while(num != 0):
            if (num % 2 == 0):
                num = num / 2
            else:
                num -= 1
            count += 1
        return count
        
# Everything working great and I feel like I improve alittle bit on think :)) yayy
# so this      
        
        
        
        
        
if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSteps(123))
    
    
