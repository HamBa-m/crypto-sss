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
conn = sqlite3.connect('database.db')
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
else : print("CLEES ERONNEES !",key,msg)

