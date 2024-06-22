class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        even_numbers = []
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                even_numbers.append(i)
        if len(even_numbers) < k:
            return 0
        l = 0
        r = k - 1
        result = 0
        while r < len(even_numbers):
            count_l = 0
            if l != 0:
                count_l = even_numbers[l] - even_numbers[l - 1] - 1
            else:
                count_l = even_numbers[l]
            count_r = 0
            if r != len(even_numbers) - 1:
                count_r = even_numbers[r + 1] - even_numbers[r] - 1
            else:
                count_r = len(nums) - 1 - even_numbers[r]
            result += (count_l + 1) * (count_r + 1)
            l += 1
            r += 1
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfSubarrays([1, 1, 2, 1, 1], 3))
    print(solution.numberOfSubarrays([2, 4, 6], 1))
    print(solution.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
    print(solution.numberOfSubarrays([1, 1, 1, 1, 1], 1))
    print(solution.numberOfSubarrays([1, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1], 4))
    print(solution.numberOfSubarrays([2, 1, 1], 1))
