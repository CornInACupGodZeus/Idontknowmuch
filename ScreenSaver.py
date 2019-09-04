import time

#desen_sayac = 0 # hangi desen basılacak, her desen aynı sırada basılacağı bilgisi kullanılarak

class sayac:
    desen=0
    def __init__(self):
        self.desen = 0
    def __setattr__(self,desen,girdi):
        super().__setattr__(desen,girdi)
    def __call__(self):
         return desen

def desen(d_sayac):
    pattern = "\\O/|/\\"
    sarmasik= "»♥♥»♥»»♥»♥♥/♥»♥♥»♥♥♥»♥"
    d_sayac.__setattr__('desen',( d_sayac.desen + 1)  % len(sarmasik))


    return sarmasik[d_sayac.desen - 1]


def main():
    width = 80
    height = 23
    leng = width * height
    d_sayac=sayac()
    dikey_hareket = -160 # dikey hareket miktar
    yatay_hareket = 2 # yatay hareket miktarı
    sutun = 40 # 2 ile 78 arası
    satir = 2 # 2 ile 22 arası
    sutun_sayac = 2 # sütun takip hızı
    satir_sayac = -2 # satır takip hızı
    #columns = [39,40,41,120,199,201]
    columns = [40,119,120,121,198,199,200,201,278,279,280,281,358,359,360,361,439,440,520,521,600,679]
    while 1:

        Matrix = [desen(d_sayac) if x in columns else ' ' for x in range(leng)]
        print("".join(Matrix))

        gecici=columns
        if(satir<=2):
            dikey_hareket*=(-1)
            satir_sayac*=(-1)
        if(satir>=16):
            dikey_hareket*=(-1)
            satir_sayac*=(-1)
        if(sutun<=2):
            yatay_hareket*=(-1)
            sutun_sayac*=(-1)
        if(sutun>=77):
            yatay_hareket*=(-1)
            sutun_sayac*=(-1)
        sutun+=sutun_sayac
        satir+=satir_sayac
        columns = [x+dikey_hareket+yatay_hareket for x in gecici]
        time.sleep(0.09)


if __name__=='__main__':
    main()
