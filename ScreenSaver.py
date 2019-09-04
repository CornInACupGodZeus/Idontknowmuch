import time

class sayac:
    desen=0
    def __init__(self): # Create a Counter
        self.desen = 0
    def __setattr__(self,desen,girdi): # Update the Counter
        super().__setattr__(desen,girdi)
    def __call__(self): # Read the Counter
         return desen

def desen(d_sayac):
    pattern = "\\O/|/\\" # Stickman Pattern
    sarmasik= "»♥♥»♥»»♥»♥♥/♥»♥♥»♥♥♥»♥" # Vines and Leaves Pattern
    d_sayac.__setattr__('desen',( d_sayac.desen + 1)  % len(sarmasik)) # FIFO for Selected Pattern
    return sarmasik[d_sayac.desen - 1]

def main():
    width = 80
    height = 23
    leng = width * height
    d_sayac=sayac() # Create a Pattern Queue Counter
    apsis_hareketi = -2 * width # dikey hareket miktari
    ordinat_hareketi = 2 # yatay hareket miktari
    sutun = 40 # apsis
    satir = 2 # ordinat
    sutun_takip_hareket_miktari = 2 # sutun takip hizi
    satir_takip_hareket_miktari = -2 # satir takip hizi
    # columns = [39,40,41,120,199,201]
    # Figure Locations
    columns = [40,119,120,121,198,199,200,201,278,279,280,281,358,359,360,361,439,440,520,521,600,679]
    while 1:
        Matrix = [desen(d_sayac) if x in columns else ' ' for x in range(leng)] # Draw a Frame
        print("".join(Matrix)) # Join and Print the Frame

        temp=columns # Temporary location holder

        if(satir<=2): # Out of Bounds from Top Side
            apsis_hareketi *= (-1) # Change Movement Direction
            satir_takip_hareket_miktari *= (-1) # Change Tracing Direction
        if(satir>=16): # Out of Bounds from Bottom Side
            apsis_hareketi *= (-1)
            satir_takip_hareket_miktari *= (-1)
        if(sutun<=2): # Out of Bounds from Left Side
            ordinat_hareketi *= (-1)
            sutun_takip_hareket_miktari *= (-1)
        if(sutun>=77): # Out of Bounds from Right Side
            ordinat_hareketi *= (-1)
            sutun_takip_hareket_miktari *= (-1)

        sutun += sutun_takip_hareket_miktari # Update the Abscissa of the Trace
        satir += satir_takip_hareket_miktari # Update the Ordinate of the Trace

        columns = [ x + apsis_hareketi + ordinat_hareketi for x in temp ] # Update the Locations

        time.sleep(0.09) # Wait Time for Visibility

if __name__=='__main__':
    main()
