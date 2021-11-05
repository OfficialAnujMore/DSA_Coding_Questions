class Mythread1 extends Thread {

  @Override
  public void run() {
    int i = 0;
    while (i < 100) {
      System.out.println("Good morning");
      try{
          Thread.sleep(200);
      }
      catch(Exception e){}
      i++;
    }
  }
}

class Mythread2 extends Thread {

  @Override
  public void run() {
    int i = 0;
    while (i < 100) {
      System.out.println("Welcome");
      i++;
    }
  }
}

public class CWH_10_ThreadP1 {

  public static void main(String[] args) {
    Mythread1 t1 = new Mythread1();
    Mythread2 t2 = new Mythread2();
    t1.start();
    t2.start();
  }
}
