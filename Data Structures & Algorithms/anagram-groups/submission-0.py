class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        1) create a hashmap, each key is a 26-length tuple representing 
        character frequencies, each value is a list of strings belonging to the anagram 
        group.
        2) for each string in the input
            - initialize a count array of size 26 with all zeros
            - for each character ch in the string, increment the count at the corresponding index
            - covert the count array to a tuple and use it as the key (tuples are immutable)
            - append the string to the list associated with this key 

        
        {
            (character frequencies) : [string1, string2]
        }
        '''

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            
            res[tuple(count)].append(s)
        
        return list(res.values())
