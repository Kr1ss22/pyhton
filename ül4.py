#Kristjan Mustkivi
#21.11.2023
#Ülesanne 04
#KUUBID
for i in range(1,11):
    print(f"{i:2} {i**2:4} {i**3:4}")







#PANK
raha = 10000
konto = raha
aastad = 5
intress = 0.05

print(f"Aasta Algsumma Intress Aasta lõouks")
for i in range(aastad):
    print(f"{i+1:<7}{konto:.2f} {konto*0.05:9.2f} {konto + konto * intress:13.2f}")
    konto = konto + konto * intress

print(f"summa kokku: {round(konto,2)}")
print(f"Kasum: {round(konto-raha,2)}")





#WHILE+FOR -arvamismäng
input()
import random
loop= 1
KordadeArv = 0 
while loop==1:
    KordadeArv +=1
    print(f"Katse: {KordadeArv}")
    print("Arva arv 1-10 \n--------------------")
    SuArv = random.randint(1 ,10)
   # print(SuArv)
    for i in range (3):
        vastus=int(input("Sinu arv: "))
        if SuArv == vastus:
            print("Arvasid ära")
            break
        else:
            print("Proovi veel")
    print("Game over")
    uusMang = input("Soovid uut mängu? jah/ei:")
    if uusMang == "ei":
        loop = 0




input()

#Viisikud
#Programm väljastab ainult 5ga jaguvad arvud 1-100

for i in range(1,51):
    if i % 5 ==0:
        print(i)


"""
Pisike korrutustabel
Koosta programm, mis tekitab automaatselt viiega korrutustabeli.

"""
arv=5
for i in range(1,11):
    print(f"5 x {i} = {arv*i}")



"""
Paaris ja paaritu
Loo tsükkel, mis genereerib arvud 1-100 koos vastava tekstiga, kas arv on paaris või paaritu
"""
#paaris,#paaritu
for arv in range(11):
    if arv % 2 == 0:
        v = "paaris"
    else:
        v = "paaritu"
    print(arv, v)





import random
#print(f"Tere {nimi} {pnimi}!")

# loto
for i in range(5):
    print(random.randint(0, 9),end="")




print()
#tärnid
k=5
for i in range (6):
    print("* " * k)
    k=k-1




print()
k=5
for i in range (1,k+1):
    print("* " * i)
print()


"""
tärnid
"""
ruut=5
for i in range (ruut+1):
    print("* " * ruut)


"""
algpalli meeskond
Sa pead looma programmi, mis kontrollib kas kandideerija sobib antud meeskonda.
Vanus peab jääma vahemikku 16-18 ning lubatud on ainult meessugu.
Täienda programmi nii, et kui kandideerija on naissoost, siis vanust üldse ei küsita.
"""
sugu = "n"
vanus =22

if sugu == "m":
    if vanus>=16 and vanus<=18:
        print("pääaseb meeskonda!")
    else:
        print("vanus ei sobi")
else:
    print("Sugu ei sobi!")

"""
Müük
Kasutaja sisestab toote hinna. Kui see on hinnaga kuni 10€, saab ta allahindlust 10%. Üle 10€ tooted saavad soodukat 20%.
Kuva toote lõplik hind. Plokkskeemi pole vaja!
"""

toote_hind = int(input("Sisesta toote hind: "))

if toote_hind <= 10:
    allahindlus_protsent = 10
else:
    allahindlus_protsent = 20

allahindlus_summa = (allahindlus_protsent / 100) * toote_hind
loplik_hind = toote_hind - allahindlus_summa

print(f"Lõplik hind pärast {allahindlus_protsent}% allahindlust on {loplik_hind}€.")

"""
Juubel
Kasutaja sisestab oma sünnipäeva ja sinu programm ütleb, kas tegemist on juubeliga.
"""
a=10
if a % 5 == 0:
    v = "on"
else:
    v = "ei ole"
    
print(f"Vanus: {a} {v} juubel")

"""
Matemaatika
    Kasutaja sisestab kaks arvu ning programm küsib kasutajalt, mis tehet ta soovib (+-*/) ning viib kasutaja valiku ellu.
"""
"""
arv1 = int(input("Sisesta külg1:"))
arv2 = int(input("Sisesta külg2:"))
tehe = input("Vali tehe (+ - * /):")

if tehe == "+":
    vastus = arv1+arv2
elif tehe == "-":
    vastus = arv1-arv2
elif tehe == "*":
    vastus = arv1*arv2
elif tehe == "/":
    vastus = round(arv1/arv2,2)
else:
    Vastus = "tehet ei saa teha"

print(f"{arv1} {tehe} {arv2} = {vastus}")

"""



"""
Ruut
    Kasutaja sisestab ruudu küljed ning programm tuvastab kas tegemist saab olla ruuduga.
"""

arv1 = input("Sisesta külg1:")
arv2 = input("Sisesta külg2:")
if arv1 == arv2:
    print("Võimalik, et saab ruudu")
else:
    print("Nii ei saa ruutu teha")
    
    
