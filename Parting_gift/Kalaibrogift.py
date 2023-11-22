#####################---------------Cake for Parting Event---------#########################

import turtle
import random
import time
from pygame import mixer

# Adding music is optional as per your choice.
mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=512)
mixer.init()
mixer.music.load("C://Users//rohit//Desktop//123//baba kalyani[ExtAudio].mp3") #add your music file name or path

# sets background
bg = turtle.Screen()
bg.bgcolor("black")
mixer.music.play()


# Bottom Line 1
turtle.penup()
turtle.goto(-170,-180)
turtle.color("white")
turtle.pendown()
turtle.forward(350)

# Mid Line 2
turtle.penup()
turtle.goto(-160,-150)
turtle.color("white")
turtle.pendown()
turtle.forward(300)

# First Line 3
turtle.penup()
turtle.goto(-150,-120)
turtle.color("white")
turtle.pendown()
turtle.forward(250)
bg.bgcolor("lightgreen")

# Cake
turtle.penup()
turtle.goto(-100,-100)
turtle.color("pink")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()
bg.bgcolor("green")

# Candles
turtle.penup()
turtle.goto(-90,0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-60,0)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-30,0)
turtle.color("brown")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(0,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(30,0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)
bg.bgcolor("orange")

# Decoration
colors = ["red", "orange", "brown", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)

bg.bgcolor("silver")

# Message

turtle.penup()
turtle.goto(-150, 50)
turtle.color("maroon")
turtle.pendown()

# ENTER YOUR NAME IN THE NAME PLACE
turtle.write(arg=f"All the best in your future \nendeavours, --KALAI BRO--!", align="left", font=("monotype corsiva", 24, "bold"))

time.sleep(15)

#############------Drawing Pikachu for hifi---------#########
def setup(x, y):
    turtle.setx(x)
    turtle.sety(y)
    print(x, y)


class Draw_Pikachu:

    def __init__(self):
        self.t = turtle.Turtle()
        t = self.t
        t.pensize(3)
        t.speed(9)
        t.ondrag(setup)

    def meme(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def aankha1(self, x, y):
        self.meme(x, y)
        t = self.t
        t.seth(0)
        t.fillcolor('#333333')
        t.begin_fill()
        t.circle(22)
        t.end_fill()

        self.meme(x, y + 10)
        t.fillcolor('#000000')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        self.meme(x + 6, y + 22)
        t.fillcolor('#ffffff')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def aankha2(self, x, y):
        self.meme(x, y)
        t = self.t
        t.seth(0)
        t.fillcolor('#333333')
        t.begin_fill()
        t.circle(22)
        t.end_fill()

        self.meme(x, y + 10)
        t.fillcolor('#000000')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        self.meme(x - 6, y + 22)
        t.fillcolor('#ffffff')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def mukh(self, x, y):
        self.meme(x, y)
        t = self.t

        t.fillcolor('#88141D')
        t.begin_fill()
        #
        l1 = []
        l2 = []
        t.seth(190)
        a = 0.7
        for i in range(28):
            a += 0.1
            t.right(3)
            t.fd(a)
            l1.append(t.position())

        self.meme(x, y)

        t.seth(10)
        a = 0.7
        for i in range(28):
            a += 0.1
            t.left(3)
            t.fd(a)
            l2.append(t.position())

        #

        t.seth(10)
        t.circle(50, 15)
        t.left(180)
        t.circle(-50, 15)

        t.circle(-50, 40)
        t.seth(233)
        t.circle(-50, 55)
        t.left(180)
        t.circle(50, 12.1)
        t.end_fill()

        #
        self.meme(17, 54)
        t.fillcolor('#DD716F')
        t.begin_fill()
        t.seth(145)
        t.circle(40, 86)
        t.penup()
        for pos in reversed(l1[:20]):
            t.goto(pos[0], pos[1] + 1.5)
        for pos in l2[:20]:
            t.goto(pos[0], pos[1] + 1.5)
        t.pendown()
        t.end_fill()

        #
        self.meme(-17, 94)
        t.seth(8)
        t.fd(4)
        t.back(8)

    #
    def gaala1(self, x, y):
        turtle.tracer(False)
        t = self.t
        self.meme(x, y)
        t.seth(300)
        t.fillcolor('#DD4D28')
        t.begin_fill()
        a = 2.3
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                t.lt(3)
                t.fd(a)
            else:
                a += 0.05
                t.lt(3)
                t.fd(a)
        t.end_fill()
        turtle.tracer(True)

    def gaala2(self, x, y):
        t = self.t
        turtle.tracer(False)
        self.meme(x, y)
        t.seth(60)
        t.fillcolor('#DD4D28')
        t.begin_fill()
        a = 2.3
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                t.lt(3)
                t.fd(a)
            else:
                a += 0.05
                t.lt(3)
                t.fd(a)
        t.end_fill()
        turtle.tracer(True)

    def kaan1(self, x, y):
        t = self.t
        self.meme(x, y)
        t.fillcolor('#000000')
        t.begin_fill()
        t.seth(330)
        t.circle(100, 35)
        t.seth(219)
        t.circle(-300, 19)
        t.seth(110)
        t.circle(-30, 50)
        t.circle(-300, 10)
        t.end_fill()

    def kaan2(self, x, y):
        t = self.t
        self.meme(x, y)
        t.fillcolor('#000000')
        t.begin_fill()
        t.seth(300)
        t.circle(-100, 30)
        t.seth(35)
        t.circle(300, 15)
        t.circle(30, 50)
        t.seth(190)
        t.circle(300, 17)
        t.end_fill()

    def jiu(self):
        t = self.t

        t.fillcolor('#F6D02F')
        t.begin_fill()
        #
        t.penup()
        t.circle(130, 40)
        t.pendown()
        t.circle(100, 105)
        t.left(180)
        t.circle(-100, 5)

        #
        t.seth(20)
        t.circle(300, 30)
        t.circle(30, 50)
        t.seth(190)
        t.circle(300, 36)

        #
        t.seth(150)
        t.circle(150, 70)

        #
        t.seth(200)
        t.circle(300, 40)
        t.circle(30, 50)
        t.seth(20)
        t.circle(300, 35)
        # print(t.pos())

        #
        t.seth(240)
        t.circle(105, 95)
        t.left(180)
        t.circle(-105, 5)

        #
        t.seth(210)
        t.circle(500, 18)
        t.seth(200)
        t.fd(10)
        t.seth(280)
        t.fd(7)
        t.seth(210)
        t.fd(10)
        t.seth(300)
        t.circle(10, 80)
        t.seth(220)
        t.fd(10)
        t.seth(300)
        t.circle(10, 80)
        t.seth(240)
        t.fd(12)
        t.seth(0)
        t.fd(13)
        t.seth(240)
        t.circle(10, 70)
        t.seth(10)
        t.circle(10, 70)
        t.seth(10)
        t.circle(300, 18)

        t.seth(75)
        t.circle(500, 8)
        t.left(180)
        t.circle(-500, 15)
        t.seth(250)
        t.circle(100, 65)

        #
        t.seth(320)
        t.circle(100, 5)
        t.left(180)
        t.circle(-100, 5)
        t.seth(220)
        t.circle(200, 20)
        t.circle(20, 70)

        t.seth(60)
        t.circle(-100, 20)
        t.left(180)
        t.circle(100, 20)
        t.seth(300)
        t.circle(10, 70)

        t.seth(60)
        t.circle(-100, 20)
        t.left(180)
        t.circle(100, 20)
        t.seth(10)
        t.circle(100, 60)

        #
        t.seth(180)
        t.circle(-100, 10)
        t.left(180)
        t.circle(100, 10)
        t.seth(5)
        t.circle(100, 10)
        t.circle(-100, 40)
        t.circle(100, 35)
        t.left(180)
        t.circle(-100, 10)

        #
        t.seth(290)
        t.circle(100, 55)
        t.circle(10, 50)

        t.seth(120)
        t.circle(100, 20)
        t.left(180)
        t.circle(-100, 20)

        t.seth(0)
        t.circle(10, 50)

        t.seth(110)
        t.circle(100, 20)
        t.left(180)
        t.circle(-100, 20)

        t.seth(30)
        t.circle(20, 50)

        t.seth(100)
        t.circle(100, 40)

        #
        t.seth(200)
        t.circle(-100, 5)
        t.left(180)
        t.circle(100, 5)
        t.left(30)
        t.circle(100, 75)
        t.right(15)
        t.circle(-300, 21)
        t.left(180)
        t.circle(300, 3)

        #
        t.seth(43)
        t.circle(200, 60)

        t.right(10)
        t.fd(10)

        t.circle(5, 160)
        t.seth(90)
        t.circle(5, 160)
        t.seth(90)

        t.fd(10)
        t.seth(90)
        t.circle(5, 180)
        t.fd(10)

        t.left(180)
        t.left(20)
        t.fd(10)
        t.circle(5, 170)
        t.fd(10)
        t.seth(240)
        t.circle(50, 30)

        t.end_fill()
        self.meme(130, 125)
        t.seth(-20)
        t.fd(5)
        t.circle(-5, 160)
        t.fd(5)

        #
        self.meme(166, 130)
        t.seth(-90)
        t.fd(3)
        t.circle(-4, 180)
        t.fd(3)
        t.seth(-90)
        t.fd(3)
        t.circle(-4, 180)
        t.fd(3)

        #
        self.meme(168, 134)
        t.fillcolor('#F6D02F')
        t.begin_fill()
        t.seth(40)
        t.fd(200)
        t.seth(-80)
        t.fd(150)
        t.seth(210)
        t.fd(150)
        t.left(90)
        t.fd(100)
        t.right(95)
        t.fd(100)
        t.left(110)
        t.fd(70)
        t.right(110)
        t.fd(80)
        t.left(110)
        t.fd(30)
        t.right(110)
        t.fd(32)

        t.right(106)
        t.circle(100, 25)
        t.right(15)
        t.circle(-300, 2)
        ##############
        # print(t.pos())
        t.seth(30)
        t.fd(40)
        t.left(100)
        t.fd(70)
        t.right(100)
        t.fd(80)
        t.left(100)
        t.fd(46)
        t.seth(66)
        t.circle(200, 38)
        t.right(10)
        t.fd(10)
        t.end_fill()

        #
        t.fillcolor('#923E24')
        self.meme(126.82, -156.84)
        t.begin_fill()

        t.seth(30)
        t.fd(40)
        t.left(100)
        t.fd(40)
        t.pencolor('#923e24')
        t.seth(-30)
        t.fd(30)
        t.left(140)
        t.fd(20)
        t.right(150)
        t.fd(20)
        t.left(150)
        t.fd(20)
        t.right(150)
        t.fd(20)
        t.left(130)
        t.fd(18)
        t.pencolor('#000000')
        t.seth(-45)
        t.fd(67)
        t.right(110)
        t.fd(80)
        t.left(110)
        t.fd(30)
        t.right(110)
        t.fd(32)
        t.right(106)
        t.circle(100, 25)
        t.right(15)
        t.circle(-300, 2)
        t.end_fill()

        self.topi(-134.07, 147.81)
        self.mukh(-5, 25)
        self.gaala1(-126, 32)
        self.gaala2(107, 63)
        self.kaan1(-250, 100)
        self.kaan2(140, 270)
        self.aankha1(-85, 90)
        self.aankha2(50, 110)
        t.hideturtle()

    def topi(self, x, y):
        self.meme(x, y)
        t = self.t
        t.fillcolor('#CD0000')
        t.begin_fill()
        t.seth(200)
        t.circle(400, 7)
        t.left(180)
        t.circle(-400, 30)
        t.circle(30, 60)
        t.fd(50)
        t.circle(30, 45)
        t.fd(60)
        t.left(5)
        t.circle(30, 70)
        t.right(20)
        t.circle(200, 70)
        t.circle(30, 60)
        t.fd(70)
        # print(t.pos())
        t.right(35)
        t.fd(50)
        t.circle(8, 100)
        t.end_fill()
        self.meme(-168.47, 185.52)
        t.seth(36)
        t.circle(-270, 54)
        t.left(180)
        t.circle(270, 27)
        t.circle(-80, 98)

        t.fillcolor('#444444')
        t.begin_fill()
        t.left(180)
        t.circle(80, 197)
        t.left(58)
        t.circle(200, 45)
        t.end_fill()

        self.meme(-58, 270)
 #       t.pencolor('#228B22')
        t.pencolor("blue")
        t.dot(35)

        self.meme(-30, 280)
 #       t.fillcolor('#228B22')
        t.fillcolor("blue")
        t.begin_fill()
        t.seth(100)
        t.circle(30, 180)
        t.seth(190)
        t.fd(15)
        t.seth(100)
        t.circle(-45, 180)
        t.right(90)
        t.fd(15)
        t.end_fill()
        t.pencolor('#000000')

    def start(self):
        self.jiu()


def main():
    print('Painting Pikachu... ')
    turtle.screensize(1000, 900)
    turtle.title('All the Best from Pikachu')
    drawing = Draw_Pikachu()
    drawing.start()
    turtle.mainloop()

if __name__ == '__main__':
    main()



####################----------------Goku Power UP---------------------#####################
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QIcon, QMovie
import sys

# Adding music is optional as per your choice.
mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=512)
mixer.init()
mixer.music.load("C://Users//rohit//Desktop//123//Attack on Titan Opening theme song.mp3") #add your music file name or path

# sets background
bg = turtle.Screen()
bg.bgcolor("black")
mixer.music.play()
class Window(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(100,100,430,250)
        self.setWindowTitle("Kalai Bro Gift")
        self.setWindowIcon(QIcon('icons/qt.png'))

        label = QLabel(self)
        movie = QMovie("C://Users//rohit//Desktop//123//kalai_bro_gif.gif")
        label.setMovie(movie)
        movie.start()

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())