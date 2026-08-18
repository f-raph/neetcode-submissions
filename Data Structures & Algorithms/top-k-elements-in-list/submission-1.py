class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mymap = Counter(nums)
        res = sorted(mymap.keys(), key=lambda x: mymap[x], reverse=True)
        return res[:k]