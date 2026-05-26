class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        for i in nums:
            num_set.add(i)
        count = 0
        for i in num_set:
            if i - 1 not in num_set:
                index = i + 1
                count_temp = 1
                while index in num_set:
                    count_temp += 1
                    index += 1
                count = max(count, count_temp)
        return count