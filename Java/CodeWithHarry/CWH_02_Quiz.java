import java.util.Scanner;

public class CWH_02_Quiz {

    public static void main(String[] args) {

        int sum = 0;
        int percent = 0;
        int mark = 0;
        Scanner sc = new Scanner(System.in);
        for (int i = 1; i <= 5; i++) {

            System.out.print("Enter subject " + i + " marks  : ");
            mark = sc.nextInt();
            sum += mark;
        }
        // System.out.println((floa);
        percent = (sum / 500) * 100;
        System.out.println("Percent " + (float) percent);
        sc.close();

    }
}
