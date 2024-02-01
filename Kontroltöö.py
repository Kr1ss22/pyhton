#Kristjan Mustkivi
#16.01.2024

#1. Korrutamise kontrollimine

import random

õiged_vastused = 0
küsimuste_arv = 10

for _ in range(küsimuste_arv):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    õige_vastus = a * b

    tehe = f"{a} * {b}"
    kasutaja_vastus = input(f"{tehe} = ? ")

    if kasutaja_vastus.isdigit() and int(kasutaja_vastus) == õige_vastus:
        print("Õige!")
        õiged_vastused += 1
    else:
        print(f"Vale! Õige vastus oli {õige_vastus}.")

print(f"Sa said {õiged_vastused} õiget vastust {küsimuste_arv} küsimusest.")

#2. Vanused

def leia_suurem_väiksem_summa_keskmine(vanused):
    if not vanused:
        print("Vanuste loend on tühi.")
        return

    suurim = max(vanused)
    väikseim = min(vanused)
    kogusumma = sum(vanused)
    keskmine = kogusumma / len(vanused)

    print(f"Suurim vanus: {suurim}")
    print(f"Väikseim vanus: {väikseim}")
    print(f"Kogusumma: {kogusumma}")
    print(f"Keskmine vanus: {keskmine}")

vanused = [20, 12, 40, 34, 11, 16, 7]
leia_suurem_väiksem_summa_keskmine(vanused)

#4.# Take a list and write a program that prints out all the elements of the list that are less than 5. 1p
	# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list. 1p
	# Write this in one line of Python. 1p
	# # Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user. 1p
	
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def vähem_kui_viis():
    new_list = []
    for i in a: new_list.append(i) if i < 5 else None
    print (new_list)
    print(a)
    add = int(input("Sisesta number: "))
    a.append(add)
    vähem_kui_viis()


#6 Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris vĆµi paaritu
	# kuvatakse korrektne arusaadav kĆ¼simus ja vastus - 1p
	# eelnev kontroll, kas kasutaja ei lisanud arvu vĆµi pani nulli - 1p
	# kood mis teavitab paaris vĆµi paaritust arvust - 1p
	# kuvatakse programmi pealkiri - 1p
	# kood kommenteeritud - 1p

kasutaja_arv = int(input("Sisesta arv: "))

if kasutaja_arv == 0:
    print("Sisestasid nulli. Palun sisesta mõni muu arv.")
elif kasutaja_arv % 2 == 0:
    print("Sisestatud arv on paaris.")
else:
    print("Sisestatud arv on paaritu.")







