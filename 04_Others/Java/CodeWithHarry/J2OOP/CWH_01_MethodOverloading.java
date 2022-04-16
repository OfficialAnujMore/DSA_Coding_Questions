package Java.CodeWithHarry.J2OOP;
class CWH_01_MethodOverloading {

  // Same method name but different parameter list
  // Return type should be same
  static void reply() {
    System.out.println("Hello");
  }

  static void reply(int x) {
    System.out.println(x);
  }

  public static void main(String[] args) {
    reply();

    // X is a parameters 2 is a argument!!
    reply(2);
  }
}
