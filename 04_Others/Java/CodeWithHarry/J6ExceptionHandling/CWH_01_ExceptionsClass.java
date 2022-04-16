package Java.CodeWithHarry.J6ExceptionHandling;
import java.util.Scanner;

class MyException extends Exception {

  @Override
  public String toString() {
    return super.toString() + "To String";
  }

  @Override
  public String getMessage() {
    return super.getMessage() + "Get message";
  }
}

public class CWH_01_ExceptionsClass {

  public static void main(String[] args) {
    int a = 8;
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter number   ");
    a = sc.nextInt();
    sc.close();
    if (a < 99) {
      try {
        throw new MyException();  
      } catch (Exception e) {
        System.out.println(e.getMessage());
        System.out.println(e.toString());
        e.printStackTrace();
        System.out.println("Finished");
      }
    }
 
  }
}
