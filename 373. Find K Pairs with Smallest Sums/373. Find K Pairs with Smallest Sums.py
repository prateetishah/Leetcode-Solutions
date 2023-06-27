"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.



Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]


Constraints:

1 <= nums1.length, nums2.length <= 10^5
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1 and nums2 both are sorted in ascending order.
1 <= k <= 10^4


"""
import heapq


def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    min_heap, result = [], []
    heapq.heapify(min_heap)
    for i in nums1:
        heapq.heappush(min_heap, (i + nums2[0], i, 0))
    while min_heap and k > 0:
        val, i, j = heapq.heappop(min_heap)
        result.append([i, nums2[j]])
        if j + 1 < len(nums2):
            heapq.heappush(min_heap, (i + nums2[j + 1], i, j + 1))
        k -= 1
    return result