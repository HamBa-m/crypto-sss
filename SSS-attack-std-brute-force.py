#copyrights 2021 Hamza Ba-mohammed
#fonction pour calculer la puissance n-ième de x mod p
def modPow(x,n,p):
    if n==0 : return 1
    u=modPow(x,int(n/2),p)
    u=(u*u)%p
    if n%2==1 : u=(u*x)%p
    return u

#fonction pour calculer l'inverse p-modulaire de x (APP du petit théorème de Fermat)
def modInv(x,p):
    return modPow(x,p-2,p)

#fonction pour interpoler un polynome de degrée k-1 dans Z/pZ
def lagrangeInterpolMod(Xdata,Ydata,k,p):
    msg=0
    for e in range(k) :
        nominator=1
        denominator=1
        for x in range(k) :
            if x!=e :
                denominator*=((Xdata[e]-Xdata[x]))
                denominator=(denominator%p)
                nominator*=(-Xdata[x])
                nominator=(nominator%p)
        msg+=(Ydata[e]*nominator*modInv(denominator,p))%p
        msg%=p
    return msg

k=4 #on fixe k=4
p=int(input('le module de codage: '))
target=int(input('le message secret: '))

P=[0]*k
found=False 
import time
begin = time.time()
for i in range(p): #boucles imbriquées de force brute
    P[0]=i
    for j in range(p):
        P[1]=j
        for n in range(p):
            P[2]=n
            for l in range(p):
               P[3]=l
               cle=[0]*k
               for m in range(1,k+1):
                   for a in range(k):
                       cle[m-1]+=(P[a]*(m**a))
               x=[i for i in range(1,k+1)]
               secret=lagrangeInterpolMod(x,cle,k,p)
               if target==secret :
                   time.sleep(1)
                   end = time.time()
                   print('chiffrement cassé dans' ,end - begin,' secondes.')
                   found=True
                   break
            if found : break
        if found : break
    if found : break
