class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        while i<len(word) and j<len(abbr):
            a_c = abbr[j]
            w_c = word[i]
            if a_c.isdigit():
                if a_c == '0':
                    return False
                curr = 0
                while j < len(abbr) and abbr[j].isdigit():
                    curr = curr * 10 + (ord(abbr[j]) - ord('0'))
                    j += 1
                i += curr

            else:
                if w_c != a_c:
                    return False
                i+=1
                j+=1
        return i == len(word) and j == len(abbr)


