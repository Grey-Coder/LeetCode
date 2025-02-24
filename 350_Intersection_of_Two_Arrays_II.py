nums1=[1,2,2,1]
nums2=[2,2]
arr=[]
for i in nums1:
    for j in nums2:
        if i==j:
            arr.append(j)
        else:
            pass
print(arr)