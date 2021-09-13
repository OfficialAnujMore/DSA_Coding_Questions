import java.lang.Math;
import java.util.*;

class conditions {

  Scanner sc = new Scanner(System.in);

  //   sc.close();

  public int conditions() {
    Random rand = new Random();
    int ran = rand.nextInt(100);
    System.out.println("Random number " + ran);
    return ran;
  }

  public int TakeInput() {
    int num = sc.nextInt();
    return num;
  }
}

public class CWH_04_Game {

  public static void main(String[] args) {
    conditions con = new conditions();

    System.out.println("User input is :- " + con.TakeInput());
    System.out.println("User input is :- " + con.TakeInput());
  }
}
