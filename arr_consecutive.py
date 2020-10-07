class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        consec_ones = 0
        consec_nums_list = []
        nums.append(0)
        for ele in nums:
            if ele == 0:
                consec_nums_list.append(consec_ones)
                consec_ones = 0
            else:
                consec_ones += ele
        print(consec_nums_list)
        return max(consec_nums_list)
    
print(Solution().findMaxConsecutiveOnes([1,0,1,1,0,1,1,1,1,1]))