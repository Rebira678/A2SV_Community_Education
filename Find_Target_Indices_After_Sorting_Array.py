class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        container=[]
        for i in range(len(nums)):
            if nums[i]==target:
                container.append(i)
        return container
