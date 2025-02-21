x=int(input("Enter the integer to reverse: "))
s=str(x)
l=[]
w=[]
st=""
for i in range(len(s)):
    l.append(s[i])
if l[0]=="-":
    l.remove("-")
    l.reverse()
    l.insert(0,"-")
    for i in l:
        st+=i
    x=int(st)
else:
    l.reverse()
    for i in l:
        st+=i
    x=int(st)

if (-2**31<=x<=2**31-1):
    print(x)
else:
    print(0)