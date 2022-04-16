package Java.CodeWithHarry.Practice;
interface BasicAnimal {
  void eat();
  void sleep();
}

class Monkey {

  public void jump() {
    System.out.println("Jumping");
  }

  public void bite() {
    System.out.println("Bite");
  }
}

class Human extends Monkey implements BasicAnimal {

  public void eat() {
    System.out.println("Eating");
  }

  public void sleep() {
    System.out.println("Sleeping");
  }
}

class CWH_09_AbstractClass {

  public static void main(String[] args) {
    Human hum = new Human();
    hum.eat();
    hum.bite();
    hum.jump();
    hum.sleep();
    Monkey m1 = new Human();
    // m1.sleep(); Cannot use sleep method
  }
}
