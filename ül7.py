#Kristjan Mustkivi
#5.12.23
import math
def kera(r):
    v=round((4*math.pi*r**3)/3,2)
    print(f"Kera ruumala on {v}")

def kuup(a):
    v = a**3
    print(f"Kuubi ruumala on {v}")
def koonus (r, h):
    print(f"Koonuse ruumala on")
def silinder (r, h):
    print(f"Silindri ruumala")

loop = 1
while loop ==1:
    print ("********** MEGA HEA KALK **********")
    print("1.Kera\n2.Kuup\n3.Koonus\n4.Silinder\n5.EXIT\n")
    valik = int(input("Sisest valik:"))
    print("****************************************")

    if valik==1:
        r = int(input("Sisesta kera raadius"))
        kera(r)
    elif valik==2:
        k = int(input("Sisesta kuubi 1 külg"))
        kuup(k)
    elif valik==3:
        koonus(r, h)
    elif valik==4:
        silinder(r, h)
    else:
        loop = 0
        print("täname, et kasutasite meie mega head kalkulaatortit")












"""

def tervita(nimi, keel="ge"):
    if keel== "en":
        print(f"Hi  {nimi}!")
    elif keel== "et":
     print (f"Hallo {nimi}!")
    else: print(f"Hallo {nimi}!")


tervita ("Märt" ,"en")
tervita ("Märt" ,"et")
tervita ("Märt" ,"edasdasdasdadadad")
tervita ("Märt")
"""