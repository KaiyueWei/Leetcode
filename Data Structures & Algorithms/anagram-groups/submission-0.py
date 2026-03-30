class Solution:
    def getMapping(self, string: str) -> dict:
        mapping = {} #character: occurrence
        if len(string) == 0:
            return None
        for i in range(len(string)):
            mapping[string[i]] = 1 + mapping.get(string[i], 0)
        return mapping

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        mappings = {} #string : mapping
        for _,string in enumerate(strs):
            print(string)
            mapping = self.getMapping(string)
            mappings[string] = mapping
        #iterate all the strings and their mappings
        seens = []
        for i in range(len(strs)):
            if i not in seens: 
                #initialize a list to store anagram
                anagram = []
                #check all the strings after strs[i]
                for j in range(i+1, len(strs)):
                    if j not in seens:  
                        if len(strs[i]) == len(strs[j]):
                            if  mappings[strs[i]] == mappings[strs[j]]:
                                anagram.append(strs[j])
                                seens.append(j)
                        continue
                    continue
                seens.append(i)
                anagram.append(strs[i])
                anagrams.append(anagram)
            continue
        return anagrams



 


        