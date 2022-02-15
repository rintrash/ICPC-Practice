//INCOMPLETE: need help
//I think the problem is im just finding a solution, but not the minimum number of inserts 
package PNW2016;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class M2016 {
    public static void main (String[] args) {
  
        //Map<Character, Integer> map = new HashMap<>(); 
        
        //Scanner scan = new Scanner("abc");
        //String str = scan.nextLine();
        String str = "abc";
        int count = getCount(str);

        System.out.println(count);
    }

    public static int getCount(String s) {
        if(s.length() == 0) {
            return 26;
        } else if(s.length() == 1) {
            return 25;
        }

        StringBuilder str = new StringBuilder(s); 
        int minIndex = 0;
        for(char c = 'a'; c <= 'z'; c++) {
            minIndex = str.indexOf(String.valueOf(c));
            if(minIndex != -1) {
                break;
            }
        }

        int maxIndex = str.length() - 1;
        for(char ch = 'z'; ch >= 'a'; ch--) {
            maxIndex = str.lastIndexOf(String.valueOf(ch));
            if(maxIndex != -1) {
                break;
            }
        }

        int nextIndex = 0; 
        while(nextIndex != str.length() - 1) { //hasn't iterated to the last num
            char curr = str.charAt(0);
            char next;
            for(int i = minIndex + 1; i <= maxIndex; i++) {
                next = str.charAt(i);
                nextIndex = i;  
                if(curr >= next) { //if out of order 
                    str.deleteCharAt(i - 1);
                        break;
                }
                curr = next; 
            }
        }
        int count = 0;
        System.out.println(str.toString());
        for(char j = 'a'; j <= 'z'; j++) {
            if(str.indexOf(String.valueOf(j)) == -1){ //not there
                count++;
            } 
        }
        return count;
    }
}
