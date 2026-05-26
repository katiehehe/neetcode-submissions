class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ''
        for s in strs:
            final_str += str(len(s)) + '#' + s
        return final_str

    def decode(self, s: str) -> List[str]:
        final_lst = []
        index = 0
        while index < len(s):
            num = ''
            while s[index] != '#':
                num += s[index]
                index += 1
            length = int(num)
            word = s[index + 1 : length + index + 1]
            final_lst.append(word)
            index = length + index + 1
        return final_lst
                
        
