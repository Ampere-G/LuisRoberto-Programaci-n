import turtle as tr

#Minima medida en pixeles
#Establecer a cuantos pixeles equivaldrá la unidad
u=10

#Establecer propiedades de la ventana
alto=400
ancho=800

tr.setup(ancho,alto)
tr.title('Tiro parabólico')

#Configuración del cursor
tr.shape('turtle')
tr.color('green')

#Establecer los ejes coordenados justo hasta la izquierda y en el medio del eje vertical para una mejor visualización
tr.setworldcoordinates(0,-alto,ancho,alto)

#Mostrar tortuga
tr.showturtle()

#Ecuaciones de movimiento convertidas a las unidades deseadas

t=0
x_0=0
y_0=0
v_0x=80
v_0y=100
g=(9.8)*u

posx=lambda t: (x_0 + v_0x*t)*u
posy=lambda t: (y_0 + v_0y*t - g*t**2)*u

#Hacer que se actualize la posicion en aumentando 0.1 segundo en cada iteracion y que pare cuando posicion en y sea igual a 0 de nuevo
while posy(t)>=0:
    tr.goto(posx(t),posy(t))
    t+=0.1

tr.done()

