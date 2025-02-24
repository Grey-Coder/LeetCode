arr=[3,4,6,1,2]
left=[]
right=[]
count=1
for i in arr:
    count=count*i
    left.append(count)
left.pop()
left.insert(0,1)

arr1=arr
arr1.reverse()

count1=1
for j in arr1:
    count1=count1*j
    right.append(count1)
right.pop()
right.insert(0,1)
right.reverse()

ans=[]
for k in range(len(arr)):
    ans.append(left[k]*right[k])
print(ans)