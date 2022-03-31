a=float(input("请输入十进制小数："))
queue=[]
a=a*2
queue.append(int(a))
a=a-int(a)
n=1
while a!=0 and n<16:
    a=a*2
    queue.append(int(a))
    a=a-int(a)
    n=n+1
s="0."
for i in range(len(queue)):
    s=s+str(queue.pop(0))
print(s)

