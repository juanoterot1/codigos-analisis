// Juan David Otero - Juan Manuel Marmolejo - Andres Felipe Vivas
import random

def necesidad_segundo_cajero(personas_a_atender, tiempo_de_trabajo):
    fila1 = []
    fila2 = []
    modulo1 = 1
    modulo2 = 1
    modulo_max = 12
    modulo_min = 1
    atendidos = 0

    for i in range(personas_a_atender):
        if i % 2 == 0:
            fila1.append(modulo1)
            modulo1 = random.randint(modulo_min, modulo_max + 1)
        else:
            fila2.append(modulo2)
            modulo2 = random.randint(modulo_min, modulo_max + 1)

    for i in range(tiempo_de_trabajo * 60):
        if len(fila1) > 0:
            modulo_actual = fila1.pop(0)
            if modulo_actual <= 0:
                if len(fila1) > 0:
                    modulo_actual = fila1.pop(0)
                else:
                    break
            modulo_actual -= 1
            atendidos += 1

        elif len(fila2) > 0:
            modulo_actual = fila2.pop(0)
            if modulo_actual <= 0:
                if len(fila2) > 0:
                    modulo_actual = fila2.pop(0)
                else:
                    break
            modulo_actual -= 1
            atendidos += 1

        else:
            break

    if atendidos >= 250:
        return f"El cajero atendió a {atendidos} personas en {tiempo_de_trabajo} horas de trabajo y no se necesita un segundo cajero."
    else:
        return f"El cajero atendió a {atendidos} personas en {tiempo_de_trabajo} horas de trabajo y se necesita un segundo cajero."


personas_a_atender = int(input("Ingrese la cantidad de personas que deben ser atendidas: "))
tiempo_de_trabajo = int(input("Ingrese las horas de trabajo del cajero: "))

print(necesidad_segundo_cajero(personas_a_atender, tiempo_de_trabajo))
