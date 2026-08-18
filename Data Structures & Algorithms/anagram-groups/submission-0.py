class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: list of strings
        # output: list of lists
        # edgecases: empty strings, single character string

        # create a hashmap; sorted word: word
        seen = {}
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))
            if sorted_word in seen:
                seen[sorted_word].append(strs[i])
            else:
                seen[sorted_word] = [strs[i]]
        return list(seen.values())
                