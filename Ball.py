import time

width = 80
height = 23
leng = width * height

dikeyhareket = -160 # dikey hareket miktar
yatayhareket = 2;#yatay hareket miktarı
sütun=40;#2ile78 arası
satır=2;#2ile22 arası
sütunsayac=2;#sütun takip hızı
satırsayac=-2;#satır takip hızı
desensayac=0;# hangi desen basılacak, her desen aynı sırada basılacağı bilgisi kullanılarak
columns=[39,40,41,120,199,201]
pattern = "\\O/|/\\"

def desen():
    global desensayac
    desensayac = ( desensayac + 1)  % len(pattern)

    return [desensayac - 1]


def main():
    while 1:

        Matrix = [desen() if x in columns else ' ' for x in range(leng)]
        print("".join(Matrix))

        gecici=columns
        if(satır<=2):
            dikeyhareket*=(-1)
            satırsayac*=(-1)
        if(satır>=22):
            dikeyhareket*=(-1)
            satırsayac*=(-1)
        if(sütun<=2):
            yatayhareket*=(-1)
            sütunsayac*=(-1)
        if(sütun>=76):
            yatayhareket*=(-1)
            sütunsayac*=(-1)
        sütun+=sütunsayac
        satır+=satırsayac
        columns = [x+dikeyhareket+yatayhareket for x in gecici]
        time.sleep(0.09)


if __name__=='__main__':
    main()
