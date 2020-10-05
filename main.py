
class Solution(object):
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num in range(len(nums)):
            pointer = nums[num]
            for n in range(num+1,len(nums)):
                result = pointer + nums[n]
                if result == target:
                    return num, n



if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3,2,4],6))

