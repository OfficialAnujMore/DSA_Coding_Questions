package Java.CodeWithHarry.Practice;
class CWH_02_Recusrsion {

  static int natural_num(int n) {
    if (n == 1) {
      return 1;
    } else {
      return n + natural_num(n - 1);
    }
  }

  // 0 1 1 2 3 5 `
  static int fibo(int n) {
    if (n == 1 || n == 2) {
      return n - 1;
    } else {
      return fibo(n - 1) + fibo(n - 2);
    }
  }

  public static void main(String[] args) {
    System.out.println(natural_num(2));
    System.out.println(fibo(6));
  }
}
