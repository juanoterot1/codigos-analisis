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

// Explicacion

"""Este código es una simulación de la necesidad de un segundo cajero en una entidad bancaria. El programa solicita al usuario la cantidad de personas que deben ser atendidas y las horas de trabajo del cajero.

El programa luego procede a simular la atención de los clientes en dos filas, fila1 y fila2, utilizando la función randint() del módulo random para generar aleatoriamente el tiempo que cada cliente requerirá para ser atendido. La lista fila1 contendrá los clientes que llegaron primero, mientras que la lista fila2 contendrá los clientes que llegaron después.

Luego, el programa procede a simular la atención de los clientes por parte del cajero durante el tiempo de trabajo especificado por el usuario. En cada ciclo de bucle, el programa verifica si hay clientes en la fila1, si es así, atiende al cliente que ha estado esperando más tiempo y disminuye su tiempo de atención en 1 unidad. Si el tiempo de atención del cliente llega a cero, el cliente es eliminado de la fila. Si la fila1 está vacía, el programa atiende a un cliente de la fila2 siguiendo el mismo proceso.

El programa cuenta la cantidad de clientes atendidos y luego verifica si la cantidad de clientes atendidos es mayor o igual a 250. Si es así, se considera que no es necesario un segundo cajero, de lo contrario, se informa que se necesita un segundo cajero.

El programa devuelve una cadena de texto que indica la cantidad de clientes atendidos y si se necesita o no un segundo cajero."""
