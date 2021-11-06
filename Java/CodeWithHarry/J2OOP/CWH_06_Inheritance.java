package Java.CodeWithHarry.J2OOP;
class Parent {

  public String Fname = "Anuj";
  public String Lname = "Anuj111";

  public String printName() {
    return Lname;
  }
}

class Child extends Parent {

  String Fname = "Anish";
}

class CWH_06_Inheritance {

  public static void main(String[] args) {
    Parent p = new Parent();
    Child c = new Child();

    // System.out.println(p.name);
    System.out.println(p.printName());
    System.out.println(c.printName());
    System.out.println(c.Fname);
  }
}
