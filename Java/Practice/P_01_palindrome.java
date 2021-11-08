import java.util.Scanner;

public class P_01_palindrome {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter a number to check ");
    int num = sc.nextInt();
    sc.close();
    int reversedNum=0,  remainder = 0;

    while (num != 0) {
      remainder = num % 10;
      reversedNum = reversedNum * 10 + remainder;
      num/=10;

    }
    System.out.println(reversedNum);


 
  }
}
