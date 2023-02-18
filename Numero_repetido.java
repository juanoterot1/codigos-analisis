package tarea;

import java.util.Date;
import java.util.Random;
import javax.swing.JOptionPane;

public class Array {
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        Date fechaInicio = new Date(startTime);
        System.out.println("Hora de inicio: " + fechaInicio.toString());

        int a[];
        int elementos;
        elementos = Integer.parseInt(JOptionPane.showInputDialog("Digite el tamaño del arreglo: "));
        a = new int[elementos];

        llenarArray(a);
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i] + " ");
        }
        System.out.println("");

        int[] aux = new int[elementos];
        int n = 0;

        for (int i = 0; i < a.length; i++) {
            int b = a[i];
            if (!encontrarElemento(aux, n, b)) {
                int count = contElemento(a, b);
                guardarElemento(aux, n, b);
                n++;
                System.out.println("El valor " + b + " se encuentra " + count + " veces");
            }
        }

        long endTime = System.currentTimeMillis();
        Date fechaFin = new Date(endTime);
        System.out.println("Hora de finalización: " + fechaFin.toString());

        long totalTime = endTime - startTime;
        System.out.println("El tiempo de ejecución fue de " + totalTime + " milisegundos.");
    }

    public static int contElemento(int[] a, int b) {
        int cont = 0;
        for (int i = 0; i < a.length; i++) {
            if (a[i] == b)
                cont++;
        }
        return cont;
    }

    public static boolean encontrarElemento(int[] a, int n, int b) {
        for (int i = 0; i < n; i++) {
            if (a[i] == b) {
                return true;
            }
        }
        return false;
    }

    public static boolean guardarElemento(int[] a, int n, int b) {
        if (n < a.length) {
            a[n] = b;
            return true;
        }
        return false;
    }

    public static void llenarArray(int[] a) {
        Random numero = new Random();
        for (int i = 0; i < a.length; i++) {
            a[i] = numero.nextInt(a.length);
        }
    }
}
