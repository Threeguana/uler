# nyoba buat gem uler2

import turtle
import time

delay = 0.5

# setup screen
window = turtle.Screen()
window.title("Uler by me")
window.bgcolor("white")
window.setup(width=400, height=400)
window.tracer(0) #matikan auto refresh

# kepala
kepala = turtle.Turtle() #membuat objek baru untuk menjadi kepala ulat
kepala.speed(0) #set speed
kepala.shape("triangle") #bentuk kepala segitiga dengan warna meraj
kepala.color("red")
kepala.penup() #matikan pen
kepala.goto(0,0) #posisi kepala di tengha layar
kepala.direction = "stop"

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
    gerak()

    time.sleep(delay)

window.mainloop()

