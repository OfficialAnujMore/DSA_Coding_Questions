import java.util.Scanner;
import java.util.Scanner;

class prime {

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number");
        Integer num = sc.nextInt();
        boolean flag = false;
        System.out.print(num/2);
        for (int i = 2; i < num / 2; i++) {
            if (num % i == 0) {
                flag = true;
                break;
            }

        }
        if (!flag) {
            System.out.println("prime");
        } else {
            System.out.println("Not  Prime");
        }
    }
}
