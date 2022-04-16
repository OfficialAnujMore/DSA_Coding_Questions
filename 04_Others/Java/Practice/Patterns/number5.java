// 5 5 5 5 5
// 5 5 5 5
// 5 5 5
// 5 5
// 5

public class number5 {

  public static void main(String[] args) {
    for (int i = 1; i < 6; i++) {
      for (int j = 5; j >i - 1; j--) {
        System.out.print("5 ");
      }
      System.out.println(" ");
    }
  }
}
