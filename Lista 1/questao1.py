import turtle


def desenhar_quadrado(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)


tela = turtle.Screen()
tela.bgcolor("#90ee90")
tela.title("Questão 1")

setup = turtle.Turtle()
setup.color("#d1a0a5")
setup.pensize(4)

for i in range(6):
    desenhar_quadrado(setup, 20*i)
    setup.pu()
    setup.setpos(-10*i, -10*i)
    setup.pd()

tela.mainloop()
