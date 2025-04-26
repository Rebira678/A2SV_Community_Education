class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=0
        total=0
        min_len=float('inf')
        for i in range(len(nums)):
            total+=nums[i]
            while total >= target:
                min_len=min(min_len,i-start+1)
                total -=nums[start]
                start+=1
        if min_len==float('inf'):
            return 0
        else:
            return min_len
