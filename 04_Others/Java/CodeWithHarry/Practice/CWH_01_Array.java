package Java.CodeWithHarry.Practice;
public class CWH_01_Array {

  public static void main(String[] args) {
    /*
    // P1
    float[] marks = new float[5];

    marks[0] = 100.f;
    marks[1] = 102.f;
    marks[2] = 104.f;
    marks[3] = 106.f;
    marks[4] = 1008.f;
    float sum = 0;
    for (float ele : marks) {
      sum = sum + ele;
    }
    System.out.println(sum);

    //p2

    float find = 100.0f;
    boolean isIn = false;
    for (float ele : marks) {
      if (ele == find) {
        isIn = true;
        break;
      }
    }

    if (isIn) {
      System.out.println("Found");
    } else {
      System.out.println("Not found");
    }


    //p3

    int[] marks = { 10, 20, 30, 30, 40 };
    int sum = 0;
    float avg = 0.f;

    for (int ele : marks) {
      sum = sum + ele;
    }
    avg  = sum/marks.length;
    System.out.println(avg);
  }
  


    // p4  Print elements of 2d array
    int[][] mat1 = { { 1, 2, 3 }, { 4, 5, 6 } };
    int[][] mat2 = { { 2, 6, 13 }, { 3, 7, 1 } };

    int[][] result = { { 0, 0, 0 }, { 0, 0, 0 } };

    int len = mat1.length;
    int inner_len = mat1[len - 1].length;

    for (int i = 0; i < len; i++) {
      for (int j = 0; j < inner_len; j++) {
        int res = 0;
        res = mat1[i][j] + mat2[i][j];
        result[i][j] = res;
        System.out.print(result[i][j] + " ");
      }
      System.out.println("");
    }

  */

    // p5 Reverse a array
    int[] arr = { 1, 2, 3, 4, 5 };

    int len = arr.length;
    int mid = len / 2;

    // System.out.print(len);
    // System.out.print(mid);

    // for (int i = arr.length - 1; i >= 0; i--) {
    //   System.out.print(arr[i] + " ");
    // }

    for (int i = 0; i < mid; i++) {
      int ele = arr[len - 1 - i];
      arr[len - 1 - i] = arr[i];
      arr[i] = ele;
    }

    for (int i = 0; i < len; i++) {
      System.out.print(arr[i] + " ");
    }
  }
}
