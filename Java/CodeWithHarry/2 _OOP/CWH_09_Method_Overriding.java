// In method overriding the method name and parameter list is same
// Return type can be different

class C1 {

  public int a;

  public int m1() {
    return 4;
  }

  public void m2() {
    System.out.println("Method 2 of class A");
  }
}

class C2 extends C1 {

  @Override
  public void m2() {
    System.out.println("Method 2 of class B");
  }

  public void m3() {
    System.out.println("Method 3 of class B");
  }
}

class CWH_09_Method_Overriding {

  public static void main(String[] args) {
    C1 c1 = new C1();
    C2 c2 = new C2();

    c1.m1();
    c1.m2();
    c2.m2();
    c2.m3();
  }
}
