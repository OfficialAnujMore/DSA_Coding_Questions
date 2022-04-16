// 1
// 2 1
// 3 2 1
// 4 3 2 1
// 5 4 3 2 1

public class number7 {

  public static void main(String[] args) {
    for (int i = 0; i < 5; i++) {
      int j = i + 1;
      while (j >= 1) {
        System.out.print(j + " ");
        j--;
      }
      System.out.println("");
    }
  }
}
