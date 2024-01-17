kasutaja_arv = int(input("Sisesta arv: "))

if kasutaja_arv == 0:
    print("Sisestasid nulli. Palun sisesta mõni muu arv.")
elif kasutaja_arv % 2 == 0:
    print("Sisestatud arv on paaris.")
else:
    print("Sisestatud arv on paaritu.")
