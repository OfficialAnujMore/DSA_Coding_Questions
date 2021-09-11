class CWH_02_Varargs {

  static int foo(int... arr) {
    // Variable arguments
    int result = 0;
    for (int ele : arr) {
      result += ele;
    }
    return result;
  }

  public static void main(String[] args) {
    System.out.println(foo(2, 3, 4, 5));
    System.out.println(foo(2, 3, 4, 5, 6, 7));
    System.out.println(foo(2, 3, 4));
    System.out.println(foo());
   
  }
}
