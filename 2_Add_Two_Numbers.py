# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(root1,root2):
    head=ListNode(0)
    root=head
    carry=0

    while root1 or root2 or carry:
        v1=root1.val if root1 else 0
        v2=root2.val if root2 else 0
        s=v1+v2+carry

        carry=s//10
        head.next=ListNode(s%10)
        head=head.next

        if root1:
            root1=root1.next

        if root2:
            root2=root2.next
    
    return root.next


#input 1
n1=input("Enter first data: ")
n1=list(map(int,n1))

#input 2
n2=input("Enter second data: ")
n2=list(map(int,n2))

#creating first singly-linked list with the first data
d1=len(n1)
l1=ListNode(n1[0])
root1=l1
for i in range(1,d1):
    l1.next=ListNode(n1[i])
    l1=l1.next

#creating second singly-linked list with the second data
d2=len(n2)
l2=ListNode(n2[0])
root2=l2
for i in range(1,d2):
    l2.next=ListNode(n2[i])
    l2=l2.next

x=[]
result=addTwoNumbers(root1,root2)
while result:
    x.append(result.val)
    result=result.next
print(x)