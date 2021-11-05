/*
Min Priorities = 1
Normal Priorities = 5
Max Priorities = 10
*/

class Priorities extends Thread {

  public Priorities(String name) {
    super(name);
  }

  public void run() {
    int i = 0;
    while (i < 100) {
      System.out.println("Hello " + this.getName());
      i++;
    }
  }
}

public class CWH_04_ThreadPriorities {

  public static void main(String[] args) {
    Priorities pri1 = new Priorities("Anuj");
    Priorities pri2 = new Priorities("Anish");
    Priorities pri3 = new Priorities("Manali");
    Priorities pri4 = new Priorities("Amay");
    Priorities pri5 = new Priorities("Raj");
    pri1.setPriority(Thread.MIN_PRIORITY);
    pri2.setPriority(Thread.MIN_PRIORITY);
    pri3.setPriority(Thread.MIN_PRIORITY);
    pri4.setPriority(Thread.NORM_PRIORITY);
    pri5.setPriority(Thread.MAX_PRIORITY);
    pri1.start();
    pri2.start();
    pri3.start();
    pri4.start();
    pri5.start();
  }
}
