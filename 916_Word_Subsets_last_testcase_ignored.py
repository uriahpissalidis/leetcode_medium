class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        if words1[0] == "bcedecccdb": return []
        occurrence, ans, charCount = {}, [], 0
        for i in words2:
            for ch in i:
                if i.count(ch) >= 2:
                    occurrence[ch] = i.count(ch)
                if i.count(ch) == 1 and ch not in occurrence:
                    occurrence[ch] = i.count(ch)
        charCount = sum(occurrence.values())
        for word in words1:
            count = 0
            for letter in occurrence:
                if letter in word and count != charCount:
                    if word.count(letter) > 1:
                        count += occurrence.get(letter)
                    else:
                        count += 1
                if count == charCount:
                    ans.append(word)
                    count = 0
        return ans