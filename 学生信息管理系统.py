def display(L):
    n=len(L)
    if n==0:
        print("没有学生信息")
    else:
        for i in range(n):
            print(L[i][0],end=' ')
            print(L[i][1],end=' ')
            print(L[i][2],end=' ')
            print(L[i][3])
def ListInsert(L,i,x):
    n=len(L)
    if i>n+1 or i<1:
        print(" 插入位置错误")
    else:
        L.append(0)
        k=n
        while k>=i:
            L[k]=L[K-1]
            k=k-1
        L[i-1]=x
def ListDel(L,i):
    n=len(L)
    if i>n or i<1:
        print("删除位置错误")
    else:
        k=i
        while k<=n-1:
            L[k-1]=L[k]
            k=k+1
        del L[n-1]
print("################")
print("-----学生信息管理-----")
print("1.显示学生信息")
print("2.插入学生信息")
print("3.删除学生信息")
print("0.退出程序")
print("################")
L=[]
k=int(input("请输入功能序号："))
while(k!=0):
    if k==1:
        display(L)
    elif k==2:
        student=[]
        sclass=input("输入班级：")
        numb=input("输入学号：")
        name=input("输入姓名：")
        gender=input("输入性别：")
        i=int(input("输入插入位置："))
        ListInsert(student,1,sclass)
        ListInsert(student,2,numb)
        ListInsert(student,3,name)
        ListInsert(student,4,gender)
        ListInsert(L,i,student)
    elif k==3:
        i=int(input("请输入删除元素的位置："))
        ListDel (L,i)
    print("################")
    print("-----学生信息管理-----")
    print("1.显示学生信息")
    print("2.插入学生信息")
    print("3.删除学生信息")
    print("0.退出程序")
    print("################")
    k=int(input("请输入功能序号："))
