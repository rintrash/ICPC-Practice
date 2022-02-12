//INCOMPLETE
package PNW2016;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class M2016 {
    public static void main (String[] args) {
        //I have to find number of added letters or deleted to make alphabetical

        //I should first check if it is alphabetical
        Scanner scan = new Scanner(System.in);
        String str = scan.nextLine();

        int count = 0;
        while(!isAlpha(str)){
            
        }

        System.out.println(count);
    }

    public static boolean isAlpha(String s) {
        Map<Character, Integer> map = new HashMap<>(); 
        if(s.length() < 26) {
            return false; 
        }

        for(int j = 97; j < 123; j++) {
            for(int i = 0; i < s.length(); i++) {
                if(s.charAt(i) == j) { //it's one of the letters 
                    
                } 
            }     
        }
        return true;
    }
}
