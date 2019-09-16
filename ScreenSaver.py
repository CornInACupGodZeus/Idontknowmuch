import time
import os
import shutil


class WidthDiff:
    OldWidth = 0

    def __init__(self):  # Create a Counter
        w, h = shutil.get_terminal_size((80, 30))
        self.OldWidth = w

    def __call__(self):  # Read the Counter
        return self.OldWidth


class Sayac:
    indeks = 0

    def __init__(self):  # Create a Counter
        self.indeks = 0

    def __call__(self):  # Read the Counter
        return self.indeks


class Betern:
    pattern= "♥"

    def __init__(self, Beter):
        self.pattern = Beter
        self.sayac = Sayac()

    def khar(self):
        self.sayac.__setattr__('indeks', (self.sayac.indeks + 1) % len(self.pattern))  # FIFO
        return self.pattern[self.sayac.indeks - 1]

#  def desen(d_sayac):
#    pattern = "\\O/|/\\"  # Stickman Pattern
#   sarmasik = "»♥♥»♥»»♥»♥♥/♥»♥♥»♥♥♥»♥"  # Vines and Leaves Pattern
#   d_sayac.__setattr__('indeks', (d_sayac.indeks + 1) % len(sarmasik))  # FIFO for Selected Pattern
#   return sarmasik[d_sayac.indeks - 1]


def main():
    file = open(input("\nDrag & Drop a text file containing what you want to be drawn\n").replace("\"", ""), "r")
    Diff = WidthDiff()  # Create a Memory Class
    golumns = []
    Battern = ""
    PatternWidth = 0
    PatternHeight = 0
    satirbasi = 39
    currentIndex = 0
    sutun = 40  # apsis
    satir = 1  # ordinat
    sutun_takip_hareket_miktari = 1  # sutun takip hizi
    satir_takip_hareket_miktari = -1  # satir takip hizi
    # columns = [39,40,41,120,199,201]
    # Figure Locations
    width, height = shutil.get_terminal_size((80, 30))
    apsis_hareketi = -1 * width  # dikey hareket miktari
    ordinat_hareketi = 1  # yatay hareket miktari

    for lines in file.readlines():
        currentIndex = satirbasi
        for chars in lines:
            if chars == '\n':
                continue
            golumns.append(currentIndex + 1)
            Battern += str(chars)
            currentIndex += 1
        satirbasi += width
        PatternHeight += 1
        if len(lines) > PatternWidth:
            PatternWidth = len(lines)

    Peter = Betern(Battern)  # Create a Pattern Class

    while 1:
        width, height = shutil.get_terminal_size((80, 30))
        leng = width * (height - 2)

        matrix = [Peter.khar() if x in golumns else ' ' for x in range(leng)]  # Draw a Frame
        print("".join(matrix))  # Join and Print the Frame

        temp = golumns  # Temporary location holder

        if satir <= 1:  # Out of Bounds from Top Side
            apsis_hareketi *= (-1)  # Change Movement Direction
            satir_takip_hareket_miktari *= (-1)  # Change Tracing Direction
        if satir >= height - PatternHeight - 1:  # Out of Bounds from Bottom Side
            apsis_hareketi *= (-1)
            satir_takip_hareket_miktari *= (-1)
        if sutun <= 1:  # Out of Bounds from Left Side
            ordinat_hareketi *= (-1)
            sutun_takip_hareket_miktari *= (-1)
        if sutun >= width - PatternWidth:  # Out of Bounds from Right Side
            ordinat_hareketi *= (-1)
            sutun_takip_hareket_miktari *= (-1)

        sutun += sutun_takip_hareket_miktari  # Update the Abscissa of the Trace
        satir += satir_takip_hareket_miktari  # Update the Ordinate of the Trace

        golumns = [x + apsis_hareketi + ordinat_hareketi + (width-Diff.OldWidth)*(x//width) for x in temp]  # Update the Locations

        Diff.__setattr__('OldWidth', width)
        time.sleep(0.09)  # Wait Time for Visibility


if __name__ == '__main__':
    main()
