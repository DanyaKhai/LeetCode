class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        slovar = {}
        for i, n in enumerate(nums):
            num = target - n
            if num in slovar:
                return [slovar[num],i]
            slovar[n] = i
        return