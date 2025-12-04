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
kepala.direction = "up"

# function
def gerak():
    if kepala.direction == "up": #cek jika arah ke atas
        y = kepala.ycor() #ambil koordinat y
        kepala.sety(y + 20) #geser kepala ke atas sebanyak 20px

# main loop
while True:
    window.update()
    gerak()

    time.sleep(delay)

window.mainloop()

