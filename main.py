import time

RESET = "\033[39m"
RED = "\033[31m"
BLUE = "\033[34m"
AMARILLO = "\033[33m"
VERDE = "\033[32m"
WHITE = "\033[37m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
trivia=True

#introduccion
print("\n Bienvenido a la Trivia de " + RED + "CO" + BLUE +"LO" + AMARILLO + "RES\n" + RESET)
usuario = input("Ingrese su nombre porfavor y presione \n\n"+RED+"ENTER"+RESET+" para continuar : ")
print(CYAN + "\n==========" + RED + "==========" + BLUE + "==========" +VERDE + "==========" + MAGENTA + "==========\n" + RESET)
print(" bienvenido ", usuario,
      "a la trivia de " + RED + "CO" + BLUE + "LO" + AMARILLO + "RES" + RESET)
print("\n Seran 3 preguntas las q tendras q responder\n")
time.sleep(1)
print(" - Cada respuesta correcta obtendras " + VERDE + "+15 pts" + RESET)
print(" - Cada respuesta incorrecta perderas " + RED + "-10 pts" + RESET)
print(" -", usuario,
      " comenzaras con " + VERDE + "100 pts " + RESET + "Suerte!")
print(CYAN + "\n==========" + RED + "==========" + BLUE + "==========" +VERDE + "==========" + MAGENTA + "==========\n" + RESET)
time.sleep(1)
input("\n Preciona Enter para continuar " + RED + "...\n" + RESET)
intentos=0
puntaje = 100
#aqui comienza la pregunta 1
while trivia == True:
    print(CYAN + "\n==========" + RED + "==========" + BLUE + "==========" +VERDE + "==========" + MAGENTA + "==========\n" + RESET)
    print(VERDE + "", usuario, "Tienes", puntaje, "puntos" + RESET)
    time.sleep(1)
    print("\n         Primera pregunta :")
    time.sleep(1)
    print("\n ¿ Que colores debes combinar para conseguir el color " +MAGENTA + "MORADO " + RESET + "?\n")
    print("a - Combinar " + RED + "ROJO " + RESET + "+ " + VERDE + "VERDE" +RESET)
    print("b - Combinar " + AMARILLO + "AMARILLO " + RESET + "+ " + BLUE +"AZUL" + RESET)
    print("c - Combinar " + RED + "ROJO " + RESET + "+ " + BLUE + "AZUL" +RESET)
    print("d - Combinar BLANCO + " + RED + "ROJO" + RESET)
    respuesta_p1 = input("\n -- Escriba a, b, c ó d como respuesta y luego presione enter: ").lower()

    while respuesta_p1 not in ("a", "b", "c", "d"):
        respuesta_p1 = input("\n -- Debes elejir entre a , b , c ó d : ").lower()
    if respuesta_p1 == "a":
        intentos+=1
        puntaje -= 10
        print("\n ---------------")
        print(RED + "  Respuesta:\n" + RESET)
        time.sleep(1)
        print(" Al mezclar " + RED + "ROJO +" + VERDE + " VERDE" + RESET +" optienes " + AMARILLO + "AMARILLO\n" + RESET)
        time.sleep(1)
        print(RED + " - No es la respuesta correcta" + RESET)
        print(RED + " - pierdes -10 pts" + RESET)
        print(RED +" -", usuario," Ahora tienes :", puntaje, " puntos"+RESET)
        print(CYAN + "\n==========" + RED + "==========" + BLUE +"==========" + VERDE + "==========" + MAGENTA + "==========\n" +RESET)
        print("\n - Si deseas pasar a la pregunta 2 presione "+RED+"ENTER"+RESET)
        sgt = input("\n - Si desea volver a intentarlo escriba "+RED+"si"+RESET+" y presione ENTER: ")
        if sgt != "si":
            trivia = False

    elif respuesta_p1 == "b":
        puntaje -= 10
        intentos+=1
        print("\n ---------------")
        print(RED + "\n  Respuesta:\n" + RESET)
        time.sleep(1)
        print(" Combinando " + AMARILLO + "AMARILLO + " + BLUE + "AZUL " +RESET + "obtines " + VERDE + "VERDE " + RESET)
        time.sleep(1)
        print(RED + " - No es la respuesta correcta " + RESET)
        print(RED + " - Pierdes -10 pts" + RESET)
        print(RED +" -", usuario, " ahora tienes :", puntaje, " puntos"+RESET)
        print(CYAN + "\n==========" + RED + "==========" + BLUE +"==========" + VERDE + "==========" + MAGENTA + "==========\n" +RESET)
        print("\n - Si deseas pasar a la pregunta 2 presione "+RED+"ENTER"+RESET)
        sgt = input("\n - Si desea volver a intentarlo escriba "+RED+"si"+RESET+" y presione ENTER: ")
        if sgt != "si":
            trivia = False
    elif respuesta_p1 == "d":
        puntaje -= 10
        intentos+=1
        print("\n ---------------")
        print(RED + "\n  Respuesta:\n" + RESET)
        time.sleep(1)
        print(" - Al combinar BLANCO + " + RED + "ROJO " + RESET +"obtienes " + RED + "ROSA" + RESET)
        time.sleep(1)
        print(RED + " - No es la respuesta correcta" + RESET)
        print(RED + " - pierdes 10 pts" + RESET)
        print(RED +" -", usuario, " tienes :", puntaje, " puntos"+RESET)
        print(CYAN + "\n==========" + RED + "==========" + BLUE +"==========" + VERDE + "==========" + MAGENTA + "==========\n" +RESET)
        print("\n - Si deseas pasar a la pregunta 2 presione "+RED+"ENTER"+RESET)
        sgt = input("\n - Si desea volver a intentarlo escriba "+RED+"si"+RESET+" y presione ENTER: ")
        if sgt != "si":
            trivia = False
    else:  #la respuestacorrecta es la "c"
        puntaje += 15
        intentos+=1
        print("\n ---------------")
        print(RED + "\n  Respuesta:\n" + RESET)
        time.sleep(1)
        print(" Al mezclar " + RED + "ROJO" + RESET + " Y " + BLUE + "AZUL " +RESET + "optines " + MAGENTA + "MORADO" + RESET)
        time.sleep(1)
        print(MAGENTA+" * * * * * * * * * * * * * * * * "+RESET)
        print(" Felicidades es la respuesta correcta!!\n")
        print(" -", usuario, " optienes 15 pts")
        print(VERDE + " -", usuario, " ahora tienes :", puntaje,
              " puntos" + RESET)
        trivia = False
print(CYAN + "\n==========" + RED + "==========" + BLUE + "==========" +VERDE + "==========" + MAGENTA + "==========\n" + RESET)
input("\n presione ENTER para continuar \n")

#aqui comienza la pregunta 2
trivia2 = True
while trivia2 == True:
    print(CYAN + "\n==========" + RED + "==========" + BLUE + "==========" +VERDE + "==========" + MAGENTA + "==========\n" + RESET)
    print(VERDE + "", usuario, "Tienes", puntaje, "puntos" + RESET)
    time.sleep(1)
    print("\n         Segunda pregunta :")
    time.sleep(1)
    print("\n ¿Que color obtendre si mezclo " + BLUE + "AZUL " + RESET + "+ " +AMARILLO + "AMARILLO" + RESET + " + BLANCO ?\n")
    print("a - Obtendre CELESTE CIELO")
    print("b - Obtendre ROSA CLARO")
    print("c - Obtendre NARANJA")
    print("d - Obtendre VERDE LIMON")
    respuesta_p2 = input("\n Escriba a, b, c ó d como respuesta : ").lower()

    while respuesta_p2 not in ("a", "b", "c", "d"):
        respuesta_p2 = input("\n Debes elejir entre a , b , c ,d : ").lower()
    if respuesta_p2 == "a":
        puntaje -= 10
        intentos+=1
        print("\n ---------------")
        print(RED + "\n  Respuesta:\n" + RESET)
        time.sleep(1)
        print(" Para obtener CELESTE CIELO debes mezclar AZUL + BLANCO")
        time.sleep(1)
        print(RED + " - No es la respuesta correcta pierdes 10 pts" + RESET)
        print(RED + " -", usuario, " ahora tienes :", puntaje," puntos" + RESET)
        print("\n - Si deseas pasar a la pregunta 3 presione "+RED+"ENTER"+RESET)
        sgt = input("\n - Si desea volver a intentarlo escriba "+RED+"si"+RESET+" y presione ENTER: ")
        if sgt != "si":
            trivia2 = False

    elif respuesta_p2 == "b":
        puntaje -= 10
        intentos+=1
        print("\n ---------------")
        print(RED + "\n  Respuesta:\n" + RESET)
        time.sleep(1)
        print(" ROSA CLARO se obtiene de mezclar " + RED + "ROJO" + RESET +"+ BLANCO")
        time.sleep(1)
        print(RED + " No es la respuesta correcta pierdes 10 pts" + RESET)
        print(RED + " -", usuario, " ahora tienes :", puntaje,
              " puntos" + RESET)
        print("\n - Si deseas pasar a la pregunta 3 presione "+RED+"ENTER"+RESET)
        sgt = input("\n - Si desea volver a intentarlo escriba "+RED+"si"+RESET+" y presione ENTER: ")
        if sgt != "si":
            trivia2 = False
    elif respuesta_p2 == "c":
        puntaje -= 10
        intentos+=1
        print("\n ---------------")
        print(RED + "\n  Respuesta:\n" + RESET)
        time.sleep(1)
        print(" NARANJA se obtiene de combinar " + RED + "ROJO" + RESET +" +" + AMARILLO + " AMARILLO" + RESET)
        time.sleep(1)
        print(RED + " No es la respuesta correcta" + RESET)
        print(RED + " Pierdes 10 puntos" + RESET)
        print(RED +"",usuario, " tienes :", puntaje, " puntos"+RESET)
        print("\n - Si deseas pasar a la pregunta 3 presione "+RED+"ENTER"+RESET)
        sgt = input("\n - Si desea volver a intentarlo escriba "+RED+"si"+RESET+" y presione ENTER: ")
        if sgt != "si":
            trivia2 = False
    else:  #la respuestacorrecta es la "d"
        puntaje += 15
        intentos+=1
        print("\n ---------------")
        print(RED + "\n  Respuesta:\n" + RESET)
        time.sleep(1)
        print(" VERDE LIMON se obtiene de mezclar AZUL + AMARILLO + BLANCO")
        time.sleep(1)
        print(MAGENTA+"* * * * * * * * * * * * * * * *"+RESET)
        print(" Es la respuesta correcta!!")
        print(" Felicidades optienes 15 pts")
        print(VERDE + " -", usuario, " ahora tienes :", puntaje," puntos" + RESET)
        trivia2 = False

print(CYAN + "\n==========" + RED + "==========" + BLUE + "==========" +VERDE + "==========" + MAGENTA + "==========\n" + RESET)
input("\n presione ENTER para continuar \n")

#aqui comineza la pregunta 3
trivia3 = True
while trivia3 == True:
    print(CYAN + "\n==========" + RED + "==========" + BLUE + "==========" +VERDE + "==========" + MAGENTA + "==========\n" + RESET)
    print(VERDE + "", usuario, "Tienes", puntaje, "puntos" + RESET)
    time.sleep(1)
    print("\n         Tercera pregunta :")
    time.sleep(1)
    print("\n Ahora seran 2 preguntas juntas :")
    time.sleep(3)
    print("\n ¿Cuales son los " + RED + "CO" + BLUE + "LO" + AMARILLO +"RES" + RESET + " primarios?")
    print(" ¿cuantas combinaciones de " + RED + "CO" + BLUE + "LO" + AMARILLO +"RES" + RESET + " existen?\n")
    print("\na - BLANCO, " + RED + "ROJO," + RESET + " " + VERDE + "VERDE" +RESET + " y existen 9999 654 de combinaciones")
    print("\nb - " + RED + "ROJO" + RESET + ", " + AMARILLO + "AMARILLO" +RESET + ", " + BLUE + "AZUL" + RESET +" y existen 16 777 216 de combinaciones ")
    print("\nc - NARANJA, " + RED + "ROJO" + RESET +", "+ MAGENTA +"MORADO"+RESET+" y existen 1 000 combinaciones")
    print("\nd - " + AMARILLO + "AMARILLO" + RESET + ", " + BLUE + "AZUL" +RESET + ", " + RED + "ROJO" + RESET +" y exieten una cantidad infinita de combinaciones")
    respuesta_p3 = input("\n Escriba a, b, c ó d como respuesta y luego presione enter: ").lower()

    while respuesta_p3 not in ("a", "b", "c", "d"):
        respuesta_p3 = input("\n Debes elejir entre a , b , c ,d : ").lower()
    if respuesta_p3 == "a":
        puntaje -= 10
        intentos+=1
        print("\n ---------------")
        print(RED + "\n  Respuesta:\n" + RESET)
        time.sleep(1)
        print("\n - No es la respuesta correcta \n")
        print(RED + " - Pierdes 10 puntos" + RESET)
        print(RED +" ", usuario, " ahora tienes :", puntaje, " puntos" + RESET)
        print("\n - Presione "+RED+"ENTER"+RESET+"para continuar :")
        sgt = input("\n - Si desea volver a intentarlo escriba "+RED+"si"+RESET+" y presione ENTER: ")
        if sgt != "si":
            trivia3 = False

    elif respuesta_p3 == "c":
        puntaje -= 10
        intentos+=1
        print("\n ---------------")
        print(RED + "\n  Respuesta:\n" + RESET)
        time.sleep(1)
        print(" - No es la respuesta correcta ")
        print(RED + " - Pierdes 10 puntos" + RESET)
        print(RED + " -", usuario, " ahora tienes :", puntaje,
              " puntos" + RESET)
        print("\n - Presione "+RED+"ENTER"+RESET+"para continuar :")
        sgt = input("\n - Si desea volver a intentarlo escriba "+RED+"si"+RESET+" y presione ENTER: ")
        if sgt != "si":
            trivia3 = False
    elif respuesta_p3 == "d":
        puntaje -= 10
        intentos+=1
        print("\n ---------------")
        print(RED + "\n  Respuesta:\n" + RESET)
        time.sleep(1)
        print(" - No es la respuesta correcta ")
        print(RED + " - Pierdes 10 puntos" + RESET)
        print(RED + " -", usuario, " tienes :", puntaje, " puntos" + RESET)
        print("\n - Presione "+RED+"ENTER"+RESET+"para continuar :")
        sgt = input("\n - Si desea volver a intentarlo escriba "+RED+"si"+RESET+" y presione ENTER: ")
        if sgt != "si":
            trivia3 = False
    else:  #la respuestacorrecta es la "b"
        puntaje += 15
        intentos+=1
        print("\n ---------------")
        print(RED + "\n  Respuesta:\n" + RESET)
        time.sleep(1)
        print(MAGENTA+"* * * * * * * * * * * * * * * *"+RESET)
        print(" Respuesta correcta!!")
        print("\n - " + RED + "ROJO," + RESET + " " + AMARILLO + "AMARILLO" +RESET + ", " + BLUE + "AZUL" + RESET + " son los " + RED + "CO" +BLUE + "LO" + AMARILLO + "RES" + RESET + " primarios\n")
        print(" - Existen 16 777 216 combinaciones distintas en el sistema RGB de 24 bits y, por lo tanto, 16 777 216 colores")
        print("\n - Felicidades es la respuesta correctamente optienes 15 pts\n")
        print(VERDE + " -", usuario, " ahora tienes :", puntaje," puntos" + RESET)
        trivia3 = False
time.sleep(2)
#final
print(CYAN + "\n==========" + RED + "==========" + BLUE + "==========" +VERDE + "==========" + MAGENTA + "==========\n" + RESET)
print("\n Finalisaste la Trivia ", usuario)
print("\n Comezaste con 100 pts")
print("\n Ahora tienes ", puntaje, " puntos")
print("\n En total resolviste ",intentos," preguntas")
time.sleep(2)
print("\n ---------------")
print(" Gracias por jugar la Trivia de " + RED + "CO" + BLUE + "LO" +
      AMARILLO + "RES" + RESET)
