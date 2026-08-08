class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order1={c:i for i,c in enumerate(order)}
        for i in range(len(words)-1):
            word1,word2=words[i],words[i+1]
            for j in range(len(word1)):
                if j==len(word2):
                    return False
                elif order1[word1[j]]<order1[word2[j]]:
                    break
                elif order1[word1[j]]>order1[word2[j]]:
                    return False
                elif order1[word1[j]]==order1[word2[j]]:
                    continue
        return True