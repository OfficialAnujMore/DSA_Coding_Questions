package Java.CodeWithHarry.J2OOP;
abstract class Shape {

  String name;
  int height;
  int radius;

  abstract void shapeName();
  // abstract void shapeName(String name); Can pass parameters
}

class Circle extends Shape {

  Circle(String name, int radius) {
    this.name = name;
    this.radius = radius;
  }

  @Override
  public void shapeName() {
    System.out.println("Shape is " + name);
  }

  public void area() {
    System.out.println(radius);
  }
}

class Square extends Shape {

  Square(String name) {
    this.name = name;
  }

  @Override
  public void shapeName() {
    System.out.println("Shape is " + name);
  }
}

public class CWH_11_AbstractClasses {

  public static void main(String[] args) {
    Circle ci = new Circle("Circle", 20);
    ci.shapeName();
    ci.area();
    Square sq = new Square("Square");
    sq.shapeName();
  }
}

// Base structure
abstract class Parent1 {

  public void sayHello() {
    System.out.println("Hello");
  }

  public abstract void greet();
}

class Child1 extends Parent1 {

  @Override
  public void greet() {
    System.out.println("Good morning");
  }
}
