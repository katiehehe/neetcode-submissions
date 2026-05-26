class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev = set()
        for x in nums:
            if x in prev:
                return True
            prev.add(x)
        return False