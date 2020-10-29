from random import *
from turtle import *
from freegames import path
#Variables inciales
car = path('car.gif')
tiles = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","#","$","%","&","+","-"]*2
state = {'mark': None}
hide = [True] * 64
#Dibujar el cuadrado en coordenadas
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()
#Encontrar el índice de una coordenada
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)
#Convierte un tila a coordenadas
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200
#Registra entrada en el tablero
def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:#Primera selección
        state['mark'] = spot
    else:#Segunda selección
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

#Imprime todo y evalúa
def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    #Imprime los tableros necesarios
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']
    #Imprime el valor
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))
    if True not in hide:#Si no queda nada oculto
        print("Se acabo")#Impriir en consola
        done()#Finalizar el ontimer
        return
    update()
    ontimer(draw, 100)
shuffle(tiles)#Revolver fichas
setup(420, 420, 370, 0)
addshape(car)#Poner el carro en el fondo
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()