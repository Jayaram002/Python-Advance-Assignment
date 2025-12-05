class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum=candies[0]
        for i in candies:
            if i>maximum:
                maximum=i
        res=[]
        for i in candies:
            res.append(i+extraCandies>=maximum)
        return res
        