// 1
// 3 3
// 5 5 5
// 7 7 7 7
// 9 9 9 9 9

public class number6 {

  public static void main(String[] args) {
    int num = 1;
    for (int i = 1; i <= 5; i++) {
      for (int j = 1; j < i + 1; j++) {
        System.out.print(num + " ");
      }
      num += 2;
      System.out.println(" ");
    }
  }
}
