package Java.CodeWithHarry.J5MultiThreading;

class MyThread extends Thread {

  @Override
  public void run() {
    int i = 0;
    while (i < 1000) {
      System.out.println("1.......");
      System.out.println("2.......");
      i++;
    }
  }
}

class MyThread2 extends Thread {

  @Override
  public void run() {
    int i = 0;
    while (i < 1000) {
      System.out.println("3.........................");
      System.out.println("4.........................");
      i++;
    }
  }
}

class CWH_01_ThreadsExtends {

  public static void main(String[] args) {
    MyThread t1 = new MyThread();
    MyThread2 t2 = new MyThread2();
    t1.start();
    t2.start();
  }
}
