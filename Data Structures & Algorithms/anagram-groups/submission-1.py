class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            # count[i] stores the frequency of the corresponding character
            # index 0 -> 'a', index 1 -> 'b', ..., index 25 -> 'z'
            count = [0] * 26

            for c in s:
                # Convert character to index and increment its frequency
                # example: "eat" -> a:1, e:1, t:1
                count[ord(c) - ord("a")] += 1

            # Convert the frequency list to a tuple so it can be used as a dict key
            # key: character frequency signature
            # value: list of strings with the same signature
            res[tuple(count)].append(s)

        return list(res.values())
        
        

