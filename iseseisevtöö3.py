#Kristjan Mustkivi  
#10.01 2024

import random
import datetime
#from  datetime import *

#tahvli juurde

fail = open("nimekiri.txt", encoding ="utf-8")

p = (datetime.datetime.now().day)
 nr = 1
for rida in fail:
    if nr==p:
    jrk = int(input("\tahvli ette tuleb::"))
    nr+=1















""""
#jukebox
failinimi = input("Palun sisestage failinimi: ")

fail = open ( failinimi, encoding ="utf-8")
nr = 1
for rida in fail:
    print(f"{nr}. {rida}",end="")
    nr+=1
fail.seek(0)
nr = 1
jrk = int(input("\nValike laulu järjekorrda number:"))
fail.seek(jrk)
for rida in fail:
    if nr==jrk:
        print(f"Mängitab muusika pala on: {rida}","")
    nr+=1
"""


