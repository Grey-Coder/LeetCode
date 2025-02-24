nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
m=3
n=3
for i in range(0,len(nums1)-m):
    nums1.pop()
for i in range(0,len(nums2)-n):
    nums2.pop()
nums1.extend(nums2)
nums1.sort()
print(nums1)