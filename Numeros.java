/* ejercicio 2.30
Escribir un programa que lea números enteros de teclado hasta que encuentre uno que cumpla las siguientes 
condiciones: 
Múltiplo de 2. 
No múltiplo de 5. 
Mayor que 100. 
Menor que 10.000*/
package Numeros;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class DefinirNum {

    public static void main(String[] args) {
      Scanner Entrada= new Scanner(System.in);
      int elementos;
      // pide al usuario la cantidad de elementos  
      elementos=Integer.parseInt(JOptionPane.showInputDialog("Ingrese la cantidad de numeros"));
      // bucle para mostrar todos los eslementos
      for (int i = 0; i <= elementos; i++) {
            System.out.println("\nEl numeros es: " +i);
      // condicionales segun lo que pide el ejercicio
      if(i%2==0){
          System.out.println("El "+i+" es multiplo de 2");
      }else{
          System.out.println("El "+i+" no es multiplo de 2");
      }if(i%5==0){
          System.out.println("El "+i+" es multiplo de 5");
      }else{
          System.out.println("El "+i+" no es multiplo de 5");
      }
      if(i>100){
          System.out.println("El "+i+" es mayor que 100");
      }else{
          System.out.println("El "+i+" no es mayor que 100");
      }
       if(i>10000){
          System.out.println("El "+i+" es mayor que 10000");
      }else{
           System.out.println("El "+i+" es menor que 10000");
       }
      }
      
     
        }
    
    }
