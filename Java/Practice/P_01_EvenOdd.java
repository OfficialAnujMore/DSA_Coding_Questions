// package classFiles;

import java.util.Scanner;

class P_01_EvenOdd {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter a number to check ");
    int num = sc.nextInt();

    String normalMethod = (num % 2 == 0)
      ? "Number " + num + " is a even number using normal method"
      : "Number " + num + " is a odd number using normal method";
    System.out.println(normalMethod);

    String bitwiseMethod =
      (
        (num ^ 1) == num + 1
          ? "Number " + num + " is a even number using bitwise operation"
          : "Number " + num + " is a odd number using bitwise operation"
      );

    System.out.println(bitwiseMethod);

    // if (num % 2 == 0) {
    //   System.out.println("Number " + num + " is a even number");
    // } else {
    //   System.out.println("Number " + num + " is a odd number");
    // }
    sc.close();
  }
}
