package Java.CodeWithHarry.Practice;
import java.util.*;

class Circle {

  public int radius;
  public float area;

  Circle(int ra) {
    this.radius = ra;
  }

  public double area() {
    area = (float) Math.PI * radius * radius;
    return area;
  }
}

class Cylinder extends Circle {

  public int height;
  public float volume;

  Cylinder(int r, int height) {
    super(r);
    this.height = height;
  }

  public double volume() {
    volume = (float) Math.PI * radius * radius * height;
    return volume;
  }
}

class CWH_08_Inheritance_2 {

  public static void main(String[] args) {
    Circle cir = new Circle(12);
    Cylinder cyl = new Cylinder(12, 24);

    System.out.println(cir.area());
    System.out.println(cyl.volume());
  }
}
