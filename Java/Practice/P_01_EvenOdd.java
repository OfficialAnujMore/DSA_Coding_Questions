// package classFiles;

import java.util.Scanner;

class P_01_EvenOdd {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter a number to check ");
    int num = sc.nextInt();

    String result = (num % 2 == 0)
      ? "Number " + num + " is a even number"
      : "Number " + num + " is a odd number";
    System.out.println(result);

    // if (num % 2 == 0) {
    //   System.out.println("Number " + num + " is a even number");
    // } else {
    //   System.out.println("Number " + num + " is a odd number");
    // }
    sc.close();
  }
}
