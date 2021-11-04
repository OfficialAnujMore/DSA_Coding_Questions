interface sampleInterface {
  void method1();
  void method2();
}

// Cannot implement other interface
// We can extend other interface
interface childSampleInterface extends sampleInterface {
  void method3();
  void method4();
}

class SampleClass implements childSampleInterface {

  public void method1() {
    System.out.println("Method1");
  }

  public void method2() {
    System.out.println("Method2");
  }

  public void method3() {
    System.out.println("Method3");
  }

  public void method4() {
    System.out.println("Method4");
  }
}

public class CWH_14_InheritanceInInterface {

  public static void main(String[] args) {
    SampleClass sc = new SampleClass();
    sc.method1();
    sc.method2();
    sc.method3();
    sc.method4();
  }
}
