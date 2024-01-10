#Kristjan Mustkivi
#21.11.2023
#Ülesanne 03

#print(f"Tere {nimi} {pnimi}!")

"""
PALINDROOM
"""
tekst=input("Sisesta sõna palindroomi kontrolliks:")
print(tekst==tekst[::-1])


"""
Tundide ajad
    Kasutaja sisestab tundide alguse ja lõpu. Näiteks 8:30 ja 14:15
    Sinu programm leiab, kui pikk oli õpilase päev
    Väljasta täislause ja kasuta vormindamisel format() meetodit.
"""
algus=input("Sisesta algusaeg:")
lopp=input("Sisesta lõpuaeg:")

#aja tükeldamine
h1, m1= algus.split(":")
h2,m2 = algus.split(":")

#tee,e aja minutiteks
minutid1= int(h1) * 60+int(m1)
minutid2= int(h2) * 60+int(m2)
ajavahe = minutid2-minutid1
#minutid kellaajaks
hh1 = ajavahe // 60
mm1 = ajavahe % 60

print(f"Päeva pikkus on {hh1}:{mm1}")







"""
Email
    Küsi kasutajalt emaili ja kontrolli, kas see sisaldas @-märki.
    Näiteks: sisend–>minu@mail.ee; väljund–> True või False
"""
email=input("Trüki oma email:")
print(f"On email{'@'in email}")


"""
Vandumine
Kui kasutaja sisestab “kogemata” teksti, kus leidub sõna ‘kurat’, siis sinu programm asendab need tärnidega.
Näiteks: sisend–>Kurat küll!; väljund–>*** küll!
"""
tekst=input("Trüki kurat küll: ")
print(f"{tekst.replace('kurat','***')}")



"""
Korralik nimi
Küsi kasutajalt nime
Tervita teda ja sinu programm väljastab nime kirjapildi õigesti – suure algustähega ja eemaldab ülearused tühikud
Näiteks: sisend–>mARiO; väljund–>Tere, Mario!
"""
nimi=input("Ütle oma nimi: ")
print(f"Tere, {nimi.strip().capitalize()}!")
