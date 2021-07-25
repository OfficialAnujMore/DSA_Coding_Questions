import java.util.Scanner;

public class fibo {

    // 0 1 1 2 3 5
    public static void main(String args[]) {
        int a = 0;
        int b = 1;
        int c = 0;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter length of series ");
        Integer num = sc.nextInt();
        for (int i = 0; i < num; i++) {
            System.out.print(a + ",");
            c = a + b;

            a = b;
            b = c;

        }
        sc.close();
    }

}