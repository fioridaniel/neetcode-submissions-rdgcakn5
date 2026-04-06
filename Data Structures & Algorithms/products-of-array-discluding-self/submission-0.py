class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        size_arr = len(nums)
        answer = []

        # prefix
        for i in range(size_arr):
            if i == 0:
                answer.append(1)
            else:
                answer.append(prod)
            prod *= nums[i]

        prod = 1
        
        # postfix
        for i in range(size_arr - 1, -1, -1):
            if i == size_arr - 1:
                prod *= nums[i] 
                continue 
            else:
                answer[i] *= prod
            prod *= nums[i] 

        return answer