#fonctions de cryptage SSS
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
            x*=y
        modkey[y]=((temp+coef[0])%p)
    return modkey

#corps du programme de cryptage SSS
print("CREATION D'UN COMPTE BANCAIRE MULTI-PROPRIETAIRES")
print("-------------------------------------------------")
k=int(input("insérez le nombre minimum de personnes nécessaires pour autoriser l'accès: "))
n=int(input("insérez le nombre de clées à générer: "))
primes=generatePrimes()
p=random.choice(list(primes))
coef=generatePoly(k,p)
modkey=generateKeysMod(coef,n,p)
import sqlite3
conn = sqlite3.connect('database.sq3')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     key INTEGER,
     deg INTEGER,
     mod INTEGER)""")
conn.commit()
cursor.execute("""INSERT INTO users(id, key, deg, mod) VALUES(?, ?, ?, ?)""", (1, coef[0],k,p))
print()
print("LES", n,"CLES PRIVEES: ")
for e in modkey:
    print(e,end=" ")
print()
for e in modkey:
    print(modkey[e],end=" ")
print()
print("VOTRE IDENTIFIANT: ", 1)
print()
print('------------------------------------------------------------------------')
#fonctions de décryptage SSS
#fonction pour calculer la puissance n-ième de x mod p en temps logarithmique
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

#corps du programme de décryptage SSS
print("AUTHENTIFICATION BANCAIRE")
print("-------------------------")
print("insérer votre identifiant: ")
idd=int(input())

import sqlite3
conn = sqlite3.connect('database.sq3')
cursor = conn.cursor()
cursor.execute("""SELECT key, deg, mod FROM users WHERE id=?""", (idd,))
user = cursor.fetchone()

print("insérer la première partie des",user[1],"clés modulaires séparés par des espaces: ")
Xdata=list(map(int,input().split()))
print("respectivement insérer la deuxième partie des",user[1],"clés modulaires: ")
Ydata=list(map(int,input().split()))
print()
msg=lagrangeInterpolMod(Xdata,Ydata,user[1],user[2])

if msg==user[0] : print("ACCES OUVERT AU COMPTE BANCAIRE.")
else : print("CLEES ERONNEES !")
conn.close()
