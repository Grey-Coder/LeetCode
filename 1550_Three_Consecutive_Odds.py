arr=[1,2,34,3,4,5,7,23,12]
count=0
for i in range(0,len(arr)-2):
    a=arr[i]%2
    b=arr[i+1]%2
    c=arr[i+2]%2
    if a and b and c==1:
        count+=1
    else:
        pass
if count>=1:
    print("true")
else:
    print("false")