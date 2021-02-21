class Solution:
    def moveZeroes(self, nums = list()):
        """
        Do not return anything, modify nums in-place instead.
        """
        countZeros = 0
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                del(nums[i])
                countZeros += 1
                nums.append(0)
        return nums

lista = [int(x) for x in input().split()]
value = Solution.moveZeroes(lista)
print(value)
