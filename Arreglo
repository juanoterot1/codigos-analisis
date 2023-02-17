/* ejercicio 5.3
Llenar un vector de 20 elementos, imprimir la posición y el valor del elemento mayor almacenado en el vector. 
Suponga que todos los elementos del vector son diferentes
*/
package arreglo;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class mayor {

    public static void main(String[] args) {
     
     Scanner entrada=new Scanner(System.in);
     //definimos el arreglo y el tamaño
     int arreglo[];
     arreglo=new int[20];
     // bucle para llenar el arreglor
     for(int i=0;i<arreglo.length;i++){
         arreglo[i]=Integer.parseInt(JOptionPane.showInputDialog("Digite el "+i+" elemento del arreglo: "));
    }
     // bucle para imprimir el arreglo
        for (int i = 0; i < arreglo.length; i++) {
            System.out.println(arreglo[i]);
        }
        // definimos variables
     int mayor= arreglo[0];
    
     int pos=0;
// recorremos el arreglo para buscar el mayor y su poscion en la que se ecuentra 
     for (int i = 0; i < arreglo.length; i++) {
            if(mayor<arreglo[i]){
                mayor=arreglo[i];
                pos=i;
            }
           
        }
     // muestra el mayor y su posicion
        System.out.println("El numero mayor es: "+mayor+" \nse encuentra el la posicion "+pos);
      
    }
    
}
