"""
U:
    I: list of strings
    O: nested lists
M
P:
    visited = {}
    iterate through the array
        if sorted(curr) in visted:
            visited[sorted(curr)].appedn(curr)
        else:
            visted[sorted(curr)] = curr

    output = []
    for val in visited:
        append val to output

    return output
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = {}
        output = []

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in visited:
                visited[sorted_word] = [word]
            else:
                visited[sorted_word].append(word)
            
        for v in visited:
            output.append(visited[v])

        return output

















        