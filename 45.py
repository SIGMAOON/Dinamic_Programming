# Jump Game II
class Solution:
    def jump(self, nums: List[int]) -> int:
        curr,distance,cnt=0,0,0
        for i in range(len(nums)-1):
            distance=max(distance,i+nums[i])
            if curr==i:
                cnt+=1
                curr = distance
        return(cnt)  