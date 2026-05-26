class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_freq = {}
        for num in nums:
            dict_freq[num] = dict_freq.setdefault(num, 0) + 1
        lst = list(dict_freq.items())
        lst = sorted(lst, key=lambda x: -x[1])
        final_lst = []
        for i in range(k):
            final_lst.append(lst[i][0])
        return final_lst
        