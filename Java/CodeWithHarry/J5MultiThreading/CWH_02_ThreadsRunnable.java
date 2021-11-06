package Java.CodeWithHarry.J5MultiThreading;
class MythreadRunnable1 implements Runnable {

  public void run() {
    int i = 0;
    while (i < 1000) {
      System.out.println("1....*****");
      i++;
    }
  }
}

class MythreadRunnable2 implements Runnable {

  public void run() {
    int i = 0;
    while (i < 1000) {
      System.out.println("2....*");
      i++;
    }
  }
}

/*
New 
Runnable
Running
Terminated
Blocked 

*/
public class CWH_02_ThreadsRunnable {

  public static void main(String[] args) {

    MythreadRunnable1 r1 = new MythreadRunnable1();
    MythreadRunnable2 r2 = new MythreadRunnable2();

    Thread t1 = new Thread(r1);
    Thread t2 = new Thread(r2);
    t1.start();
    t2.start();
  }
}
