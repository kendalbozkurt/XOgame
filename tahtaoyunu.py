tahta = [["___", "___", "___"],
         ["___", "___", "___"],
         ["___", "___", "___"]]

print("\n"*15) # ekrandaki boşluğu sağlamak amacıyla

for i in tahta:
    print("\t".expandtabs(30), *i, end="\n"*2)  #tahtayı yazdırmak

kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
                     [[0, 1], [1, 1], [2, 1]],
                     [[0, 2], [1, 2], [2, 2]],
                     [[0, 0], [0, 1], [0, 2]],
                     [[1, 0], [1, 1], [1, 2]],
                     [[2, 0], [2, 1], [2, 2]],
                     [[0, 0], [1, 1], [2, 2]],
                     [[0, 2], [1, 1], [2, 0]]] # kazanma koordinatları

x_durumu = [] #x ve o nun bulunduğu konumları tutan listeler
o_durumu = []

sıra = 1
while True:
    if sıra % 2 == 0:
        işaret = "X".center(3)
    else:
        işaret = "O".center(3)

    print()
    print("İŞARET: {}\n".format(işaret))
    
    x = input("yukarıdan aşağıya(1,2 veya 3 giriniz)(exit q) : ")#x konumunu alıyoruz
    if x == "q":
        break

    y = input("soldan sağa(1,2 veya 3 giriniz(exit q)): ")#y konumunu alıyoruz
    if y == "q":
        break

    x = int(x)-1 #atama işlemi
    y = int(y)-1

    print("\n"*15)

    if tahta[x][y] == "___":#tahta da boş ise
        tahta[x][y] = işaret #işareti oraya ata
        if işaret == "X".center(3):
            x_durumu += [[x, y]] #Sıra X te ise x durumuna ata koordinatları
        elif işaret == "O".center(3): #O da ise o durumuna ata koordinatları
            o_durumu += [[x, y]]
        sıra += 1 #sırayı arttırıyoruz çünkü bir X giricek bir O 
    else:
        print("\nORASI DOLU! TEKRAR DENEYİN\n") #tahtadaki konum dolu ise

    for i in tahta:
         print("\t".expandtabs(30), *i, end="\n"*2) #tajtanın güncellenmiş hali yazdırılır

    for i in kazanma_ölçütleri:  # burda ise durumlar kontrol edilir koordinatlar kazanma koordinatları ile eş ise mesaj verilir
        o = [z for z in i if z in o_durumu]
        x = [z for z in i if z in x_durumu] 

        if len(o) == len(i):
            print("O KAZANDI!")
            quit()
        if len(x) == len(i):
            print("X KAZANDI!")
            quit()

