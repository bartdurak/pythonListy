# czym są listy?

imiona= ["Arkadiusz", "janusz", "Mateusz", "Mate "]
liczby =[ 1, 54, -2, 20]
mieszane = [1,"aa", 52,"k"]


#for imie in imiona:
#    print(imie)
# wyświetla wybrane elementy z listy imiona 1, 2, 3
print (imiona[1], imiona[2], imiona[3])

# liczy elemennty w liście (imiona[1], imiona[2], imiona[3])
print(len(imiona))

# funkcje append rozszerzająca na kolejność elementów
imiona.append(liczby[0])
print(imiona)

