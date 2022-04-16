// 1
// 2 3 4
// 5 6 7 8 9

public class number8 {

  public static void main(String[] args) {
    int num = 1;
    int count = 1;
    for (int i = 0; i < 3; i++) {
      for (int j = 1; j < count; j++) {
        System.out.print(num);
        num += 1;
      }
      System.out.println(" ");
      count += 2;
    }
  }
}
