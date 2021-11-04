class custom_class {

  int id;
  String name;

  public void printDetails() {
    System.out.println("Id " + id);
    System.out.println("name " + name);
  }

  public int getSalary() {
    return 12000;
  }
}

class CWH_04_ClassesObject {

  public static void main(String[] args) {
    custom_class c1 = new custom_class(); // Instantiation
    c1.id = 12;
    c1.name = "Anuj";
    c1.printDetails();

    custom_class c2 = new custom_class();
    c2.id = 18;
    c2.name = "Anish";
    c2.printDetails();
    System.out.println(c2.getSalary());
  }
}
