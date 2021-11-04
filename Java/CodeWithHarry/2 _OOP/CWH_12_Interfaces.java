// Interface conatins all abstract methods
// A class can implement more than one interface
// Interface is a template

interface Bicycle {
  void applyBrake(int decrement);
  void speedUp(int increment);
}

interface Volume {
  int vol = 20;
  void horn();
}

class AvonCycle implements Bicycle, Volume {

  int speed = 8;

  public void applyBrake(int decrement) {
    speed -= decrement;
    System.out.println("Brake applied, speed is " + speed);
  }

  public void speedUp(int increment) {
    speed += increment;
    System.out.println("Speedup, speed is " + speed);
  }

  public void horn() {
    System.out.println("Peeee");
  }
}

public class CWH_12_Interfaces {

  public static void main(String[] args) {
    AvonCycle av = new AvonCycle();
    // System.out.println(av.vol);  // Vol is final, it cannot be changes
    System.out.println(AvonCycle.vol); // It should be access using static way
    // av.vol = 20;
    av.applyBrake(2);
    av.speedUp(45);
    av.horn();
  }
}
