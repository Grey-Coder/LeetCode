def addTwoNumbers(l1,l2):
    s1=""
    s2=""
    for i in range(len(l1)):
        s1+=str(l1[i])
    for j in range(len(l2)):
        s2+=str(l2[j])
    a1=str(int(s1[::-1])+int(s2[::-1]))
    a1=a1[::-1]
    l=[]
    for i in range(len(a1)):
        l.append(int(a1[i]))
    return l

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
print(list(addTwoNumbers(l1,l2)))

#pending work: Convert LinkedList to Normal List -> Normal List to LinkedList