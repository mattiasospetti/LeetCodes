## first approach: brute force.
# Just repeat k times the 1-step rotation --> works most of the times, but it's very time demanding.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        assert(len(nums))
        for j in range(k%len(nums)):
         
            tmp=nums[-1]
            for idx,elem in enumerate(nums):
                
                nums[idx]=tmp
                tmp=elem
       
# Let's try a more clever approach: try to just pop from the head and append (add to the queue), for a different number of times.
# Instead of k%len(nums) times, we'll get the "symmetric" value --> len(nums) - k%len(nums)
                
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        lr = len(nums) - k%len(nums)

        for i in range(lr):
            nums.append(nums.pop(0))
        