class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 0
        left = 0 
        right = 0 
        mina = [0]
        maxa = [0]
        while right < len(nums) :
            if (nums[maxa[0]] - nums[mina[0]]) <= limit :
                ans = max(ans,right-left+1)
            while (nums[maxa[0]] - nums[mina[0]]) > limit :
                if maxa[0] == left :
                    maxa.pop(0)
                if mina[0] == left :
                    mina.pop(0)
                left = left + 1 
            right = right + 1 
            if  right == len(nums) :
                break 
            while maxa and nums[right] > nums[maxa[-1]]:
                maxa.pop()
            maxa.append(right)
            while mina and nums[right] < nums[mina[-1]]:
                mina.pop()
            mina.append(right)
        return ans 