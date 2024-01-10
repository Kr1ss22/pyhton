#- funktsioon, mis loob erineva suuruse ja asukohaga ringe kogu platsi ulatuses
import turtle
import random
aken = turtle.Screen()
aken.setup(600,600)



def tee_ruut():
    r = random.randint(5,25)
    x ,y =random.randint(-200,300), random.randint(-200,300)
    john  = turtle.Turtle()
    john.hideturtle()
    john.speed("fastest")
    john.penup()
    john.goto(x,y)
    john.pendown()
    for i in range(4):
        john.fd(r)
        john.rt(90)
    


def tee_ring():
    r= random.randint(5,25)
    x ,y =random.randint(-300,300), random.randint(-300,300)
    john  = turtle.Turtle()
    john.hideturtle()
    john.speed("fastest")
    john.penup()
    john.goto(x,y)
    john.pendown()
    print(r)
    john.circle(r)



def tee_suvalised_kujundid():
    suv=random.randint(1,2)
    if suv== 1:
        tee_ring()
    else:
        tee_ruut()


kasutaja_valik = w.numinput("Vali kujund"," 1. Ring\n2. Ruut\n3. Suvaline")
kasutaja_valik = w.numinput("Vali kujundite arv", "sisesta arv:")
for i in range(int(kasutaja_valik_kogus)):
    if kasutaja_valik_kujund == 1
        tee_ring
        elif kasutaja_valik_kujund == 2
        tee_ruut
        else:
            tee_suvalised_kujundid
          tee_suvalised_kujundid()
    


















turtle.exitonclick()