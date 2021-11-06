// package Java.CodeWithHarry.J7CollectionFramework;
import java.util.*;

public class CWH_01_ArrayList {

  public static void main(String[] args) {
    ArrayList<Integer> l1 = new ArrayList<Integer>();
    ArrayList<Integer> l2 = new ArrayList<Integer>(2); //Set initial capacity
    l1.add(52532);
    l1.add(23);
    l1.add(33);
    l1.add(46);
    l1.add(0, 2); // Index, element

    l2.add(123);
    l2.add(52532);
    l2.add(2342);
    l2.add(242);
    l2.addAll(l1);

    for (int i = 0; i < l1.size(); i++) {
      System.out.println("L1 " + l1.get(i));
    }
    for (int i = 0; i < l2.size(); i++) {
      System.out.println("L2 " + l2.get(i));
    }
    // l1.clear();
    // for (int i = 0; i < l1.size(); i++) {
    //   System.out.println("L1 " + l1.get(i));
    // }

    System.out.println(l1.contains(1));
    System.out.println("Index of" + l1.indexOf(23));

    for (int el : l1) {
      System.out.println(el);
    }
  }
}
