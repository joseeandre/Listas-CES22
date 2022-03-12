import turtle

def desenhar_poligono(t, n, sz):
    ang = 360/n
    for i in range(n):
        t.forward(sz)
        t.left(ang)


tela = turtle.Screen()
tela.bgcolor("#90ee90")
tela.title("Questão 1")

setup = turtle.Turtle()
setup.color("#d1a0a5")
setup.pensize(4)

desenhar_poligono(setup,8,50)

tela.mainloop()