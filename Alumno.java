//Pregunta 1.21
//Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su promedio de tres 
//calificaciones es mayor o igual a 70; reprueba en caso contrario. 
package alumno;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class curso {

    public static void main(String[] args) {
      Scanner entrada= new Scanner(System.in);
      // definimos variables
      float nota1, nota2, nota3;
      float promedio;
      // pedimos los datos al ususario
        nota1=Float.parseFloat(JOptionPane.showInputDialog("Ingrese la primer nota: ")); 
        nota2=Float.parseFloat(JOptionPane.showInputDialog("Ingrese la segunda nota: "));
        nota3=Float.parseFloat(JOptionPane.showInputDialog("Ingrese la tercer nota: "));
        promedio= (nota1+ nota2+nota3)/3;
        // muestra en patalla el promedio de los datos
      
        System.out.println("El promedio es: "+promedio);
        // condicion para determinar si el estudiante aprobo o desaprobo
        if(promedio>=70){
            System.out.println("Aprobaste");
        }else{
            System.out.println("Desaprobaste");
        }
        
    }
    
}
