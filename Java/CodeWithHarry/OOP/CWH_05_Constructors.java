class CWH_05_Constructors {

  private int id;
  private String name;

  public String getName() {
    return name;
  }

  public int getId() {
    return id;
  }

  public void setName(String na) {
    this.name = name;
  }

  public void setId(int i) {
    id = i;
  }

  // Name same as class name
  public CWH_05_Constructors() {
    id = 45;
    name = "Name here";
  }

  public static void main(String[] args) {

    // Constructor can be overloaded
    CWH_05_Constructors c = new CWH_05_Constructors();

    System.out.println(c.getId());
    System.out.println(c.getName());
  }
}
