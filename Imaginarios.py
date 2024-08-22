import math

def suma(t1, t2):
    parte_r = t1[0] + t2[0]
    parte_i = t1[1] + t2[1]
    
    return (parte_r, parte_i)
    
def resta(t1, t2):
    parte_r = t1[0] - t2[0]
    parte_i = t1[1] - t2[1]

    return (parte_r, parte_i)

def multiplicacion(t1, t2):
    parte_r = (t1[0] * t2[0]) - (t1[1] * t2[1])
    parte_i = (t1[0] * t2[1]) + (t1[1] * t2[0])
    
    return (parte_r, parte_i)

def division(t1, t2):
    parte_r = ((t1[0] * t2[0]) + (t1[1] * t2[1])) / ((t2[0] ** 2) * (t2[1] ** 2))
    parte_i = ((t1[0] * t2[0]) - (t1[1] * t2[1])) / ((t2[0] ** 2) * (t2[1] ** 2))
    
    return (parte_r, parte_i)

def modulo(t):
    return str(((t[0])**2 + (t[1])**2)**(1/2))

def conjugado(t):

    return (t[0],-t[1])

def fase(t):

    return math.atan(t[1] / t[0])

def carte_polares(t):

    angulo = fase(t)
    angulo = math.degrees(angulo)
    radio = modulo(t)

    if t[0] > 0:
        if t[1] < 0:
            return (radio, 360 + angulo)
        else:
            return (radio, angulo)
    else:
        if t[1] < 0:
            return (radio, 180 + angulo)
        else:
            return (radio, 180 + angulo)
    
def polares_carte(p):

    x = p[0] * math.cos(p[1])
    y = p[0] * math.sin(p[1])
    
    return (x,y)
def main():
    #PRUEBAS
    print("PRUEBAS")
    #SUMA

    #PRUEBA 1
    
    print("SUMA")

    print("PRUEBA 1")

    print(suma((8,2), (10,27)))

    #PRUEBA 2

    print("PRUEBA 2")


    print(suma((30,12),(78,1)))

    #RESTA
    print("RESTA")
    #PRUEBA 1


    print("PRUEBA 1")


    print(resta((8,2), (10,27)))

    #PRUEBA 2

    print("PRUEBA 2")


    print(resta((30,12),(78,1)))

    #MULTIPLICACION
    print("MULTIPLICACION")
    #PRUEBA 1

    print("PRUEBA 1")



    print(multiplicacion((8,2), (10,27)))

    #PRUEBA 2

    print("PRUEBA 2")


    print(multiplicacion((30,12),(78,1)))


    #DIVISION
    print("DIVISION")
    #PRUEBA 1

    print("PRUEBA 1")



    print(division((8,2), (10,27)))

    #PRUEBA 2

    print("PRUEBA 2")


    print(division((30,12),(78,1)))

    #MODULO
    print("MODULO")
    #PRUEBA 1

    print("PRUEBA 1")

    print(modulo((10,27)))

    #PRUEBA 2

    print("PRUEBA 2")


    print(modulo((30,12)))


    #CONJUGADO
    print("CONJUGADO")
    #PRUEBA 1

    print("PRUEBA 1")



    print(conjugado((8,2)))

    #PRUEBA 2

    print("PRUEBA 2")

    
    print(conjugado((78,-1)))


    #FASE
    print("FASE")
    #PRUEBA 1

    print("PRUEBA 1")



    print(fase((8,10)))

    #PRUEBA 2

    print("PRUEBA 2")


    print(fase((30,78)))

    #De Cartesianas a polares
    print("CARTESIANAS A POLARES")
    #PRUEBA 1

    print("PRUEBA 1")



    print(carte_polares((8,-10)))

    #PRUEBA 2

    print("PRUEBA 2")


    print(carte_polares((30,78)))

    #DE POLARES A CARTESIANAS
    print("POLARES A CARTESIANAS")
    #PRUEBA 1

    print("PRUEBA 1")



    print(polares_carte((8,10)))

    #PRUEBA 2

    print("PRUEBA 2")


    print(polares_carte((30,78)))
    

main()
