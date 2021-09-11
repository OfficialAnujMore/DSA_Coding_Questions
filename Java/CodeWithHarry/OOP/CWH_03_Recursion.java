class CWH_03_Recursion {

  static int factorial(int n) {
    if (n == 0 || n == 1) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }

  //   0 1 1 2 3 5

  static void fibonnaci(int n) {
    int a = 0;
    int b = 1;
    int sum = 0;

    System.out.print(a + " ");
    System.out.print(b + " ");

    for (int i = 0; i <= n; i++) {
      sum = a + b;
      System.out.print(sum + " ");
      a = b;
      b = sum;
      //   a = sum;
    }
  }

  public static void main(String[] args) {
    System.out.println(factorial(5));
    // in
    fibonnaci(5);
  }
}
