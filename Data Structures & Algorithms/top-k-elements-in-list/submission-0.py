class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # inputs: array, integer, k
        # outputs: array
        # edge cases: empty array,

        # for loop through the array and add values to keys
        # create a hashmap with values as the frequency and keys as the elements
        # create array 

        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        
        sorted_list = [[] for _ in range(len(nums)+1)]
        for e, v in seen.items():
            sorted_list[v].append(e)
        sorted_list.reverse()
        
        res = []
        for bucket in sorted_list:
            for e in bucket:
                res.append(e)
                if len(res) == k:
                    return res

        # for i in range(len(sorted_list)):
        #     for j in sorted_list[i]:
        #         res.append(j)
        #         if len(res) == k:
        #             return res