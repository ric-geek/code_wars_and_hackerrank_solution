import java.util.ArrayList;
import java.util.List;

public class neutralise {

    public static String neutralise(String s1, String s2) {

        List<String> result = new ArrayList<>();

        for (int i = 0; i < s1.length(); i++) {

            if (s1.charAt(i) == s2.charAt(i)){

                result.add(String.valueOf(s1.charAt(i)));

            }
            else{

                result.add("0");

            }
        }

        return String.join("", result);

    }

    public static void main(String[] args) {


        String str1 = "--++--";
        String str2 = "++--++";

        System.out.println("Test case 1:");
        System.out.println(neutralise(str1,str2));

        String str3 = "-+-+-+";
        String str4 = "-+-+-+";

        System.out.println("Test case 2:");
        System.out.println(neutralise(str3,str4));

    }
}
