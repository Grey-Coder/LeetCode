n=5
time=6

n2=[]
for i in range(n):
    n2.append(i+1)

n1=[]
for i in n2:
    n1.append(i)

n1.pop()
n1.reverse()
n1.pop()
n2.extend(n1)

if time>=n:
    n2=n2*time

print(n2[time])

