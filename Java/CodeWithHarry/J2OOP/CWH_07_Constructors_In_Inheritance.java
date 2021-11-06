package Java.CodeWithHarry.J2OOP;
class Parent {

  public int x;

  public int getX() {
    return x;
  }

  public void setX(int x) {
    this.x = x;
  }

  Parent() {
    System.out.println("Inside parent constructor");
  }

  Parent(int a) {
    System.out.println("Inside parent constructor " + a);
  }
}

class Child extends Parent {

//   Child() {
//     super(2);
//     System.out.println("Inside Child constructor");
//   }

  Child(int x, int y) {
    super(x);
    System.out.println("Inside Child overloaded constructor " + x + " " + y);
  }

  public int y;

  public int getY() {
    return y;
  }

  public void setY(int y) {
    this.y = y;
  }
}

public class CWH_07_Constructors_In_Inheritance {

  public static void main(String[] args) {
    // Parent par = new Parent();

    // Child chi = new Child(12,23);
  }
}
