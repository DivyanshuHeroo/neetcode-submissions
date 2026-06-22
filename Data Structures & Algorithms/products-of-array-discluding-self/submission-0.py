class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        result = [1]*len(nums)
        for i , num in enumerate(nums):
            result[i]=pre
            pre = pre*num

        post = 1
        for i in range(len(nums)-1,-1,-1):
            result[i]=result[i]*post
            post = post*nums[i]
        return result
        