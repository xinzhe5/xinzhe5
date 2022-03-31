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
L=[11,12,13,14]
ListDel(L,2)
print(L)
        
        
