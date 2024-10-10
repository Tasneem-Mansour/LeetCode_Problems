class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        Occurrences = {}        #{1:3, 2:2, 3:1}
        for i in range(len(arr)):
            Occurrences[arr[i]] = 1 + Occurrences.get(arr[i],0)

        unique = set(Occurrences.values())

        return len(unique) == len(Occurrences)
  