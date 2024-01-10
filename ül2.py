# Kristjan Mustkivi
#14.11.2023
#ülesanne 02

"""
kilpkonn küsib kasutajalt, kui suurt ruutu tahad ja joonistab ruudu (kasuta funktsiooni)
"""
import turtle
w = turtle.Screen()
def ruut(k):
    john = turtle.Turtle()
    for i in range(4):
        john.fd(k)
        john.rt(90)
   
kylg = w.numinput("Joonistame ruudu","sisesta ruudu kylje pikkus:")
ruut(kylg)





turtle.exitonclick()

"""
Kütusekulu arvutamine
    Kasutaja sisestab tangitud kütuse liitrid
    Kasutaja sisestab läbitud kilomeetrid
    Programm leiab kütusekulu 100km kohta keskmiselt
"""
l=int(input("lisa tangitud kütuse kogus liitrites"))
km=int(input("Lisa läbitud kilomeetrid: "))
kytusekulu= l /(km / 100)
print("sinu masin võtab keskmiselt",kytusekulu,"liitrit 100km")


"""
Arvusüsteemid
Kasutaja sisestab täisarvu kümnendsüsteemis
Sinu programm teisendab selle 2nd ja 16nd süsteemi
"""
arv = int(input("Sisesta 10nd arv: "))
bii=bin(arv)
heks=hex(arv)
print("kümnendarv",arv,"kahendsüsteemis",bii,"ja kuueteistkümnednsüsteemis",heks)


"""
Ajateisendus
    Kasutaja sisestab aja minutites
    Sinu valem leiab ja väljastab tunnid ja minutid
    Näiteks: sisestus 72, vastus 1:12
"""
aeg=int(input("Sisesta aeg minutites: "))
h=aeg//60
m=aeg % 60
print(h,":",m)


"""
    Leia kolmnurga hüpotenuus
    Kolmnurga külgede pikkused on a=16 ja b=9
    Kasuta Pythagorase teoreemi (a2 + b2 = c2) ja leia kolmnurga hüpotenuus
"""
a,b= 16,9
c=sqrt(a**2+b**2) 
print("Vastus:",c)


"""
Rulluisutajad
    Rulluisutaja keskmine kiirus on 29,9km/h
    Kui kaugele jõuab 24minutiga
"""
kiirus=29.9
aeg=24
Tee_Pikkus=kiirus /60*aeg
print("kaugus",round)(tee_pikkus,2);"km"



"""
Pitsa
    Võtsite 3 sõbraga suure pitsa hinnaga 12,90€
    Jätate teenindajale 10% jootraha
    Koosta programm, mis leiab kui palju peab igaüks maksma
"""
sobrad=3
hind=12.9
tip=0.1
kokku= (hind * tip + hind) / sobrad
print("Igaüks maksab "+str(kokku)+"€")



"""
Toote hind
    Toote hind 36,75€
    Soodushind hetkel 40%
    Soovin kolme toote summat
"""
hind=36.75
soodus=0.4
kogus=3


"""
Arvutame komnurga ümbernöödu
Loo kolm täisarvulist muutujat a, b, c
Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
"""

a=5
b=10
c=15
p=a+b+c
print("Kolmnurga ümbermööt on:",p)


 