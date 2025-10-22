##Thiago Gomez PREP 4to

## Escribir una funcion que reciba un archivo
## e intente leer los datos del siguiente enemigo
##Si no hay mas enemigos debe devolver None
##Si hay más enemigos devuelve una lista de 
## 4 valores: Nombre, vida, daño, probabilidad
## de daño golpe, menos el nombre los otros valores
## deben ser ints
import random 

# 1) Leer el archivo de items y guardarlo en una lista de listas, 
# donde para cada item hay 3 lineas
# la primera es el nombre del item
# la segunda es la palabra "Curar" o "Atacar" 
# la tercera es la cantidad que cura o que me suma a la fuerza

# 2) Agregar una opción extra que es utilizar item
# Si se elige esa opción me tiene que mostrar los items dispnibles y
# permitir elegir uno o cancelar
# Si cancela vuelve al menu de elegir accion
# Si se elige un item de curar, se me suma esa vida
# Si se elige un item de atacar, se le suma el valor del item a la fuerza
# del personaje hasta finalizar el juego
# El item elegido tiene que ser quitado de la lista de items al usarse

def leerEnemigo(a):
    nombre = a.readline().strip()
    
    if not nombre:
        return None
    
    vida = int(a.readline().strip())
    fuerza = int(a.readline().strip())
    probabilidad = int(a.readline().strip())
    
    return [nombre, vida, fuerza, probabilidad]

def cacularAtaque(probabilidad, fuerza, vida):
    ataque = random.randint(1, 100)
    if ataque <= probabilidad:
        print(f"Ataque éxitoso. Hace {fuerza} de daño.")
        vida -= fuerza
    else:
        print(f"Ataque errado. ")
    return max(vida, 0)

def calcularCuracion(probabilidadCuracion, cantidadCuracion, vida):
    intento = random.randint(1, 100)
    if intento <= probabilidadCuracion:
        print(f"Curación exitosa. Recuperas {cantidadCuracion} puntos de vida.")
        vida += cantidadCuracion
    else:
        print("No pudiste curarte.")
    return vida


a = open("enemigos.txt", "r")

##  Vida: 30
##  Esqueleto (vida: 10)
##
enemigo = leerEnemigo(a)
vida = 30
probabilidad=80
fuerza=3
probabilidadPot= 50
fuerzaPot=7

probabilidadCuracion=75
cantidadCuracion=7

print(f"vida: {vida}")
while enemigo != None and vida > 0:
    print(f"\nvida: {vida}")
    print(f"Enemigo: {enemigo[0]}, vida: {enemigo[1]}")
    
    ## Turno del jugador: elegir acción
    accion = ""
    while accion not in ["1", "2", "3"]:  # Se agrega la opción 3 para el ataque potenciado
        print("\nTu turno: ")
        print("1. Atacar")
        print("2. Curarse")
        print("3. Ataque potenciado")  # Opción añadida
        accion = input("Elige una acción (1/2/3): ")
    
    ## Se ejecuta la habilidad elegida del jugador
    if accion == "1":
        enemigo[1] = cacularAtaque(probabilidad, fuerza, enemigo[1])
    elif accion == "2":
        vida = calcularCuracion(probabilidadCuracion, cantidadCuracion, vida)
    elif accion == "3":  # Si el jugador elige ataque potenciado
        enemigo[1] = cacularAtaque(probabilidadPot, fuerzaPot, enemigo[1])  # 50% de probabilidad, 7 de daño
    
    if enemigo[1] <= 0:
        print(f"{enemigo[0]} fue derrotado")
        
    # Cargar siguiente enemigo o anunciar victoria
        enemigo = leerEnemigo(a)
        if enemigo is not None:
            print(f"\n Se aproxima un {enemigo[0]}")
        continue


    print(f"\n{enemigo[0]} ataca!")
    vida = cacularAtaque(enemigo[3], enemigo[2], vida)

if enemigo is None:
    print("\n¡Ganaste! Derrotaste a todos los enemigos.")
else:
    print("\nPerdiste. Has sido derrotado.")

a.close()
