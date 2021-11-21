import java.util.Scanner;

public class demo {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    System.out.print("Number:");
    int n = in.nextInt();
    System.out.print("Line1:");
    String r1 = in.nextLine();
    System.out.print("Line2:");
    String r2 = in.nextLine();
    System.out.println("Done " + r1);
    System.out.println("Done " + r2);
  }
}
