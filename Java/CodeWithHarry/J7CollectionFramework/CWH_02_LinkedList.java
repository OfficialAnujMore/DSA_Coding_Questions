// package Java.CodeWithHarry.J7CollectionFramework;

import java.util.*;
import java.util.*;

public class CWH_02_LinkedList {

  public static void main(String[] args) {
    LinkedList<Integer> l1 = new LinkedList<Integer>();

    l1.add(12);
    l1.addLast(122);
    l1.addFirst(712);
    l1.add(123);
    l1.add(1342);
    l1.add(23);
    l1.add(9);

    for (int ele : l1) {
      System.out.print(ele);
      System.out.print(" ,");
    }
  }
}
