#Kristjan Mustkivi
#10.01.2024

import random
import datetime



#Mündid

fail = open("mundid.txt", encoding ="utf-8")
kassa= 0
for mynt in fail:
    if int(mynt) <10:
        kassa+=int(mynt)
    
print (kassa)  




"""
#tervitused mõtisklustega

def tervitus(jrk):
    print('võõrustaja: "Tere!"')
    print(f"Täna {jrk} . Kord terivitada mõtiskleb võõrustaja.")
    print('külaline: Tere, suur täna kutse eest!"')
    
    kylaliste_arv = int(input("Mitu inimest on kutsutud:"))
    for i in range (1, kylaliste_arv):
     tervitus(i+1)
     """


"""
#Peo eelarve 

def eelarve(arv):
    kogusumma  = arv * 10 + 55
    return kogusumma

kylaliste_arv = int(input("Mitu inimest on kutsutud:"))
kylaliste_arv_tegelik = int(input("Mitu inimest tuleb:"))
print(f"MAX eelarve: {eelarve(kylaliste_arv)}")
print(f"MIN eelarve: {eelarve(kylaliste_arv_tegelik)}")
                
print(f"Eelarve:{eelarve(5)}")
"""


"""
#õunamahl
def mahlapakkide_arv(kg):
    mahlapakkidearv = round(kg * 0,4 / 3)
    return mahlapakkidearv
ountekogus = float(int(input("Sisesta õunte kogus:")))
print(mahlapakkide_arv(ountekogus))
"""



"""
#banner
def banner(l):
    def banner(l):
            print(l.upper())
kord =int (input("Mitu korda: "))
tekst = input ("Lisa tekst: ")
for i in range (kord):
    banner(tekst)
banner()

"""