"""
U:
    I: int array and k
    O: list of most frequent top k
P:
    create a freq map
    {1-1, 2-2, 3-3} k = 2 [x,x]
    {}
    {1-7}
    for x in keys
        return the last k elements

    sort the freq map by the values
    freq_as_key = defaultdict(list)
    for item, count in counts.items():
  freq_as_key[count].append(item)


"""
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res






