class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        _sum=0
        for n in nums:
            _sum+=n
            res.append(_sum)
        return res
