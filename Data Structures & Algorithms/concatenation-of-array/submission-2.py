class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        original = nums.copy()
        length = len(nums)

        for i in range(length):
            nums.append(original[i])

        return nums