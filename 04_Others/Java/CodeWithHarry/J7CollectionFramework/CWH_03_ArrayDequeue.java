package Java.CodeWithHarry.J7CollectionFramework;

import java.util.ArrayDeque;

// ArrayDeque implements Deque

public class CWH_03_ArrayDequeue {

  public static void main(String[] args) {
    ArrayDeque<Integer> d1 = new ArrayDeque<Integer>();
    d1.add(12);
    d1.add(45);
    d1.add(85);
    d1.addLast(67);
    d1.add(55);
    d1.addFirst(122);
    d1.addLast(67);

    for (int ele : d1) {
      System.out.println(ele);
    }
    System.out.println("First " + d1.getFirst());
  }
}
