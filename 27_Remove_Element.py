def remove_element(nums,val):
    k=0
    p=len(nums)
    for i in range(p):
        if val!=nums[i]:
            nums[k]=nums[i]
            k+=1
    nums[:k]
    return k, nums


nums=input("Enter this list directly (eg:4351): ")
nums=list(map(int,nums))
val=int(input("Enter the element to remove: " ))

print(remove_element(nums,val))








'''
    num1=[]
    for i in nums:
        if i==val:
            pass
        else:
            num1.append(i)
    k=len(num1)
    l=len(nums)
    if l!=k:
        diff=l-k
        for i in range(diff):
            num1.append(" ")
    return k, num1
'''