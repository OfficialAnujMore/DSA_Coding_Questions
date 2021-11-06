public class CWH_01_Q2 {
    public static void main(String[] args) {
        try{
            int a = 12;
            int b  =0;
            System.out.println(a/b);
            
        }
        catch(ArithmeticException ae){
            System.out.println("Haha");
        }
        catch(Exception e){
            System.out.println(e);
        }
    }
}
