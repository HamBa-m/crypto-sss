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

#corps du programme : décryptage modulaire
print("SIMULATION DU DECRYPTAGE PAR SHAMIR'S SECRET SHARING")
print()
k=int(input("insérez le nombre minimum de clées nécessaires pour décrypter le chiffrement: "))
p=int(input("insérez le module des clées : "))
print("insérer la première partie des",k,"clés modulaires séparés par des espaces: ")
Xdata=list(map(int,input().split()))
print("respectivement insérer la deuxième partie des",k,"clés modulaires: ")
Ydata=list(map(int,input().split()))
print()
print("Message décrypté avec succès.")
print("Le message crypté est:", lagrangeInterpolMod(Xdata,Ydata,k,p))
