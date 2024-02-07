import random
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
                 