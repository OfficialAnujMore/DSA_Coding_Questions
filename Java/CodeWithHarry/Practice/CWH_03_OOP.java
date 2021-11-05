package Java.CodeWithHarry.Practice;

class Employee {

  // int id;
  String name;
  int salary;

  public String getName() {
    return name;
  }

  public int getSalary() {
    return salary;
  }

  public void setName(String n) {
    name = n;
  }

  public void setSalary(int sal) {
    salary = sal;
  }
}

class square {

  int side;

  public int getSide() {
    return side;
  }

  public void setSide(int si) {
    side = si;
  }

  public int area() {
    return side * side;
  }

  public int peri() {
    return side * 4;
  }
}

class rect {

  int width;
  int length;

  public int getWidth() {
    return width;
  }

  public int getlength() {
    return length;
  }

  public void setWidth(int w) {
    width = w;
  }

  public void setlength(int l) {
    length = l;
  }

  public int rectArea() {
    return width * length;
  }
}

public class CWH_03_OOP {

  public static void main(String[] args) {
    /*
    // p1
    Employee e1 = new Employee();
    e1.setName("Anuj");
    e1.setSalary(15000);

    System.out.println(e1.getName());
    System.out.println(e1.getSalary());

    Employee e2 = new Employee();
    e2.setName("Anish");
    e2.setSalary(12000);

    System.out.println(e2.getName());
    System.out.println(e2.getSalary());



    // p2

    square sq = new square();
    sq.setSide(12);
    System.out.println("Area " + sq.area());
    System.out.println("Perimeter " + sq.peri());
    */

    //p3

    rect re = new rect();

    re.setWidth(12);
    re.setlength(12);
    System.out.println("Rect area " + re.rectArea());
  }
}
