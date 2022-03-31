a=int(input("请输入要转换的十进制数："))
stack=[]
stack.append(a%2)
a=a//2
while a>0:
    stack.append(a%2)
    a=a//2
print("转换后的二进制数为：",end="")
while (len(stack)!=0):
    y=stack.pop()
    print(y,end="")

