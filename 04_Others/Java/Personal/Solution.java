import java.io.*;
import java.util.*;

public class Solution {

  public static void main(String[] args) {
    String a = "anagramm";
    String b = "marganaa";
    boolean Ana = false;
    int lenA = a.length();
    int lenB = b.length();
    String A = a.toLowerCase();
    String B = b.toLowerCase();
    int i = 0;
    int j = 0;
    int count = 0;
    if (lenA != lenB) {
      System.out.println("Not Ana");
    } else {
      while ((Ana == false) && (i < lenA)) {
        System.out.println(A.charAt(i) + "  " + B.charAt(j));
        if (A.charAt(i) == B.charAt(j)) {
          i++;
          j = 0;
          count++;
        } else {
          j++;
        }
      }
    }
    if (count == lenA) {
      System.out.println("Ana");



      
    } else {
      System.out.println("Not Ana");
    }
  }
}
