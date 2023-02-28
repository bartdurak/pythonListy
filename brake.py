"""
brake
"""


wynik = 0
i= 0

while i<3:
    x= int(input( "Podaj dodatnią liczbę: "))
    if (x> 0):
        wynik+= x
    else:

        print("Miała być liczba dodatnia , kończymy za karę: ")
        continue
    print("Aktualny wynik dodawaia to", wynik)
    i+=1

