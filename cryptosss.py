#fonction pour générer un polynome de degré k-1
import random
def generatePoly(k):
    coef=[0]*(k-1)
    for i in range(1,k-1):
        coef[i]=random.randrange(1,1e5+1)
    return coef

#fonction pour insérer le message secret
def insertSecretMsg(coef,msg):
    coef[0]=msg
    return

#fonction pour générer n clées privées
def generateKeys(coef,n):
    key=dict()
    for i in range(n):
        x=random.randrange(1,1e5+1)
        temp=0
        for j in range(1,len(coef)):
            temp+=(coef[j]*x)
            x*=j
        key[x]=temp+coef[0]
    return key

#fonction pour générer l'ensemble des nombres premiers INTER [0,n]
def generatePrimes(n):
    n=int(n)
    prime=[1]*(n+1)
    prime[0]=0
    prime[1]=0
    for i in range(2,n+1):
        if prime[i]==1 :
            for j in range(i*2,n+1,i):
                prime[j]=0
    primes=set()
    for i in range(n+1):
        if prime[i]==1 : primes.add(i)
    return primes

#fonction pour générer n clées privées modulaires
def generateKeysMod(coef,n,p):
    modkey=dict()
    for i in range(n):
        x=random.randrange(1,p)
        temp=0
        for j in range(1,len(coef)):
            temp+=(coef[j]*x)
            x*=j
        modkey[x]=((temp+coef[0])%p)
    return modkey
