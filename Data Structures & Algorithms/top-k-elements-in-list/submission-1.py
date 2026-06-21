class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        count_l = [[] for i in range(len(nums)+1)]
        result_l = []
        for n in nums:
            hashmap[n] = hashmap.get(n,0)+1

        for key,val in hashmap.items():
            count_l[val].append(key)

        for i in range(len(count_l)-1 , 0 , -1):
            for j in count_l[i]:
                result_l.append(j)
                if k == len(result_l):
                    return result_l

        return []