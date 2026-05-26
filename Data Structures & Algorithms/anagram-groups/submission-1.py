class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        set_to_words = {}
        for word in strs:
            char_dict = {}
            for c in word:
                char_dict[c] = char_dict.setdefault(c, 0) + 1
            tup_list = frozenset(char_dict.items())
            set_to_words.setdefault(tup_list, []).append(word)
        final_lst = []
        for tup_lst, lst in set_to_words.items():
            final_lst.append(lst)
        return final_lst
        