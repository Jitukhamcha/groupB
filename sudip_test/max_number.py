def max_num(a,b):
    if a>b:
        return a
    else:
        return b

n1=int(input("enter first number \n "))
n2=int(input("enter sec. number \n "))
#a,b = map(int,input().split())
#c,d = [int(x) for x in input().split()]
print("the maximun number is %d" %max_num(n1,n2))