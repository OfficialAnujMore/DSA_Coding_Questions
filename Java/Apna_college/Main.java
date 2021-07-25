
import java.util.Arrays;

public class Main {

    public static void printJava() {
        System.out.println("Hello");
    }

    public static void printName(String name) {
        System.out.println(name);
    }

    public static void main(String[] args) {

        for (int i = 0; i < 5; i++) {
            printJava();
            printName("Anuj");
        }

    }

}
