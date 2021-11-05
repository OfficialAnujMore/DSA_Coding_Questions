class Thr1 extends Thread {

  public Thr1(String name) {
    super(name);
  }

  public void run() {
    int i = 0;
    while (i < 11) {
      System.out.println(
        "Name is " +
        this.getName() +
        " " +
        this.getPriority() +
        " " +
        this.getState()
      );
      i++;
      try {
        Thread.sleep(1000);
      } catch (Exception e) {
        System.out.println(e);
      }
    }
  }
}

public class CWH_10_ThreadP2 {

  public static void main(String[] args) {
    Thr1 t1 = new Thr1("Anuj");
    Thr1 t2 = new Thr1("Anish------");
    Thr1 t3 = new Thr1("Manali");

    t1.start();
    t2.start();
    t3.start();

    t3.setPriority(7);
    // t2.setPriority(-1); // If negative priority is provided NORM priorities is assigned
    t2.setPriority(8); 
    t1.setPriority(Thread.MAX_PRIORITY);
  }
}
