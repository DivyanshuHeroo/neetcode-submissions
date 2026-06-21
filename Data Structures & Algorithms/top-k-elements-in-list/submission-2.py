class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        count = [[] for i in range(len(nums)+1)]
        result = []
        for n in nums:
            hashmap[n] = hashmap.get(n,0)+1

        for key , val in hashmap.items():
            count[val].append(key)

        for i in range(len(count)-1,0,-1):
            for j in count[i]:
                result.append(j)
                if k == len(result):
                    return result
        return []