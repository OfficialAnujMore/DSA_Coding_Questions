class Animal {

  boolean canWalk = true;
  boolean canSwim = true;
  boolean canFly = true;
}

class Dog extends Animal {

  boolean canSwim = false;
  boolean canFly = false;
}

class Bird extends Animal {

  boolean canSwim = false;
}

class CWH_06_Inheritance {

  public static void main(String[] args) {
    Animal ani = new Animal();

    Dog dog = new Dog();
    Bird bird = new Bird();

    System.out.println("Walk " + dog.canWalk);
    System.out.println("Bird can walk " + bird.canWalk);
    System.out.println("Bird can fly " + bird.canFly);
    System.out.println("Bird can swim " + bird.canSwim);
  }
}
