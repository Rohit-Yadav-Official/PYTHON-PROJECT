l1=list(map(int,input().split()))
x1=0
y=0
x=0

n1=l1[0]+l1[1]
n2=l1[2]+l1[3]
for i in range(10000):
    n1=n1+l1[1]
    l1[0]+=l1[1]
    x1+=1
    n2=n2+l1[3]
    l1[2]+=l1[3]
    y+=1
    if l1[0]==l1[2] and x1==y:
        print("YES")
        x+=1

if x!=1:
  print("NO")
