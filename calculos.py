import tkinter as tk
import math
from tkinter import ttk

def calcular_sismo():
    magnitud = float(entrada_magnitud.get())
    distancia = float(entrada_distancia.get())
    piso = seleccion_piso.get() # Obtener el valor seleccionado en el Combobox
    intensidad = math.log10(magnitud) + 3 * math.log10(8 * distancia) - 2.92
    etiqueta_resultado.config(text=f"Intensidad: {intensidad}")

    if magnitud >= 7:
        recomendacion = "Evacuar inmediatamente"
    elif magnitud >= 6:
        if piso == "Alto":
            recomendacion = "Dirigirse a un piso inferior"
        else:
            recomendacion = "Buscar una zona segura dentro del edificio"
    else:
        recomendacion = "Mantener la calma y seguir las instrucciones de las autoridades"

    etiqueta_recomendacion.config(text=f"Recomendación: {recomendacion}")

# Creacion de la ventana
ventana = tk.Tk()
ventana.geometry('800x500')  # Establece el tamaño de la ventana
ventana.title('Mi Ventana')

# Personalizacion de colores
color_fondo = '#4682B4'  # Azul oscuro
color_boton = '#FFFFFF'  # Blanco
color_texto = '#000000'  # Blanco

# Cambia el color de fondo de la ventana
ventana.configure(bg=color_fondo)

estilo_titulo = {
    'font': ('Open Sans', 24),
    'bg': '#FFFFFF', 
    'fg': color_texto,
    'padx': 20,
    'pady': 20,
    'relief': 'solid',  # Hace que el borde sea sólido
}

titulo = tk.Label(ventana, text='calculadora', **estilo_titulo)
titulo.pack(side='top', fill='x') # centrar el titulo

etiqueta_magnitud = tk.Label(ventana, text="Magnitud:")
etiqueta_magnitud.place(x=5, y=100)
etiqueta_magnitud.config(width=30, height=2)
entrada_magnitud = tk.Entry(ventana)
entrada_magnitud.place(x=230, y=100)
entrada_magnitud.config(width=10, font=('Open Sans', 18))


etiqueta_distancia = tk.Label(ventana, text="Distancia del epicentro (en km):")
etiqueta_distancia.place(x=5, y=170)
etiqueta_distancia.config(width=30, height=2)
entrada_distancia = tk.Entry(ventana)
entrada_distancia.place(x=230, y=170)
entrada_distancia.config(width=10, font=('Open Sans', 18))


etiqueta_piso = tk.Label(ventana, text="Piso (Alto/Bajo):")
etiqueta_piso.place(x=5, y=240)
etiqueta_piso.config(width=30, height=2)

# Crear un Combobox con opciones para los pisos del 1 al 5
pisos = [str(i) for i in range(1, 6)]
seleccion_piso = ttk.Combobox(ventana, values=pisos, state="readonly") # Configurar el estado en "readonly"
seleccion_piso.place(x=230, y=240)
seleccion_piso.config(width=9, font=('Open Sans', 18))

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_sismo)
boton_calcular.place(x=5, y=310)
boton_calcular.config(width=42, height=2)

etiqueta_resultado = tk.Label(ventana, text="Intensidad:")
etiqueta_resultado.place(x=5, y=380)
etiqueta_resultado.config(width=42, height=2)

etiqueta_recomendacion = tk.Label(ventana, text="Recomendación:")
etiqueta_recomendacion.place(x=5, y=440)
etiqueta_recomendacion.config(width=42, height=2)

#---------------------------------------------------------------
etiqueta_N = tk.Label(ventana, text="Número de personas:")
etiqueta_N.place(x=530, y=80)
etiqueta_N.config(width=30, height=1)
entrada_N = tk.Entry(ventana)
entrada_N.place(x=530, y=105) # Cambiar la coordenada y para colocar la entrada debajo de la etiqueta
entrada_N.config(width=20, font=('Open Sans', 12))

etiqueta_A = tk.Label(ventana, text="Ancho de la salida (m):")
etiqueta_A.place(x=530, y=140) # Aumentar la distancia entre las coordenadas y para separar más las etiquetas y entradas
etiqueta_A.config(width=30, height=1)
entrada_A = tk.Entry(ventana)
entrada_A.place(x=530, y=165) # Aumentar la distancia entre las coordenadas y para separar más las etiquetas y entradas
entrada_A.config(width=20, font=('Open Sans', 12))

etiqueta_h = tk.Label(ventana, text="Altura del edificio (m):")
etiqueta_h.place(x=530, y=200) # Aumentar la distancia entre las coordenadas y para separar más las etiquetas y entradas
etiqueta_h.config(width=30, height=1)
entrada_h = tk.Entry(ventana)
entrada_h.place(x=530, y=225) # Aumentar la distancia entre las coordenadas y para separar más las etiquetas y entradas
entrada_h.config(width=20, font=('Open Sans', 12))

etiqueta_b = tk.Label(ventana, text="Ancho del edificio (m):")
etiqueta_b.place(x=530, y=260) # Aumentar la distancia entre las coordenadas y para separar más las etiquetas y entradas
etiqueta_b.config(width=30, height=1)
entrada_b = tk.Entry(ventana)
entrada_b.place(x=530, y=285) # Aumentar la distancia entre las coordenadas y para separar más las etiquetas y entradas
entrada_b.config(width=20, font=('Open Sans', 12))

etiqueta_D = tk.Label(ventana, text="Distancia total del recorrido (m):")
etiqueta_D.place(x=530, y=320)
etiqueta_D.config(width=30, height=1)
entrada_D = tk.Entry(ventana)
entrada_D.place(x=530, y=345) # Cambiar la coordenada y para colocar la entrada debajo de la etiqueta
entrada_D.config(width=20, font=('Open Sans', 12))

# Agregar una etiqueta para mostrar el resultado del cálculo
etiqueta_tiempo_salida = tk.Label(ventana, text="Tiempo de salida")
etiqueta_tiempo_salida.place(x=530, y=440)
etiqueta_tiempo_salida.config(width=25, font=('Open Sans', 10))

def calcular_tiempo_salida():
    # Obtener los valores ingresados por el usuario
    N = float(entrada_N.get())
    A = float(entrada_A.get())
    h = float(entrada_h.get())
    b = float(entrada_b.get())
    D = float(entrada_D.get())

    # Calcular el tiempo de salida usando la fórmula proporcionada
    k = 1.3 # constante experimental
    V = 0.6 # velocidad de desplazamiento (m/s)
    Ts = (N/A) * k * h * b + D/V

    # Mostrar el resultado en la etiqueta
    etiqueta_tiempo_salida.config(text=f"Tiempo de salida: {Ts:.2f} segundos")

# Agregar un botón para calcular el tiempo de salida
boton_calcular = tk.Button(ventana, text="Calcular tiempo de salida", command=calcular_tiempo_salida)
boton_calcular.place(x=530, y=380) # Especificar la posición del botón usando el método place
boton_calcular.config(width=30, height=2) # Configurar el ancho y la altura del botón

# Centra la ventana en la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x = int((ancho_pantalla / 2) - (800 / 2))
y = int((alto_pantalla / 2) - 280)
ventana.geometry(f'800x500+{x}+{y}')

ventana.mainloop()
