import math


#!
def imprimir_hola (): 
    print("hola")
    
def raizDe2() -> int:
    print(round(math.sqrt(2), 4))
#si uso round con otro parametro, me indica donde termino de redondear

def imprimir_un_verso(cancion: str):
    print(cancion,cancion)

 
#imprimir_hola()

def imprimir_saludo (nombre: str) -> str:
    print ("Hola " + nombre)

def raiz_cuadrada(n:int) ->float:
    print(round(math.sqrt(n),4))

def perimetro () -> float :
    res : float = 2* math.pi
    return res

def perimetro2 () -> float:
    return 2*math.pi
#directamente podia poner el return

#2 % significa modulo

def es_multiplo_de (n: int, m: int) -> bool:
    return (n%m) == 0


def es_nombre_largo (nombre: str) -> bool:
    return len(nombre)>=3 and len(nombre) <= 8

#print(es_nombre_largo("jimena"))

def devolver_el_doble_si_es_par(n: int) -> int:
    if (n%2)==1:
        return n
    else: 
        return n*2

#print(devolver_el_doble_si_es_par(5))

#6
def numeros_pares_hasta () -> int:
    n=10
    while(n<=40):
        print(n)
        n+=2

#numeros_pares_hasta()

def numeros_pares () -> int:
    for i in range (10, 41, 2):
        print(i)

#numeros_pares()

def cuenta_regresiva(n:int):
    while (n>=1):
        print(n)
        n-=1
        if n == 0:
            print("Despegue")
            
def cuenta(n:int) -> int:
    for i in range (n,0,-1):
        print(i)
    print("Despegue")
cuenta_regresiva(56)
    
