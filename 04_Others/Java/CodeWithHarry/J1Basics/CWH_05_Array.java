package Java.CodeWithHarry.J1Basics;
class CWH_05_Array {

  public static void main(String[] args) {
    // reference     object
    int[] marks = new int[5];
    marks[0] = 100;
    marks[1] = 102;
    marks[2] = 104;
    marks[3] = 106;
    marks[4] = 1008;
    System.out.println(marks[0]);

    String[] stu = { "Anuj", "Anish" };
    System.out.println(stu[1]);

    int len = marks.length;

    //For each
    for (int elements : marks) {
      System.out.println(elements);
    }

    for (int i = 0; i < len; i++) {
      System.out.println(marks[i]);
    }
  }
}
