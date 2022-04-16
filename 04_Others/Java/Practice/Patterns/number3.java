// 1 1 1 1 1
// 2 2 2 2
// 3 3 3
// 4 4
// 5
public class number3 {

  public static void main(String[] args) {
    int j = 5;
    for (int i = 1; i <= 5; i++) {
      for (j = 5; j > i - 1; j--) {
        System.out.print(i + " ");
      }
      System.out.println(' ');
    }
  }
}
