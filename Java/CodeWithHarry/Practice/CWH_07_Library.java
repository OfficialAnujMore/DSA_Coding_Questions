import java.util.ArrayList;

class Management {

  // String[] warehouse = new String[] {"Book1","Book2","Book3","Book4","Book5","Book6"};
  ArrayList<String> warehouse = new ArrayList<String>();

  ArrayList<String> cars = new ArrayList<String>();

  public void addBook(String BookName) {
    warehouse.add(BookName);
  }

  public int displayBook() {
    return warehouse;
  }
}

class CWH_07_Library {

  public static void main(String[] args) {
    Management mng = new Management();

    mng.warehouse.add(new String[] { "Book1", "Book2", "Book" });
    System.out.println(mng.displayBook());
  }
}
