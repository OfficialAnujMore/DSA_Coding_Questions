package Java.CodeWithHarry.J7CollectionFramework;

import java.util.*;

public class CWH_04_Hashing {

  public static void main(String[] args) {
    HashSet<Integer> h1 = new HashSet<Integer>();
    h1.add(1);
    h1.add(2);
    h1.add(3);
    h1.add(4);
    h1.add(5);
    h1.add(2); // 2 is not inserted
    h1.add(12); // 12 is inserted

    System.out.println(h1);
    h1.remove(2);
    for (int ele : h1) {
      System.out.println("Element " + ele);
    }
  }
}
