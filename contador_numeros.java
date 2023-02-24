package tarea;
// Importamos las librerias necesarias
import java.util.Date;
import java.util.Random;
import javax.swing.JOptionPane;

public class Array {
    public static void main(String[] args) {
        // Se registra el tiempo de inicio
        long startTime = System.currentTimeMillis();
        Date fechaInicio = new Date(startTime);
        System.out.println("Hora de inicio: " + fechaInicio.toString());

        // Se solicita al usuario que ingrese el tamaño del arreglo
        int a[];
        int elementos;
        elementos = Integer.parseInt(JOptionPane.showInputDialog("Digite el tamaño del arreglo: "));
        a = new int[elementos];

        // Se llena el arreglo con números aleatorios
        llenarArray(a);

        // Se imprime el contenido del arreglo
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i] + " ");
        }
        System.out.println("");

        // Se crea un arreglo auxiliar para almacenar los valores únicos del arreglo original
        int[] aux = new int[elementos];
        int n = 0;

        // Se recorre el arreglo original para contar la cantidad de veces que se encuentra cada número único
        for (int i = 0; i < a.length; i++) {
            int b = a[i];
            if (!encontrarElemento(aux, n, b)) {
                int count = contElemento(a, b);
                guardarElemento(aux, n, b);
                n++;
                System.out.println("El valor " + b + " se encuentra " + count + " veces");
            }
        }

        // Se registra el tiempo de finalización y se calcula el tiempo de ejecución
        long endTime = System.currentTimeMillis();
        Date fechaFin = new Date(endTime);
        System.out.println("Hora de finalización: " + fechaFin.toString());
        long totalTime = endTime - startTime;
        System.out.println("El tiempo de ejecución fue de " + totalTime + " milisegundos.");
    }

    // Método para contar la cantidad de veces que se encuentra un elemento en un arreglo
    public static int contElemento(int[] a, int b) {
        int cont = 0;
        for (int i = 0; i < a.length; i++) {
            if (a[i] == b)
                cont++;
        }
        return cont;
    }

    // Método para buscar un elemento en un arreglo
    public static boolean encontrarElemento(int[] a, int n, int b) {
        for (int i = 0; i < n; i++) {
            if (a[i] == b) {
                return true;
            }
        }
        return false;
    }

    // Método para agregar un elemento a un arreglo
    public static boolean guardarElemento(int[] a, int n, int b) {
        if (n < a.length) {
            a[n] = b;
            return true;
        }
        return false;
    }

    // Método para llenar un arreglo con números aleatorios
    public static void llenarArray(int[] a) {
        Random numero = new Random();
        for (int i = 0; i < a.length; i++) {
            a[i] = numero.nextInt(a.length);
        }
    }
}

//¿Como funciona el programa?
//El programa solicita al usuario que ingrese el tamaño de un arreglo de números enteros.
//Luego, llena el arreglo con números enteros aleatorios y muestra el contenido en la consola.
//A continuación, el programa busca y cuenta la cantidad de veces que aparece cada
//número en el arreglo y muestra el resultado en la consola. Luego, muestra la hora de inicio y
//finalización del programa, tambien el tiempo ejecución en milisegundos.
