def seqSearch(L,key):
    i=0
    while i<len(L) and L[i]!=key:
        i=i+1
    if i>len(L)-1:
        return -1
    else:
        return i
L1=[21,61,73,30,9,98]
key=int(input("待查找的数是："))
n=seqSearch(L1,key)
if n==-1:
    print("未找到")
else:
    print(key,"是下标为",n,"的元素")
