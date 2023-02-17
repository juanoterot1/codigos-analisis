*/Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su promedio de tres
calificaciones es mayor o igual a 70; reprueba en caso contrario.
Juan Marmolejo10:57
Defina una clase 'Monedero' que permita gestionar la cantidad de dinero que una persona dispone en un momento
dado. La clase deberá tener un constructor que permitirá crear un monedero con una cantidad de dinero inicial y
deberá definir un método para meter dinero en el monedero, otro para sacarlo y finalmente, otro para consultar el
disponible; solo podrá conocerse la cantidad de dinero del monedero a través de este último método. Por
supuesto, no se podrá sacar más dinero del que haya en un monedero/*

class Monedero {
    private int dinero;

    public Monedero(int dineroInicial) {
        this.dinero = dineroInicial; //dinero en el monedero es igual al dinero inicial ingresado por el usuario
    }

    public void meterDinero(int cantidad) {
        this.dinero += cantidad; //sumar la cantidad de dinero ingresada al capital
    }

    public void sacarDinero(int cantidad) {
        if (cantidad <= this.dinero) { //si el capital es menor o igual al dinero que se va a sacar
            this.dinero -= cantidad; //restar la cantidad de dinero ingresada al capital
        } else {
            System.out.println("No hay suficiente dinero en el monedero"); //si la cantidad a sacar es mayor, no hacer
        }
    }

    public int consultarDinero() { 
        return this.dinero; // retorna el dinero que se tiene en la cuenta
    }
}
 public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Monedero monedero = null;

        while (true) {
            System.out.println("1. Crear Monedero");
            System.out.println("2. Meter dinero");
            System.out.println("3. Sacar dinero");
            System.out.println("4. Consultar dinero disponible");
            System.out.println("5. Salir");
            System.out.print("Opción: ");
            int opcion = scan.nextInt();

            if (opcion == 1) {
                System.out.print("Introduce la cantidad inicial: ");
                int dineroInicial = scan.nextInt();
                monedero = new Monedero(dineroInicial);
            } else if (opcion == 2) {
                System.out.print("Introduce la cantidad a meter: ");
                int cantidad = scan.nextInt();
                monedero.meterDinero(cantidad);
            } else if (opcion == 3) {
                System.out.print("Introduce la cantidad a sacar: ");
                int cantidad = scan.nextInt();
                monedero.sacarDinero(cantidad);
            } else if (opcion == 4) {
                System.out.println("Dinero disponible: " + monedero.consultarDinero());
            } else if (opcion == 5) {
                break;
            }
        }

        scan.close();
    }
}
