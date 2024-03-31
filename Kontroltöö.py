#Kristjan Mustkivi
#16.01.2024
import random

#2. Vanused
# vanused = [10,60,40,30,20,25,35]

def vanuste_stat(vanused):
    print(max(vanused))
    print(min(vanused))
    print(sum(vanused))
    average=float(sum(vanused))/float(len(vanused))
    print(round(average))

    vanuste_stat(vanused)



#4.# Take a list and write a program that prints out all the elements of the list that are less than 5. 1p
	# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list. 1p
	# Write this in one line of Python. 1p
	# # Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user. 1p
	
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

 def vaiksem_kui_viis(a):
     uus_list = []
     for i in a: uus_list.append(i) if i < 10 else None
     print(uus_list)
 print(a)
 lisa = int(input("Sisesta arv, mida soovite lisada tabelisse: "))
 a.append(lisa)
 vaiksem_kui_viis(a)


#6 Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris vĆµi paaritu
	# kuvatakse korrektne arusaadav kĆ¼simus ja vastus - 1p
	# eelnev kontroll, kas kasutaja ei lisanud arvu vĆµi pani nulli - 1p
	# kood mis teavitab paaris vĆµi paaritust arvust - 1p
	# kuvatakse programmi pealkiri - 1p
	# kood kommenteeritud - 1p

def paaris_paaritu():
     print("Kas teie sisestatud arv on paaris või paaritu?")
     arv = input("Sisesta arv: ")
     if arv == "":
         print("Te ei sisestanud midagi")
     elif int(arv) == 0:
         print("Null on paaris arv")
     elif int(arv) % 2 == 0:
         print("Arv on paaris")
     else:
         print("Arv on paaritu")
         paaris_paaritu()

# 8. TÃ¤ringud
# 	kuvatakse korrektne arusaadav kÃ¼simus ja hiljem vastus - 1p
# 	kasutaja vÃµistleb kahe tÃ¤ringuga arvuti vastu - 1p
# 	kasutaja teeb pakkumise ning suurima tÃ¤ringupunktisumma vÃµitja saab laual oleva raha endale - 2p
# 	kood kommenteeritud - 1p
    
    def taringumang():
     print("Tere tulemast täringumängu!")
     panus = int(input("Palun sisestage oma panus: "))
     print("Teie panus on ", panus, " eurot")
     print("arvuti viskab täringuid...")
     ab = random.randint(1,6)
     ac = random.randint(1,6)
     taring = ab+ac
     vastus = int(input("Arvake ära mitu tärni arvuti viskas: "))
     raha = panus*2
     if taring==vastus:
         print("Teie võitsite! Te võitsite ", raha, " eurot")
     else:
        print("Arvuti võitis, õige vastus oli", taring, "! Te kaotasite ", panus, " eurot")

    taringumang()
    
    # 10. KaugushÃ¼pe
	# kasutaja sisestab 3 kaugushÃ¼ppe tulemust - 1p
	# sinu programm leiab ning vÃ¤ljastab parima ja keskmise tulemuse - 2p
	# programmi dialoog kasutajaga on arusaadav ja Ã¼heselt mÃµistetav - 1p
	# kood kommenteeritud - 1p

    def kaugushupe():
     tulemused = []
     for i in range(3):
         tulemus = float(input("Sisesta kaugushüppe tulemus: "))
         tulemused.append(tulemus)
     print("Parim tulemus on ", max(tulemused), "m")
     print("Keskmine tulemus on ", sum(tulemused)/len(tulemused), "m")
    kaugushupe()

# 12. Eurokalkulaator
# 	Koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK vÃµi EEK->EUR.
# 	Oluline on kasutada kahte funktsiooni!!
    
    def eur_eek():
        summa = int(input("Sisestage summa eurodes: "))
        print(summa*15.6466, "krooni")
    def eek_eur():
        summa = int(input("Sisestage summa kroonides: "))  
        print(summa/15.6466, "eur")

valik = input("Kas soovite teisendada Eurosid[EUR] või Kroone[EEK]: ")
if valik == "EUR":
                    eur_eek()
elif valik == "EEK":
                    eek_eur()
else:    
                     print("Vale valik!")

    # 14 Palkade vÃµrdlus - Loo palk.txt fail tÃ¶Ã¶tajate nime, soo ja palganumbriga (10 tÃ¶Ã¶tajat).
	#Koosta programm, mis analÃ¼Ã¼sib kas firmas toimub diskrimineerimist soo jÃ¤rgi. Selleks vÃµrdle omavahel meeste ja naiste palkade keskmiseid, samuti meeste ja naiste kÃµige kÃµrgemat palka. Programm peab tegema otsuse.
     
def palgad():
        fail = open("palgad.txt", encoding="UTF-8")
        mehed = []
        naised = []
        for rida in fail:
                osad = rida.split()
                if osad[2] == "m":
                    mehed.append(int(osad[3]))
                else:
                        naised.append(int(osad[3]))
                fail.close()
                meeste_keskmine = sum(mehed)/len(mehed)
                meeste_max = max(mehed)
                naiste_keskmine = sum(naised)/len(naised)
                naiste_max = max(naised)
                print("Meeste keskmine palk on", meeste_keskmine)
                print("Naiste keskmine palk on", naiste_keskmine)
                print("Meeste kõrgeim palk on", meeste_max)
                print("Naiste kõrgeim palk on", naiste_max)
                if meeste_keskmine > naiste_keskmine and meeste_max > naiste_max:
                    print("Firmas toimub diskrimineerimist soo järgi")
                else:
                    print("Firmas ei toimu diskrimineerimist soo järgi")

                palgad()

# 16. TÃ¤ringud
# 	Kasutaja vÃµistleb kahe tÃ¤ringuga arvuti vastu. Kasutaja teeb pakkumise ning suurima tÃ¤ringupunktisumma vÃµitja saab laual oleva raha endale juurde. MÃ¤ng kestab kuni kummalgi on raha otsas.
# 	(Vihjed: kÃ¼si kasutajalt nime, kuva pidevalt konto seisu ja tÃ¤ringuviskeid, kasutajate raha hulga mÃ¤ngu alguses mÃ¤Ã¤rad sina)
     
def taringu_mang():
                raha = 100
                arvuti_raha = 100
                nimi = input("Sisesta oma nimi: ")
                print("Tere", nimi, "!")
                while raha > 0 and arvuti_raha > 0:
                    print("Sul on", raha, "€ ja arvutil on", arvuti_raha, "€.")
                    panus = int(input("Sisesta panus: "))
                    if panus > raha:
                        print("Sul ei ole nii palju raha!")
                        continue
                enter = input("Vajuta enterit, et täringuid veeretada.")
                taring = random.randint(1,6)
                print("Sul tuli", taring, "silma.")
            
                def taringu_mang():
                    raha = 100
                    arvuti_raha = 100
                    nimi = input("Sisesta oma nimi: ")
                    print("Tere", nimi, "!")
                    while raha > 0 and arvuti_raha > 0:
                        print("Sul on", raha, "€ ja arvutil on", arvuti_raha, "€.")
                        panus = int(input("Sisesta panus: "))
                        if panus > raha:
                            print("Sul ei ole nii palju raha!")
                            continue
                        enter = input("Vajuta enterit, et täringuid veeretada.")
                        taring = random.randint(1,6)
                        print("Sul tuli", taring, "silma.")
                        arvuti_taring = random.randint(1,6)
                        print("Arvutil tuli", arvuti_taring, "silma.")
                        if taring > arvuti_taring:
                            print("Sina võitsid!")
                            raha += panus
                            arvuti_raha -= panus
                        elif taring < arvuti_taring:
                            print("Arvuti võitis!")
                            raha -= panus
                            arvuti_raha += panus
                        else:
                            print("Viik!")  
                                
                taringu_mang()