/*
ejercicio 6.1
Pida al usuario que introduzca una palabra y la muestre al revés (por ejemplo: hola -> aloh)
*/
package cadena;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class cadenainvertida {
    public static void main(String[] args) {
      
       Scanner entrada= new Scanner(System.in);
       //definimos la longitud la cadena ingresada y la invertida
       int longitud=0;
       String cadenaActual;
       String cadenainvertida="";
       // pedimos al usuario la cadena
       cadenaActual=JOptionPane.showInputDialog("Digite una cadena");
       longitud=cadenaActual.length();
       // bucle para invertir yfuncion para invertir la cadena
       while(longitud!=0){
           cadenainvertida+= cadenaActual.substring(longitud-1, longitud);
           longitud--;
       }
      
         System.out.println("La cadena actual es: "+cadenaActual);
         System.out.println("La cadena invertida es: "+cadenainvertida);
    }
  
}
