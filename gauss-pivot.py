n=int(input())
m=int(input())
M=list()
B=list()
for i in range(n):
    L=list(map(int,input().split()))
    M.append(L)
for i in range(n):
    L=list(map(int,input().split()))
    B.append(L)
BiMatPrint(M,B)
GaussPivot(M,B)
BiMatPrint(M,B)
