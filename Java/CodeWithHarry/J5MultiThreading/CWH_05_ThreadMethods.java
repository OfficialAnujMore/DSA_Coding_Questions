package Java.CodeWithHarry.J5MultiThreading;

class Method1 extends Thread {

  public Method1(String name) {
    super(name);
  }

  public void run() {
    int i = 0;
    while (i < 10) {
      System.out.println("Name in method1 is " + this.getName());
      try {
        Thread.sleep(455);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
      i++;
    }
  }
}

class Method2 extends Thread {

  public Method2(String name) {
    super(name);
  }

  public void run() {
    int i = 0;
    while (i < 10) {
      System.out.println("Name in method2 is " + this.getName());
      i++;
    }
  }
}

public class CWH_05_ThreadMethods {

  public static void main(String[] args) {
    Method1 m1 = new Method1("Anuj");
    Method2 m2 = new Method2("Anish");
    m1.start();
    // try {
    //   m1.join();
    // } catch (Exception e) {
    //   System.out.println("Error" + e);
    // }

    m2.start();
  }
}
