package Java.Personal;

import java.util.*;

class Pr_01_Strings {

  public static void main(String[] args) {
    String name = "Anuj More";
    int len = name.length();

    List<Character> chr = new ArrayList<>();

    for (int i = 0; i < len; i++) {
      chr.add(name.charAt(i));
    }

    System.out.println(chr);
    System.out.println(name.replace(" ", "_"));

    System.out.println("Dear " + name);
  }
}
