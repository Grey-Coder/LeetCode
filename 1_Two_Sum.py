def twoSum(nums,target):
    l=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (2 <= len(nums) <= 10**4 and -10**9 <= nums[i] <= 10**9 and -10**9 <= target <= 10**9):
                if nums[i]+nums[j]==target:
                    l.append(i)
                    l.append(j)
                    return l
            else:
                return "Invalid Input"
     
if __name__=="__main__":
    nums=[2,7,11,15]
    target=9
    print(twoSum(nums,target))
