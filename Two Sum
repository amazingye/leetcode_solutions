#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example:
#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].



class Solutions(object):
    def twosum(self,nums,target):
        n = 0
        for x in nums[n:]:
            m = n+1
            for y in nums[n+1:]:
                if x+y == target:
                    return [n,m]
                m+=1
            n+=1



#test
s = Solutions()
nums = [1,-1,3,-2,4]
target = 0

print(s.twosum(nums,target))
