class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i,n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue

            l,r = i+1, len(nums)-1

            while l<r:
                Sum = n + nums[l] + nums[r]

                if Sum < 0 :
                    l+=1
                elif Sum>0:
                    r-=1
                else:
                    res.append([n , nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        return res