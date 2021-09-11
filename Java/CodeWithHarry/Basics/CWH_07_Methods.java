class CWH_07_Methods {

  static int logic(int x, int y) {
    return x + y;
  }

  int new_logic(int x, int y) {
    return x + y;
  }

  public static void main(String[] args) {
    System.out.println(logic(2, 3));
    CWH_07_Methods obj = new CWH_07_Methods();

    int c =  obj.new_logic(3,3);
    System.out.println(c);

  }
}
