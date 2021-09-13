import java.lang.Math;

class cylinder {

  private int radius;
  private int height;
  private double sArea;

  // public int getRadius() {
  //   return radius;
  // }

  // public int getHeight() {
  //   return height;
  // }

  // public void setRadius(int rad) {
  //   this.radius = rad;
  // }

  // public void setHeight(int hei) {
  //   this.height = hei;
  // }

  public cylinder(int radius, int height) {
    this.radius = radius;
    this.height = height;
  }

  public double surfaceArea() {
    sArea = 2 * Math.PI * radius * radius + 2 * Math.PI * radius * height;
    return sArea;
  }

  public double volume() {
    return Math.PI * radius * radius * height;
  }
}

class Rectangle {

  private int length;
  private int breath;

  public Rectangle() {
    this.length = 4;
    this.breath = 5;
  }

  public Rectangle(int length, int breath) {
    this.length = length;
    this.breath = breath;
  }

  public int getLength() {
    return length;
  }

  public int getBreath() {
    return breath;
  }
}

class Sphere {

  int radius = 12;

  public Sphere() {
    this.radius = radius;
  }

  public double surfaceArea() {
    return 4 * Math.PI * radius * radius;
  }
}

class CWH_05_AccessModifier {

  public static void main(String[] args) {
    cylinder cy = new cylinder(9, 12);

    // int radius = 9;
    // int height = 12;

    // cy.setRadius(radius);
    // cy.setHeight(height);

    // System.out.println(cy.getRadius());
    System.out.println(cy.surfaceArea());
    System.out.println(cy.volume());

    Rectangle rec = new Rectangle(12, 9);
    System.out.println(rec.getLength());
    System.out.println(rec.getBreath());

    Sphere sp = new Sphere();

    System.out.println(sp.surfaceArea());
  }
}
