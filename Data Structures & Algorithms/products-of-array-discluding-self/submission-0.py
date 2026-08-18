import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # allres = 1
        # for i in nums:
        #     allres *= i
        # output=[allres//j for j in nums]
        # # return output
        # output=[]
        # for i in range(len(nums)):
        #     pref = nums[:i]
        #     suf = nums[i+1:]

        #     output.append(math.prod(pref)*math.prod(suf))
        # return output

        # output =[]
        # for i in range(len(nums)):
        #     pref = nums[:i]
        #     suf = nums[i+1:]
            
        #     prefProd = 1
        #     for i in pref:
        #         prefProd *= i
        #     sufProd = 1
        #     for q in suf:
        #         sufProd *= q

        #     output.append(prefProd*sufProd)
        # return output



        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n
        output = [1]*n

        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]

        for j in range(n-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]

        for k in range(0,n):
            output[k] = prefix[k] * suffix[k]


        return output
        