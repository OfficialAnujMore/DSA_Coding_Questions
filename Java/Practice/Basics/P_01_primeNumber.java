package Basics;

import java.util.Scanner;

public class P_01_primeNumber {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter a number to check ");
    int num = sc.nextInt();
    sc.close();

    // for (int i = 2; i < num; i++) {}

    int i = 2;
    boolean flag = false;
    String result;

    if (num == 1) {
      flag = true;
    } else if (num == 2) {
      flag = false;
    }

    while (flag == false && i < num) {
      if (num % i == 0) {
        flag = true;
      } else {
        flag = false;
        i++;
      }
    }

    result = ((flag == false) ? "Prime" : "Not prime");
    System.out.println(result);
  }
}
