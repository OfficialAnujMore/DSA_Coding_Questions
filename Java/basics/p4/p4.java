public class p4 {

    public static void main(String args[]) {
        int[] arr = new int[20];

        int i;
        int n = 20;
        for (i = 1; i < n; i++) {
            if (n % i == 0) {
                arr[i] = i;
            }
        }
        System.out.println(Integer(arr));
    }

}
