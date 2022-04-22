#fonction pour générer l'ensemble des nombres premiers INTER [100000,n]
def generatePrimes():
    n=int(1e7)
    prime=[1]*(n+1)
    prime[0]=0
    prime[1]=0
    for i in range(2,n+1):
        if prime[i]==1 :
            for j in range(i*2,n+1,i):
                prime[j]=0
    primes=set()
    for i in range(100000,n+1):
        if prime[i]==1 : primes.add(i)
    return primes

#fonction pour générer un polynome de degré k-1 sur Z/pZ
import random
def generatePoly(k,p):
    coef=[0]*k
    for i in range(k):
        coef[i]=random.randrange(0,p-1)
    return coef

#fonction pour générer n clées privées p-modulaires
def generateKeysMod(coef,n,p):
    modkey=dict()
    for i in range(1,n+1):
        x=i
        y=x
        temp=0
        for j in range(1,len(coef)):
            temp+=(coef[j]*x)
            x*=x
        modkey[y]=((temp+coef[0])%p)
    return modkey

#corps du programme : cryptage modulaire
print("SIMULATION DU CRYPTAGE PAR SHAMIR'S SECRET SHARING")
print("--------------------------------------------------")
k=int(input("insérez le nombre minimum de clées nécessaires pour décrypter le chiffrement: "))
n=int(input("insérez le nombre de clées à générer: "))

primes=generatePrimes()
p=random.choice(list(primes))

coef=generatePoly(k,p)
modkey=generateKeysMod(coef,n,p)

print()
print("LES", n,"CLES PRIVEES: ")
for e in modkey:
    print(e,modkey[e])
