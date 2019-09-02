leng= 1840;
dikeyhareket= -160;#dikey hareket miktarı
yatayhareket= 2;#yatay hareket miktarı
sütun=40;#2ile78 arası
satır=2;#2ile22 arası
sütunsayac=2;#sütun takip hızı
satırsayac=-2;#satır takip hızı
desensayac=0;# hangi desen basılacak, her desen aynı sırada basılacağı bilgisi kullanılarak
columns=[39,40,41,120,199,201]
import time

def desen():
    global desensayac
    if(desensayac==0):
        desensayac+=1
        return chr(92)
    elif(desensayac==1):
        desensayac+=1
        return chr(79)
    elif(desensayac==3):
        desensayac+=1
        return chr(124)
    elif(desensayac==2):
        desensayac+=1
        return chr(47)
    elif(desensayac==4):
        desensayac+=1
        return chr(47)
    else:
        desensayac=0
        return chr(92)

while 1:

    Matrix = [desen() if x in columns else chr(32) for x in range(leng)]
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
