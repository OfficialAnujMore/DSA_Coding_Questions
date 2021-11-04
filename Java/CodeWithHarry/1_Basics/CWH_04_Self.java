import java.util.*;  
class CWH_04_Self{
    public static void main(String[] args) {
        String name  = "Anuj";
        int len = name.length();
        // List<String> list=new ArrayList<String>();  
        List <Character> lst = new ArrayList <>();

        for (int i = 0; i<len ;i++){
            lst.add(name.charAt(i));
        }
        System.out.println(lst);
    }
}