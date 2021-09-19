class Parent {

  public int a;

  Parent(int a) { // Constructor
    this.a = a; // this is a reference to current object
  }

  public int getX() {
    return a;
  }
}

class Child extends Parent {

  public int b;

  Child(int a, int b) {
    super(a);
    System.out.println("Child" + b);
  }

  public int getB() {
    return b;
  }
}

class CWH_08_This_Super {

  public static void main(String[] args) {
    Parent p = new Parent(23);
    Child c = new Child(12, 34);

    System.out.println(p.getX());
  }
}
