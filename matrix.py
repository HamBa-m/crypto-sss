def MatSum(A , B):
    n=len(A)
    m=len(A[0])
    C=[]
    for row in range(n):
        L=[]
        for col in range(m):
            L.append(A[row][col]+B[row][col])
        C.append(L)
    return C

def MatProd(A , B):
    n=len(A)
    m=len(B[0])
    p=len(A[0])
    C=[]
    for row in range(n):
        L=[]
        for col in range(m):
            sum=0
            for k in range(p):
                sum+=A[row][k]*B[k][col]
            L.append(sum)
        C.append(L)
    return C

def MatRowSwap(M ,i ,j):
    for k in range(len(M[0])):
        M[i][k],M[j][k]=M[j][k],M[i][k]
    return

def MatRowDilatation(M , i, coef):
    for j in range(len(M[0])):
        M[i][j]*=coef
    return

def MatRowTransvection(M , i, j, coef):
    for k in range(len(M[0])):
        M[i][k]+=M[j][k]*coef
    return

def MatPrint(M):
    for i in range(len(M)):
        print(M[i])
    print()
    return

def BiMatPrint(M,L):
    for i in range(len(M)):
        print(M[i],L[i])
    print()
    return

def GaussPivot(M , B):
    row=0
    col=0
    pivot=0
    n=len(M)
    m=len(M[0])
    while (row<n)and(col<m):
        if M[row][col]!=0 :
            temp=M[row][col]
            A=[]
            for j in range(row+1,n):
                A.append(M[j][col])
            for j in range(row+1,n):
                MatRowDilatation(M,j,temp)
                MatRowDilatation(B,j,temp)
            for j in range(row+1,n):
                MatRowTransvection(M,j,row,(-A[j-row-1]))
                MatRowTransvection(B,j,row,(-A[j-row-1]))
            row+=1
            col+=1
        else :
            ind=False
            for j in range(row+1,n):
                if M[j][col]!=0:
                    MatRowSwap(M,j,row)
                    MatRowSwap(B,j,row)
                    ind=True
                    break
            if ind==False :
                col+=1
                row+=1
    return
