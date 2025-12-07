# nyoba buat gem uler2

import turtle
import time
import random

delay = 0.2

# setup screen
window = turtle.Screen()
window.title("Uler by me")
window.bgcolor("white")
window.setup(width=400, height=400)
window.tracer(0) #matikan auto refresh

# kepala
kepala = turtle.Turtle() #membuat objek baru untuk menjadi kepala ulat
kepala.speed(0) #set speed
window.addshape("gif/totorobocil.gif")
window.addshape("gif/firemini.gif")
window.addshape("gif/pizzamini.gif")
kepala.shape("gif/totorobocil.gif") #bentuk kepala totoro
kepala.color("red")
kepala.penup() #matikan pen
kepala.goto(0,0) #posisi kepala di tengha layar
kepala.direction = "stop"

# makanan totoro
makanan = turtle.Turtle()
makanan.speed(0)
makanan.shape("gif/pizzamini.gif")
makanan.penup()
makanan.goto(0,100) #posisi makanan
# kepala.direction = "stop"

# menambahkan bada totoro saat ia makan pizza
segments = []

# function
def keatas():
    kepala.direction = "up"

def kebawah():
    kepala.direction = "down"

def kekiri():
    kepala.direction = "left"

def kekanan():
    kepala.direction = "right"


def gerak():
    if kepala.direction == "up": #cek jika arah ke atas
        y = kepala.ycor() #ambil koordinat y
        kepala.sety(y + 20) #geser kepala ke atas sebanyak 20px

    if kepala.direction == "down":
        y = kepala.ycor()
        kepala.sety(y - 20)

    if kepala.direction == "left":
        x = kepala.xcor()
        kepala.setx(x - 20)

    if kepala.direction == "right":
        x = kepala.xcor()
        kepala.setx(x + 20)

# keyboard binding
window.listen()
window.onkeypress(keatas, "w")
window.onkeypress(kebawah, "s")
window.onkeypress(kekiri, "a")
window.onkeypress(kekanan, "d")

# main loop
while True:
    window.update()

    # cek tabrakan dengan batas layar
    if kepala.xcor() > 180 or kepala.xcor() < -180 or kepala.ycor() > 180 or kepala.ycor() <-180:
        time.sleep(1)
        kepala.goto(0, 0)
        kepala.direction = "stop"

        # sembunyikan segmen
        for segment in segments:
            segment.goto(1000, 1000) #pindahkan segmen ke luar layar

        # bersihkan list segmen
        segments.clear()

    # cek adanya makanan
    if kepala.distance(makanan) < 20:
        # membuat makanan muncul di spot random
        x = random.randint(-180, 180) # agar makanan tidak berada di luar frame
        y = random.randint(-180, 180)
        makanan.goto(x,y)

        # menambahkan segments
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("gif/firemini.gif")
        new_segment.penup()
        segments.append(new_segment)

    # geser semua segmen badan dari belakang ke posisi segmen sebelumnya
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor() # posisi segmen depan
        y = segments[index-1].ycor()
        segments[index].goto(x, y) # pindahkan segmen ini ke posisi segmen depan

    # pindahkan segmen pertama agar mengikuti kepala
    if len(segments) > 0:
        x = kepala.xcor() # ambil posisi kepala
        y = kepala.ycor()
        segments[0].goto(x, y) # segmen pertama mengikuti kepala

    gerak()

    # cek kepala bertabrakan dengan badan
    for segment in segments:
        if segment.distance(kepala) < 20:
            time.sleep(1) # untuk menghentikan (pause) program selama 1 detik
            kepala.goto(0, 0)
            kepala.direction = "stop"

            # sembunyikan segmen
            for segment in segments:
                segment.goto(1000, 1000)

            # bersihkan list segmen
            segments.clear()

    time.sleep(delay)

window.mainloop()

