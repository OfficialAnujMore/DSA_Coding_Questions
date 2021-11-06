package Java.CodeWithHarry.J5MultiThreading;
class MyThr extends Thread {

  public MyThr(String name) {
    super(name);
  }

  public void run() {
    int i = 0;
    while (i < 10) {
      System.out.println("1.------------------........");
      i++;
    }
  }
}

public class CWH_03_ConstructorsInThreads {

  public static void main(String[] args) {
    MyThr t1 = new MyThr("Anuj");
    MyThr t2 = new MyThr("Anish");
    t1.start();
    t2.start();
    System.out.println("ID of thread is" + t1.getId());
    System.out.println("Name of thread is" + t1.getName());
    System.out.println("ID of thread is" + t2.getId());
    System.out.println("Name of thread is" + t2.getName());
  }
}
