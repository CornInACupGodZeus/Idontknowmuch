import time

width = 80
height = 23
leng = width * height

dikey_hareket = -160 # dikey hareket miktar
yatay_hareket = 2 #yatay hareket miktarı
sutun = 40 # 2 ile 78 arası
satir = 2 # 2 ile 22 arası
sutun_sayac = 2 # sütun takip hızı
satir_sayac = -2 # satır takip hızı
desen_sayac = 0 # hangi desen basılacak, her desen aynı sırada basılacağı bilgisi kullanılarak
columns =[39,40,41,120,199,201]
pattern = "\\O/|/\\"

def desen():
    global desensayac
    desen_sayac = ( desen_sayac + 1)  % len(pattern)

    return [desen_sayac - 1]


def main():
    while 1:

        Matrix = [desen() if x in columns else ' ' for x in range(leng)]
        print("".join(Matrix))

        gecici=columns
        if(satır<=2):
            dikey_hareket*=(-1)
            satir_sayac*=(-1)
        if(satır>=22):
            dikey_hareket*=(-1)
            satir_sayac*=(-1)
        if(sütun<=2):
            yatay_hareket*=(-1)
            sutun_sayac*=(-1)
        if(sütun>=76):
            yatay_hareket*=(-1)
            sutun_sayac*=(-1)
        sütun+=sütunsayac
        satır+=satırsayac
        columns = [x+dikeyhareket+yatayhareket for x in gecici]
        time.sleep(0.09)


if __name__=='__main__':
    main()
