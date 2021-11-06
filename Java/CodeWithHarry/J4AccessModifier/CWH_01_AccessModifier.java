// Public
// Protected
// Default
// Private

//        Modifier        Class        Package       Subclass       World
//
//         Public          Yes          Yes           Yes            Yes
//         Protected       Yes          Yes           Yes            No
//         Default         Yes          Yes           No             No
//         Private         Yes          No            No             No
package Java.CodeWithHarry.J4AccessModifier;
class C1 {

  public int x = 6;
  protected int y = 2;
  int xyz = 12;
  private int z = 3;

  public void publicVar() {
    System.out.println(x);
    System.out.println(y);
    System.out.println(z);
    System.out.println(xyz);
  }
}

public class CWH_01_AccessModifier {

  public static void main(String[] args) {
    C1 c1 = new C1();
    c1.publicVar();
  }
}
