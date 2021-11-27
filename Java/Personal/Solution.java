import java.io.*;
import java.util.*;

public class Solution {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String A = "hello";
    String B = "java";
    int lenA = A.length();
    int lenB = B.length();
    int sum = lenA + lenB;
    int i = 0, j = 0;
    boolean flag = true;
    System.out.println("Sum " + sum);

    while ((i < lenA && j < lenB) && flag == true) {
      System.out.println(A.charAt(i) + "  " + B.charAt(j));
      if (!(A.charAt(i) < B.charAt(j))) {
        flag = false;
      } else {
        i++;
        j++;
      }
    }

    String s1 = A.substring(0, 1).toUpperCase() + A.substring(1);
    String s2 = B.substring(0, 1).toUpperCase() + B.substring(1);
    // System.out.println(A);
    if (flag == true) {
      System.out.println("Yes");
    } else {
      System.out.println("No");
    }

    System.out.println(s1 + " " + s2);
    /* Enter your code here. Print output to STDOUT. */

  }
}
